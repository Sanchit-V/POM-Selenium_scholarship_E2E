from Import_Libraries import Import_libraries
By=Import_libraries.By

class EmploymentInformation:
    def __init__(self, driver):
        self.driver = Import_libraries.driver
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

        self.currency_employment = By.CSS_SELECTOR, '[data-test-id="select-display-employment-currency-code"]'

        # Currency Code
        self.currency_code_ARS = By.CSS_SELECTOR, '[data-test-id="li-employment-currency-code-$"][data-value="ARS"]'
        self.currency_code_BOB = By.CSS_SELECTOR, '[data-test-id="li-employment-currency-code-Bs"][data-value="BOB"]'
        self.currency_code_BRL = By.CSS_SELECTOR, '[data-test-id="li-employment-currency-code-R$"][data-value="BRL"]'
        self.currency_code_CLP = By.CSS_SELECTOR, '[data-test-id="li-employment-currency-code-$"][data-value="CLP"]'
        self.currency_code_COP = By.CSS_SELECTOR, '[data-test-id="li-employment-currency-code-$"][data-value="COP"]'
        self.currency_code_USD = By.CSS_SELECTOR, '[data-test-id="li-employment-currency-code-$"][data-value="USD"]'
        self.currency_code_EUR = By.CSS_SELECTOR, '[data-test-id="li-employment-currency-code-€"][data-value="EUR"]'
        self.currency_code_MXN = By.CSS_SELECTOR, '[data-test-id="li-employment-currency-code-$"][data-value="MXN"]'
        self.currency_code_PAB = By.CSS_SELECTOR, '[data-test-id="li-employment-currency-code-B/."][data-value="PAB"]'
        self.currency_code_PEN = By.CSS_SELECTOR, '[data-test-id="li-employment-currency-code-S/."][data-value="PEN"]'
        self.currency_code_GTQ = By.CSS_SELECTOR, '[data-test-id="li-employment-currency-code-Q"][data-value="GTQ"]'
        self.currency_code_UYU = By.CSS_SELECTOR, '[data-test-id="li-employment-currency-code-$"][data-value="UYU"]'
        self.currency_code_C = By.CSS_SELECTOR, '[data-test-id="li-employment-currency-code-C"][data-value="CRC"]'
        self.currency_code_DOP = By.CSS_SELECTOR, '[data-test-id="li-employment-currency-code-RD$"][data-value="DOP"]'
        self.currency_code_AOA = By.CSS_SELECTOR, '[data-test-id="li-employment-currency-code-Kz"][data-value="AOA"]'
        self.currency_code_CVE = By.CSS_SELECTOR, '[data-test-id="li-employment-currency-code-Esc."][data-value="CVE"]'
        self.currency_code_MZN = By.CSS_SELECTOR, '[data-test-id="li-employment-currency-code-MZN"][data-value="MZN"]'
        self.currency_code_VEF = By.CSS_SELECTOR, '[data-test-id="li-employment-currency-code-Bs.F."][data-value="VEF"]'
        self.currency_code_PYG = By.CSS_SELECTOR, '[data-test-id="li-employment-currency-code-Gs."][data-value="PYG"]'
        self.currency_code_HNL = By.CSS_SELECTOR, '[data-test-id="li-employment-currency-code-L"][data-value="HNL"]'
        self.currency_code_NIO = By.CSS_SELECTOR, '[data-test-id="li-employment-currency-code-C$"][data-value="NIO"]'
        self.currency_code_XAF = By.CSS_SELECTOR, '[data-test-id="li-employment-currency-code-FCFA"][data-value="XAF"]'
        self.currency_code_XOF = By.CSS_SELECTOR, '[data-test-id="li-employment-currency-code-FCFA"][data-value="XOF"]'
        self.currency_code_BLU = By.CSS_SELECTOR, '[data-test-id="li-employment-currency-code-$B"][data-value="BLU"]'
        self.currency_code_SIM = By.CSS_SELECTOR, '[data-test-id="li-employment-currency-code-$S"][data-value="SIM"]'
        self.currency_code_VES = By.CSS_SELECTOR, '[data-test-id="li-employment-currency-code-Bs.S."][data-value="VES"]'

        self.monthly_salary_emp = By.CSS_SELECTOR, '[data-test-id="input-employment-monthly-salary"]'

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


