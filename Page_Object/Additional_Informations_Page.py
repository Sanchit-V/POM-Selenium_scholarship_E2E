from Import_Libraries import Import_libraries
By=Import_libraries.By

class AdditionalInfo:
    def __init__(self, driver):
        self.driver = Import_libraries.driver
        self.google = By.CSS_SELECTOR, '[data-test-id="radio-input-additional-information-knowledge-pathway-Google"]'
        self.facebook = By.CSS_SELECTOR, '[data-test-id="radio-input-additional-information-knowledge-pathway-Facebook"]'
        self.instagram = By.CSS_SELECTOR, '[data-test-id="radio-input-additional-information-knowledge-pathway-Instagram"]'
        self.referred = By.CSS_SELECTOR, '[data-test-id="radio-input-additional-information-knowledge-pathway-Referred"]'
        self.company = By.CSS_SELECTOR, '[data-test-id="radio-input-additional-information-knowledge-pathway-Company"]'
        self.agreement = By.CSS_SELECTOR, '[data-test-id="radio-input-additional-information-knowledge-pathway-Agreement"]'
        self.university = By.CSS_SELECTOR, '[data-test-id="radio-input-additional-information-knowledge-pathway-University"]'
        self.speech = By.CSS_SELECTOR, '[data-test-id="radio-input-additional-information-knowledge-pathway-Speech"]'
        self.webinar = By.CSS_SELECTOR, '[data-test-id="radio-input-additional-information-knowledge-pathway-Webinar"]'
        self.Text_Bar = By.CSS_SELECTOR, '[data-test-id="input-additional-information-referral-details"]'
        self.Finish_button = By.CSS_SELECTOR, '[data-test-id="btn-continue-additional"]'

        self.referred_spanish = By.CSS_SELECTOR, '[data-test-id="radio-input-additional-information-knowledge-pathway-Referido"]'
        self.company_spanish = By.CSS_SELECTOR, '[data-test-id="radio-input-additional-information-knowledge-pathway-Empresa"]'
        self.agreement_spanish = By.CSS_SELECTOR, '[data-test-id="radio-input-additional-information-knowledge-pathway-Convenio"]'
        self.university_spanish = By.CSS_SELECTOR, '[data-test-id="radio-input-additional-information-knowledge-pathway-Universidad"]'
        self.speech_spanish = By.CSS_SELECTOR, '[data-test-id="radio-input-additional-information-knowledge-pathway-Charla"]'




