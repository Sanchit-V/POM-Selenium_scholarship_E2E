import os

from deep_translator import GoogleTranslator
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

import Data.Reference_Page_Data as user_details
from Page_Objects.References_Page import ReferencesPageObjects
from Model.Reference_Page_Model import PersonalOrEmploymentReferencesPage
time_short = user_details.time_short
time_med = user_details.time_med
time_long = user_details.time_long
selected_language = user_details.selected_language


class ReferencesPageFunctions (ReferencesPageObjects):

    def add_references(self, data:PersonalOrEmploymentReferencesPage):
        WebDriverWait(self.driver,12).until(EC.presence_of_element_located(self.add_reference))
        try:
            if 0 < data.additional_references <=2 :
                for additional_reference in range(data.additional_references):
                    added_references = self.driver.find_element(*self.add_reference)
                    added_references.click()
                    time.sleep(time_short)

            elif data.additional_references == 0:
                print("No references added, 0 option selected.")

            else:
                print("Wrong input given, the references should be less than or equal to 2")

        except:
            print(f'The error occurred adding the references.')

    def delete_references(self, data:PersonalOrEmploymentReferencesPage):
        try:
            for delete in range (data.additional_references + 2):
                delete_reference = self.driver.find_element(*self.delete_additional_reference)
                delete_reference.click()
                time.sleep(time_short)


        except:
            print("No additional field to be deleted.")

    
    def add_references_details(self, data:PersonalOrEmploymentReferencesPage):
        
        for i in range(1, 6):

            try:


                ref_First_name = self.driver.find_element(*self.ref_first_name[i-1])
                print(ref_First_name)
                ref_First_name.click()
                time.sleep(time_short)
                ref_First_name.send_keys(Keys.CONTROL + "a")
                ref_First_name.send_keys(Keys.DELETE)
                time.sleep(time_short)
                ref_First_name.send_keys(data.ref_First_Name[i-1])
                time.sleep(time_short)

                ref_Last_name = self.driver.find_element(*self.ref_last_name[i-1])
                ref_Last_name.click()
                time.sleep(time_short)
                ref_Last_name.send_keys(Keys.CONTROL + "a")
                ref_Last_name.send_keys(Keys.DELETE)
                time.sleep(time_short)
                ref_Last_name.send_keys(data.ref_Last_Name[i-1])
                time.sleep(time_short)

                ref_position_occupation = self.driver.find_element(*self.ref_occupation[i-1])
                ref_position_occupation.click()
                time.sleep(time_short)
                ref_position_occupation.send_keys(Keys.CONTROL + "a")
                ref_position_occupation.send_keys(Keys.DELETE)
                time.sleep(time_short)
                ref_position_occupation.send_keys(data.ref_Pos_Occupation[i-1])
                time.sleep(time_short)

                ref_Email = self.driver.find_element(*self.ref_email[i-1])
                ref_Email.click()
                time.sleep(time_short)
                ref_Email.send_keys(Keys.CONTROL + "a")
                ref_Email.send_keys(Keys.DELETE)
                time.sleep(time_short)
                ref_Email.send_keys(data.ref_Emails[i-1])
                time.sleep(time_short)

                ref_Phone_Number = self.driver.find_element(*self.ref_phone_number[i-1])
                ref_Phone_Number.click()
                time.sleep(time_short)
                ref_Phone_Number.send_keys(Keys.CONTROL + "a")
                ref_Phone_Number.send_keys(Keys.DELETE)
                time.sleep(time_short)
                ref_Phone_Number.send_keys(data.ref_phone_numbers[i-1])
                time.sleep(time_short)

                ref_Landline_Number = self.driver.find_element(*self.ref_landline[i-1])
                ref_Landline_Number.click()
                time.sleep(time_short)
                ref_Landline_Number.send_keys(Keys.CONTROL + "a")
                ref_Landline_Number.send_keys(Keys.DELETE)
                time.sleep(time_short)
                ref_Landline_Number.send_keys(data.ref_landline_numbers[i-1])
                time.sleep(time_short)

                
                # Phone Number
                ref_phone_country = self.driver.find_element(*self.ref_country_code_phone_number[i-1])
                ref_phone_country.click()
                time.sleep(time_short)
                Country_menu = self.driver.find_element(*self.country_menu)
                Country_menu.click()
                time.sleep(time_short)
                Country_menu.send_keys(Keys.CONTROL + "a")
                Country_menu.send_keys(Keys.DELETE)
                time.sleep(time_short)
                Country_menu.send_keys(data.ref_phone_CC[i-1])
                time.sleep(time_long)
                country_lower = data.ref_phone_CC[i-1].lower()
                print(country_lower)

                if selected_language == 0:
                    english_country_lower = GoogleTranslator(source='es', target='en').translate(country_lower)
                    country_lower = english_country_lower.lower()
                elif selected_language == 1:
                    country_lower = country_lower
                else:
                    print("Issue in Country translation")

                country_selected = f"li-{country_lower}"
                print(country_selected)

                try:
                    new_datatest_ID = self.driver.find_element(By.CSS_SELECTOR, f'[data-test-id="{country_selected}"]')
                    time.sleep(time_short)
                    new_datatest_ID.click()
                
                except:
                    print('Country-Code not found')


                time.sleep(time_short)


            #Landline Number
                ref_landline_country = self.driver.find_element(*self.ref_country_code_landline[i-1])
                ref_landline_country.click()
                time.sleep(time_short)
                Country_menu = self.driver.find_element(*self.country_menu)
                Country_menu.click()
                time.sleep(time_short)
                Country_menu.send_keys(Keys.CONTROL + "a")
                Country_menu.send_keys(Keys.DELETE)
                time.sleep(time_short)
                Country_menu.send_keys(data.ref_landline_CC[i-1])
                time.sleep(time_long)
                country_lower = data.ref_landline_CC[i-1].lower()
                print(country_lower)

                if selected_language == 0:
                    english_country_lower = GoogleTranslator(source='es', target ='en').translate(country_lower)
                    country_lower = english_country_lower.lower()

                elif selected_language == 1:
                    country_lower = country_lower

                else:
                    print("Issue in Country translation")
                
                country_selected = f"li-{country_lower}"

                print(country_selected)

                try:
                    new_datatest_ID = self.driver.find_element(By.CSS_SELECTOR, f'[data-test-id="{country_selected}"]')
                    time.sleep(time_short)
                    new_datatest_ID.click()
                
                except:
                    print('Country-Code not found')

                
                time.sleep(time_short)

                try:
                        Dropdown_Arrow = self.driver.find_element(*self.ref_dropdown[i])
                        Dropdown_Arrow.click()
                        time.sleep(time_short)
                
                except:
                        print(f"Dropdown not found for {i}.")

                time.sleep(time_med)
        
            except:
                print(f'Error occurred while adding details for reference {i}.')
    

    def continue_references(self):
        time.sleep(time_long)
        continue_reference_bttn = self.driver.find_element(*self.continue_bttn_reference)
        continue_reference_bttn.click()
        time.sleep(time_med)



















