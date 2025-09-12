import os
from dotenv import load_dotenv, dotenv_values
import random
import string
from datetime import datetime
from datetime import date
from deep_translator import GoogleTranslator
from faker import Faker
import json
from Model.Employement_Information_Page_Model import EmploymentInformationPageData, EmploymentStatusData, PositionInformationData, EmploymentAddressData, EmploymentContactData

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

currently_working = 1 #random.randint(0, 1) # 0 for No, 1 for Yes

Institution_Name = fake.company()

Position = fake.job()

Area = random.choice(json_data['Area'])

Activity = fake.job()

work_category =  random.randint(0, 1) # 1 for Dependent, 0 for Independent

seniority_position =  random.randint(1, 6) # Enter digits 1 to 6

Monthly_Salary = random.randint(10_000_000_000, 99_999_999_999)

Emp_Currency = random.randint(1, 26)

Emp_Country = json_data['Emp_Country']
Emp_State = json_data['Emp_State']
Emp_City = json_data['Emp_City']

def zip(length=10):
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choices(chars, k=length))

Zip_Code = zip()
Address = fake.address().replace('\n', ', ')

def generate_phone_number():
    length = random.randint(10, 20)
    return str(random.randint(10**(length - 1), 10**length - 1))


Landline_Phone = generate_phone_number()

Phone_Mobile =generate_phone_number()

Website = fake.url()


Landline_Nation = random.choice(json_data['countries_visited']) #fake.country()

Mobile_Nation = random.choice(json_data['countries_visited']) #fake.country()

if selected_language == 0:
    Emp_Country = GoogleTranslator(source='en', target='es').translate(Emp_Country)
    Emp_State = GoogleTranslator(source='en', target='es').translate(Emp_State)
    Emp_City = GoogleTranslator(source='en', target='es').translate(Emp_City)
    Landline_Nation = GoogleTranslator(source='en', target='es').translate(Landline_Nation)
    Mobile_Nation = GoogleTranslator(source='en', target='es').translate(Mobile_Nation)

else:
    Emp_Country =  Emp_Country
    Emp_State = Emp_State
    Emp_City = Emp_City
    Landline_Nation = Landline_Nation
    Mobile_Nation = Mobile_Nation


class EmploymentInformationPageMother:
    @staticmethod
    def get() -> EmploymentInformationPageData:
        return EmploymentInformationPageData(
            EmploymentStatusData=EmploymentStatusData(currently_working= currently_working),
            
            PositionInformationData=PositionInformationData(
               Institution_Name= Institution_Name,
                Position= Position,
                Area= Area,
                Activity= Activity,
                work_category= work_category,
                seniority_position= seniority_position,
                Monthly_Salary= Monthly_Salary,
                Emp_Currency= Emp_Currency,
            ),
            EmploymentAddressData=EmploymentAddressData(
                Emp_Country= Emp_Country,
                Emp_State= Emp_State,
                Emp_City= Emp_City,
                Zip_Code= Zip_Code,
                Address= Address,
            ),
            EmploymentContactData=EmploymentContactData(
            Landline_Phone= Landline_Phone,
            Phone_Mobile= Phone_Mobile,
            Website= Website,
            Landline_Nation= Landline_Nation,
            Mobile_Nation= Mobile_Nation,
        )
        )






 