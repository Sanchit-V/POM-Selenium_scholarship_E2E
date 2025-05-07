from Import_Libraries import Import_libraries
By=Import_libraries.By

class ReferencesPage:
    def __init__(self, driver):
        self.driver =  Import_libraries._driver

        self.add_reference = By.CSS_SELECTOR, '[data-test-id="label-add-references"]'

        self.ref1_dropdown = By.CSS_SELECTOR, '[data-test-id="button-applicant-reference-accordion-1"]'

        self.ref1_first_name = By.CSS_SELECTOR, '[data-test-id="input-applicant-reference-first-name-1"]'
        self.ref1_last_name = By.CSS_SELECTOR, '[data-test-id="input-applicant-reference-last-name-1"]'
        self.ref1_occupation = By.CSS_SELECTOR, '[data-test-id="input-applicant-reference-position-or-occupation-1"]'
        self.ref1_email = By.CSS_SELECTOR, '[data-test-id="input-applicant-reference-email-address-1"]'
        self.ref1_country_code_phone_number = By.CSS_SELECTOR, '[data-test-id="applicant-reference-phone-number-1-country-iso2-code-open-country-code-menu"]'
        self.ref1_phone_number = By.CSS_SELECTOR, '[data-test-id="input-employment-address-applicant-reference-phone-number-1"]'
        self.ref1_landline = By.CSS_SELECTOR, '[data-test-id="input-employment-address-applicant-reference-landline-phone-1"]'
        self.ref1_country_code_landline = By.CSS_SELECTOR, '[data-test-id="applicant-reference-landline-phone-1-country-iso2-code-open-country-code-menu"]'

        self.ref2_dropdown = By.CSS_SELECTOR, '[data-test-id="button-applicant-reference-accordion-2"]'

        self.ref2_first_name = By.CSS_SELECTOR, '[data-test-id="input-applicant-reference-first-name-2"]'
        self.ref2_last_name = By.CSS_SELECTOR, '[data-test-id="input-applicant-reference-last-name-2"]'
        self.ref2_occupation = By.CSS_SELECTOR, '[data-test-id="input-applicant-reference-position-or-occupation-2"]'
        self.ref2_email = By.CSS_SELECTOR, '[data-test-id="input-applicant-reference-email-address-2"]'
        self.ref2_country_code_phone_number = By.CSS_SELECTOR, '[data-test-id="applicant-reference-phone-number-2-country-iso2-code-open-country-code-menu"]'
        self.ref2_phone_number = By.CSS_SELECTOR, '[data-test-id="input-employment-address-applicant-reference-phone-number-2"]'
        self.ref2_landline = By.CSS_SELECTOR, '[data-test-id="input-employment-address-applicant-reference-landline-phone-2"]'
        self.ref2_country_code_landline = By.CSS_SELECTOR, '[data-test-id="applicant-reference-landline-phone-2-country-iso2-code-open-country-code-menu"]'

        self.ref3_dropdown = By.CSS_SELECTOR, '[data-test-id="button-applicant-reference-accordion-3"]'

        self.ref3_first_name = By.CSS_SELECTOR, '[data-test-id="input-applicant-reference-first-name-3"]'
        self.ref3_last_name = By.CSS_SELECTOR, '[data-test-id="input-applicant-reference-last-name-3"]'
        self.ref3_occupation = By.CSS_SELECTOR, '[data-test-id="input-applicant-reference-position-or-occupation-3"]'
        self.ref3_email = By.CSS_SELECTOR, '[data-test-id="input-applicant-reference-email-address-3"]'
        self.ref3_country_code_phone_number = By.CSS_SELECTOR, '[data-test-id="applicant-reference-phone-number-3-country-iso2-code-open-country-code-menu"]'
        self.ref3_phone_number = By.CSS_SELECTOR, '[data-test-id="input-employment-address-applicant-reference-phone-number-3"]'
        self.ref3_landline = By.CSS_SELECTOR, '[data-test-id="input-employment-address-applicant-reference-landline-phone-3"]'
        self.ref3_country_code_landline = By.CSS_SELECTOR, '[data-test-id="applicant-reference-landline-phone-3-country-iso2-code-open-country-code-menu"]'

        self.ref4_dropdown = By.CSS_SELECTOR, '[data-test-id="button-applicant-reference-accordion-4"]'

        self.ref4_first_name = By.CSS_SELECTOR, '[data-test-id="input-applicant-reference-first-name-4"]'
        self.ref4_last_name = By.CSS_SELECTOR, '[data-test-id="input-applicant-reference-last-name-4"]'
        self.ref4_occupation = By.CSS_SELECTOR, '[data-test-id="input-applicant-reference-position-or-occupation-4"]'
        self.ref4_email = By.CSS_SELECTOR, '[data-test-id="input-applicant-reference-email-address-4"]'
        self.ref4_country_code_phone_number = By.CSS_SELECTOR, '[data-test-id="applicant-reference-phone-number-4-country-iso2-code-open-country-code-menu"]'
        self.ref4_phone_number = By.CSS_SELECTOR, '[data-test-id="input-employment-address-applicant-reference-phone-number-4"]'
        self.ref4_landline = By.CSS_SELECTOR, '[data-test-id="input-employment-address-applicant-reference-landline-phone-4"]'
        self.ref4_country_code_landline = By.CSS_SELECTOR, '[data-test-id="applicant-reference-landline-phone-4-country-iso2-code-open-country-code-menu"]'

        self.ref5_dropdown = By.CSS_SELECTOR, '[data-test-id="button-applicant-reference-accordion-5"]'

        self.ref5_first_name = By.CSS_SELECTOR, '[data-test-id="input-applicant-reference-first-name-5"]'
        self.ref5_last_name = By.CSS_SELECTOR, '[data-test-id="input-applicant-reference-last-name-5"]'
        self.ref5_occupation = By.CSS_SELECTOR, '[data-test-id="input-applicant-reference-position-or-occupation-5"]'
        self.ref5_email = By.CSS_SELECTOR, '[data-test-id="input-applicant-reference-email-address-5"]'
        self.ref5_country_code_phone_number = By.CSS_SELECTOR, '[data-test-id="applicant-reference-phone-number-5-country-iso2-code-open-country-code-menu"]'
        self.ref5_phone_number = By.CSS_SELECTOR, '[data-test-id="input-employment-address-applicant-reference-phone-number-5"]'
        self.ref5_landline = By.CSS_SELECTOR, '[data-test-id="input-employment-address-applicant-reference-landline-phone-5"]'
        self.ref5_country_code_landline = By.CSS_SELECTOR, '[data-test-id="applicant-reference-landline-phone-5-country-iso2-code-open-country-code-menu"]'

        self.delete_additional_reference = By.CSS_SELECTOR, '[data-test-id="button-delete-reference-details-4"]'

        self.continue_bttn_reference = By.CSS_SELECTOR, '[data-test-id="btn-continue-references"]'
        self.country_menu = By.CSS_SELECTOR, '[data-test-id="input-filter-flag"]'






