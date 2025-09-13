import os
import sys
from dotenv import load_dotenv
import streamlit as st

# ✅ Add project root (Multy_agent) to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Import agents
from agents.research_agent import ResearchAgent
from agents.qualify_agent import QualifyAgent
from agents.communication_agent import CommunicationAgent
from agents.reporting_agent import ReportingAgent


def main():
    # Load API key
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        st.error("❌ Missing OPENAI_API_KEY in .env file")
        return

    # Initialize agents
    research_agent = ResearchAgent(api_key)
    qualify_agent = QualifyAgent(api_key)
    comms_agent = CommunicationAgent(api_key)
    report_agent = ReportingAgent(api_key)

    # Session state for history
    if "history" not in st.session_state:
        st.session_state.history = []

    # Sidebar: choose agents
    st.sidebar.title("⚙️ Agent Settings")
    run_research = st.sidebar.checkbox("🔍 Research Agent", True)
    run_qualify = st.sidebar.checkbox("✅ Qualify Agent", True)
    run_comms = st.sidebar.checkbox("📢 Communication Agent", True)
    run_report = st.sidebar.checkbox("📊 Reporting Agent", True)

    # Main UI
    st.title("🤖 Joyal's Multi-Agent AI System")
    topic = st.text_input("Enter your topic:", "")

    if st.button("Run Agents"):
        results = {"topic": topic}

        if run_research:
            with st.spinner("🔍 Researching..."):
                research_result = research_agent.run(topic)
                results["Research Agent"] = str(getattr(research_result, "content", research_result))
                st.subheader("🔍 Research Agent Result")
                st.markdown(results["Research Agent"])

        if run_qualify and "Research Agent" in results:
            with st.spinner("✅ Qualifying insights..."):
                qualified_result = qualify_agent.run(results["Research Agent"])
                results["Qualify Agent"] = str(getattr(qualified_result, "content", qualified_result))
                st.subheader("✅ Qualify Agent Result")
                st.markdown(results["Qualify Agent"])

        if run_comms and "Qualify Agent" in results:
            with st.spinner("📢 Creating communication..."):
                comms_result = comms_agent.run(results["Qualify Agent"])
                results["Communication Agent"] = str(getattr(comms_result, "content", comms_result))
                st.subheader("📢 Communication Agent Result")
                st.markdown(results["Communication Agent"])

        if run_report and "Communication Agent" in results:
            with st.spinner("📊 Generating final report..."):
                report_result = report_agent.run(results["Communication Agent"])
                results["Report Agent"] = str(getattr(report_result, "content", report_result))
                st.subheader("📊 Reporting Agent Final Report")
                st.markdown(results["Report Agent"])

        # Save results to history
        st.session_state.history.append(results)

    # Show conversation history
    if st.session_state.history:
        st.sidebar.subheader("📜 Run History")
        for i, run in enumerate(st.session_state.history[::-1], 1):
            with st.sidebar.expander(f"Run {len(st.session_state.history) - i + 1}: {run['topic']}"):
                for agent, output in run.items():
                    if agent != "topic":
                        st.write(f"**{agent}**: {output[:150]}...")

    # Download final report (if available)
    if st.session_state.history:
        last_run = st.session_state.history[-1]
        if "Report Agent" in last_run:
            st.download_button(
                label="📥 Download Final Report",
                data=last_run["Report Agent"],
                file_name="final_report.txt",
                mime="text/plain"
            )


if __name__ == "__main__":
    main()
