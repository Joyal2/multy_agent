# agents/research_agent.py
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

class ResearchAgent:
    def __init__(self, api_key):
        self.llm = ChatOpenAI(openai_api_key=api_key, model="gpt-4o-mini")
        self.prompt = PromptTemplate(
            input_variables=["topic"],
            template="Research the following topic and return key insights:\n\n{topic}"
        )

    def run(self, topic: str):
        chain = self.prompt | self.llm
        return chain.invoke({"topic": topic})
