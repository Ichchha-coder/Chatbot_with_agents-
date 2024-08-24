# app/agents.py

from dateutil import parser

class ToolAgent:
    def parse_date(self, user_input):
        try:
            return parser.parse(user_input, fuzzy=True).date().isoformat()
        except ValueError:
            return None
