import time

from selenium import webdriver

from Page_Functions.Academic_Records_Functions import AcademicRecordsFunctions
from Page_Functions.Address_Page_Functions import AddressPageFunctions
from Page_Functions.Documents_Page_Functions import DocumentsPageFunctions
from Page_Functions.Employments_Information_Functions import EmploymentInformationFunction
from Page_Functions.Login_Page_Functions import LoginPageFunctions
from Page_Functions.PersonalDetails_Page_Functions import PersonalDetailsFunctions
from Page_Functions.References_Page_Functions import ReferencesPageFunctions
from Page_Functions.Submit_Page_Functions import SubmitPageFunctions
from Page_Functions.Submitted_Page_Functions import SubmittedPageFunctions
from Page_Functions.Welcome_Page_Functions import Welcome_Page
from Page_Functions.Additional_Informations_Page_Functions import AdditionalInformationFunctions


from Processes.Academic_Records_Processes import AcademicRecordsProcess
from Processes.Additional_Info_Processes import AdditionalInfoProcess
from Processes.Address_Page_Processes import AddressPageProcess
from Processes.Documents_Page_Processes import DocumentsPageProcess
from Processes.Employment_Info_Process import EmployementInfoProcess
from Processes.Login_Process import LoginPageProcess
from Libraries.Libraries import Import_libraries
from Processes.Personal_Details_Process import PersonalDetailsProcess
from Processes.References_Page_Processes import ReferencePageProcess
from Processes.Summary_Page_Process import SummaryPageProcess
from Processes.Welcome_Process import Welcome_Process
from Processes.Submitted_Page_Processes import SubmittedPageProcess

import Data.Login_Page_Data as Login_Page_Data
import Data.Welcome_Page_Data as Welcome_Page_Data
import Data.Personal_Page_Data as Personal_Page_Data
import Data.Address_Page_Data as Address_Page_Data
import Data.Academic_Page_Data as Academic_Page_Data
import Data.Employment_Page_Data as Employment_Page_Data
import Data.Reference_Page_Data as Reference_Page_Data
import Data.Document_Page_Data as Document_Page_Data
import Data.Additional_Information_Page_Data as Additional_Information_Page_Data


_driver = Import_libraries.get_driver()
_driver.get(Login_Page_Data.url)


time.sleep(4)


login_page_functions = LoginPageFunctions(_driver)
welcome_page_functions = Welcome_Page(_driver)
personal_details_functions = PersonalDetailsFunctions(_driver)
address_page_functions = AddressPageFunctions(_driver)
additional_page_functions = AdditionalInformationFunctions(_driver)
submit_report_page_functions = SubmitPageFunctions(_driver)
final_page_functions = SubmittedPageFunctions(_driver)
academic_page_functions = AcademicRecordsFunctions(_driver)
employment_page_functions = EmploymentInformationFunction(_driver)
reference_page_functions = ReferencesPageFunctions(_driver)
document_page_functions = DocumentsPageFunctions(_driver)




def test_login_process():
    login_process = LoginPageProcess(login_page_functions)
    login_process.run_process()

def test_welcome_page():
    welcome_process = Welcome_Process(welcome_page_functions)
    welcome_process.run_process()


def test_personal_details():
    personal_details = PersonalDetailsProcess(personal_details_functions)
    personal_details.run_process() 

def test_address_details():
    address_details = AddressPageProcess(address_page_functions)
    address_details.run_processes()

def test_academic_records():
    academic_details = AcademicRecordsProcess(academic_page_functions)
    academic_details.run_processes()

def test_employment_information():
    employment_details = EmployementInfoProcess(employment_page_functions)
    employment_details.run_processes()

def test_reference_page():
    references_page = ReferencePageProcess(reference_page_functions)
    references_page.run_processes()

def test_documents_upload_page():
    documents_upload = DocumentsPageProcess(document_page_functions)
    documents_upload.run_processes()

def test_additional_info_page():
    addition_info = AdditionalInfoProcess(additional_page_functions)
    addition_info.run_processes()

def test_submit_page():
    submit_page = SummaryPageProcess(submit_report_page_functions)
    submit_page.run_process()

def test_final_submit():
    final_submit = SubmittedPageProcess(final_page_functions)
    final_submit.run_process()























