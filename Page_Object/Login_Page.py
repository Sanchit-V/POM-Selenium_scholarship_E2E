
from Import_Libraries import Import_libraries
By=Import_libraries.By


class LoginPage:
    def __init__(self, driver):
        self.driver=Import_libraries._driver
        self.Language_Button=By.CSS_SELECTOR, '[data-test-id="select-language"]'
        self.Access_Code = By.CSS_SELECTOR, '[data-test-id="input-login-access-code"]'
        self.Language_English = By.CSS_SELECTOR, '[data-test-id="li-en-US-language"]'
        self.Language_Spanish = By.CSS_SELECTOR, '[data-test-id="li-es-ES-language"]'
        self.Login_Button = By.CSS_SELECTOR,'[data-test-id="btn-submit-login"]'
        self.Visible_Icon = By.CSS_SELECTOR, '[data-test-id="icon-visibility-on-access-code-login"]'

