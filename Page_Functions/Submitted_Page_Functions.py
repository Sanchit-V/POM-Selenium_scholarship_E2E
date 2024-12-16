from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from Page_Object.Submitted_Page import SubmittedPage

class Submitted_Page(SubmittedPage):
    def final_page(self):
        final_form_submitted = self.driver.find_element(*self.form_submitted_final)
        print(final_form_submitted.text)
        print('***************************************')

        final_form_message_submission = self.driver.find_element(*self.form_submitted_message)
        print(final_form_message_submission.text)
        print('***************************************')

        time.sleep(4)

