from Data.Employment_Page_Data import EmploymentInformationPageMother
class EmployementInfoProcess:
    def __init__(self, employment_info_page):
        self.employment_info_page = employment_info_page

    def run_processes(self):
        data = EmploymentInformationPageMother.get()

        self.employment_info_page.Currently_working(data.EmploymentStatusData)

        self.employment_info_page.position_info(data.PositionInformationData)
        
        self.employment_info_page.Currency_Selection(data.PositionInformationData)

        self.employment_info_page.employment_country(data.EmploymentAddressData)

        self.employment_info_page.employment_contact(data.EmploymentContactData)

        self.employment_info_page.nations(data.EmploymentContactData)

        self.employment_info_page.emp_info_continue()
