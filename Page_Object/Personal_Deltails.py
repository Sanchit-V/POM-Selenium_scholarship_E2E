from Import_Libraries import Import_libraries
By=Import_libraries.By

class PersonalDetails:
    def __init__(self, driver):
        #Document Type Web-Elements
        self.driver = Import_libraries.driver
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

        #Birth Details
        self.DOB = By.CSS_SELECTOR, '[data-test-id="date-picker-input-personal-birth-date"]' #Main-Dialogue Box


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

        #Monthly_Expense
        self.Monthly_Expense = By.CSS_SELECTOR, '[data-test-id="input-personal-monthly-expense"]'

        #Monthly_Income
        self.Monthly_Income = By.CSS_SELECTOR, '[data-test-id="input-personal-monthly-income"]'

        #Financial_Independent
        self.Financial_Independent_Yes = By.CSS_SELECTOR,'[data-test-id="radio-input-personal-financially-dependent-YES"]'
        self.Financial_Independent_No = By.CSS_SELECTOR,'[data-test-id="radio-input-personal-financially-dependent-NO"]'

        #Children_Details
        self.has_Children = By.CSS_SELECTOR,'[data-test-id="radio-input-personal-has-children-YES"]'
        self.does_Not_Have_Children = By.CSS_SELECTOR,'[data-test-id="radio-input-personal-has-children-NO"]'

        #Number_of_children
        self.zero_to_four = By.CSS_SELECTOR, '[data-test-id="input-personal-age-range-0-4"]'
        self.five_to_twelve = By.CSS_SELECTOR, '[data-test-id="input-personal-age-range-5-12"]'
        self.thirteen_to_eighteen = By.CSS_SELECTOR, '[data-test-id="input-personal-age-range-13-18"]'
        self.eighteen_plus = By.CSS_SELECTOR, '[data-test-id="input-personal-age-range-+18"]'

        #Continue_Button_personal_details
        self.continue_button = By.CSS_SELECTOR, '[data-test-id="btn-continue-personal"]'


















