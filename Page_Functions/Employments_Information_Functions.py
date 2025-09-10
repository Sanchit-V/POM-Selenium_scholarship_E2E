import os

from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

import Data.Employment_Page_Data as user_details
from Model.Employement_Information_Page_Model import EmploymentInformationPageData

time_short = user_details.time_short
time_med = user_details.time_med
time_long = user_details.time_long

from Page_Objects.Employments_Information_Page import EmploymentInformationObjects

class EmploymentInformationFunction(EmploymentInformationObjects):
    def Currently_working(self, data:EmploymentInformationPageData):
        WebDriverWait(self.driver,12).until(EC.presence_of_element_located(self.currently_working_yes))
        if data.currently_working == 1:
            yes_radio = self.driver.find_element(*self.currently_working_yes)
            yes_radio.click()
            time.sleep(time_med)

        elif data.currently_working == 0:
            no_radio = self.driver.find_element(*self.currently_working_no)
            no_radio.click()
            time.sleep(time_med)

        else:
            print('Wrong input given.')

    def position_info(self, data:EmploymentInformationPageData):
        try:
            Institution_name = self.driver.find_element(*self.institution_name)
            Institution_name.click()
            time.sleep(time_short)
            Institution_name.send_keys(Keys.CONTROL + "a")
            Institution_name.send_keys(Keys.DELETE)
            time.sleep(time_short)
            Institution_name.send_keys(data.Institution_Name)
            time.sleep(time_short)

        except:
            print('Institution details block not found.')

        try:
            Position_name = self.driver.find_element(*self.position)
            Position_name.click()
            time.sleep(time_short)
            Position_name.send_keys(Keys.CONTROL + "a")
            Position_name.send_keys(Keys.DELETE)
            time.sleep(time_short)
            Position_name.send_keys(data.Position)
            time.sleep(time_short)

        except:
            print('Position details block not found.')

        try:
            Area_name = self.driver.find_element(*self.area)
            Area_name.click()
            time.sleep(time_short)
            Area_name.send_keys(Keys.CONTROL + "a")
            Area_name.send_keys(Keys.DELETE)
            time.sleep(time_short)
            Area_name.send_keys(data.Area)
            time.sleep(time_short)

        except:
            print('Area details not found.')

        try:
            Worker_category = self.driver.find_element(*self.work_category)
            Worker_category.click()
            time.sleep(time_short)

            if data.work_category == 1:
                Dependent=self.driver.find_element(*self.dependent)
                Dependent.click()
                time.sleep(time_short)

            elif data.work_category == 0:
                Independent = self.driver.find_element(*self.independent)
                Independent.click()
                time.sleep(time_short)

            else:
                print('Wrong input selected.')

        except:
            print('Worker category not found.')

        try:
            Activity_name = self.driver.find_element(*self.activity)
            Activity_name.click()
            time.sleep(time_short)
            Activity_name.send_keys(Keys.CONTROL + "a")
            Activity_name.send_keys(Keys.DELETE)
            time.sleep(time_short)
            Activity_name.send_keys(data.Activity)
            time.sleep(time_short)

        except:
            print('Activity block not present.')

        try:
            seniority_dropdown = self.driver.find_element(*self.seniority)
            seniority_dropdown.click()
            time.sleep(time_short)

            # Map numeric input to web elements
            seniority_map = {
                1: self.driver.find_element(*self.one_year),
                2: self.driver.find_element(*self.two_year),
                3: self.driver.find_element(*self.three_year),
                4: self.driver.find_element(*self.four_year),
                5: self.driver.find_element(*self.five_year),
                6: self.driver.find_element(*self.six_or_more)
            }

            # Select based on input
            selected_option = seniority_map.get(data.seniority_position)

            if selected_option:
                selected_option.click()
                time.sleep(time_short)
            else:
                print("Wrong input given.")


        except:
            print('Seniority section not available.')

        try:
            Monthly_salary = self.driver.find_element(*self.monthly_salary_emp)
            Monthly_salary.click()
            time.sleep(time_short)
            Monthly_salary.send_keys(Keys.CONTROL + "a")
            Monthly_salary.send_keys(Keys.DELETE)
            time.sleep(time_short)
            Monthly_salary.send_keys(data.Monthly_Salary)
            time.sleep(time_short)

        except:
            print('Monthly salary section not available.')

    def Currency_Selection(self, data:EmploymentInformationPageData):
        try:

            currency = self.driver.find_element(*self.currency_code_dropdown)
            currency.click()
            time.sleep(time_short)

            print(data.Emp_Currency)

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
            locator = currency_map.get(data.Emp_Currency)

            if locator:
                self.driver.find_element(*locator).click()
            else:
                print('Wrong Input')

            time.sleep(time_med)
        except:
            print('Currency selection not available.')
            
    def employment_country(self, data:EmploymentInformationPageData): #, Zip_Code, Address
        try:
            country_select = self.driver.find_element(*self.country)
            country_select.click()
            country_select.send_keys(Keys.CONTROL + "a")
            country_select.send_keys(Keys.DELETE)
            time.sleep(time_short)

            country_select.send_keys(data.Emp_Country)

            if data.Emp_Country == 'India':
                for i in range(2):
                    self.driver.find_element(*self.country).send_keys(Keys.ARROW_DOWN)

                time.sleep(time_short)

                self.driver.find_element(*self.country).send_keys(Keys.ENTER)

            else:
                self.driver.find_element(*self.country).send_keys(Keys.ARROW_DOWN)
                self.driver.find_element(*self.country).send_keys(Keys.ENTER)

            time.sleep(time_med)

        except:
            print('Country block not found.')

        try:
            state_select = self.driver.find_element(*self.state)
            state_select.click()
            state_select.send_keys(Keys.CONTROL + "a")
            state_select.send_keys(Keys.DELETE)
            time.sleep(time_short)

            state_select.send_keys(data.Emp_State)
            self.driver.find_element(*self.state).send_keys(Keys.ARROW_DOWN)
            self.driver.find_element(*self.state).send_keys(Keys.ENTER)

            time.sleep(time_med)

        except:
            print('State block not found')

        try:
            city_select = self.driver.find_element(*self.city)
            city_select.click()
            city_select.send_keys(Keys.CONTROL + "a")
            city_select.send_keys(Keys.DELETE)
            time.sleep(time_short)

            city_select.send_keys(data.Emp_City)
            self.driver.find_element(*self.city).send_keys(Keys.ARROW_DOWN)
            self.driver.find_element(*self.city).send_keys(Keys.ENTER)

            time.sleep(time_med)

        except:
            print('City block not found')

        try:
            Zip_code = self.driver.find_element(*self.zip_code)
            Zip_code.click()
            time.sleep(time_short)
            Zip_code.send_keys(Keys.CONTROL + "a")
            time.sleep(time_short)
            Zip_code.send_keys(Keys.DELETE)
            time.sleep(time_short)
            Zip_code.send_keys(data.Zip_Code)
            time.sleep(time_short)

        except:
            print('Zip code block not found')

        try:
            AddresS = self.driver.find_element(*self.address)
            AddresS.click()
            time.sleep(time_short)
            AddresS.send_keys(Keys.CONTROL + "a")
            time.sleep(time_short)
            AddresS.send_keys(Keys.DELETE)
            time.sleep(time_short)
            AddresS.send_keys(data.Address)
            time.sleep(time_short)

        except:
            print('Address block not found')



    def employment_contact(self, data:EmploymentInformationPageData):

        try:
            landline_phune = self.driver.find_element(*self.landline_number)
            landline_phune.click()
            time.sleep(time_short)
            landline_phune.send_keys(Keys.CONTROL + "a")
            landline_phune.send_keys(Keys.DELETE)
            time.sleep(time_short)
            landline_phune.send_keys(data.Landline_Phone)
            time.sleep(time_short)

        except:
            print('Landline block not found.')


        try:
            mobile_phune = self.driver.find_element(*self.phone_number)
            mobile_phune.click()
            time.sleep(time_short)
            mobile_phune.send_keys(Keys.CONTROL + "a")
            mobile_phune.send_keys(Keys.DELETE)
            time.sleep(time_short)
            mobile_phune.send_keys(data.Phone_Mobile)
            time.sleep(time_short)

        except:
            print('Mobile number block not found')


        try:
            website = self.driver.find_element(*self.url)
            website.click()
            time.sleep(time_short)
            website.send_keys(Keys.CONTROL + "a")
            website.send_keys(Keys.DELETE)
            time.sleep(time_short)
            website.send_keys(data.Website)
            time.sleep(time_short)

        except:
            print('Website block not found.')



    def nations(self, data:EmploymentInformationPageData):
        try:
            landline_phune_country = self.driver.find_element(*self.landline_number_country)
            landline_phune_country.click()
            time.sleep(time_short)
            CountrY = self.driver.find_element(*self.country_menu)
            CountrY.click()
            time.sleep(time_short)
            CountrY.send_keys(Keys.CONTROL + "a")
            CountrY.send_keys(Keys.DELETE)
            time.sleep(time_short)
            CountrY.send_keys(data.Landline_Nation)
            time.sleep(time_long)

            if data.Landline_Nation == 'India':
                for i in range(2):
                    self.driver.find_element(*self.country_menu).send_keys(Keys.ARROW_DOWN)

                    time.sleep(time_short)

                    self.driver.find_element(*self.country_menu).send_keys(Keys.ENTER)

            else:
                self.driver.find_element(*self.country_menu).send_keys(Keys.ARROW_DOWN)
                self.driver.find_element(*self.country_menu).send_keys(Keys.ENTER)

            time.sleep(2)

            mobile_phune_country = self.driver.find_element(*self.phone_number_country)
            mobile_phune_country.click()
            time.sleep(time_short)
            CountrY = self.driver.find_element(*self.country_menu)
            CountrY.click()
            time.sleep(time_short)
            CountrY.send_keys(Keys.CONTROL + "a")
            CountrY.send_keys(Keys.DELETE)
            time.sleep(time_short)
            CountrY.send_keys(data.Mobile_Nation)
            time.sleep(time_long)

            if data.Mobile_Nation == 'India':
                for i in range(2):
                    self.driver.find_element(*self.country_menu).send_keys(Keys.ARROW_DOWN)

                    time.sleep(time_short)

                    self.driver.find_element(*self.country_menu).send_keys(Keys.ENTER)

            else:
                self.driver.find_element(*self.country_menu).send_keys(Keys.ARROW_DOWN)
                self.driver.find_element(*self.country_menu).send_keys(Keys.ENTER)

            time.sleep(time_med)

        except:
            print('Country entry fields not found.')



    def emp_info_continue(self):
        continue_bttn = self.driver.find_element(*self.employment_continue_button)
        continue_bttn.click()
        time.sleep(time_med)























