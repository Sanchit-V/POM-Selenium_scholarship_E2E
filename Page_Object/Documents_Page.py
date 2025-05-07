from Import_Libraries import Import_libraries
By=Import_libraries.By

class DocumentsPage:
    def __init__(self, driver):
        self.driver = Import_libraries._driver

        self.bttn_id_passport = By.CSS_SELECTOR, '[data-test-id="upload-btn-documents-id/passport"]'
        self.bttn_curriculum = By.CSS_SELECTOR, '[data-test-id="upload-btn-documents-curriculum-vitae"]'
        self.bttn_letter_of_motive = By.CSS_SELECTOR, '[data-test-id="upload-btn-documents-letter-of-motive"]'
        self.bttn_other_document = By.CSS_SELECTOR, '[data-test-id="upload-btn-documents-other"]'

        self.bttn_degree = By.CSS_SELECTOR, '[data-test-id="upload-btn-documents-degree"]'
        self.checkbox_no_degree = By.CSS_SELECTOR, '[data-test-id="checkbox-has-academic-degree"]'
        self.checked_degree_box = By.CSS_SELECTOR, '[data-testid="CheckBoxIcon"]'
        self.unchecked_degree_box = By.CSS_SELECTOR, '[data-testid="CheckBoxOutlineBlankIcon"]'
        self.transcript = By.CSS_SELECTOR, '[data-test-id="upload-btn-documents-transcript-of-records"]'
        self.graduate_certificate = By.CSS_SELECTOR, '[data-test-id="upload-btn-documents-graduation-certificates"]'
        self.letter_of_commitment = By.CSS_SELECTOR, '[data-test-id="upload-btn-documents-letter-of-commitment"]'

        self.bttn_continue_documents = By.CSS_SELECTOR, '[data-test-id="btn-continue-documents"]'

        self.bttn_delete_id_passport = By.CSS_SELECTOR, '[data-test-id="clear-btn-icon-documents-id/passport"]'
        self.bttn_delete_curriculum = By.CSS_SELECTOR, '[data-test-id="clear-btn-icon-documents-curriculum-vitae"]'
        self.bttn_delete_letter_of_motive = By.CSS_SELECTOR, '[data-test-id="clear-btn-icon-documents-letter-of-motive"]'
        self.bttn_delete_other_documents = By.CSS_SELECTOR, '[data-test-id="clear-btn-icon-documents-other"]'

        self.bttn_delete_degree = By.CSS_SELECTOR, '[data-test-id="clear-btn-icon-documents-degree"]'
        self.bttn_delete_transcript = By.CSS_SELECTOR, '[data-test-id="clear-btn-icon-documents-transcript-of-records"]'
        self.bttn_delete_graduation_certificate = By.CSS_SELECTOR, '[data-test-id="clear-btn-icon-documents-graduation-certificates"]'
        self.bttn_delete_letter_of_commitment = By.CSS_SELECTOR, '[data-test-id="clear-btn-documents-letter-of-commitment"]'





