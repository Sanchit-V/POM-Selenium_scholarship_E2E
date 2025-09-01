from Pydentic_Model.models import EmploymentInfoData
class EmployementInfoProcess:
    def __init__(self, employment_info_page):
        self.employment_info_page = employment_info_page

    def run_processes(self, data:EmploymentInfoData):

        self.employment_info_page.Currently_working(data)

        self.employment_info_page.position_info(data)
        
        self.employment_info_page.Currency_Selection(data)

        self.employment_info_page.employment_country(data)

        self.employment_info_page.employment_contact(data)

        self.employment_info_page.nations(data)

        self.employment_info_page.emp_info_continue()
