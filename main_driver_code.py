import time  

from selenium import webdriver

from Page_Functions.Address_Page_Functions import Address_Page
from Page_Functions.Login_Page_Functions import Login_Page
from Page_Functions.PersonalDetails_Page_Functions import Personal_Details
from Page_Functions.Submit_Page_Functions import Submit
from Page_Functions.Submitted_Page_Functions import Submitted_Page
from Page_Functions.Welcome_Page_Functions import Welcome_Page
from Page_Functions.Additional_Informations_Page_Functions import Additional_Information
from Page_Object.Summary_Page import Summary
from Processes.Additional_Info_Processes import Additional_Info_Process
from Processes.Address_Page_Processes import Address_Page_Process
from Processes.Login_Process import Login_Process
from Import_Libraries import Import_libraries
from Processes.Personal_Details_Process import Personal_Details_Process
from Processes.Summary_Page_Process import Summary_Process
from Processes.Welcome_Process import Welcome_Process
from Processes.Submitted_Page_Processes import  Submitted_Page_Process

import user_details

# Initialize WebDriver
driver = Import_libraries.initialize_driver()

# Navigate to the URL
driver.get(user_details.url)
driver.maximize_window()

time.sleep(4)

# Create an instance of Pages
login_page_functions = Login_Page(driver)
welcome_page_functions = Welcome_Page(driver)
personal_details_functions = Personal_Details(driver)
address_page_functions = Address_Page(driver)
additional_page_functions = Additional_Information(driver)
submit_report_page_functions = Submit(driver)
final_page_functions = Submitted_Page(driver)






# Create an instance of Login_Process and run the process

def test_login_process():
    login_process = Login_Process(login_page_functions)
    login_process.run_process(user_details.access_code, user_details.selected_language)



def test_welcome_page():
    welcome_process = Welcome_Process(welcome_page_functions)
    welcome_process.run_process(user_details.expected_message, user_details.user_greeting)


def test_personal_details():
    personal_details = Personal_Details_Process(personal_details_functions)
    personal_details.run_process(user_details.document_type, user_details.Document_number, user_details.Martial_status,
                                 user_details.Profession, user_details.Date_Of_Birth,
                                 user_details.Country, user_details.State, user_details.City, user_details.Nationality,
                                 user_details.Monthly_Income,
                                 user_details.Monthly_Expense, user_details.Financially_Dependent,
                                 user_details.Has_Children, user_details.Range_0to4,
                                 user_details.Range_5to12, user_details.Range_13to18, user_details.Range_18plus)

def test_address_details():
    address_details = Address_Page_Process(address_page_functions)
    address_details.run_processes(user_details.additional_emails_to_be_added, user_details.email_Ids,user_details.default_phone,
                                  user_details.default_whatsapp,user_details.total_additionals, user_details.number_of_additional_phone,
                                  user_details.number_of_additional_whatsapp, user_details.additional_1, user_details.additional_2,
                                  user_details.additional_3,user_details.country_0,user_details.country_1,
                                  user_details.country_2, user_details.country_3, user_details.country_4,user_details.housing_type,
                                  user_details.housing_conditions, user_details.Country,user_details.State,
                                  user_details.City, user_details.home_address, user_details.zip_code)

def test_additional_info_page():
    addition_info = Additional_Info_Process(additional_page_functions)
    addition_info.run_processes(user_details.additional_type,user_details.Text_Additional_field)

def test_submit_page():
    submit_page = Summary_Process(submit_report_page_functions)
    submit_page.run_process()

def test_final_submit():
    final_submit = Submitted_Page_Process(final_page_functions)
    final_submit.run_process()






















