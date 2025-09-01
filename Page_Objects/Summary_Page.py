from Libraries.Libraries import Import_libraries
By=Import_libraries.By

class SummaryPageObjects:
    def __init__(self, driver):
        self.driver = Import_libraries._driver
        self.Submit = By.CSS_SELECTOR, '[data-test-id="btn-send-summary"]'
        self.TnC = By.XPATH, "//input[@type='checkbox']"



