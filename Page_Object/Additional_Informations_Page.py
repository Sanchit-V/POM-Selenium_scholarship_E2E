from Import_Libraries import Import_libraries
By=Import_libraries.By

class AdditionalInfo:
    def __init__(self, driver):
        self.driver = Import_libraries.driver
        self.google = By.CSS_SELECTOR, '[data-test-id="radio-input-additional-information-knowledge-pathway-no"][value="GOOGLE"]'
        self.facebook = By.CSS_SELECTOR, '[data-test-id="radio-input-additional-information-knowledge-pathway-no"][value="FACEBOOK"]'
        self.instagram = By.CSS_SELECTOR, '[data-test-id="radio-input-additional-information-knowledge-pathway-no"][value="INSTAGRAM"]'
        self.referred = By.CSS_SELECTOR, '[data-test-id="radio-input-additional-information-knowledge-pathway-no"][value="REFERRED"]'
        self.company = By.CSS_SELECTOR, '[data-test-id="radio-input-additional-information-knowledge-pathway-no"][value="COMPANY"]'
        self.agreement = By.CSS_SELECTOR, '[data-test-id="radio-input-additional-information-knowledge-pathway-no"][value="AGREEMENT"]'
        self.university = By.CSS_SELECTOR, '[data-test-id="radio-input-additional-information-knowledge-pathway-no"][value="UNIVERSITY"]'
        self.speech = By.CSS_SELECTOR, '[data-test-id="radio-input-additional-information-knowledge-pathway-no"][value="SPEECH"]'
        self.webinar = By.CSS_SELECTOR, '[data-test-id="radio-input-additional-information-knowledge-pathway-no"][value="WEBINAR"]'
        self.Text_Bar = By.CSS_SELECTOR, '[data-test-id="input-additional-information-referral-details"]'
        self.Finish_button = By.CSS_SELECTOR, '[data-test-id="btn-continue-additional"]'






