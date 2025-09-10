import os
from dotenv import load_dotenv, dotenv_values
import random
import string
from datetime import datetime
from datetime import date
from deep_translator import GoogleTranslator
from faker import Faker
import json

from dateutil.relativedelta import relativedelta

load_dotenv()
fake = Faker()

with open('Data/user_details.json') as f:
     json_data = json.load(f)

time_long = int(os.getenv("TIME_LONG"))  # Default to 5 seconds if not set
time_med = int(os.getenv("TIME_MED"))  # Default to 2 seconds if not set
time_short = int(os.getenv("TIME_SHORT"))  # Default to 1 second if not set
selected_language = os.getenv("SELECTED_LANGUAGE")


def get_language_code(selected_language):
    # Normalize input (lowercase and remove accents for consistency)
    normalized = selected_language.strip().lower()

    language_map = {
        0: {"spanish", "español", "espana", "españa"},
        1: {"english", "inglés", "united states", "estados unidos"},
    }

    for code, variants in language_map.items():
        if normalized in variants:
            return code

    print("Please select a valid language option.")
    return None

def generate_phone_number():
    length = random.randint(10, 20)
    return str(random.randint(10**(length - 1), 10**length - 1))


selected_language = get_language_code(selected_language)

additional_references =  random.randint(0, 2) 
ref_First_Name = [fake.first_name() for _ in range(5)]
ref_Last_Name = [fake.last_name() for _ in range(5)]
ref_Pos_Occupation = [fake.job() for _ in range(5)]
ref_Emails = [fake.email() for _ in range(5)]
ref_phone_numbers = [generate_phone_number() for _ in range(5)]
ref_landline_numbers = [generate_phone_number() for _ in range(5)]
ref_phone_CC = [random.choice(json_data['countries_visited']) for _ in range(5)]
ref_landline_CC = [random.choice(json_data['countries_visited']) for _ in range(5)]


if selected_language == 0:
    for i in range(5):
        ref_phone_CC[i] = GoogleTranslator(source='en', target='es').translate(ref_phone_CC[i])
        ref_landline_CC[i] = GoogleTranslator(source='en', target='es').translate( ref_landline_CC[i])

else:
    ref_phone_CC = ref_phone_CC
    ref_landline_CC = ref_landline_CC

