from Model.Personal_Page_Model import PersonalDetailsPageModel
class PersonalDetailsProcess:
    def __init__(self, personal_details):
        self.personal_details = personal_details

    def run_process(self, data:PersonalDetailsPageModel):
        self.personal_details.document_type_selection(data)
        self.personal_details.document_number(data)
        self.personal_details.marital_status(data)
        self.personal_details.Applicant_profession(data)
        self.personal_details.Applicant_DOB(data)
        self.personal_details.Applicant_Nation(data)
        self.personal_details.Applicant_State(data)
        self.personal_details.Applicant_City(data)
        self.personal_details.Applicant_Nationality(data)
        self.personal_details.Currency_Selection(data)
        self.personal_details.Applicant_Income(data)
        self.personal_details.Applicant_Expense(data)
        self.personal_details.Financial_Dependent(data)
        self.personal_details.Has_Children(data)
        self.personal_details.Number_of_children(data)
        self.personal_details.Continue_button()

