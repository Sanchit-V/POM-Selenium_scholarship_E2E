from Model.Reference_Page_Model import PersonalOrEmploymentReferencesPage
class ReferencePageProcess:
    def __init__(self, reference_page):
        self.reference_page = reference_page

    def run_processes(self, data:PersonalOrEmploymentReferencesPage):

        self.reference_page.delete_references(data)

        self.reference_page.add_references(data)

        self.reference_page.add_references_details(data)

        self.reference_page.continue_references()






