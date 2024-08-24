# app/chatbot.py

from app.document_handler import DocumentHandler
from app.conversational_form import ConversationalFormHandler
from app.agents import ToolAgent
from app.config import GEMINI_API_KEY
from langchain.llms import Gemini

class Chatbot:
    def __init__(self):
        self.llm = Gemini(api_key=GEMINI_API_KEY)
        self.document_handler = DocumentHandler(self.llm)
        self.form_handler = ConversationalFormHandler()
        self.tool_agent = ToolAgent()

    def process_input(self, user_input):
        if self.form_handler.is_form_active():
            return self.form_handler.process_form(user_input)
        
        if "call me" in user_input.lower():
            return self.form_handler.collect_user_info(user_input)

        return self.document_handler.handle_query(user_input)

    def run(self):
        print("Chatbot is ready to interact with users.")
        while True:
            user_input = input("You: ")
            response = self.process_input(user_input)
            print(f"Bot: {response}")

if __name__ == "__main__":
    bot = Chatbot()
    bot.run()
