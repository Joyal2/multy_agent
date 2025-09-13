from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

class QualifyAgent:
    def __init__(self, api_key):
        self.llm = ChatOpenAI(api_key=api_key, model="gpt-4o-mini")
        self.prompt = PromptTemplate(
            input_variables=["research"],
            template=(
                "You are a qualification agent. Review the following research insights:\n\n"
                "{research}\n\n"
                "Filter and return only the **3 most relevant, accurate, and high-quality insights**."
            )
        )

    def run(self, research: str):
        chain = self.prompt | self.llm
        return chain.invoke({"research": research})
