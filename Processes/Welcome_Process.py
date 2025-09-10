from Model.Welcome_Page_Model import WecomePageData
class Welcome_Process:
    def __init__(self, welcome_page):
        self.welcome_page=welcome_page

    def run_process(self,data:WecomePageData):
        self.welcome_page.Check_snack_bar(data)
        self.welcome_page.Check_Greetings(data)
        self.welcome_page.Get_Started()


