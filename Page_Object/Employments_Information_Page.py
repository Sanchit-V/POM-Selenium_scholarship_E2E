from Import_Libraries import Import_libraries
By=Import_libraries.By

class EmploymentInformation:
    def __init__(self, driver):
        self.driver = Import_libraries._driver
        self.currently_working_yes = By.CSS_SELECTOR, '[data-test-id="radio-input-employment-status-yes"]'
        self.currently_working_no = By.CSS_SELECTOR, '[data-test-id="radio-input-employment-status-no"]'

        self.institution_name = By.CSS_SELECTOR, '[data-test-id="input-employment-information-institution-name"]'
        self.position = By.CSS_SELECTOR, '[data-test-id="input-employment-information-position"]'
        self.area = By.CSS_SELECTOR, '[data-test-id="input-employment-information-area"]'

        self.work_category = By.CSS_SELECTOR, '[data-test-id="select-display-employment-information-worker-category"]'
        self.dependent = By.CSS_SELECTOR, '[data-test-id="li-employment-information-worker-category-Dependent"]'
        self.independent = By.CSS_SELECTOR, '[data-test-id="li-employment-information-worker-category-Independent"]'

        self.activity = By.CSS_SELECTOR, '[data-test-id="input-employment-information-activity"]'

        self.seniority = By.CSS_SELECTOR, '[data-test-id="select-display-employment-information-seniority-in-position"]'
        self.one_year = By.CSS_SELECTOR, '[data-test-id="li-employment-information-seniority-in-position-oneYear"]'
        self.two_year = By.CSS_SELECTOR, '[data-test-id="li-employment-information-seniority-in-position-twoYears"]'
        self.three_year = By.CSS_SELECTOR, '[data-test-id="li-employment-information-seniority-in-position-threeYears"]'
        self.four_year = By.CSS_SELECTOR, '[data-test-id="li-employment-information-seniority-in-position-fourYears"]'
        self.five_year = By.CSS_SELECTOR, '[data-test-id="li-employment-information-seniority-in-position-fiveYears"]'
        self.six_or_more = By.CSS_SELECTOR, '[data-test-id="li-employment-information-seniority-in-position-sixOrMoreYears"]'

        self.monthly_salary_emp = By.CSS_SELECTOR, '[data-test-id="input-personal-monthly-expense"]'

        self.country = By.CSS_SELECTOR, '[data-test-id="autocomplete-input-employment-address-country"]'
        self.state = By.CSS_SELECTOR, '[data-test-id="autocomplete-input-employment-address-state"]'
        self.city = By.CSS_SELECTOR, '[data-test-id="autocomplete-input-employment-address-city"]'
        self.zip_code = By.CSS_SELECTOR, '[data-test-id="input-employment-address-zip-code"]'
        self.address = By.CSS_SELECTOR, '[data-test-id="input-employment-address-address"]'

        self.landline_number = By.CSS_SELECTOR, '[data-test-id="input-employment-address-employment-contact-landline-phone"]'
        self.landline_number_country = By.CSS_SELECTOR, '[data-test-id="employment-contact-landline-phone-country-iso2-code-open-country-code-menu"]'
        self.country_menu = By.CSS_SELECTOR, '[data-test-id="input-filter-flag"]'

        # [placeholder="Landline phone"]
        self.phone_number = By.CSS_SELECTOR, '[data-test-id="input-employment-address-employment-contact-phone-number"]'
        self.phone_number_country = By.CSS_SELECTOR, '[data-test-id="employment-contact-phone-number-country-iso2-code-open-country-code-menu"]'
        # [placeholder="Phone number"]



        self.url = By.CSS_SELECTOR, '[data-test-id="input-employment-information-website"]'

        self.employment_back_button = By.CSS_SELECTOR, '[data-test-id="btn-back-employment"]'
        self.employment_cancel_button = By.CSS_SELECTOR, '[data-test-id="btn-cancel-employment"]'
        self.employment_continue_button = By.CSS_SELECTOR, '[data-test-id="btn-continue-employment"]'


