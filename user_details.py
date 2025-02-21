#URL
from deep_translator import GoogleTranslator
import json



with open('user_details.json') as f:
     json_data = json.load(f)

url = "http://localhost:80/"
selected_language = 0     # 1 for English, 0 for Spanish
document_type = 3 # 1 for NIC     # 2 for Passport    # 3 for FIC    # 4 for RUC    # 5 for Other
Martial_status = 2 # 1 for Married    # 2 for Single    # 3 for Divorced   # 4 for Widowed      # 5 for Separated
Financially_Dependent = 1   # 0 for No  # 1 for Yes
Has_Children = 1   # 0 for No  # 1 for Yes
additional_emails_to_be_added = 4
number_of_additional_phone=1
number_of_additional_whatsapp=1
total_additionals = number_of_additional_phone + number_of_additional_whatsapp
housing_type = 1   # 1 for department    # 2 for House
housing_conditions = 1 # 1 for Family     # 2 for Own     # 3 for Rented
additional_type = 4 # 1-Google 2-Facebook 3-Instagram 4-Referred 5-Company 6-Agreement 7-University 8-Speech 9-Webinar

additional_education = 2

education_level_1 = 4 # 1-Postgraduate 2-University 3-Technical 4-High School
education_level_2 = 1 # 1-Postgraduate 2-University 3-Technical 4-High School
education_level_3 = 2 # 1-Postgraduate 2-University 3-Technical 4-High School
online_mode_study = 1 # 0 for No, 1 for Yes
training_type_university = 0 # 0 for No, 1 for Yes
training_type_employment = 1 # 0 for No, 1 for Yes
training_type_second_language = 1 # 0 for No, 1 for Yes

currently_working = 1 # 0 for No, 1 for Yes

work_category =  0 # 1 for Dependent, 0 for Independent

seniority_position = 4 # Enter digits 1 to 6




access_code = json_data['access_code']
previous_access_code = json_data['previous_access_code']
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

