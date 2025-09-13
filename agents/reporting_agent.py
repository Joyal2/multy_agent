from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

class ReportingAgent:
    def __init__(self, api_key):
        self.llm = ChatOpenAI(api_key=api_key, model="gpt-4o-mini")
        self.prompt = PromptTemplate(
            input_variables=["comms"],
            template=(
                "You are a reporting agent. Convert the following communication draft:\n\n"
                "{comms}\n\n"
                "into a **well-structured final report** with:\n"
                "- Title\n"
                "- Executive Summary\n"
                "- Key Insights (bullet points)\n"
                "- Conclusion"
            )
        )

    def run(self, comms: str):
        chain = self.prompt | self.llm
        return chain.invoke({"comms": comms})
