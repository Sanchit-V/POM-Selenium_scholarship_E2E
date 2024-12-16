class Personal_Details_Process:
    def __init__(self, personal_details):
        self.personal_details = personal_details

    def run_process(self, document_type, Document_number, Martial_status, Profession, Date_Of_Birth, Country, State, City, Nationality, Monthly_Income, Monthly_Expense, Financially_Dependent, Has_Children, Range_0to4, Range_5to12, Range_13to18, Range_18plus, selected_language):
        self.personal_details.document_type_selection(document_type)
        self.personal_details.document_number(Document_number)
        self.personal_details.martial_Status(Martial_status)
        self.personal_details.Applicant_profession(Profession)
        self.personal_details.Applicant_DOB(Date_Of_Birth)
        self.personal_details.Applicant_Nation(Country)
        self.personal_details.Applicant_State(State)
        self.personal_details.Applicant_City(City)
        self.personal_details.Applicant_Nationality(Nationality)
        self.personal_details.Applicant_Income(Monthly_Income)
        self.personal_details.Applicant_Expense(Monthly_Expense)
        self.personal_details.Financial_Dependent(Financially_Dependent,selected_language)
        self.personal_details.Has_Children(Has_Children, selected_language)
        self.personal_details.Number_of_children(Range_0to4, Range_5to12, Range_13to18, Range_18plus)
        self.personal_details.Continue_button()

