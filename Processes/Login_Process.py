class Login_Process:
    def __init__(self, login_page):  # Accept instance of Login_Page
        self.login_page = login_page

    def run_process(self, access_code, selected_language):
        self.login_page.select_language(selected_language)
        self.login_page.enter_access_code(access_code)
        self.login_page.login()


