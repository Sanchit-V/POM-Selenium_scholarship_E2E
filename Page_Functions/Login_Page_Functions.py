from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import Data.user_details as user_details
from Page_Objects.Login_Page import LoginPageObjects

time_short = user_details.time_short
time_med = user_details.time_med
time_long = user_details.time_long

class LoginPageFunctions(LoginPageObjects):

    def select_language(self, selected_language):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(self.Access_Code))
        
        selected_language_button = self.driver.find_element(*self.Language_Button)
        
        selected_language_button.click()
        time.sleep(time_med)

        if selected_language == 1 :
            select_english = self.driver.find_element(*self.Language_English)
            select_english.click()
            print("Selected Language: English")
        
        if selected_language == 0:
            select_spanish = self.driver.find_element(*self.Language_Spanish)
            select_spanish.click()
            print("Selected Language: Spanish")

        time.sleep(time_med)

    def enter_access_code(self, access_code):
        access_code_element = self.driver.find_element(*self.Access_Code)
        time.sleep(time_short)
        access_code_element.send_keys(access_code)
        time.sleep(time_short)
        print(f"Entered Access Code: {access_code}")
        time.sleep(time_short)
        # access_visible = self.driver.find_element(*self.Visible_Icon)
        # access_visible.click()
        # time.sleep(time_med)
        try:
            access_visible = self.driver.find_element(*self.Visible_Icon)
            access_visible.click()
            time.sleep(time_med)

        except:
            print("No visible icon found.")
        
    def login(self):
        try:
            # Always re-locate the login button
            login_button = self.driver.find_element(*self.Login_Button)

            # Wait for the login button to be clickable
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(login_button)
            )
            
            login_button.click()
            print("Clicked Login Button")
        except:
            print(f"Error in clicking login button.")


        time.sleep(time_long)
        
        # additional_redirect = self.driver.find_element(*self.red_ref)
        # WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(additional_redirect))

  
        # additional_redirect.click()
        # time.sleep(2)

        
