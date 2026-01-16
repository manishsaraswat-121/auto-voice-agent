import json
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from app.config import OPENROUTER_API_KEY, OPENROUTER_BASE_URL, LLM_MODEL


class ConversationAgent:
    def __init__(self):
        self.llm = ChatOpenAI(
            model=LLM_MODEL,
            temperature=0,
            openai_api_key=OPENROUTER_API_KEY,
            openai_api_base=OPENROUTER_BASE_URL
        )

    def extract_slots(self, user_text: str) -> dict:
        system_prompt = """
You are a slot extraction engine.

Rules:
- Output ONLY valid JSON
- No markdown
- No explanation

Schema:
{
  "intent": "book_test_drive",
  "vehicle_type": "SUV|Sedan|Hatchback",
  "date": "string",
  "time": "string"
}
"""
        response = self.llm.invoke([
            HumanMessage(content=system_prompt + "\nInput:\n" + user_text)
        ])
        #print(response)

        content = response.content.strip()

        if not content:
            raise ValueError("LLM returned empty response")

        try:
            return json.loads(content)
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON from LLM: {content}")
