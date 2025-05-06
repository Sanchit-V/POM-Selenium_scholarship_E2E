import time

import user_details
from Page_Object.Summary_Page import Summary
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
time_short = user_details.time_short
time_med = user_details.time_med
time_long = user_details.time_long

class Submit(Summary):


    def submitReport(self):
        WebDriverWait(self.driver,12).until(EC.presence_of_element_located(self.TnC))
        TnC_button = self.driver.find_element(*self.TnC)
        y_position = TnC_button.location['y']

        current_position = 0
        step = 100
        while current_position < y_position:
            self.driver.execute_script(f"window.scrollTo(0, {current_position});")
            current_position += step
            time.sleep(0.05)

        TnC_button.click()
        time.sleep(time_short)

        Send_button = self.driver.find_element(*self.Submit)
        Send_button.click()

        time.sleep(time_med)

        


