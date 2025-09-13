from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

class CommunicationAgent:
    def __init__(self, api_key):
        self.llm = ChatOpenAI(api_key=api_key, model="gpt-4o-mini")
        self.prompt = PromptTemplate(
            input_variables=["qualified"],
            template=(
                "You are a communication agent. Take the following qualified insights:\n\n"
                "{qualified}\n\n"
                "Reframe them into a **clear, concise, and professional summary** "
                "that can be shared with a non-technical audience."
            )
        )

    def run(self, qualified: str):
        chain = self.prompt | self.llm
        return chain.invoke({"qualified": qualified})
