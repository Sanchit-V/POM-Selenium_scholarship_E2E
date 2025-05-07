import os

from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import calendar

import user_details
from Page_Object.Personal_Deltails import PersonalDetails
from user_details import Has_Children, expected_message

time_short = user_details.time_short
time_med = user_details.time_med
time_long = user_details.time_long
selected_language = user_details.selected_language


class Personal_Details(PersonalDetails):
    def document_type_selection(self, document_type):
        WebDriverWait(self.driver,12).until(EC.presence_of_element_located(self.document_type_button))
        Document_click = self.driver.find_element(*self.document_type_button)
        Document_click.click()

        if document_type == 1:
            NIC = self.driver.find_element(*self.NIC)
            NIC.click()

        elif document_type == 2:
            Passport = self.driver.find_element(*self.passport)
            Passport.click()

        elif document_type == 3:
            FIC = self.driver.find_element(*self.foreign_identity_card)
            FIC.click()

        elif document_type == 4:
            RUC = self.driver.find_element(*self.RUC)
            RUC.click()

        else:
            Other = self.driver.find_element(*self.other_document)
            Other.click()

    def document_number(self, Document_number):
        Doc_number_click = self.driver.find_element(*self.document_number_field)
        Doc_number_click.click()

        Doc_number_click.send_keys(Keys.CONTROL+"a")
        Doc_number_click.send_keys(Keys.DELETE)
        time.sleep(time_short)

        number = self.driver.find_element(*self.document_number_enter)
        number.send_keys(Document_number)

    def martial_Status(self, Martial_status):

        Martial_status_click = self.driver.find_element(*self.martial_status)
        Martial_status_click.click()

        time.sleep(time_long)

        if Martial_status == 1:
            married = self.driver.find_element(*self.married)
            married.click()

        elif Martial_status == 2:
            single = self.driver.find_element(*self.single)
            single.click()

        elif Martial_status == 3:
            divorced = self.driver.find_element(*self.divorced)
            divorced.click()

        elif Martial_status == 4:
            widowed = self.driver.find_element(*self.widowed)
            widowed.click()

        else:
            separated = self.driver.find_element(*self.separated)
            separated.click()


    def Applicant_profession(self, Profession):
        prof_click = self.driver.find_element(*self.profession_field)
        prof_click.click()

        prof_click.send_keys(Keys.CONTROL + "a")
        prof_click.send_keys(Keys.DELETE)
        time.sleep(time_short)

        prof_enter = self.driver.find_element(*self.profession)
        prof_enter.send_keys(Profession)

        time.sleep(time_med)

    def Applicant_DOB(self,Date_Of_Birth):
        enter_DOB = self.driver.find_element(*self.DOB)
        if selected_language == 1:
            month = Date_Of_Birth[0:2]
        elif selected_language == 0:
            month = Date_Of_Birth[2:4]
        else:
            print('Error in DOB')

        month_name = calendar.month_name[int(month)]
        print(month_name)
        print(Date_Of_Birth)
        print(enter_DOB)
        enter_DOB.click()
        folder_path = "screenshots"
        os.makedirs(folder_path, exist_ok=True)
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        screenshot_name = f"{folder_path}/date of birth.{timestamp}.png"
        self.driver.save_screenshot(screenshot_name)

        enter_DOB.send_keys(Date_Of_Birth)

        time.sleep(time_med)

    def Applicant_Nation(self, Country):
        WebDriverWait(self.driver,12).until(EC.presence_of_element_located(self.Country))
        country = self.driver.find_element(*self.Country)
        country.click()
        country.send_keys(Country)

        time.sleep(time_med)
        nation_options = self.driver.find_elements(*self.dropdown)
        for option in nation_options:
            option_text = option.text.strip()
            if option_text == Country:
                option.click()
                break

        time.sleep(time_short)

    def Applicant_State(self, State):
        state = self.driver.find_element(*self.State)
        state.click()
        state.send_keys(State)

        time.sleep(time_med)
        state_options = self.driver.find_elements(*self.dropdown)
        for option in state_options:
            option_text = option.text.strip()
            if option_text == State:
                option.click()
                break

        time.sleep(time_short)

    def Applicant_City(self, City):
        city = self.driver.find_element(*self.City)
        city.click()
        city.send_keys(City)

        time.sleep(time_med)
        city_options = self.driver.find_elements(*self.dropdown)
        for option in city_options:
            option_text = option.text.strip()
            if option_text == City:
                option.click()
                break

        time.sleep(time_short)

    def Applicant_Nationality(self, Nationality):
        nationality = self.driver.find_element(*self.Nationality)
        nationality.click()
        nationality.send_keys(Nationality)

        time.sleep(time_med)
        try:

            nationality_options = self.driver.find_elements(*self.dropdown)
            for option in nationality_options:
                option_text = option.text.strip()
                if option_text == Nationality:
                    option.click()
                    break

        except:
            print("Error finding Nationality.")

        time.sleep(time_short)


    def Applicant_Income(self, Monthly_Income):
        income = self.driver.find_element(*self.Monthly_Income)
        income.click()
        income.send_keys(Keys.CONTROL + "a")
        income.send_keys(Keys.DELETE)
        time.sleep(time_short)
        income.send_keys(Monthly_Income)
        time.sleep(time_short)

    def Applicant_Expense(self, Monthly_Expense):
        expense = self.driver.find_element(*self.Monthly_Expense)
        expense.click()
        expense.send_keys(Keys.CONTROL + "a")
        expense.send_keys(Keys.DELETE)
        time.sleep(time_short)
        expense.send_keys(Monthly_Expense)
        time.sleep(time_short)


    def Financial_Dependent(self, Financially_Dependent):

        not_dependent = self.driver.find_element(*self.Financial_Independent_Yes)
        dependent = self.driver.find_element(*self.Financial_Independent_No)

        if Financially_Dependent == 1:
                dependent.click()

        else:
                not_dependent.click()

        time.sleep(time_long)


    def Has_Children(self, Has_Children):                  
        has_children = self.driver.find_element(*self.has_Children)
        does_not_have_children = self.driver.find_element(*self.does_Not_Have_Children)
        if Has_Children == 1:
            has_children.click()

        else:
            does_not_have_children.click()

        time.sleep(time_long)


    def Number_of_children(self,Range_0to4, Range_5to12, Range_13to18, Range_18plus):


        try:

            zero_To_four = self.driver.find_element(*self.zero_to_four)
            five_To_twelve = self.driver.find_element(*self.five_to_twelve)
            thirteen_To_eighteen = self.driver.find_element(*self.thirteen_to_eighteen)
            eighteen_Plus = self.driver.find_element(*self.eighteen_plus)

            zero_To_four.click()
            zero_To_four.send_keys(Keys.BACKSPACE+Keys.BACKSPACE)
            time.sleep(time_short)
            zero_To_four.send_keys(Range_0to4)
            time.sleep(time_short)

            five_To_twelve.click()
            five_To_twelve.send_keys(Keys.BACKSPACE+Keys.BACKSPACE)
            time.sleep(time_short)
            five_To_twelve.send_keys(Range_5to12)
            time.sleep(time_short)

            thirteen_To_eighteen.click()
            thirteen_To_eighteen.send_keys(Keys.BACKSPACE+Keys.BACKSPACE)
            time.sleep(time_short)
            thirteen_To_eighteen.send_keys(Range_13to18)
            time.sleep(time_short)

            eighteen_Plus.click()
            eighteen_Plus.send_keys(Keys.BACKSPACE+Keys.BACKSPACE)
            time.sleep(time_short)
            eighteen_Plus.send_keys(Range_18plus)
            time.sleep(time_short)

            print("All fields filled.")




        except Exception as e:
            print(f"No children Field, found : {e}")
            folder_path = "screenshots"
            os.makedirs(folder_path, exist_ok=True)
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            screenshot_name = f"{folder_path}/snackbar_exception_{timestamp}.png"

            # Take screenshot
            self.driver.save_screenshot(screenshot_name)
            time.sleep(time_med)



    def Continue_button(self):
        continue_bttn = self.driver.find_element(*self.continue_button)
        continue_bttn.click()


        time.sleep(time_long)
































