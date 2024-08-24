# app/conversational_form.py

from app.utils import validate_email, validate_phone

class ConversationalFormHandler:
    def __init__(self):
        self.user_info = {}
        self.form_active = False
        self.current_step = None

    def is_form_active(self):
        return self.form_active

    def collect_user_info(self, user_input):
        self.form_active = True
        self.current_step = "name"
        return "Please provide your name."

    def process_form(self, user_input):
        if self.current_step == "name":
            self.user_info["name"] = user_input
            self.current_step = "phone"
            return "Please provide your phone number."

        elif self.current_step == "phone":
            if validate_phone(user_input):
                self.user_info["phone"] = user_input
                self.current_step = "email"
                return "Please provide your email."
            else:
                return "Invalid phone number. Please enter a valid phone number."

        elif self.current_step == "email":
            if validate_email(user_input):
                self.user_info["email"] = user_input
                self.form_active = False
                self.current_step = None
                return f"Thank you, {self.user_info['name']}. We will contact you at {self.user_info['phone']} or {self.user_info['email']}."
            else:
                return "Invalid email. Please enter a valid email address."
