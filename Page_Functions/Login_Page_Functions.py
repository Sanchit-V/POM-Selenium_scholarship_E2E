from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import user_details
from Page_Object.Login_Page import LoginPage

time_short = user_details.time_short
time_med = user_details.time_med
time_long = user_details.time_long

class Login_Page(LoginPage):

    def select_language(self, selected_language):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(self.Access_Code))
        
        selected_language_button = self.driver.find_element(*self.Language_Button)
        
        selected_language_button.click()
        time.sleep(time_med)

        if selected_language == 1:
            select_english = self.driver.find_element(*self.Language_English)
            select_english.click()
            print("Selected Language: English")
        else:
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
            folder_path = "screenshots"
            os.makedirs(folder_path, exist_ok=True)
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            screenshot_name = f"{folder_path}/eye_button_login_page{timestamp}.png"

            # Take screenshot
            self.driver.save_screenshot(screenshot_name)

        
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
        except Exception as e:
            print(f"Error in clicking login button: {e}")


        time.sleep(time_long)
