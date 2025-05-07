from Import_Libraries import Import_libraries
By=Import_libraries.By

class AddressPage:
    def __init__(self, driver):
        self.driver = Import_libraries._driver

        #############################################################################################################################

        #Email Field Elements
        self.default_email = By.CSS_SELECTOR, '[data-test-id="input-address-contact-default-email"]'
        self.add_email_button = By.CSS_SELECTOR,'[data-test-id="text-address-contact-email-add"]'
        self.add_email_dialogue_box_0 = By.CSS_SELECTOR, '[data-test-id="input-address-contact-email-0"]'
        self.add_email_dialogue_box_1 = By.CSS_SELECTOR, '[data-test-id="input-address-contact-email-1"]'
        self.add_email_dialogue_box_2 = By.CSS_SELECTOR, '[data-test-id="input-address-contact-email-2"]'
        self.add_email_dialogue_box_3 = By.CSS_SELECTOR, '[data-test-id="input-address-contact-email-3"]'
        self.add_email_dialogue_box_4 = By.CSS_SELECTOR, '[data-test-id="input-address-contact-email-4"]'
        self.delete_email_0 = By.CSS_SELECTOR, '[data-test-id="btn-end-adornment-address-contact-email-0"]'
        self.delete_email_1 = By.CSS_SELECTOR, '[data-test-id="btn-end-adornment-address-contact-email-1"]'
        self.delete_email_2 = By.CSS_SELECTOR, '[data-test-id="btn-end-adornment-address-contact-email-2"]'
        self.delete_email_3 = By.CSS_SELECTOR, '[data-test-id="btn-end-adornment-address-contact-email-3"]'
        self.delete_email_4 = By.CSS_SELECTOR, '[data-test-id="btn-end-adornment-address-contact-email-4"]'
        self.confirm_delete = By.CSS_SELECTOR, '[data-test-id="btn-dialog-confirm-delete-email"]'
        self.cancel_delete = By.CSS_SELECTOR, '[data-test-id="btn-dialog-close-delete-email"]'

        #############################################################################################################################

        #Phone-Number Field Elements
        self.add_additional_phone_number_button = By.CSS_SELECTOR, '[data-test-id="text-address-contact-add-phone-number"]'
        self.add_additional_phone_option = By.CSS_SELECTOR, "input[value='PHONE']"
        self.add_additional_whatsapp_option = By.CSS_SELECTOR, "input[value='WHATSAPP']"
        self.add_default_phone_number = By.CSS_SELECTOR, '[data-test-id="input-address-contact-phone-number-0"]'
        self.add_default_whatsapp_number = By.CSS_SELECTOR, '[data-test-id="input-address-contact-phone-number-1"]'

        self.add_new_phone_2 = By.CSS_SELECTOR, '[data-test-id="input-address-contact-phone-number-2"]'
        self.add_new_phone_3 = By.CSS_SELECTOR, '[data-test-id="input-address-contact-phone-number-3"]'
        self.add_new_phone_4 = By.CSS_SELECTOR, '[data-test-id="input-address-contact-phone-number-4"]'

        self.select_country_code_0 = By.CSS_SELECTOR, '[data-test-id="text-country-phone-code-0"]'
        self.select_country_code_1 = By.CSS_SELECTOR, '[data-test-id="text-country-phone-code-1"]'
        self.select_country_code_2 = By.CSS_SELECTOR, '[data-test-id="text-country-phone-code-2"]'
        self.select_country_code_3 = By.CSS_SELECTOR, '[data-test-id="text-country-phone-code-3"]'
        self.select_country_code_4 = By.CSS_SELECTOR, '[data-test-id="text-country-phone-code-4"]'

        self.select_ADD_dialogue_box = By.CSS_SELECTOR,'[data-test-id="btn-dialog-confirm-add-number"]'
        self.select_CANCEL_dialogue_box = By.CSS_SELECTOR ,'[data-test-id="btn-dialog-close-add-number"]'

        self.confirm_add_number = By.CSS_SELECTOR, '[data-test-id="btn-dialog-confirm-add-number"]'
        self.delete_added_phone_number = By.CSS_SELECTOR, '[data-test-id="btn-end-adornment-address-contact-phone-number-2"]'
        self.delete_confirmation = By.CSS_SELECTOR, '[data-test-id="btn-dialog-confirm-delete-phone"]'

        self.country_code_box = By.CSS_SELECTOR, '[data-test-id="input-filter-flag"]'

        self.delete_phone_number_2 = By.CSS_SELECTOR, '[data-test-id="btn-end-adornment-address-contact-phone-number-2"]'
        self.delete_phone_number_3 = By.CSS_SELECTOR, '[data-test-id="btn-end-adornment-address-contact-phone-number-3"]'
        self.delete_phone_number_4 = By.CSS_SELECTOR, '[data-test-id="btn-end-adornment-address-contact-phone-number-4"]'

        self.country_code_listbox = By.CSS_SELECTOR, '[data-test-id="autocomplete-listbox"]'
        self.India_list_box = By.CSS_SELECTOR, '[data-test-id="li-india"]'





        #############################################################################################################################

        #Residence Field Elements
        self.housing_type = By.CSS_SELECTOR, '[data-test-id="select-display-addresses-residence-type-of-housing"]'
        self.Department = By.CSS_SELECTOR, '[data-test-id="li-addresses-residence-type-of-housing-Department"]'
        self.House =  By.CSS_SELECTOR, '[data-test-id="li-addresses-residence-type-of-housing-House"]'

        self.Housing_conditions = By.CSS_SELECTOR, '[data-test-id="select-display-addresses-residence-housing-condition"]'
        self.Family = By.CSS_SELECTOR, '[data-test-id="li-addresses-residence-housing-condition-Family"]'
        self.Own = By.CSS_SELECTOR, '[data-test-id="li-addresses-residence-housing-condition-Own"]'
        self.Rented = By.CSS_SELECTOR, '[data-test-id="li-addresses-residence-housing-condition-Rented"]'

        self.country_residence = By.CSS_SELECTOR, '[data-test-id="autocomplete-input-addresses-residence-country"]'
        self.state_residence = By.CSS_SELECTOR, '[data-test-id="autocomplete-input-addresses-residence-state"]'
        self.city_residence = By.CSS_SELECTOR, '[data-test-id="autocomplete-input-addresses-residence-city"]'
        self.zipcode = By.CSS_SELECTOR, '[data-test-id="input-addresses-residence-zip-code"]'
        self.address = By.CSS_SELECTOR, '[data-test-id="input-addresses-residence-address"]'

        #############################################################################################################################

        #Buttons
        self.continue_button = By.CSS_SELECTOR, '[data-test-id="btn-continue-address"]'
        self.back_button = By.CSS_SELECTOR, '[data-test-id="btn-mobile-stepper-previous-step"]'

        #############################################################################################################################















