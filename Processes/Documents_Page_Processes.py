from Pydentic_Model.models import DocumentUploadData
class DocumentsPageProcess:
    def __init__(self, documents_page):
        self.documents_page = documents_page

    def run_processes(self, data:DocumentUploadData):
        self.documents_page.delete_documents()
        self.documents_page.ID_Passport()
        self.documents_page.Curriculum()
        self.documents_page.Letter_of_moTive()
        self.documents_page.other_Document()
        self.documents_page.Have_degree_checkbox(data)
        self.documents_page.deGree()
        self.documents_page.transCript()
        self.documents_page.graDuation()
        self.documents_page.LoM()
        self.documents_page.continue_documents()
