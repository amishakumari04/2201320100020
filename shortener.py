import random, string
from app.models.data import urls

def generate_shortcode(length=6):
    while True:
        code = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        if code not in urls:
            return code

def is_valid_shortcode(shortcode):
    return shortcode.isalnum() and 3 <= len(shortcode) <= 20
