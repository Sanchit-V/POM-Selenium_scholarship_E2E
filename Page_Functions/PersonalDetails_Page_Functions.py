from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from Page_Object.Personal_Deltails import PersonalDetails
from user_details import Has_Children, expected_message


class Personal_Details(PersonalDetails):
    def document_type_selection(self, document_type):
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
        time.sleep(1)

        number = self.driver.find_element(*self.document_number_enter)
        number.send_keys(Document_number)

    def martial_Status(self, Martial_status):

        Martial_status_click = self.driver.find_element(*self.martial_status)
        Martial_status_click.click()



        time.sleep(4)

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
        time.sleep(1)

        prof_enter = self.driver.find_element(*self.profession)
        prof_enter.send_keys(Profession)

        time.sleep(2)

    def Applicant_DOB(self, Date_Of_Birth):
        enter_DOB = self.driver.find_element(*self.DOB)
        enter_DOB.click()
        enter_DOB.send_keys(Date_Of_Birth)

        time.sleep(2)

    def Applicant_Nation(self, Country):
        country = self.driver.find_element(*self.Country)
        country.click()
        country.send_keys(Country)

        time.sleep(2)
        nation_options = self.driver.find_elements(*self.dropdown)
        for option in nation_options:
            option_text = option.text.strip()
            if option_text == Country:
                option.click()
                break

        time.sleep(1)

    def Applicant_State(self, State):
        state = self.driver.find_element(*self.State)
        state.click()
        state.send_keys(State)

        time.sleep(2)
        state_options = self.driver.find_elements(*self.dropdown)
        for option in state_options:
            option_text = option.text.strip()
            if option_text == State:
                option.click()
                break

        time.sleep(1)

    def Applicant_City(self, City):
        city = self.driver.find_element(*self.City)
        city.click()
        city.send_keys(City)

        time.sleep(2)
        city_options = self.driver.find_elements(*self.dropdown)
        for option in city_options:
            option_text = option.text.strip()
            if option_text == City:
                option.click()
                break

        time.sleep(1)

    def Applicant_Nationality(self, Nationality):
        nationality = self.driver.find_element(*self.Nationality)
        nationality.click()
        nationality.send_keys(Nationality)

        time.sleep(2)
        nationality_options = self.driver.find_elements(*self.dropdown)
        for option in nationality_options:
            option_text = option.text.strip()
            if option_text == Nationality:
                option.click()
                break

        time.sleep(1)


    def Applicant_Income(self, Monthly_Income):
        income = self.driver.find_element(*self.Monthly_Income)
        income.click()
        income.send_keys(Keys.CONTROL + "a")
        income.send_keys(Keys.DELETE)
        time.sleep(1)
        income.send_keys(Monthly_Income)
        time.sleep(1)

    def Applicant_Expense(self, Monthly_Expense):
        expense = self.driver.find_element(*self.Monthly_Expense)
        expense.click()
        expense.send_keys(Keys.CONTROL + "a")
        expense.send_keys(Keys.DELETE)
        time.sleep(1)
        expense.send_keys(Monthly_Expense)
        time.sleep(1)


    def Financial_Dependent(self, Financially_Dependent, selected_language):

        if selected_language == 1:
            not_dependent = self.driver.find_element(*self.Financial_Independent_Yes)
            dependent = self.driver.find_element(*self.Financial_Independent_No)

            if Financially_Dependent == 1:
                dependent.click()

            else:
                not_dependent.click()

            time.sleep(3)

        else:
            not_dependent = self.driver.find_element(*self.Financial_Independent_SI)
            dependent = self.driver.find_element(*self.Financial_Independent_NO)

            if Financially_Dependent == 1:
                dependent.click()

            else:
                not_dependent.click()

            time.sleep(3)





    def Has_Children(self, Has_Children, selected_language):                  #

       if selected_language == 1:
            has_children = self.driver.find_element(*self.has_Children)
            does_not_have_children = self.driver.find_element(*self.does_Not_Have_Children)
            if Has_Children == 1:
                has_children.click()

                time.sleep(2)

            else:
                does_not_have_children.click()




       else:
           has_children = self.driver.find_element(*self.has_Children_SI)
           does_not_have_children = self.driver.find_element(*self.has_Children_NO)

           if Has_Children == 1:
               has_children.click()

               time.sleep(2)

           else:
               does_not_have_children.click()




    def Number_of_children(self,Range_0to4, Range_5to12, Range_13to18, Range_18plus):


        try:

            zero_To_four = self.driver.find_element(*self.zero_to_four)
            five_To_twelve = self.driver.find_element(*self.five_to_twelve)
            thirteen_To_eighteen = self.driver.find_element(*self.thirteen_to_eighteen)
            eighteen_Plus = self.driver.find_element(*self.eighteen_plus)

            zero_To_four.click()
            zero_To_four.send_keys(Keys.BACKSPACE+Keys.BACKSPACE)
            time.sleep(1)
            zero_To_four.send_keys(Range_0to4)
            time.sleep(1)

            five_To_twelve.click()
            five_To_twelve.send_keys(Keys.BACKSPACE+Keys.BACKSPACE)
            time.sleep(1)
            five_To_twelve.send_keys(Range_5to12)
            time.sleep(1)

            thirteen_To_eighteen.click()
            thirteen_To_eighteen.send_keys(Keys.BACKSPACE+Keys.BACKSPACE)
            time.sleep(1)
            thirteen_To_eighteen.send_keys(Range_13to18)
            time.sleep(1)

            eighteen_Plus.click()
            eighteen_Plus.send_keys(Keys.BACKSPACE+Keys.BACKSPACE)
            time.sleep(1)
            eighteen_Plus.send_keys(Range_18plus)
            time.sleep(1)

            print("All fields filled.")




        except Exception as e:
            print(f"No children Field, found : {e}")
            time.sleep(2)

    def Continue_button(self):
        continue_bttn = self.driver.find_element(*self.continue_button)
        continue_bttn.click()


        time.sleep(5)
































