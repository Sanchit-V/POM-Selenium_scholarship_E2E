#URL
url = "http://localhost:3000/"

# Provide user details
access_code = 'db59418' # Example access code
previous_access_code = 'db59418'
selected_language = '1'  # 1 for English, 0 for Spanish

dob_English = '09302001' #MMDDYYYY
dob_Spanish = '30092001' #DDMMYYYY

if selected_language == 1:
    user_greeting = "Welcome to the online scholarship application form"
    expected_message = "Login successful"
    Date_Of_Birth = dob_English

else:
    user_greeting = "Bienvenido al formulario de solicitud de beca online"
    expected_message = "Inicio de sesión correcto"
    Date_Of_Birth = dob_Spanish


document_type = 2 # 1 for NIC     # 2 for Passport    # 3 for FIC    # 4 for RUC    # 5 for Other

Document_number = '1224435334'

Martial_status = 4 # 1 for Married    # 2 for Single    # 3 for Divorced   # 4 for Widowed      # 5 for Separated

Profession = 'Teacher'

Country = 'India'
State = 'Bihar'
City = 'Patna'
Nationality = 'India'

Monthly_Income = '98767123'
Monthly_Expense = '1234321'

Financially_Dependent = 0   # 0 for No  # 1 for Yes

Has_Children = 0   # 0 for No  # 1 for Yes

Range_0to4 = 1
Range_5to12 = 1
Range_13to18 = 1
Range_18plus = 2


additional_emails_to_be_added = 4

email_Ids = ["example1@gmail.com", "example2@yahoo.com", "example3@outlook.com", "example4@gmail.com", "example5@yahoo.com"]

default_phone = 9800199911
default_whatsapp = 8766223432

number_of_additional_phone=2
number_of_additional_whatsapp=1

total_additionals = number_of_additional_phone+number_of_additional_whatsapp



additional_1=7676716221
additional_2=9088989765
additional_3=9666777887


country_0 = 'India'
country_1 = 'Spain'
country_2 = 'Pakistan'
country_3 = 'Brazil'
country_4 = 'Bhutan'

housing_type = 1   # 1 for department    # 2 for House
housing_conditions = 1 # 1 for Family     # 2 for Own     # 3 for Rented

home_address = "7684 Cambridge Road, Lake Noramouth, NY 12345"
zip_code = "QW12321"

additional_type = 7 # 1-Google 2-Facebook 3-Instagram 4-Referred 5-Company 6-Agreement 7-University 8-Speech 9-Webinar

Text_Additional_field = 'Hello 12343213 Hello hello hello'



























