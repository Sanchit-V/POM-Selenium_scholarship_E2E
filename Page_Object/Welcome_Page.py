from Import_Libraries import Import_libraries
By=Import_libraries.By

class WelcomePage:
    def __init__(self, driver):
        self.driver=Import_libraries._driver
        self.user_greetings=By.CSS_SELECTOR, '[data-test-id="text-welcome-message"]'
        self.logged_in_snack=By.CSS_SELECTOR,'#notistack-snackbar > .MuiTypography-root'
        self.get_started_button=By.CSS_SELECTOR, '[data-test-id="btn-get-started-welcome"]'
