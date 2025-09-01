from Libraries.Libraries import Import_libraries
By=Import_libraries.By

class PersonalDetailObjects:
    def __init__(self, driver):
        #Document Type Web-Elements
        self.driver = Import_libraries._driver
        self.document_type_button = By.CSS_SELECTOR, '[data-test-id="select-display-personal-document-type"]'  #Main-Dialogue Box
        self.other_document = By.CSS_SELECTOR, '[data-test-id="li-personal-document-type-Other"]'
        self.RUC = By.CSS_SELECTOR,'[data-test-id="li-personal-document-type-RUC"]'
        self.foreign_identity_card = By.CSS_SELECTOR,'''[data-test-id="li-personal-document-type-Foreigner's identity card"]'''
        self.passport = By.CSS_SELECTOR, '[data-test-id="li-personal-document-type-Passport"]'
        self.NIC = By.CSS_SELECTOR,'[data-test-id="li-personal-document-type-National identity card"]'

        #Document Number Web-Elements
        self.document_number_field = By.CSS_SELECTOR, '[data-test-id="input-personal-document-number"]'    #Main-Dialogue Box
        self.document_number_enter = By.CSS_SELECTOR, '[data-test-id="input-personal-document-number"]'

        #Martial Status Web-Elements
        self.martial_status = By.CSS_SELECTOR, '[data-test-id="select-display-personal-marital-status"]'   #Main-Dialogue Box
        self.married = By.CSS_SELECTOR, '[data-test-id="li-personal-marital-status-Married"]'
        self.single = By.CSS_SELECTOR, '[data-test-id="li-personal-marital-status-Single"]'
        self.divorced = By.CSS_SELECTOR, '[data-test-id="li-personal-marital-status-Divorced"]'
        self.widowed = By.CSS_SELECTOR, '[data-test-id="li-personal-marital-status-Widowed"]'
        self.separated = By.CSS_SELECTOR, '[data-test-id="li-personal-marital-status-Separated"]'

        #Profession Web-Elements
        self.profession_field = By.CSS_SELECTOR, '[data-test-id="input-personal-profession"]'    #Main-Dialogue Box
        self.profession = By.CSS_SELECTOR, '[data-test-id="input-personal-profession"]'

        # Birth Details
        self.DOB = By.CSS_SELECTOR, '[data-test-id="date-picker-input-personal-birth-date"]'    #By.XPATH, '/html/body/div[2]/div/main/div/div[2]/form/div[2]/div[1]/div/div/div[2]/div[1]/div/div/div/input' # #Main-Dialogue Box
        #self.DOB = By.CSS_SELECTOR, '[data-test-id="btn-date-picker-open-personal-birth-date"]'


        #Nation
        self.Country = By.CSS_SELECTOR, '[data-test-id="autocomplete-input-personal-birth-country"]' #Main-Dialogue Box


        #State
        self.State = By.CSS_SELECTOR, '[data-test-id="autocomplete-input-personal-birth-state"]' #Main-Dialogue Box


        #City
        self.City = By.CSS_SELECTOR, '[data-test-id="autocomplete-input-personal-birth-city"]'  #Main-Dialogue Box

        #Nationality
        self.Nationality = By.CSS_SELECTOR, '[data-test-id="autocomplete-input-personal-birth-nationality"]'  #Main-Dialogue Box

        #Common_DropDown
        self.dropdown = By.CSS_SELECTOR, '#combo-box-demo-listbox li'

        #Currency Menu
        self.currency_dropdown = By.CSS_SELECTOR, '[data-test-id="select-display-personal-currency-code"]'

        #Currency Code
        self.currency_code_ARS = By.CSS_SELECTOR, '[data-test-id="li-personal-currency-code-$"][data-value="ARS"]'
        self.currency_code_BOB = By.CSS_SELECTOR, '[data-test-id="li-personal-currency-code-Bs"][data-value="BOB"]'
        self.currency_code_BRL = By.CSS_SELECTOR, '[data-test-id="li-personal-currency-code-R$"][data-value="BRL"]'
        self.currency_code_CLP = By.CSS_SELECTOR, '[data-test-id="li-personal-currency-code-$"][data-value="CLP"]'
        self.currency_code_COP = By.CSS_SELECTOR, '[data-test-id="li-personal-currency-code-$"][data-value="COP"]'
        self.currency_code_USD = By.CSS_SELECTOR, '[data-test-id="li-personal-currency-code-$"][data-value="USD"]'
        self.currency_code_EUR = By.CSS_SELECTOR, '[data-test-id="li-personal-currency-code-€"][data-value="EUR"]'
        self.currency_code_MXN = By.CSS_SELECTOR, '[data-test-id="li-personal-currency-code-$"][data-value="MXN"]'
        self.currency_code_PAB = By.CSS_SELECTOR, '[data-test-id="li-personal-currency-code-B/."][data-value="PAB"]'
        self.currency_code_PEN = By.CSS_SELECTOR, '[data-test-id="li-personal-currency-code-S/."][data-value="PEN"]'
        self.currency_code_GTQ = By.CSS_SELECTOR, '[data-test-id="li-personal-currency-code-Q"][data-value="GTQ"]'
        self.currency_code_UYU = By.CSS_SELECTOR, '[data-test-id="li-personal-currency-code-$"][data-value="UYU"]'
        self.currency_code_C = By.CSS_SELECTOR, '[data-test-id="li-personal-currency-code-C"][data-value="CRC"]'
        self.currency_code_DOP = By.CSS_SELECTOR, '[data-test-id="li-personal-currency-code-RD$"][data-value="DOP"]'
        self.currency_code_AOA = By.CSS_SELECTOR, '[data-test-id="li-personal-currency-code-Kz"][data-value="AOA"]'
        self.currency_code_CVE = By.CSS_SELECTOR, '[data-test-id="li-personal-currency-code-Esc."][data-value="CVE"]'
        self.currency_code_MZN = By.CSS_SELECTOR, '[data-test-id="li-personal-currency-code-MZN"][data-value="MZN"]'
        self.currency_code_VEF = By.CSS_SELECTOR, '[data-test-id="li-personal-currency-code-Bs.F."][data-value="VEF"]'
        self.currency_code_PYG = By.CSS_SELECTOR, '[data-test-id="li-personal-currency-code-Gs."][data-value="PYG"]'
        self.currency_code_HNL = By.CSS_SELECTOR, '[data-test-id="li-personal-currency-code-L"][data-value="HNL"]'
        self.currency_code_NIO = By.CSS_SELECTOR, '[data-test-id="li-personal-currency-code-C$"][data-value="NIO"]'
        self.currency_code_XAF = By.CSS_SELECTOR, '[data-test-id="li-personal-currency-code-FCFA"][data-value="XAF"]'
        self.currency_code_XOF = By.CSS_SELECTOR, '[data-test-id="li-personal-currency-code-FCFA"][data-value="XOF"]'
        self.currency_code_BLU = By.CSS_SELECTOR, '[data-test-id="li-personal-currency-code-$B"][data-value="BLU"]'
        self.currency_code_SIM = By.CSS_SELECTOR, '[data-test-id="li-personal-currency-code-$S"][data-value="SIM"]'
        self.currency_code_VES = By.CSS_SELECTOR, '[data-test-id="li-personal-currency-code-Bs.S."][data-value="VES"]'

        # Monthly_Income
        self.Monthly_Income = By.CSS_SELECTOR, '[data-test-id="input-personal-monthly-income"]'

        #Monthly_Expense
        self.Monthly_Expense = By.CSS_SELECTOR, '[data-test-id="input-personal-monthly-expense"]'
        #Monthly_Expense
        self.Monthly_Expense = By.CSS_SELECTOR, '[data-test-id="input-personal-monthly-expense"]'

        #Monthly_Income
        self.Monthly_Income = By.CSS_SELECTOR, '[data-test-id="input-personal-monthly-income"]'

        #Financial_Independent
        self.Financial_Independent_Yes = By.CSS_SELECTOR,'[data-test-id="radio-input-personal-financially-dependent-yes"]'
        self.Financial_Independent_No = By.CSS_SELECTOR,'[data-test-id="radio-input-personal-financially-dependent-no"]'

        #Children_Details
        self.has_Children = By.CSS_SELECTOR,'[data-test-id="radio-input-personal-has-children-yes"]'
        self.does_Not_Have_Children = By.CSS_SELECTOR,'[data-test-id="radio-input-personal-has-children-no"]'


        #Number_of_children
        self.zero_to_four = By.CSS_SELECTOR, '[data-test-id="input-personal-age-range-0-4"]'
        self.five_to_twelve = By.CSS_SELECTOR, '[data-test-id="input-personal-age-range-5-12"]'
        self.thirteen_to_eighteen = By.CSS_SELECTOR, '[data-test-id="input-personal-age-range-13-18"]'
        self.eighteen_plus = By.CSS_SELECTOR, '[data-test-id="input-personal-age-range-+18"]'

        #Continue_Button_personal_details
        self.continue_button = By.CSS_SELECTOR, '[data-test-id="btn-continue-personal"]'


















