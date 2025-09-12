from Data.Personal_Page_Data import PersonalPageMother
class PersonalDetailsProcess:
    def __init__(self, personal_details):
        self.personal_details = personal_details

    def run_process(self):
        data = PersonalPageMother.get()
        self.personal_details.document_type_selection(data.BasicData)
        self.personal_details.document_number(data.BasicData)
        self.personal_details.marital_status(data.BasicData)
        self.personal_details.Applicant_profession(data.BasicData)
        self.personal_details.Applicant_DOB(data.BirthData)
        self.personal_details.Applicant_Nation(data.BirthData)
        self.personal_details.Applicant_State(data.BirthData)
        self.personal_details.Applicant_City(data.BirthData)
        self.personal_details.Applicant_Nationality(data.BirthData)
        self.personal_details.Currency_Selection(data.FinancialData)
        self.personal_details.Applicant_Income(data.FinancialData)
        self.personal_details.Applicant_Expense(data.FinancialData)
        self.personal_details.Financial_Dependent(data.FinancialData)
        self.personal_details.Has_Children(data.FamilyDetailsData)
        self.personal_details.Number_of_children(data.FamilyDetailsData)
        self.personal_details.Continue_button()

