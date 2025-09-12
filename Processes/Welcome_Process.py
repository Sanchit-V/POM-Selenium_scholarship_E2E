from Data.Welcome_Page_Data import WelcomePageMother
class Welcome_Process:
    def __init__(self, welcome_page):
        self.welcome_page=welcome_page

    def run_process(self):
        data = WelcomePageMother.get()
        self.welcome_page.Check_snack_bar(data.ExpectedMessageData)
        self.welcome_page.Check_Greetings(data.UserGreetingData)
        self.welcome_page.Get_Started()


