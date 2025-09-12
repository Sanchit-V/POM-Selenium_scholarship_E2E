from Data.Login_Page_Data import LoginPageMother
class LoginPageProcess:
    def __init__(self, login_page):  
        self.login_page = login_page

    def run_process(self):
        data = LoginPageMother.get()
        self.login_page.select_language(data.LanguageSelectionData)
        self.login_page.enter_access_code(data.AccessCodeData)
        self.login_page.login()


