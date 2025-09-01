import os

from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import calendar

import Data.user_details as user_details
from Page_Objects.Personal_Deltails_Page import PersonalDetailObjects
from Pydentic_Model.models import PersonalDetailsData

time_short = user_details.time_short
time_med = user_details.time_med
time_long = user_details.time_long
selected_language = user_details.selected_language


class PersonalDetailsFunctions(PersonalDetailObjects):
    def document_type_selection(self, data:PersonalDetailsData):
        WebDriverWait(self.driver, 12).until(EC.presence_of_element_located(self.document_type_button))
        Document_click = self.driver.find_element(*self.document_type_button)
        Document_click.click()

        # Map document_type numbers to locators
        doc_map = {
            1: self.NIC,
            2: self.passport,
            3: self.foreign_identity_card,
            4: self.RUC
        }

        # Get locator or fallback to "Other"
        locator = doc_map.get(data.document_type, self.other_document)

        self.driver.find_element(*locator).click()
        time.sleep(time_short)

    def document_number(self, data:PersonalDetailsData):
        Doc_number_click = self.driver.find_element(*self.document_number_field)
        Doc_number_click.click()

        Doc_number_click.send_keys(Keys.CONTROL+"a")
        Doc_number_click.send_keys(Keys.DELETE)
        time.sleep(time_short)

        number = self.driver.find_element(*self.document_number_enter)
        number.send_keys(data.Document_number)
        time.sleep(time_short)

    def marital_status(self, data:PersonalDetailsData):
        # Open marital status dropdown
        marital_status_click = self.driver.find_element(*self.martial_status)
        marital_status_click.click()

        # Map status codes to locators
        status_map = {
            1: self.married,
            2: self.single,
            3: self.divorced,
            4: self.widowed
        }

        # Default to "separated" if not found
        locator = status_map.get(data.Martial_status, self.separated)

        self.driver.find_element(*locator).click()
        time.sleep(time_short)

    def Applicant_profession(self, data:PersonalDetailsData):
        prof_click = self.driver.find_element(*self.profession_field)
        prof_click.click()

        prof_click.send_keys(Keys.CONTROL + "a")
        prof_click.send_keys(Keys.DELETE)
        time.sleep(time_short)

        prof_enter = self.driver.find_element(*self.profession)
        prof_enter.send_keys(data.Profession)

        time.sleep(time_med)

    def Applicant_DOB(self,data:PersonalDetailsData):
        enter_DOB = self.driver.find_element(*self.DOB)
        if selected_language == 1:
            month = data.Date_Of_Birth[0:2]
        elif selected_language == 0:
            month = data.Date_Of_Birth[2:4]
        else:
            print('Error in DOB')

        month_name = calendar.month_name[int(month)]
        print(month_name)
        print(data.Date_Of_Birth)
        print(enter_DOB)
        enter_DOB.click()
        enter_DOB.send_keys(data.Date_Of_Birth)

        time.sleep(time_med)

    def Applicant_Nation(self, data:PersonalDetailsData):
        WebDriverWait(self.driver,12).until(EC.presence_of_element_located(self.Country))
        country = self.driver.find_element(*self.Country)
        country.click()
        country.send_keys(data.Country)

        time.sleep(time_med)
        nation_options = self.driver.find_elements(*self.dropdown)
        for option in nation_options:
            option_text = option.text.strip()
            if option_text == data.Country:
                option.click()
                break

        time.sleep(time_short)

    def Applicant_State(self, data:PersonalDetailsData):
        state = self.driver.find_element(*self.State)
        state.click()
        state.send_keys(data.State)

        time.sleep(time_med)
        state_options = self.driver.find_elements(*self.dropdown)
        for option in state_options:
            option_text = option.text.strip()
            if option_text == data.State:
                option.click()
                break

        time.sleep(time_short)

    def Applicant_City(self, data:PersonalDetailsData):
        city = self.driver.find_element(*self.City)
        city.click()
        city.send_keys(data.City)

        time.sleep(time_med)
        city_options = self.driver.find_elements(*self.dropdown)
        for option in city_options:
            option_text = option.text.strip()
            if option_text == data.City:
                option.click()
                break

        time.sleep(time_short)

    def Applicant_Nationality(self, data:PersonalDetailsData):
        nationality = self.driver.find_element(*self.Nationality)
        nationality.click()
        nationality.send_keys(data.Nationality)

        time.sleep(time_med)
        try:

            nationality_options = self.driver.find_elements(*self.dropdown)
            for option in nationality_options:
                option_text = option.text.strip()
                if option_text == data.Nationality:
                    option.click()
                    break

        except:
            print("Error finding Nationality.")

        time.sleep(time_short)


    def Currency_Selection(self, data:PersonalDetailsData):
        currency = self.driver.find_element(*self.currency_dropdown)
        currency.click()
        time.sleep(time_short)

        print(data.Currency)

        currency_map = {
            1: self.currency_code_ARS,
            2: self.currency_code_BOB,
            3: self.currency_code_BRL,
            4: self.currency_code_COP,   
            5: self.currency_code_USD,
            6: self.currency_code_EUR,
            7: self.currency_code_MXN,
            8: self.currency_code_PAB,
            9: self.currency_code_PEN,
            10: self.currency_code_GTQ,
            11: self.currency_code_UYU,
            12: self.currency_code_C,
            13: self.currency_code_DOP,
            14: self.currency_code_AOA,
            15: self.currency_code_CVE,
            16: self.currency_code_MZN,
            17: self.currency_code_VEF,
            18: self.currency_code_PYG,
            19: self.currency_code_HNL,
            20: self.currency_code_NIO,
            21: self.currency_code_XAF,
            22: self.currency_code_XOF,
            23: self.currency_code_BLU,
            24: self.currency_code_COP,
            25: self.currency_code_SIM,
            26: self.currency_code_VES,
        }

        # Get locator from map
        locator = currency_map.get(data.Currency)

        if locator:
            self.driver.find_element(*locator).click()
        else:
            print('Wrong Input')

        time.sleep(time_med)

    def Applicant_Income(self, data:PersonalDetailsData):
        income = self.driver.find_element(*self.Monthly_Income)
        income.click()
        income.send_keys(Keys.CONTROL + "a")
        income.send_keys(Keys.DELETE)
        time.sleep(time_short)
        income.send_keys(data.Monthly_Income)
        time.sleep(time_short)

    def Applicant_Expense(self, data:PersonalDetailsData):
        expense = self.driver.find_element(*self.Monthly_Expense)
        expense.click()
        expense.send_keys(Keys.CONTROL + "a")
        expense.send_keys(Keys.DELETE)
        time.sleep(time_short)
        expense.send_keys(data.Monthly_Expense)
        time.sleep(time_short)



    def Financial_Dependent(self, data:PersonalDetailsData):

        not_dependent = self.driver.find_element(*self.Financial_Independent_Yes)
        dependent = self.driver.find_element(*self.Financial_Independent_No)

        if data.Financially_Dependent == 1:
                dependent.click()

        else:
                not_dependent.click()

        time.sleep(time_long)


    def Has_Children(self, data:PersonalDetailsData):                  
        has_children = self.driver.find_element(*self.has_Children)
        does_not_have_children = self.driver.find_element(*self.does_Not_Have_Children)
        if data.Has_Children == 1:
            has_children.click()

        else:
            does_not_have_children.click()

        time.sleep(time_long)


    def Number_of_children(self,data:PersonalDetailsData):


        try:

            zero_To_four = self.driver.find_element(*self.zero_to_four)
            five_To_twelve = self.driver.find_element(*self.five_to_twelve)
            thirteen_To_eighteen = self.driver.find_element(*self.thirteen_to_eighteen)
            eighteen_Plus = self.driver.find_element(*self.eighteen_plus)

            zero_To_four.click()
            zero_To_four.send_keys(Keys.BACKSPACE+Keys.BACKSPACE)
            time.sleep(time_short)
            zero_To_four.send_keys(data.Range_0to4)
            time.sleep(time_short)

            five_To_twelve.click()
            five_To_twelve.send_keys(Keys.BACKSPACE+Keys.BACKSPACE)
            time.sleep(time_short)
            five_To_twelve.send_keys(data.Range_5to12)
            time.sleep(time_short)

            thirteen_To_eighteen.click()
            thirteen_To_eighteen.send_keys(Keys.BACKSPACE+Keys.BACKSPACE)
            time.sleep(time_short)
            thirteen_To_eighteen.send_keys(data.Range_13to18)
            time.sleep(time_short)

            eighteen_Plus.click()
            eighteen_Plus.send_keys(Keys.BACKSPACE+Keys.BACKSPACE)
            time.sleep(time_short)
            eighteen_Plus.send_keys(data.Range_18plus)
            time.sleep(time_short)

            print("All fields filled.")




        except Exception as e:
            print(f"No children Field, found : {e}")
            time.sleep(time_med)



    def Continue_button(self):
        continue_bttn = self.driver.find_element(*self.continue_button)
        continue_bttn.click()


        time.sleep(time_long)
































