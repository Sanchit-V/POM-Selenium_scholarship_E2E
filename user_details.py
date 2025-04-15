#URL
import calendar
import random
import string
from datetime import datetime

from dateutil.relativedelta import relativedelta
from deep_translator import GoogleTranslator
from faker import Faker
import json

fake = Faker()

with open('user_details.json') as f:
     json_data = json.load(f)

url = "http://localhost:80/"
selected_language = 0     # 1 for English, 0 for Spanish
document_type = random.randint(1, 5) # 1 for NIC     # 2 for Passport    # 3 for FIC    # 4 for RUC    # 5 for Other
Martial_status = random.randint(1, 5) # 1 for Married    # 2 for Single    # 3 for Divorced   # 4 for Widowed      # 5 for Separated
Financially_Dependent = random.randint(0, 1)   # 0 for No  # 1 for Yes
Has_Children = random.randint(0, 1)   # 0 for No  # 1 for Yes
additional_emails_to_be_added = random.randint(1, 5)
number_of_additional_phone=2
number_of_additional_whatsapp=1
total_additionals = number_of_additional_phone + number_of_additional_whatsapp
housing_type = random.randint(1, 2)   # 1 for department    # 2 for House
housing_conditions = random.randint(1, 3) # 1 for Family     # 2 for Own     # 3 for Rented
additional_type = random.randint(1, 8) # 1-Google 2-Facebook 3-Instagram 4-Referred 5-Company 6-Agreement 7-University 8-Speech 9-Webinar

additional_education = random.randint(0, 2)

education_level_1 = random.randint(1, 4) # 1-Postgraduate 2-University 3-Technical 4-High School
education_level_2 = random.randint(1, 4) # 1-Postgraduate 2-University 3-Technical 4-High School
education_level_3 = random.randint(1, 4) # 1-Postgraduate 2-University 3-Technical 4-High School
online_mode_study = random.randint(0, 1) # 0 for No, 1 for Yes

training_type_university = random.randint(0, 1) # 0 for No, 1 for Yes

training_type_employment = random.randint(0, 1) # 0 for No, 1 for Yes

training_type_second_language = 1 #random.randint(0, 1) # 0 for No, 1 for Yes

currently_working =   random.randint(0, 1) # 0 for No, 1 for Yes

work_category =  random.randint(0, 1) # 1 for Dependent, 0 for Independent

seniority_position = random.randint(1, 6) # Enter digits 1 to 6

additional_references = random.randint(0, 2) # Enter digits 0 to 2

have_degree_checkbox = random.randint(0, 1)  # 0 for no(Check the checkbox) 1 for yes(Un-check the checkbox)

time_long = 3
time_med = 2
time_short = 1


access_code = json_data['access_code']
previous_access_code = json_data['previous_access_code']

fake_date = fake.date_object()

dob_Spanish = fake_date.strftime("%d%m%Y")

dob_English = fake_date.strftime("%m%d%Y")


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
Nationality = "India"#random.choice(json_data['countries_visited'])#fake.country()

def generate_financials():

    income = random.randint(10_000_000, 99_999_999)
    expense = int(income * random.uniform(0.5, 0.95))

    return {
        "income": income,
        "expense": expense
    }

# Example usage
finances = generate_financials()


# Monthly_Income = json_data['Monthly_Income']
# Monthly_Expense = json_data['Monthly_Expense']
Monthly_Income = finances['income']
Monthly_Expense = finances['expense']

# print(Monthly_Income)
# print(Monthly_Expense)

#Range_0to4 = json_data['range_0to4']
# Range_5to12 = json_data['range_5to12']
# Range_13to18 = json_data['range_13to18']
# Range_18plus = json_data['range_18plus']
Range_0to4 = random.randint(0,99)
Range_5to12 = random.randint(0,99)
Range_13to18 = random.randint(0,99)
Range_18plus = random.randint(0,99)

# print(Range_0to4)
# print(Range_5to12)
# print(Range_13to18)
# print(Range_18plus)


# email_Ids = json_data['email_ids']


email_Ids = [fake.email() for _ in range(5)]

# print(email_Ids)

# default_phone = json_data['default_phone']
def generate_phone_number():
    length = random.randint(10, 20)
    return str(random.randint(10**(length - 1), 10**length - 1))

# Example usage
default_phone = generate_phone_number()
#print(default_phone)

# default_whatsapp = json_data['default_whatsapp']
default_whatsapp = generate_phone_number()
#print(default_whatsapp)

#additional_numbers = json_data['additional_phones']


additional_numbers = [generate_phone_number() for _ in range(3)]

additional_1 = additional_numbers[0]
additional_2 = additional_numbers[1]
additional_3 = additional_numbers[2]

# print(additional_1)
# print(additional_2)
# print(additional_3)

#countries = json_data['countries_visited']
country_0 =fake.country() #random.choice(json_data['countries_visited'])
#print(country_0)
country_1 =fake.country() #random.choice(json_data['countries_visited'])
#print(country_1)
country_2 =fake.country() #random.choice(json_data['countries_visited'])
#print(country_2)
country_3 =fake.country() #random.choice(json_data['countries_visited'])
#print(country_3)
country_4 =fake.country() #random.choice(json_data['countries_visited'])
#print(country_4)

# home_address = json_data['home_address']
home_address = fake.address().replace('\n', ', ')
#print(home_address)

# zip_code = json_data['zip_code']

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
# Degree = json_data['Degree']
#Starting_Date = json_data['Starting_Date']
#Graduation_Date = json_data['Graduation_Date']

University_Institution_1 = University_Institution[0]
#print(University_Institution_1)
degree_1 = random.choice(json_data['Degree'])
#print(degree_1)

#starting_Date_0 = random.choice(json_data['Starting_Date'])
#graduation_Date_0 = random.choice(json_data['Graduation_Date'])
fake_date = fake.date_between(start_date='-10y', end_date='-5y')
starting_Date_0 = fake_date.strftime("%m%Y")
starting_datetime = datetime.strptime(starting_Date_0, "%m%Y")
graduation_datetime = starting_datetime + relativedelta(years=5)
graduation_Date_0 = graduation_datetime.strftime("%m%Y")
print(starting_Date_0)
print(graduation_Date_0)

University_Institution_2 = University_Institution[1]
#print(University_Institution_2)

degree_2 = random.choice(json_data['Degree'])
#print(degree_2)

#starting_Date_1 = random.choice(json_data['Starting_Date'])
starting_Date_1 = fake_date.strftime("%m%Y")
starting_datetime = datetime.strptime(starting_Date_1, "%m%Y")
graduation_datetime = starting_datetime + relativedelta(years=5)
graduation_Date_1 = graduation_datetime.strftime("%m%Y")
print(starting_Date_1)
print(graduation_Date_1)
#graduation_Date_1 = random.choice(json_data['Graduation_Date'])
# print(starting_Date_1)
# print(graduation_Date_1)

University_Institution_3 = University_Institution[2]
#print(University_Institution_3)
degree_3 = random.choice(json_data['Degree'])
#print(degree_3)

# starting_Date_2 = random.choice(json_data['Starting_Date'])
# graduation_Date_2 = random.choice(json_data['Graduation_Date'])
starting_Date_2 = fake_date.strftime("%m%Y")
starting_datetime = datetime.strptime(starting_Date_2, "%m%Y")
graduation_datetime = starting_datetime + relativedelta(years=5)
graduation_Date_2 = graduation_datetime.strftime("%m%Y")
print(starting_Date_2)
print(graduation_Date_2)
# print(starting_Date_2)
# print(graduation_Date_2)

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

Landline_Nation = fake.country()#random.choice(json_data['countries_visited'])
#print(Landline_Nation)
Mobile_Nation = fake.country()#random.choice(json_data['countries_visited'])
#print(Mobile_Nation)
Base_Folder_Path = "C:\\Users\\Sanchit\\Desktop\\scholarship-POM_E2E\\Upload_Files"

def pdf_file_path():
    random_number= random.randint(1,15)
    return random_number

def jpg_file_path():
    random_number = random.randint(1,9)
    return "a" + str(random_number)

Passport_File = Base_Folder_Path + "\\" +str(pdf_file_path()) + ".pdf"
print(Passport_File)
Curriculum_File = Base_Folder_Path + "\\" +str(pdf_file_path()) + ".pdf"
print(Curriculum_File)
Letter_Of_Motive = Base_Folder_Path + "\\" +str(jpg_file_path()) + ".jpg"
print(Letter_Of_Motive)
Other_Document = Base_Folder_Path + "\\" +str(jpg_file_path()) + ".jpg"
print(Other_Document)
Degree = Base_Folder_Path + "\\" +str(jpg_file_path()) + ".jpg"
print(Degree)
Transcript = Base_Folder_Path + "\\" +str(pdf_file_path()) + ".pdf"
print(Transcript)
Graduation_Certificate = Base_Folder_Path + "\\" +str(pdf_file_path()) + ".pdf"
print(Graduation_Certificate)
Letter_Of_Commitment = Base_Folder_Path + "\\" +str(pdf_file_path()) + ".pdf"
print(Letter_Of_Commitment)






ref1_FirstName = fake.first_name()
ref1_LastName = fake.last_name()
#print(ref1_FirstName +' '+ref1_LastName)
ref1_Pos_Occupation = fake.job()
#print(ref1_Pos_Occupation)
ref1_email = fake.email()
#print(ref1_email)
ref1_phone_number = generate_phone_number()
ref1_landline_number = generate_phone_number()
ref1_phone_CC = fake.country()#random.choice(json_data['countries_visited'])
ref1_landline_CC = fake.country()#random.choice(json_data['countries_visited'])

ref2_FirstName = fake.first_name()
ref2_LastName = fake.last_name()
#print(ref2_FirstName +' '+ref2_LastName)
ref2_Pos_Occupation = fake.job()
#print(ref2_Pos_Occupation)
ref2_email = fake.email()
#print(ref2_email)
ref2_phone_number = generate_phone_number()
ref2_landline_number = generate_phone_number()
ref2_phone_CC =fake.country() #random.choice(json_data['countries_visited'])
ref2_landline_CC =fake.country() #random.choice(json_data['countries_visited'])

ref3_FirstName = fake.first_name()
ref3_LastName = fake.last_name()
#print(ref3_FirstName +' '+ref3_LastName)
ref3_Pos_Occupation = fake.job()
#print(ref3_Pos_Occupation)
ref3_email = fake.email()
#print(ref3_email)
ref3_phone_number = generate_phone_number()
ref3_landline_number = generate_phone_number()
ref3_phone_CC = fake.country()#random.choice(json_data['countries_visited'])
ref3_landline_CC = fake.country()#random.choice(json_data['countries_visited'])

ref4_FirstName = fake.first_name()
ref4_LastName = fake.last_name()
#print(ref4_FirstName +' '+ref4_LastName)
ref4_Pos_Occupation = fake.job()
#print(ref4_Pos_Occupation)
ref4_email = fake.email()
#print(ref4_email)
ref4_phone_number = generate_phone_number()
ref4_landline_number = generate_phone_number()
ref4_phone_CC = fake.country()#random.choice(json_data['countries_visited'])
ref4_landline_CC = fake.country()#random.choice(json_data['countries_visited'])

ref5_FirstName = fake.first_name()
ref5_LastName = fake.last_name()
#print(ref5_FirstName +' '+ref5_LastName)
ref5_Pos_Occupation = fake.job()
#print(ref5_Pos_Occupation)
ref5_email = fake.email()
#print(ref5_email)
ref5_phone_number = generate_phone_number()
ref5_landline_number = generate_phone_number()
ref5_phone_CC =fake.country() #random.choice(json_data['countries_visited'])
ref5_landline_CC =fake.country() #random.choice(json_data['countries_visited'])


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

    country_0 = GoogleTranslator(source='en', target='es').translate(country_0)
    country_1 = GoogleTranslator(source='en', target='es').translate(country_1)
    country_2 = GoogleTranslator(source='en', target='es').translate(country_2)
    country_3 = GoogleTranslator(source='en', target='es').translate(country_3)
    country_4 = GoogleTranslator(source='en', target='es').translate(country_4)


else:
    country_0 = country_0
    country_1 = country_1
    country_2 = country_2
    country_3 = country_3
    country_4 = country_4


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
    ref1_phone_CC = GoogleTranslator(source='en', target='es').translate(ref1_phone_CC)
    ref1_landline_CC = GoogleTranslator(source='en', target='es').translate( ref1_landline_CC)

    ref2_phone_CC = GoogleTranslator(source='en', target='es').translate(ref2_phone_CC)
    ref2_landline_CC = GoogleTranslator(source='en', target='es').translate(ref2_landline_CC)

    ref3_phone_CC = GoogleTranslator(source='en', target='es').translate(ref3_phone_CC)
    ref3_landline_CC = GoogleTranslator(source='en', target='es').translate(ref3_landline_CC)

    ref4_phone_CC = GoogleTranslator(source='en', target='es').translate(ref4_phone_CC)
    ref4_landline_CC = GoogleTranslator(source='en', target='es').translate(ref4_landline_CC)

    ref5_phone_CC = GoogleTranslator(source='en', target='es').translate(ref5_phone_CC)
    ref5_landline_CC = GoogleTranslator(source='en', target='es').translate(ref5_landline_CC)

else:
    ref1_phone_CC = ref1_phone_CC
    ref1_landline_CC = ref1_landline_CC

    ref2_phone_CC = ref2_phone_CC
    ref2_landline_CC = ref2_landline_CC

    ref3_phone_CC = ref3_phone_CC
    ref3_landline_CC = ref3_landline_CC

    ref4_phone_CC = ref4_phone_CC
    ref3_landline_CC = ref3_landline_CC

    ref5_phone_CC = ref5_phone_CC
    ref5_landline_CC = ref5_landline_CC
