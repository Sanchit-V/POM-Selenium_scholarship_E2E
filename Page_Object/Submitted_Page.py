from Import_Libraries import Import_libraries
By=Import_libraries.By

class SubmittedPage:
    def __init__(self, driver):
        self.driver = Import_libraries.driver
        self.form_submitted_final = By.CSS_SELECTOR, '[data-test-td="text-blocked-title"]'
        self.form_submitted_message = By.CSS_SELECTOR, '[data-test-id="text-submitted-description"]'
