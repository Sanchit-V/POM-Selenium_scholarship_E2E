from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from Page_Object.Login_Page import LoginPage


class Login_Page(LoginPage):

    def select_language(self, selected_language):
        selected_language_button = self.driver.find_element(*self.Language_Button)
        selected_language_button.click()
        time.sleep(2)

        if selected_language == 1:
            select_english = self.driver.find_element(*self.Language_English)
            select_english.click()
            print("Selected Language: English")
        else:
            select_spanish = self.driver.find_element(*self.Language_Spanish)
            select_spanish.click()
            print("Selected Language: Spanish")

        time.sleep(2)

    def enter_access_code(self, access_code):
        access_code_element = self.driver.find_element(*self.Access_Code)
        access_code_element.send_keys(access_code)
        print(f"Entered Access Code: {access_code}")
        time.sleep(2)
        access_visible = self.driver.find_element(*self.Visible_Icon)
        access_visible.click()
        time.sleep(2)



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


        time.sleep(5)
