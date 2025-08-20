import os

from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import user_details
from Page_Objects.Additional_Informations_Page import AdditionalInfoObjects
import time
time_short = user_details.time_short
time_med = user_details.time_med
time_long = user_details.time_long

class AdditionalInformationFunctions(AdditionalInfoObjects):
    def select_Option(self, additional_type,Text_Additional_field):
        WebDriverWait(self.driver,12).until(EC.presence_of_element_located(self.google))

        time.sleep(time_med)
     
        option_map = {
                1: self.google,
                2: self.facebook,
                3: self.instagram,
                4: self.referred,
                5: self.company,
                6: self.agreement,
                7: self.university,
                8: self.speech
    }

        # Get locator from map (default to webinar if not found)
        locator = option_map.get(additional_type, self.webinar)

        # Find and click
        element = self.driver.find_element(*locator)
        element.click()

        try:
            text_field = self.driver.find_element(*self.Text_Bar)
            text_field.click()
            time.sleep(1)
            text_field.send_keys(Keys.CONTROL + "a")
            text_field.send_keys(Keys.DELETE)
            time.sleep(1)
            print('*****************************************\t')
            print('Web element found\t')
            print('*****************************************')
            text_field.send_keys(Text_Additional_field)

        except:
            print("No text field found")
            folder_path = "screenshots"
            os.makedirs(folder_path, exist_ok=True)
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            screenshot_name = f"{folder_path}/additional_info_page{timestamp}.png"

            # Take screenshot
            self.driver.save_screenshot(screenshot_name)

        time.sleep(time_med)

        Finish_bttn = self.driver.find_element(*self.Finish_button)
        Finish_bttn.click()
        time.sleep(time_med)








