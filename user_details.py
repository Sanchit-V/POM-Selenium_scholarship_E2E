#URL
from deep_translator import GoogleTranslator
from faker import Faker
import json

fake = Faker()

with open('user_details.json') as f:
     json_data = json.load(f)

url = "http://localhost:80/"
selected_language = 0     # 1 for English, 0 for Spanish
document_type = 3 # 1 for NIC     # 2 for Passport    # 3 for FIC    # 4 for RUC    # 5 for Other
Martial_status = 2 # 1 for Married    # 2 for Single    # 3 for Divorced   # 4 for Widowed      # 5 for Separated
Financially_Dependent = 1   # 0 for No  # 1 for Yes
Has_Children = 1   # 0 for No  # 1 for Yes
additional_emails_to_be_added = 5
number_of_additional_phone=1
number_of_additional_whatsapp=2
total_additionals = number_of_additional_phone + number_of_additional_whatsapp
housing_type = 1   # 1 for department    # 2 for House
housing_conditions = 1 # 1 for Family     # 2 for Own     # 3 for Rented
additional_type = 1 # 1-Google 2-Facebook 3-Instagram 4-Referred 5-Company 6-Agreement 7-University 8-Speech 9-Webinar

additional_education = 2

education_level_1 = 4 # 1-Postgraduate 2-University 3-Technical 4-High School
education_level_2 = 1 # 1-Postgraduate 2-University 3-Technical 4-High School
education_level_3 = 2 # 1-Postgraduate 2-University 3-Technical 4-High School
online_mode_study = 1 # 0 for No, 1 for Yes
training_type_university = 1 # 0 for No, 1 for Yes
training_type_employment = 1 # 0 for No, 1 for Yes
training_type_second_language = 1 # 0 for No, 1 for Yes

currently_working = 1 # 0 for No, 1 for Yes

work_category =  1 # 1 for Dependent, 0 for Independent

seniority_position = 4 # Enter digits 1 to 6

additional_references = 2 # Enter digits 0 to 2

have_degree_checkbox = 0  # 0 for no(Check the checkbox) 1 for yes(Un-check the checkbox)





access_code = json_data['access_code']
previous_access_code = json_data['previous_access_code']

#dob_English = fake.date_between(start_date='-19y', end_date='today')
dob_English = json_data['dob_English']
dob_Spanish = json_data['dob_Spanish']
Document_number = json_data['Document_number']
Profession = json_data['Profession']
Country = json_data['Country']
State = json_data['State']
City = json_data['City']
Nationality = json_data['Nationality']
Monthly_Income = json_data['Monthly_Income']
Monthly_Expense = json_data['Monthly_Expense']
Range_0to4 = json_data['range_0to4']
Range_5to12 = json_data['range_5to12']
Range_13to18 = json_data['range_13to18']
Range_18plus = json_data['range_18plus']
email_Ids = json_data['email_ids']
default_phone = json_data['default_phone']
default_whatsapp = json_data['default_whatsapp']
additional_numbers = json_data['additional_phones']
additional_1 = additional_numbers[0]
additional_2 = additional_numbers[1]
additional_3 = additional_numbers[2]
countries = json_data['countries_visited']
country_0 = countries[0]
country_1 = countries[1]
country_2 = countries[2]
country_3 = countries[3]
country_4 = countries[4]
home_address = json_data['home_address']
zip_code = json_data['zip_code']
Text_Additional_field = json_data['text_additional_field']

University_Institution = json_data['University/Institution']
Degree = json_data['Degree']
Starting_Date = json_data['Starting_Date']
Graduation_Date = json_data['Graduation_Date']

University_Institution_1 = University_Institution[0]
degree_1 = Degree[0]
starting_Date_0 = Starting_Date[0]
graduation_Date_0 = Graduation_Date[0]

University_Institution_2 = University_Institution[1]
degree_2 = Degree[1]
starting_Date_1 = Starting_Date[1]
graduation_Date_1 = Graduation_Date[1]

University_Institution_3 = University_Institution[2]
degree_3 = Degree[2]
starting_Date_2 = Starting_Date[2]
graduation_Date_2 = Graduation_Date[2]

Other_Expertise = json_data['Other_Expertise']

Institution_Name = json_data['Institution_Name']
Position = json_data['Position']
Area = json_data['Area']
Activity = json_data['Activity']
Monthly_Salary = json_data['Monthly_Salary']
Emp_Country = json_data['Emp_Country']
Emp_State = json_data['Emp_State']
Emp_City = json_data['Emp_City']
Zip_Code = json_data['Zip_Code']
Address = json_data['Address']
Landline_Phone = json_data['Landline_Phone']
Phone_Mobile = json_data['Phone_Mobile']
Website = json_data['Website']
Landline_Nation = json_data['Landline_Nation']
Mobile_Nation = json_data['Mobile_Nation']
Passport_File = json_data['passport_file_path']
Curriculum_File = json_data['curriculum_file_path']
Letter_Of_Motive = json_data['letter_of_motive']
Other_Document = json_data['other_document']
Degree = json_data['degree']
Transcript = json_data['transcript']
Graduation_Certificate = json_data['graduation_certificate']
Letter_Of_Commitment = json_data['letter_of_commitment']






ref1_FirstName = json_data['Reference_1']['First_Name']
ref1_LastName = json_data['Reference_1']['Last_Name']
ref1_Pos_Occupation = json_data['Reference_1']['Position/Occupation']
ref1_email = json_data['Reference_1']['Email_Address']
ref1_phone_number = json_data['Reference_1']['Phone_Number']
ref1_landline_number = json_data['Reference_1']['Landline_Number']
ref1_phone_CC = json_data['Reference_1']['Phone_CC']
ref1_landline_CC = json_data['Reference_1']['Landline_CC']

ref2_FirstName = json_data['Reference_2']['First_Name']
ref2_LastName = json_data['Reference_2']['Last_Name']
ref2_Pos_Occupation = json_data['Reference_2']['Position/Occupation']
ref2_email = json_data['Reference_2']['Email_Address']
ref2_phone_number = json_data['Reference_2']['Phone_Number']
ref2_landline_number = json_data['Reference_2']['Landline_Number']
ref2_phone_CC = json_data['Reference_2']['Phone_CC']
ref2_landline_CC = json_data['Reference_2']['Landline_CC']

ref3_FirstName = json_data['Reference_3']['First_Name']
ref3_LastName = json_data['Reference_3']['Last_Name']
ref3_Pos_Occupation = json_data['Reference_3']['Position/Occupation']
ref3_email = json_data['Reference_3']['Email_Address']
ref3_phone_number = json_data['Reference_3']['Phone_Number']
ref3_landline_number = json_data['Reference_3']['Landline_Number']
ref3_phone_CC = json_data['Reference_3']['Phone_CC']
ref3_landline_CC = json_data['Reference_3']['Landline_CC']

ref4_FirstName = json_data['Reference_4']['First_Name']
ref4_LastName = json_data['Reference_4']['Last_Name']
ref4_Pos_Occupation = json_data['Reference_4']['Position/Occupation']
ref4_email = json_data['Reference_4']['Email_Address']
ref4_phone_number = json_data['Reference_4']['Phone_Number']
ref4_landline_number = json_data['Reference_4']['Landline_Number']
ref4_phone_CC = json_data['Reference_4']['Phone_CC']
ref4_landline_CC = json_data['Reference_4']['Landline_CC']

ref5_FirstName = json_data['Reference_5']['First_Name']
ref5_LastName = json_data['Reference_5']['Last_Name']
ref5_Pos_Occupation = json_data['Reference_5']['Position/Occupation']
ref5_email = json_data['Reference_5']['Email_Address']
ref5_phone_number = json_data['Reference_5']['Phone_Number']
ref5_landline_number = json_data['Reference_5']['Landline_Number']
ref5_phone_CC = json_data['Reference_5']['Phone_CC']
ref5_landline_CC = json_data['Reference_5']['Landline_CC']


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





















# print(Starting_Date)
# print(Graduation_Date)
#
# print(starting_Date_1)
# print(starting_Date_2)
# print(starting_Date_3)
#
# print(graduation_Date_1)
# print(graduation_Date_2)
# print(graduation_Date_3)
# print(ref1_phone_CC, '#' , ref2_phone_CC, '#' , ref3_phone_CC, '#' , ref4_phone_CC, '#' , ref5_phone_CC)
# print(ref1_landline_CC, '#', ref2_landline_CC, '#', ref3_landline_CC, '#', ref4_landline_CC, '#' , ref5_landline_CC)
