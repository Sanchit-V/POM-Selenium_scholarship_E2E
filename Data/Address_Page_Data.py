import os
from dotenv import load_dotenv, dotenv_values
import random
import string
from datetime import datetime
from datetime import date
from deep_translator import GoogleTranslator
from faker import Faker
import json
from Model.Address_Page_Model import AddressPageDetailsModel, ContactDetailsData, ResidenceDetailsData

from dateutil.relativedelta import relativedelta

load_dotenv()
fake = Faker()

with open('Data/user_details.json') as f:
     json_data = json.load(f)

time_long = int(os.getenv("TIME_LONG"))  
time_med = int(os.getenv("TIME_MED"))  
time_short = int(os.getenv("TIME_SHORT"))  
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

selected_language = get_language_code(selected_language)

access_code = os.getenv("ACCESS_CODE")   
previous_access_code = os.getenv("PREVIOUS_ACCESS_CODE")   
additional_emails_to_be_added = random.randint(1, 5)
number_of_additional_phone=2
number_of_additional_whatsapp=1
total_additionals = number_of_additional_phone + number_of_additional_whatsapp
email_Ids = [fake.email() for _ in range(5)]

print(email_Ids)


def generate_phone_number():
    length = random.randint(10, 20)
    return str(random.randint(10**(length - 1), 10**length - 1))


default_phone = generate_phone_number()

default_whatsapp = generate_phone_number()



additional_numbers = [generate_phone_number() for _ in range(3)]

country = [random.choice(json_data['countries_visited']) for _ in range(5)] #fake.country()

housing_type = random.randint(1, 2)   # 1 for department    # 2 for House
housing_conditions = random.randint(1, 3) # 1 for Family     # 2 for Own     # 3 for Rented
Country = json_data['Country']
State = json_data['State']
City = json_data['City']
home_address = fake.address().replace('\n', ', ')

def zip(length=10):
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choices(chars, k=length))

zip_code = zip()

if selected_language == 0:
    for i in range (5):
        country[i] = GoogleTranslator(source='en', target='es').translate(country[i])

else:
    country = country

class AddressPageMother:
    @staticmethod
    def get() -> AddressPageDetailsModel:
        return AddressPageDetailsModel(
            ContactDetailsData=ContactDetailsData(
                additional_emails_to_be_added=additional_emails_to_be_added,
                previous_access_code=previous_access_code,
                access_code=access_code,
                email_Ids=email_Ids,
                default_phone=default_phone,
                default_whatsapp=default_whatsapp,
                number_of_additional_phone=number_of_additional_phone,
                number_of_additional_whatsapp=number_of_additional_whatsapp,
                total_additionals=total_additionals,
                additional_numbers=additional_numbers,
                country=country
            ),
            ResidenceDetailsData=ResidenceDetailsData(
                housing_type=housing_type,
                housing_conditions=housing_conditions,
                Country=Country,
                State=State,
                City=City,
                home_address=home_address,
                zip_code=zip_code
            )
        )
