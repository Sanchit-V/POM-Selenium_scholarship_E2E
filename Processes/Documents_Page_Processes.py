class Documents_Page_Process:
    def __init__(self, documents_page):
        self.documents_page = documents_page

    def run_processes(self, Passport_File,Curriculum_File,Letter_Of_Motive,Other_Document,have_degree_checkbox,Degree,
                      Transcript, Graduation_Certificate,Letter_Of_Commitment):
        self.documents_page.delete_documents()
        self.documents_page.ID_Passport(Passport_File)
        self.documents_page.Curriculum(Curriculum_File)
        self.documents_page.Letter_of_moTive(Letter_Of_Motive)
        self.documents_page.other_Document(Other_Document)
        self.documents_page.Have_degree_checkbox(have_degree_checkbox)
        self.documents_page.deGree(Degree)
        self.documents_page.transCript(Transcript)
        self.documents_page.graDuation(Graduation_Certificate)
        self.documents_page.LoM(Letter_Of_Commitment)
        self.documents_page.continue_documents()
