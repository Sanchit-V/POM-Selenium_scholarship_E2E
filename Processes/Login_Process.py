from Pydentic_Model.models import LoginData
class LoginPageProcess:
    def __init__(self, login_page):  # Accept instance of Login_Page
        self.login_page = login_page

    def run_process(self, data:LoginData):
        self.login_page.select_language(data)
        self.login_page.enter_access_code(data)
        self.login_page.login()


