import os

from deep_translator import GoogleTranslator
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

import user_details
from Page_Object.References_Page import ReferencesPage
time_short = user_details.time_short
time_med = user_details.time_med
time_long = user_details.time_long
selected_language = user_details.selected_language


class References(ReferencesPage):

    def add_references(self, additional_references):
        WebDriverWait(self.driver,12).until(EC.presence_of_element_located(self.add_reference))
        try:
            if 0 < additional_references <=2 :
                for additional_reference in range(additional_references):
                    added_references = self.driver.find_element(*self.add_reference)
                    added_references.click()
                    time.sleep(time_short)

            elif additional_references == 0:
                print("No references added, 0 option selected.")

            else:
                print("Wrong input given, the references should be less than or equal to 2")

        except Exception as e:
            print(f'The error occurred:{e}')

    def delete_references(self, additional_references):
        try:
            for delete in range (additional_references + 2):
                delete_reference = self.driver.find_element(*self.delete_additional_reference)
                delete_reference.click()
                time.sleep(time_short)


        except:
            print("No additional field to be deleted.")

    def add_reference1_details(self, ref1_FirstName, ref1_LastName, ref1_Pos_Occupation, ref1_email,
                               ref1_phone_number, ref1_landline_number, ref1_phone_CC, ref1_landline_CC):

        ref_first_name = self.driver.find_element(*self.ref1_first_name)
        ref_first_name.click()
        time.sleep(time_short)
        ref_first_name.send_keys(Keys.CONTROL + "a")
        ref_first_name.send_keys(Keys.DELETE)
        time.sleep(time_short)
        ref_first_name.send_keys(ref1_FirstName)
        time.sleep(time_short)

        ref_last_name = self.driver.find_element(*self.ref1_last_name)
        ref_last_name.click()
        time.sleep(time_short)
        ref_last_name.send_keys(Keys.CONTROL + "a")
        ref_last_name.send_keys(Keys.DELETE)
        time.sleep(time_short)
        ref_last_name.send_keys(ref1_LastName)
        time.sleep(time_short)

        ref_position_occupation = self.driver.find_element(*self.ref1_occupation)
        ref_position_occupation.click()
        time.sleep(time_short)
        ref_position_occupation.send_keys(Keys.CONTROL + "a")
        ref_position_occupation.send_keys(Keys.DELETE)
        time.sleep(time_short)
        ref_position_occupation.send_keys(ref1_Pos_Occupation)
        time.sleep(time_short)

        ref_email = self.driver.find_element(*self.ref1_email)
        ref_email.click()
        time.sleep(time_short)
        ref_email.send_keys(Keys.CONTROL + "a")
        ref_email.send_keys(Keys.DELETE)
        time.sleep(time_short)
        ref_email.send_keys(ref1_email)
        time.sleep(time_short)

        ref_phone_number = self.driver.find_element(*self.ref1_phone_number)
        ref_phone_number.click()
        time.sleep(time_short)
        ref_phone_number.send_keys(Keys.CONTROL + "a")
        ref_phone_number.send_keys(Keys.DELETE)
        time.sleep(time_short)
        ref_phone_number.send_keys(ref1_phone_number)
        time.sleep(time_short)

        ref_landline_number = self.driver.find_element(*self.ref1_landline)
        ref_landline_number.click()
        time.sleep(time_short)
        ref_landline_number.send_keys(Keys.CONTROL + "a")
        ref_landline_number.send_keys(Keys.DELETE)
        time.sleep(time_short)
        ref_landline_number.send_keys(ref1_landline_number)
        time.sleep(time_short)

        try:
            # Phone Number
            ref_phone_country = self.driver.find_element(*self.ref1_country_code_phone_number)
            ref_phone_country.click()
            time.sleep(time_short)
            Country_menu = self.driver.find_element(*self.country_menu)
            Country_menu.click()
            time.sleep(time_short)
            Country_menu.send_keys(Keys.CONTROL + "a")
            Country_menu.send_keys(Keys.DELETE)
            time.sleep(time_short)
            Country_menu.send_keys(ref1_phone_CC)
            time.sleep(time_long)
            country_lower = ref1_phone_CC.lower()
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
            new_datatest_ID = self.driver.find_element(By.CSS_SELECTOR, f'[data-test-id="{country_selected}"]')
            time.sleep(time_short)
            new_datatest_ID.click()


        except:
            folder_path = "screenshots"
            os.makedirs(folder_path, exist_ok=True)
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            screenshot_name = f"{folder_path}/mobile reference 1{timestamp}.png"

            # Take screenshot
            self.driver.save_screenshot(screenshot_name)
            print('Country-Code not found')

        time.sleep(time_short)


        try:
            #Landline Number
            ref_landline_country = self.driver.find_element(*self.ref1_country_code_landline)
            ref_landline_country.click()
            time.sleep(time_short)
            Country_menu = self.driver.find_element(*self.country_menu)
            Country_menu.click()
            time.sleep(time_short)
            Country_menu.send_keys(Keys.CONTROL + "a")
            Country_menu.send_keys(Keys.DELETE)
            time.sleep(time_short)
            Country_menu.send_keys(ref1_landline_CC)
            time.sleep(time_long)
            country_lower = ref1_landline_CC.lower()
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
            new_datatest_ID = self.driver.find_element(By.CSS_SELECTOR, f'[data-test-id="{country_selected}"]')
            time.sleep(time_short)
            new_datatest_ID.click()


        except:
            folder_path = "screenshots"
            os.makedirs(folder_path, exist_ok=True)
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            screenshot_name = f"{folder_path}/landline reference 1{timestamp}.png"

            # Take screenshot
            self.driver.save_screenshot(screenshot_name)
            print('Country-Code not found')
        time.sleep(time_med)



    def add_reference2_details(self, ref2_FirstName, ref2_LastName, ref2_Pos_Occupation, ref2_email,
                               ref2_phone_number, ref2_landline_number, ref2_phone_CC, ref2_landline_CC):

        dropdown_2 = self.driver.find_element(*self.ref2_dropdown)
        dropdown_2.click()
        time.sleep(time_short)

        ref_first_name = self.driver.find_element(*self.ref2_first_name)
        ref_first_name.click()
        time.sleep(time_short)
        ref_first_name.send_keys(Keys.CONTROL + "a")
        ref_first_name.send_keys(Keys.DELETE)
        time.sleep(time_short)
        ref_first_name.send_keys(ref2_FirstName)
        time.sleep(time_short)

        ref_last_name = self.driver.find_element(*self.ref2_last_name)
        ref_last_name.click()
        time.sleep(time_short)
        ref_last_name.send_keys(Keys.CONTROL + "a")
        ref_last_name.send_keys(Keys.DELETE)
        time.sleep(time_short)
        ref_last_name.send_keys(ref2_LastName)
        time.sleep(time_short)

        ref_position_occupation = self.driver.find_element(*self.ref2_occupation)
        ref_position_occupation.click()
        time.sleep(time_short)
        ref_position_occupation.send_keys(Keys.CONTROL + "a")
        ref_position_occupation.send_keys(Keys.DELETE)
        time.sleep(time_short)
        ref_position_occupation.send_keys(ref2_Pos_Occupation)
        time.sleep(time_short)

        ref_email = self.driver.find_element(*self.ref2_email)
        ref_email.click()
        time.sleep(time_short)
        ref_email.send_keys(Keys.CONTROL + "a")
        ref_email.send_keys(Keys.DELETE)
        time.sleep(time_short)
        ref_email.send_keys(ref2_email)
        time.sleep(time_short)

        ref_phone_number = self.driver.find_element(*self.ref2_phone_number)
        ref_phone_number.click()
        time.sleep(time_short)
        ref_phone_number.send_keys(Keys.CONTROL + "a")
        ref_phone_number.send_keys(Keys.DELETE)
        time.sleep(time_short)
        ref_phone_number.send_keys(ref2_phone_number)
        time.sleep(time_short)

        ref_landline_number = self.driver.find_element(*self.ref2_landline)
        ref_landline_number.click()
        time.sleep(time_short)
        ref_landline_number.send_keys(Keys.CONTROL + "a")
        ref_landline_number.send_keys(Keys.DELETE)
        time.sleep(time_short)
        ref_landline_number.send_keys(ref2_landline_number)
        time.sleep(time_short)

        try:

            #Phone Number
            ref_phone_country = self.driver.find_element(*self.ref2_country_code_phone_number)
            ref_phone_country.click()
            time.sleep(time_short)
            Country_menu = self.driver.find_element(*self.country_menu)
            Country_menu.click()
            time.sleep(time_short)
            Country_menu.send_keys(Keys.CONTROL + "a")
            Country_menu.send_keys(Keys.DELETE)
            time.sleep(time_short)

            Country_menu.send_keys(ref2_phone_CC)
            time.sleep(time_long)
            country_lower = ref2_phone_CC.lower()
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

            new_datatest_ID = self.driver.find_element(By.CSS_SELECTOR, f'[data-test-id="{country_selected}"]')
            time.sleep(time_short)
            new_datatest_ID.click()

        except:
            folder_path = "screenshots"
            os.makedirs(folder_path, exist_ok=True)
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            screenshot_name = f"{folder_path}/landline reference 2{timestamp}.png"

            # Take screenshot
            self.driver.save_screenshot(screenshot_name)
            print('Country-Code not found')

        time.sleep(time_short)

        try:
            #Landline Number
            ref_landline_country = self.driver.find_element(*self.ref2_country_code_landline)
            ref_landline_country.click()
            time.sleep(time_short)
            Country_menu = self.driver.find_element(*self.country_menu)
            Country_menu.click()
            time.sleep(time_short)
            Country_menu.send_keys(Keys.CONTROL + "a")
            Country_menu.send_keys(Keys.DELETE)
            time.sleep(time_short)

            Country_menu.send_keys(ref2_landline_CC)
            time.sleep(time_long)
            country_lower = ref2_landline_CC.lower()
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
            new_datatest_ID = self.driver.find_element(By.CSS_SELECTOR, f'[data-test-id="{country_selected}"]')
            time.sleep(time_short)
            new_datatest_ID.click()

        except:
            folder_path = "screenshots"
            os.makedirs(folder_path, exist_ok=True)
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            screenshot_name = f"{folder_path}/landline reference 2{timestamp}.png"

            # Take screenshot
            self.driver.save_screenshot(screenshot_name)
            print('Country-Code not found')

        time.sleep(time_med)




    def add_reference3_details(self, ref3_FirstName, ref3_LastName, ref3_Pos_Occupation, ref3_email,
                               ref3_phone_number, ref3_landline_number, ref3_phone_CC, ref3_landline_CC):

        dropdown_3 = self.driver.find_element(*self.ref3_dropdown)
        dropdown_3.click()
        time.sleep(time_short)

        ref_first_name = self.driver.find_element(*self.ref3_first_name)
        ref_first_name.click()
        time.sleep(time_short)
        ref_first_name.send_keys(Keys.CONTROL + "a")
        ref_first_name.send_keys(Keys.DELETE)
        time.sleep(time_short)
        ref_first_name.send_keys(ref3_FirstName)
        time.sleep(time_short)

        ref_last_name = self.driver.find_element(*self.ref3_last_name)
        ref_last_name.click()
        time.sleep(time_short)
        ref_last_name.send_keys(Keys.CONTROL + "a")
        ref_last_name.send_keys(Keys.DELETE)
        time.sleep(time_short)
        ref_last_name.send_keys(ref3_LastName)
        time.sleep(time_short)

        ref_position_occupation = self.driver.find_element(*self.ref3_occupation)
        ref_position_occupation.click()
        time.sleep(time_short)
        ref_position_occupation.send_keys(Keys.CONTROL + "a")
        ref_position_occupation.send_keys(Keys.DELETE)
        time.sleep(time_short)
        ref_position_occupation.send_keys(ref3_Pos_Occupation)
        time.sleep(time_short)

        ref_email = self.driver.find_element(*self.ref3_email)
        ref_email.click()
        time.sleep(time_short)
        ref_email.send_keys(Keys.CONTROL + "a")
        ref_email.send_keys(Keys.DELETE)
        time.sleep(time_short)
        ref_email.send_keys(ref3_email)
        time.sleep(time_short)

        ref_phone_number = self.driver.find_element(*self.ref3_phone_number)
        ref_phone_number.click()
        time.sleep(time_short)
        ref_phone_number.send_keys(Keys.CONTROL + "a")
        ref_phone_number.send_keys(Keys.DELETE)
        time.sleep(time_short)
        ref_phone_number.send_keys(ref3_phone_number)
        time.sleep(time_short)

        ref_landline_number = self.driver.find_element(*self.ref3_landline)
        ref_landline_number.click()
        time.sleep(time_short)
        ref_landline_number.send_keys(Keys.CONTROL + "a")
        ref_landline_number.send_keys(Keys.DELETE)
        time.sleep(time_short)
        ref_landline_number.send_keys(ref3_landline_number)
        time.sleep(time_short)

        try:
            #Phone Number
            ref_phone_country = self.driver.find_element(*self.ref3_country_code_phone_number)
            ref_phone_country.click()
            time.sleep(time_short)
            Country_menu = self.driver.find_element(*self.country_menu)
            Country_menu.click()
            time.sleep(time_short)
            Country_menu.send_keys(Keys.CONTROL + "a")
            Country_menu.send_keys(Keys.DELETE)
            time.sleep(time_short)

            Country_menu.send_keys(ref3_phone_CC)
            time.sleep(time_long)
            country_lower = ref3_phone_CC.lower()
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
            new_datatest_ID = self.driver.find_element(By.CSS_SELECTOR, f'[data-test-id="{country_selected}"]')
            time.sleep(time_short)
            new_datatest_ID.click()

        except:
            folder_path = "screenshots"
            os.makedirs(folder_path, exist_ok=True)
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            screenshot_name = f"{folder_path}/mobile reference 3{timestamp}.png"

            # Take screenshot
            self.driver.save_screenshot(screenshot_name)
            print('Country-Code not found')

        time.sleep(time_short)

        try:
            # Landline Number
            ref_landline_country = self.driver.find_element(*self.ref3_country_code_landline)
            ref_landline_country.click()
            time.sleep(time_short)
            Country_menu = self.driver.find_element(*self.country_menu)
            Country_menu.click()
            time.sleep(time_short)
            Country_menu.send_keys(Keys.CONTROL + "a")
            Country_menu.send_keys(Keys.DELETE)
            time.sleep(time_short)

            Country_menu.send_keys(ref3_landline_CC)
            time.sleep(time_long)
            country_lower = ref3_landline_CC.lower()
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
            new_datatest_ID = self.driver.find_element(By.CSS_SELECTOR, f'[data-test-id="{country_selected}"]')
            time.sleep(time_short)
            new_datatest_ID.click()

        except:
            folder_path = "screenshots"
            os.makedirs(folder_path, exist_ok=True)
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            screenshot_name = f"{folder_path}/landline reference 3{timestamp}.png"

            # Take screenshot
            self.driver.save_screenshot(screenshot_name)
            print('Country-Code not found')

        time.sleep(time_med)

    def add_reference4_details(self, ref4_FirstName, ref4_LastName, ref4_Pos_Occupation, ref4_email, ref4_phone_number,
                               ref4_landline_number, ref4_phone_CC, ref4_landline_CC):
        try:
            dropdown_4 = self.driver.find_element(*self.ref4_dropdown)
            dropdown_4.click()
            time.sleep(time_short)

            ref_first_name = self.driver.find_element(*self.ref4_first_name)
            ref_first_name.click()
            time.sleep(time_short)
            ref_first_name.send_keys(Keys.CONTROL + "a")
            ref_first_name.send_keys(Keys.DELETE)
            time.sleep(time_short)
            ref_first_name.send_keys(ref4_FirstName)
            time.sleep(time_short)

            ref_last_name = self.driver.find_element(*self.ref4_last_name)
            ref_last_name.click()
            time.sleep(time_short)
            ref_last_name.send_keys(Keys.CONTROL + "a")
            ref_last_name.send_keys(Keys.DELETE)
            time.sleep(time_short)
            ref_last_name.send_keys(ref4_LastName)
            time.sleep(time_short)

            ref_position_occupation = self.driver.find_element(*self.ref4_occupation)
            ref_position_occupation.click()
            time.sleep(time_short)
            ref_position_occupation.send_keys(Keys.CONTROL + "a")
            ref_position_occupation.send_keys(Keys.DELETE)
            time.sleep(time_short)
            ref_position_occupation.send_keys(ref4_Pos_Occupation)
            time.sleep(time_short)

            ref_email = self.driver.find_element(*self.ref4_email)
            ref_email.click()
            time.sleep(time_short)
            ref_email.send_keys(Keys.CONTROL + "a")
            ref_email.send_keys(Keys.DELETE)
            time.sleep(time_short)
            ref_email.send_keys(ref4_email)
            time.sleep(time_short)

            ref_phone_number = self.driver.find_element(*self.ref4_phone_number)
            ref_phone_number.click()
            time.sleep(time_short)
            ref_phone_number.send_keys(Keys.CONTROL + "a")
            ref_phone_number.send_keys(Keys.DELETE)
            time.sleep(time_short)
            ref_phone_number.send_keys(ref4_phone_number)
            time.sleep(time_short)

            ref_landline_number = self.driver.find_element(*self.ref4_landline)
            ref_landline_number.click()
            time.sleep(time_short)
            ref_landline_number.send_keys(Keys.CONTROL + "a")
            ref_landline_number.send_keys(Keys.DELETE)
            time.sleep(time_short)
            ref_landline_number.send_keys(ref4_landline_number)
            time.sleep(time_short)

            try:
                # Phone Number
                ref_phone_country = self.driver.find_element(*self.ref4_country_code_phone_number)
                ref_phone_country.click()
                time.sleep(time_short)
                Country_menu = self.driver.find_element(*self.country_menu)
                Country_menu.click()
                time.sleep(time_short)
                Country_menu.send_keys(Keys.CONTROL + "a")
                Country_menu.send_keys(Keys.DELETE)
                time.sleep(time_short)

                Country_menu.send_keys(ref4_phone_CC)
                time.sleep(time_long)
                country_lower = ref4_phone_CC.lower()
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
                new_datatest_ID = self.driver.find_element(By.CSS_SELECTOR, f'[data-test-id="{country_selected}"]')
                time.sleep(time_short)
                new_datatest_ID.click()

            except:
                folder_path = "screenshots"
                os.makedirs(folder_path, exist_ok=True)
                timestamp = time.strftime("%Y%m%d-%H%M%S")
                screenshot_name = f"{folder_path}/mobile reference 4{timestamp}.png"

                # Take screenshot
                self.driver.save_screenshot(screenshot_name)
                print('Country-Code not found')

            time.sleep(time_short)
            try:
                # Landline Number
                ref_landline_country = self.driver.find_element(*self.ref4_country_code_landline)
                ref_landline_country.click()
                time.sleep(time_short)
                Country_menu = self.driver.find_element(*self.country_menu)
                Country_menu.click()
                time.sleep(time_short)
                Country_menu.send_keys(Keys.CONTROL + "a")
                Country_menu.send_keys(Keys.DELETE)
                time.sleep(time_short)

                Country_menu.send_keys(ref4_landline_CC)
                time.sleep(time_long)
                country_lower = ref4_landline_CC.lower()
                print(country_lower)

                if selected_language == 0:
                    english_country_lower = GoogleTranslator(source='es', target='en').translate(country_lower)
                    country_lower = (english_country_lower).lower()
                elif selected_language == 1:
                    country_lower = country_lower
                else:
                    print("Issue in Country translation")
                country_selected = f"li-{country_lower}"
                print(country_selected)
                new_datatest_ID = self.driver.find_element(By.CSS_SELECTOR, f'[data-test-id="{country_selected}"]')
                time.sleep(time_short)
                new_datatest_ID.click()

            except:
                folder_path = "screenshots"
                os.makedirs(folder_path, exist_ok=True)
                timestamp = time.strftime("%Y%m%d-%H%M%S")
                screenshot_name = f"{folder_path}/landline reference 4{timestamp}.png"

                # Take screenshot
                self.driver.save_screenshot(screenshot_name)

                print('Country-Code not found')

            time.sleep(time_med)
        except:
            folder_path = "screenshots"
            os.makedirs(folder_path, exist_ok=True)
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            screenshot_name = f"{folder_path}/reference 4{timestamp}.png"

            # Take screenshot
            self.driver.save_screenshot(screenshot_name)
            print("Reference block 4 not found")

    def add_reference5_details(self, ref5_FirstName, ref5_LastName, ref5_Pos_Occupation, ref5_email, ref5_phone_number,
                               ref5_landline_number, ref5_phone_CC, ref5_landline_CC):
        try:
            dropdown_5 = self.driver.find_element(*self.ref5_dropdown)
            dropdown_5.click()
            time.sleep(time_short)

            ref_first_name = self.driver.find_element(*self.ref5_first_name)
            ref_first_name.click()
            time.sleep(time_short)
            ref_first_name.send_keys(Keys.CONTROL + "a")
            ref_first_name.send_keys(Keys.DELETE)
            time.sleep(time_short)
            ref_first_name.send_keys(ref5_FirstName)
            time.sleep(time_short)

            ref_last_name = self.driver.find_element(*self.ref5_last_name)
            ref_last_name.click()
            time.sleep(time_short)
            ref_last_name.send_keys(Keys.CONTROL + "a")
            ref_last_name.send_keys(Keys.DELETE)
            time.sleep(time_short)
            ref_last_name.send_keys(ref5_LastName)
            time.sleep(time_short)

            ref_position_occupation = self.driver.find_element(*self.ref5_occupation)
            ref_position_occupation.click()
            time.sleep(time_short)
            ref_position_occupation.send_keys(Keys.CONTROL + "a")
            ref_position_occupation.send_keys(Keys.DELETE)
            time.sleep(time_short)
            ref_position_occupation.send_keys(ref5_Pos_Occupation)
            time.sleep(time_short)

            ref_email = self.driver.find_element(*self.ref5_email)
            ref_email.click()
            time.sleep(time_short)
            ref_email.send_keys(Keys.CONTROL + "a")
            ref_email.send_keys(Keys.DELETE)
            time.sleep(time_short)
            ref_email.send_keys(ref5_email)
            time.sleep(time_short)

            ref_phone_number = self.driver.find_element(*self.ref5_phone_number)
            ref_phone_number.click()
            time.sleep(time_short)
            ref_phone_number.send_keys(Keys.CONTROL + "a")
            ref_phone_number.send_keys(Keys.DELETE)
            time.sleep(time_short)
            ref_phone_number.send_keys(ref5_phone_number)
            time.sleep(time_short)

            ref_landline_number = self.driver.find_element(*self.ref5_landline)
            ref_landline_number.click()
            time.sleep(time_short)
            ref_landline_number.send_keys(Keys.CONTROL + "a")
            ref_landline_number.send_keys(Keys.DELETE)
            time.sleep(time_short)
            ref_landline_number.send_keys(ref5_landline_number)
            time.sleep(time_short)

            try:
                # Phone Number
                ref_phone_country = self.driver.find_element(*self.ref5_country_code_phone_number)
                ref_phone_country.click()
                time.sleep(time_short)
                Country_menu = self.driver.find_element(*self.country_menu)
                Country_menu.click()
                time.sleep(time_short)
                Country_menu.send_keys(Keys.CONTROL + "a")
                Country_menu.send_keys(Keys.DELETE)
                time.sleep(time_short)

                Country_menu.send_keys(ref5_phone_CC)
                time.sleep(time_long)
                country_lower = ref5_phone_CC.lower()
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
                new_datatest_ID = self.driver.find_element(By.CSS_SELECTOR, f'[data-test-id="{country_selected}"]')
                time.sleep(time_short)
                new_datatest_ID.click()

            except:
                folder_path = "screenshots"
                os.makedirs(folder_path, exist_ok=True)
                timestamp = time.strftime("%Y%m%d-%H%M%S")
                screenshot_name = f"{folder_path}/country_code_5_mobile{timestamp}.png"

                # Take screenshot
                self.driver.save_screenshot(screenshot_name)
                print('Country-Code not found')
            time.sleep(time_short)

            try:
                # Landline Number
                ref_landline_country = self.driver.find_element(*self.ref5_country_code_landline)
                ref_landline_country.click()
                time.sleep(time_short)
                Country_menu = self.driver.find_element(*self.country_menu)
                Country_menu.click()
                time.sleep(time_short)
                Country_menu.send_keys(Keys.CONTROL + "a")
                Country_menu.send_keys(Keys.DELETE)
                time.sleep(time_short)

                Country_menu.send_keys(ref5_landline_CC)
                time.sleep(time_long)
                country_lower = ref5_landline_CC.lower()
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
                new_datatest_ID = self.driver.find_element(By.CSS_SELECTOR, f'[data-test-id="{country_selected}"]')
                time.sleep(time_short)
                new_datatest_ID.click()

            except:
                folder_path = "screenshots"
                os.makedirs(folder_path, exist_ok=True)
                timestamp = time.strftime("%Y%m%d-%H%M%S")
                screenshot_name = f"{folder_path}/country_code_5_landline{timestamp}.png"

                # Take screenshot
                self.driver.save_screenshot(screenshot_name)
                print('Country-Code not found')

            time.sleep(time_med)

        except:
            folder_path = "screenshots"
            os.makedirs(folder_path, exist_ok=True)
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            screenshot_name = f"{folder_path}/reference 5{timestamp}.png"

            # Take screenshot
            self.driver.save_screenshot(screenshot_name)
            print("Reference block 5 not found")


    def continue_references(self):
        time.sleep(time_long)
        continue_reference_bttn = self.driver.find_element(*self.continue_bttn_reference)
        continue_reference_bttn.click()
        time.sleep(time_med)

















