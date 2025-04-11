from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

import user_details

time_short = user_details.time_short
time_med = user_details.time_med
time_long = user_details.time_long

from Page_Object.Employments_Information_Page import EmploymentInformation

class Employmet_Information(EmploymentInformation):
    def Currently_working(self, currently_working):
        if currently_working == 1:
            yes_radio = self.driver.find_element(*self.currently_working_yes)
            yes_radio.click()
            time.sleep(time_med)

        elif currently_working == 0:
            no_radio = self.driver.find_element(*self.currently_working_no)
            no_radio.click()
            time.sleep(time_med)

        else:
            print('Wrong input given.')

    def position_info(self, Institution_Name, Position, Area, work_category, Activity, seniority_position, Monthly_Salary):
        try:
            Institution_name = self.driver.find_element(*self.institution_name)
            Institution_name.click()
            time.sleep(time_short)
            Institution_name.send_keys(Keys.CONTROL + "a")
            Institution_name.send_keys(Keys.DELETE)
            time.sleep(time_short)
            Institution_name.send_keys(Institution_Name)
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
            Position_name.send_keys(Position)
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
            Area_name.send_keys(Area)
            time.sleep(time_short)

        except:
            print('Area details not found.')

        try:
            Worker_category = self.driver.find_element(*self.work_category)
            Worker_category.click()
            time.sleep(time_short)

            if work_category == 1:
                Dependent=self.driver.find_element(*self.dependent)
                Dependent.click()
                time.sleep(time_short)

            elif work_category == 0:
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
            Activity_name.send_keys(Activity)
            time.sleep(time_short)

        except:
            print('Activity block not present.')

        try:
            Seniority_position = self.driver.find_element(*self.seniority)
            Seniority_position.click()
            time.sleep(time_short)

            Seniority_1_year = self.driver.find_element(*self.one_year)
            Seniority_2_year = self.driver.find_element(*self.two_year)
            Seniority_3_year = self.driver.find_element(*self.three_year)
            Seniority_4_year = self.driver.find_element(*self.four_year)
            Seniority_5_year = self.driver.find_element(*self.five_year)
            Seniority_6_year = self.driver.find_element(*self.six_or_more)

            if seniority_position == 1:
                Seniority_1_year.click()
                time.sleep(time_short)

            elif seniority_position == 2:
                Seniority_2_year.click()
                time.sleep(time_short)

            elif seniority_position == 3:
                Seniority_3_year.click()
                time.sleep(time_short)

            elif seniority_position == 4:
                Seniority_4_year.click()
                time.sleep(time_short)

            elif seniority_position == 5:
                Seniority_5_year.click()
                time.sleep(time_short)

            elif seniority_position == 6:
                Seniority_6_year.click()
                time.sleep(time_short)

            else:
                print('Wrong input given.')

        except:
            print('Seniority section not available.')

        try:
            Monthly_salary = self.driver.find_element(*self.monthly_salary_emp)
            Monthly_salary.click()
            time.sleep(time_short)
            Monthly_salary.send_keys(Keys.CONTROL + "a")
            Monthly_salary.send_keys(Keys.DELETE)
            time.sleep(time_short)
            Monthly_salary.send_keys(Monthly_Salary)
            time.sleep(time_short)

        except:
            print('Monthly salary section not available.')

    def employment_country(self, Emp_Country, Emp_State, Emp_City, Zip_Code, Address): #, Zip_Code, Address
        try:
            country_select = self.driver.find_element(*self.country)
            country_select.click()
            country_select.send_keys(Keys.CONTROL + "a")
            country_select.send_keys(Keys.DELETE)
            time.sleep(time_short)

            country_select.send_keys(Emp_Country)

            if Emp_Country == 'India':
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

            state_select.send_keys(Emp_State)
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

            city_select.send_keys(Emp_City)
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
            Zip_code.send_keys(Zip_Code)
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
            AddresS.send_keys(Address)
            time.sleep(time_short)

        except:
            print('Address block not found')



    def employment_contact(self, Landline_Phone, Phone_Mobile,Website):

        try:
            landline_phune = self.driver.find_element(*self.landline_number)
            landline_phune.click()
            time.sleep(time_short)
            landline_phune.send_keys(Keys.CONTROL + "a")
            landline_phune.send_keys(Keys.DELETE)
            time.sleep(time_short)
            landline_phune.send_keys(Landline_Phone)
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
            mobile_phune.send_keys(Phone_Mobile)
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
            website.send_keys(Website)
            time.sleep(time_short)

        except:
            print('Website block not found.')



    def nations(self, Landline_Nation, Mobile_Nation):
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
            CountrY.send_keys(Landline_Nation)
            time.sleep(time_long)

            if Landline_Nation == 'India':
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
            CountrY.send_keys(Mobile_Nation)
            time.sleep(time_long)

            if Mobile_Nation == 'India':
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























