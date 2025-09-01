from Libraries.Libraries import Import_libraries
By=Import_libraries.By

class ReferencesPageObjects:
    def __init__(self, driver):
        self.driver =  Import_libraries._driver

        self.add_reference = By.CSS_SELECTOR, '[data-test-id="label-add-references"]'
        self.delete_additional_reference = By.CSS_SELECTOR, '[data-test-id="button-delete-reference-details-4"]'

        self.continue_bttn_reference = By.CSS_SELECTOR, '[data-test-id="btn-continue-references"]'
        self.country_menu = By.CSS_SELECTOR, '[data-test-id="input-filter-flag"]'
        
        drop_down_selector = [(By.CSS_SELECTOR, f'[data-test-id="button-applicant-reference-accordion-{i}"]') for i in range(1,6)]
        first_name_selector = [(By.CSS_SELECTOR,f'[data-test-id="input-applicant-reference-first-name-{i}"]') for i in range(1,6)]
        last_name_selector = [(By.CSS_SELECTOR,f'[data-test-id="input-applicant-reference-last-name-{i}"]') for i in range(1,6)]
        occupation_selector = [(By.CSS_SELECTOR,f'[data-test-id="input-applicant-reference-position-or-occupation-{i}"]') for i in range(1,6)]
        email_selector = [(By.CSS_SELECTOR,f'[data-test-id="input-applicant-reference-email-address-{i}"]') for i in range(1,6)]
        phone_number_selector = [(By.CSS_SELECTOR,f'[data-test-id="input-employment-address-applicant-reference-phone-number-{i}"]') for i in range(1,6)]
        landline_selector = [(By.CSS_SELECTOR,f'[data-test-id="input-employment-address-applicant-reference-landline-phone-{i}"]') for i in range(1,6)]
        country_code_phone_selector = [(By.CSS_SELECTOR,f'[data-test-id="applicant-reference-phone-number-{i}-country-iso2-code-open-country-code-menu"]') for i in range(1,6)]
        country_code_landline_selector = [(By.CSS_SELECTOR,f'[data-test-id="applicant-reference-landline-phone-{i}-country-iso2-code-open-country-code-menu"]') for i in range(1,6)]


        self.ref_dropdown = drop_down_selector
        self.ref_first_name = first_name_selector
        self.ref_last_name = last_name_selector
        self.ref_occupation = occupation_selector
        self.ref_email = email_selector 
        self.ref_country_code_phone_number = country_code_phone_selector
        self.ref_phone_number = phone_number_selector
        self.ref_landline = landline_selector
        self.ref_country_code_landline = country_code_landline_selector
                
    
        
       
        






