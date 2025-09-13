from flask import Flask, render_template, request
import os
from dotenv import load_dotenv

# Import agents
from agents.research_agent import ResearchAgent
from agents.qualify_agent import QualifyAgent
from agents.communication_agent import CommunicationAgent
from agents.reporting_agent import ReportingAgent

app = Flask(__name__)

# Load API Key
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("❌ Missing OPENAI_API_KEY in .env file")

# Initialize agents
research_agent = ResearchAgent(api_key)
qualify_agent = QualifyAgent(api_key)
comms_agent = CommunicationAgent(api_key)
report_agent = ReportingAgent(api_key)

@app.route("/", methods=["GET", "POST"])
def index():
    results = {}
    if request.method == "POST":
        topic = request.form["topic"]
        research_result = research_agent.run(topic)
        qualified_result = qualify_agent.run(str(research_result))
        comms_result = comms_agent.run(str(qualified_result))
        report_result = report_agent.run(str(comms_result))

        results = {
            "research": research_result,
            "qualify": qualified_result,
            "comms": comms_result,
            "report": report_result,
        }

    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)
