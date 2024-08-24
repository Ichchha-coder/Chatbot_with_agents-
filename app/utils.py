# app/utils.py

import re

def validate_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

def validate_phone(phone):
    phone_regex = r'^\+?[1-9]\d{1,14}$'
    return re.match(phone_regex, phone) is not None
