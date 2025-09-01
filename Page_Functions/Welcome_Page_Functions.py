import os
from logging import exception

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

import Data.user_details as user_details

from Page_Objects.Welcome_Page import WelcomePage

time_short = user_details.time_short
time_med = user_details.time_med
time_long = user_details.time_long

class Welcome_Page(WelcomePage):
    def Check_snack_bar(self, expected_message):
        WebDriverWait(self.driver,12).until(EC.presence_of_element_located(self.logged_in_snack))

        try:
            snack_bar = self.driver.find_element(*self.logged_in_snack)
            actual_message = snack_bar.text

            print("Snack-Bar message Extracted as: " + actual_message)

        except :
            print(f"No Snackbar Encountered.")






    def Check_Greetings(self, user_greeting):
        try:
            greeting = self.driver.find_element(*self.user_greetings)

            actual_greeting = greeting.text

            print("Greetings Extracted as: " + actual_greeting)

        except:
            print(f"No Greeting-Message Encountered.")





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

        except:
            print(f"Error in clicking login button.")

        
        time.sleep(time_long)






