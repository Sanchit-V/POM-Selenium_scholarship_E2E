import time

from Page_Object.Summary_Page import Summary


class Submit(Summary):

    def submitReport(self):
        TnC_button = self.driver.find_element(*self.TnC)
        y_position = TnC_button.location['y']

        current_position = 0
        step = 100
        while current_position < y_position:
            self.driver.execute_script(f"window.scrollTo(0, {current_position});")
            current_position += step
            time.sleep(0.05)

        TnC_button.click()
        time.sleep(1)

        Send_button = self.driver.find_element(*self.Submit)
        Send_button.click()

        time.sleep(2)

        


