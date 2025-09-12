import os
from dotenv import load_dotenv, dotenv_values
import random
import string
from datetime import datetime
from datetime import date
from deep_translator import GoogleTranslator
from faker import Faker
from Model.Personal_Page_Model import PersonalDetailsPageModel, BasicData, BirthData, FinancialData, FamilyDetailsData  

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

selected_language = get_language_code(selected_language)

document_type = random.randint(1, 5) # 1 for NIC # 2 for Passport    # 3 for FIC    # 4 for RUC    # 5 for Other

def alphanumeric_doc_number(length=10):
    pattern = '?' * (length // 2) + '#' * (length - length // 2)
    return fake.bothify(text=pattern).upper()
Document_number = alphanumeric_doc_number()

Martial_status = random.randint(1, 5) # 1 for Married    # 2 for Single    # 3 for Divorced   # 4 for Widowed      # 5 for Separated
Profession = fake.job()

#today = date.today()
fake_date = fake.date_object()
new_year_eighteen = fake_date - relativedelta(years=18)
fake_date = fake.date_between(start_date='-100y', end_date=new_year_eighteen)
dob_Spanish = new_year_eighteen.strftime("%d%m%Y")
dob_English = new_year_eighteen.strftime("%m%d%Y")
Country = json_data['Country']
State = json_data['State']
City = json_data['City']
Nationality = random.choice(json_data['countries_visited'])


Currency = random.randint(1, 26)
def generate_financials():

    income = random.randint(10_000_000, 99_999_999)
    expense = int(income * random.uniform(0.5, 0.95))

    return {
        "income": income,
        "expense": expense
    }

finances = generate_financials()

Monthly_Income = finances['income']
Monthly_Expense = finances['expense']
Financially_Dependent = random.randint(0, 1)

Has_Children = random.randint(0, 1) 
Range_0to4 = random.randint(0,99)
Range_5to12 = random.randint(0,99)
Range_13to18 = random.randint(0,99)
Range_18plus = random.randint(0,99)


Emp_Currency = random.randint(1, 26) # 1 for USD    # 2 for EUR    # 3 for GBP    # 4 for JPY    # 5 for CNY    # 6 for INR    # 7 for RUB    # 8 for BRL    # 9 for CAD    # 10 for AUD   # 11 for CHF   # 12 for SEK   # 13 for NZD   # 14 for MXN   # 15 for SGD   # 16 for HKD   # 17 for KRW   # 18 for NOK   # 19 for TRY   # 20 for ZAR   # 21 for DKK   # 22 for PLN   # 23 for TWD   # 24 for THB   # 25 for IDR   # 26 for MYR
   # 0 for No    # 1 for Yes
  # 0 for No     # 1 for Yes





Range_0to4 = random.randint(0,99)
Range_5to12 = random.randint(0,99)
Range_13to18 = random.randint(0,99)
Range_18plus = random.randint(0,99)

if selected_language == 1:
    Date_Of_Birth = dob_English

else:
    Date_Of_Birth = dob_Spanish


if selected_language == 0:
    Profession = GoogleTranslator(source='en', target='es').translate(Profession)
    Country = GoogleTranslator(source='en', target='es').translate(Country)
    State = GoogleTranslator(source='en', target='es').translate(State)
    City = GoogleTranslator(source='en', target='es').translate(City)
    Nationality = GoogleTranslator(source='en', target='es').translate(Nationality)

else:
    Profession = Profession
    Country = Country
    State = State
    City = City
    Nationality = Nationality

class PersonalPageMother:
    @staticmethod
    def get() -> PersonalDetailsPageModel:
        return PersonalDetailsPageModel(
            BasicData=BasicData(
                document_type=document_type,
                Document_number=Document_number,
                Martial_status=Martial_status,
                Profession=Profession
            ),
            BirthData=BirthData(
                Date_Of_Birth=Date_Of_Birth,
                Country=Country,
                State=State,
                City=City,
                Nationality=Nationality
            ),
            FinancialData=FinancialData(
                Currency=Currency,
                Monthly_Income=Monthly_Income,
                Monthly_Expense=Monthly_Expense,
                Financially_Dependent=Financially_Dependent
            ),
            FamilyDetailsData=FamilyDetailsData(
                Has_Children=Has_Children,
                Range_0to4=Range_0to4,
                Range_5to12=Range_5to12,
                Range_13to18=Range_13to18,
                Range_18plus=Range_18plus
            ))

         
