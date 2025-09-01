#URL
import os
from dotenv import load_dotenv, dotenv_values
import calendar
import random
import string
from datetime import datetime
from datetime import date

from dateutil.relativedelta import relativedelta
from deep_translator import GoogleTranslator
from faker import Faker
import json
import os

load_dotenv()
fake = Faker()

with open('Data/user_details.json') as f:
     json_data = json.load(f)

url = os.getenv("URL")  #"https://sales-scholarship-application-requests-develop-iymj66chvq-uc.a.run.app/"

selected_language = os.getenv("SELECTED_LANGUAGE")
print(selected_language)
Base_Folder_Path = "/home/seluser/Upload_Files"
number_of_pdf = 15
number_of_jpg = 9


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
Martial_status = random.randint(1, 5) # 1 for Married    # 2 for Single    # 3 for Divorced   # 4 for Widowed      # 5 for Separated
Currency = random.randint(1, 26)
Emp_Currency = random.randint(1, 26) # 1 for USD    # 2 for EUR    # 3 for GBP    # 4 for JPY    # 5 for CNY    # 6 for INR    # 7 for RUB    # 8 for BRL    # 9 for CAD    # 10 for AUD   # 11 for CHF   # 12 for SEK   # 13 for NZD   # 14 for MXN   # 15 for SGD   # 16 for HKD   # 17 for KRW   # 18 for NOK   # 19 for TRY   # 20 for ZAR   # 21 for DKK   # 22 for PLN   # 23 for TWD   # 24 for THB   # 25 for IDR   # 26 for MYR
Financially_Dependent = random.randint(0, 1)   # 0 for No    # 1 for Yes
Has_Children = random.randint(0, 1)   # 0 for No     # 1 for Yes
additional_emails_to_be_added = random.randint(1, 5)
number_of_additional_phone=2
number_of_additional_whatsapp=1
total_additionals = number_of_additional_phone + number_of_additional_whatsapp
housing_type = random.randint(1, 2)   # 1 for department    # 2 for House
housing_conditions = random.randint(1, 3) # 1 for Family     # 2 for Own     # 3 for Rented
additional_type = random.randint(1, 8) # 1-Google 2-Facebook 3-Instagram 4-Referred 5-Company 6-Agreement 7-University 8-Speech 9-Webinar

additional_education = random.randint(0, 2)

education_level = [random.randint(1, 4) for _ in range(3)] # 1-Postgraduate 2-University 3-Technical 4-High School
online_mode_study = random.randint(0, 1) # 0 for No, 1 for Yes

training_type_university = random.randint(0, 1) # 0 for No, 1 for Yes

training_type_employment = random.randint(0, 1) # 0 for No, 1 for Yes

training_type_second_language =   random.randint(0, 1) # 0 for No, 1 for Yes

currently_working = random.randint(0, 1) # 0 for No, 1 for Yes

work_category =  random.randint(0, 1) # 1 for Dependent, 0 for Independent

seniority_position =  random.randint(1, 6) # Enter digits 1 to 6

additional_references =  random.randint(0, 2)  

have_degree_checkbox =  random.randint(0, 1)  # 0 for no(Check the checkbox) 1 for yes(Un-check the checkbox)

time_long = int(os.getenv("TIME_LONG"))  # Default to 5 seconds if not set
time_med = int(os.getenv("TIME_MED"))  # Default to 2 seconds if not set
time_short = int(os.getenv("TIME_SHORT"))  # Default to 1 second if not set

file_type = random.randint(0, 1)  #0 for .pdf and 1 for .jpg


access_code = os.getenv("ACCESS_CODE")    #json_data['access_code']
previous_access_code = os.getenv("PREVIOUS_ACCESS_CODE")       #json_data['previous_access_code']

print(access_code)
print(previous_access_code)


today = date.today()
fake_date = fake.date_object()
new_year_eighteen = fake_date - relativedelta(years=18)
fake_date = fake.date_between(start_date='-100y', end_date=new_year_eighteen)

dob_Spanish = new_year_eighteen.strftime("%d%m%Y")
dob_English = new_year_eighteen.strftime("%m%d%Y")



#Document_number = json_data['Document_number']

def alphanumeric_doc_number(length=10):
    pattern = '?' * (length // 2) + '#' * (length - length // 2)
    return fake.bothify(text=pattern).upper()

#print(alphanumeric_doc_number())

Document_number = alphanumeric_doc_number()
#print(Document_number)

Profession = fake.job()
Country = json_data['Country']
State = json_data['State']
City = json_data['City']
Nationality = random.choice(json_data['countries_visited'])#fake.country()

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


Range_0to4 = random.randint(0,99)
Range_5to12 = random.randint(0,99)
Range_13to18 = random.randint(0,99)
Range_18plus = random.randint(0,99)




email_Ids = [fake.email() for _ in range(5)]

print(email_Ids)


def generate_phone_number():
    length = random.randint(10, 20)
    return str(random.randint(10**(length - 1), 10**length - 1))


default_phone = generate_phone_number()

default_whatsapp = generate_phone_number()



additional_numbers = [generate_phone_number() for _ in range(3)]



country = [random.choice(json_data['countries_visited']) for _ in range(5)] #fake.country()

home_address = fake.address().replace('\n', ', ')

def zip(length=10):
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choices(chars, k=length))

zip_code = zip()
#print(zip_code)

# Text_Additional_field = json_data['text_additional_field']
description = ' '.join(fake.words(nb=30))
Text_Additional_field=description
#print(Text_Additional_field)

#University_Institution = json_data['University/Institution']
University_Institution = [fake.company() + " University" for _ in range(3)]



#print(University_Institution_1)
degree = [random.choice(json_data['Degree']) for _ in range(3)]
#print(degree_1)


fake_date = fake.date_between(start_date='-10y', end_date='-5y')
starting_Date = [fake_date.strftime("%m%Y") for _ in range(3)]
starting_datetime = datetime.strptime(starting_Date[0], "%m%Y")
graduation_datetime = starting_datetime + relativedelta(years=5)
graduation_Date = [graduation_datetime.strftime("%m%Y") for _ in range(3)]


Other_Expertise = random.choice(json_data['Other_Expertise'])
#print(Other_Expertise)

#Institution_Name = json_data['Institution_Name']
Institution_Name = fake.company()
#print(Institution_Name)

#Position = json_data['Position']
Position = fake.job()
#print(Position)

Area = random.choice(json_data['Area'])
#print(Area)
#Activity = json_data['Activity']
Activity = fake.job()
#print(Activity)

#Monthly_Salary = json_data['Monthly_Salary']

Monthly_Salary = random.randint(10_000_000_000, 99_999_999_999)
#print(Monthly_Salary)

Emp_Country = json_data['Emp_Country']
Emp_State = json_data['Emp_State']
Emp_City = json_data['Emp_City']

#Zip_Code = json_data['Zip_Code']
Zip_Code = zip()
#print(Zip_Code)
Address = fake.address().replace('\n', ', ')
#print(Address)

#Landline_Phone = json_data['Landline_Phone']
Landline_Phone = generate_phone_number()
#print(landline_Phone)
#Phone_Mobile = json_data['Phone_Mobile']
Phone_Mobile =generate_phone_number()
#print(Phone_Mobile)
#Website = json_data['Website']
Website = fake.url()
#print(Website)

Landline_Nation = random.choice(json_data['countries_visited']) #fake.country()
#print(Landline_Nation)
Mobile_Nation = random.choice(json_data['countries_visited']) #fake.country()
#print(Mobile_Nation)


#print("***********************************************************")
ref_First_Name = [fake.first_name() for _ in range(5)]
ref_Last_Name = [fake.last_name() for _ in range(5)]
ref_Pos_Occupation = [fake.job() for _ in range(5)]
ref_Emails = [fake.email() for _ in range(5)]
ref_phone_numbers = [generate_phone_number() for _ in range(5)]
ref_landline_numbers = [generate_phone_number() for _ in range(5)]
ref_phone_CC = [random.choice(json_data['countries_visited']) for _ in range(5)]
ref_landline_CC = [random.choice(json_data['countries_visited']) for _ in range(5)]




if selected_language == 1:
    user_greeting = "Welcome to the online scholarship application form"
    expected_message = "Login successful"
    Date_Of_Birth = dob_English

else:
    user_greeting = "Bienvenido al formulario de solicitud de beca online"
    expected_message = "Inicio de sesión correcto"
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


if selected_language == 0:
    for i in range (5):
        country[i] = GoogleTranslator(source='en', target='es').translate(country[i])

else:
    country = country


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

if selected_language == 0:
    for i in range(5):
        ref_phone_CC[i] = GoogleTranslator(source='en', target='es').translate(ref_phone_CC[i])
        ref_landline_CC[i] = GoogleTranslator(source='en', target='es').translate( ref_landline_CC[i])

    # print(ref_phone_CC)
    # print(ref_landline_CC)

    # ref2_phone_CC = GoogleTranslator(source='en', target='es').translate(ref2_phone_CC)
    # ref2_landline_CC = GoogleTranslator(source='en', target='es').translate(ref2_landline_CC)

    # ref3_phone_CC = GoogleTranslator(source='en', target='es').translate(ref3_phone_CC)
    # ref3_landline_CC = GoogleTranslator(source='en', target='es').translate(ref3_landline_CC)

    # ref4_phone_CC = GoogleTranslator(source='en', target='es').translate(ref4_phone_CC)
    # ref4_landline_CC = GoogleTranslator(source='en', target='es').translate(ref4_landline_CC)

    # ref5_phone_CC = GoogleTranslator(source='en', target='es').translate(ref5_phone_CC)
    # ref5_landline_CC = GoogleTranslator(source='en', target='es').translate(ref5_landline_CC)

else:
    ref_phone_CC = ref_phone_CC
    ref_landline_CC = ref_landline_CC

    print(ref_phone_CC)
    print(ref_landline_CC)

    # ref2_phone_CC = ref2_phone_CC
    # ref2_landline_CC = ref2_landline_CC

    # ref3_phone_CC = ref3_phone_CC
    # ref3_landline_CC = ref3_landline_CC

    # ref4_phone_CC = ref4_phone_CC
    # ref3_landline_CC = ref4_landline_CC

    # ref5_phone_CC = ref5_phone_CC
    # ref5_landline_CC = ref5_landline_CC
