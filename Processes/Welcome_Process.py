class Welcome_Process:
    def __init__(self, welcome_page):
        self.welcome_page=welcome_page

    def run_process(self, expected_message, user_greeting):
        self.welcome_page.Check_snack_bar(expected_message)
        self.welcome_page.Check_Greetings(user_greeting)
        self.welcome_page.Get_Started()


