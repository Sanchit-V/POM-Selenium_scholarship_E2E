from logging import exception

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

import user_details
from Page_Object.Login_Page import LoginPage
from Page_Object.Welcome_Page import WelcomePage

time_short = user_details.time_short
time_med = user_details.time_med
time_long = user_details.time_long

class Welcome_Page(WelcomePage):
    def Check_snack_bar(self, expected_message):

        try:
            snack_bar = self.driver.find_element(*self.logged_in_snack)
            actual_message = snack_bar.text

            print("Snack-Bar message Extracted as: " + actual_message)

        except Exception as e:
            print(f"No Snackbar Encountered.:{e}")






    def Check_Greetings(self, user_greeting):
        try:
            greeting = self.driver.find_element(*self.user_greetings)

            actual_greeting = greeting.text

            print("Greetings Extracted as: " + actual_greeting)

        except Exception as e:
            print(f"No Greeting-Message Encountered.:{e}")





    def Get_Started(self):
        try:
            # Always re-locate the login button
            get_Started_button = self.driver.find_element(*self.get_started_button)

            # Wait for the login button to be clickable
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(get_Started_button)
            )

            get_Started_button.click()
            print("Clicked Login Button")
        except Exception as e:
            print(f"Error in clicking login button: {e}")


        time.sleep(time_long)






