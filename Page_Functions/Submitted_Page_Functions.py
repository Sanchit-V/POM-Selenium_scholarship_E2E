from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

import user_details

time_short = user_details.time_short
time_med = user_details.time_med
time_long = user_details.time_long
from Page_Object.Submitted_Page import SubmittedPage

class Submitted_Page(SubmittedPage):
    def final_page(self):
        
        WebDriverWait(self.driver,12).until(EC.presence_of_element_located(self.form_submitted_final))

        final_form_submitted = self.driver.find_element(*self.form_submitted_final)
        print(final_form_submitted.text)
        print('***************************************')

        final_form_message_submission = self.driver.find_element(*self.form_submitted_message)
        print(final_form_message_submission.text)
        print('***************************************')


        time.sleep(time_long)

