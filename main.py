import os
from dotenv import load_dotenv

# Import all agents
from agents.research_agent import ResearchAgent
from agents.qualify_agent import QualifyAgent
from agents.communication_agent import CommunicationAgent
from agents.reporting_agent import ReportingAgent

def main():
    # Load API key from .env
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError("❌ Missing OPENAI_API_KEY in .env file")

    # Initialize agents
    research_agent = ResearchAgent(api_key)
    qualify_agent = QualifyAgent(api_key)
    comms_agent = CommunicationAgent(api_key)
    report_agent = ReportingAgent(api_key)

    # Step 0: Take topic input from user
    topic = input("📝 Enter the topic for research: ").strip()
    if not topic:
        print("❌ Topic cannot be empty. Exiting...")
        return

    # Step 1: Research
    research_result = research_agent.run(topic)
    print("\n" + "="*80)
    print("🔍 Research Agent Result:\n")
    print(research_result.content.strip())
    print("="*80 + "\n")

    # Step 2: Qualification
    qualified_result = qualify_agent.run(research_result.content)
    print("\n" + "="*80)
    print("✅ Qualify Agent Result:\n")
    print(qualified_result.content.strip())
    print("="*80 + "\n")

    # Step 3: Communication
    comms_result = comms_agent.run(qualified_result.content)
    print("\n" + "="*80)
    print("📢 Communication Agent Result:\n")
    print(comms_result.content.strip())
    print("="*80 + "\n")

    # Step 4: Reporting
    report_result = report_agent.run(comms_result.content)
    print("\n" + "="*80)
    print("📊 Reporting Agent Final Report:\n")
    print(report_result.content.strip())
    print("="*80 + "\n")

if __name__ == "__main__":
    main()
