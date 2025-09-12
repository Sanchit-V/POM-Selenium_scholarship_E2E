from Data.Address_Page_Data import AddressPageMother
class AddressPageProcess:
    def __init__(self, address_page):
        self.address_page = address_page

    def run_processes(self):
        data = AddressPageMother.get()
        self.address_page.default_Email()
        self.address_page.delete_email(data.ContactDetailsData)
        self.address_page.add_email(data.ContactDetailsData)
        self.address_page.add_additional_emails(data.ContactDetailsData)
        self.address_page.phone_number(data.ContactDetailsData)
        self.address_page.delete_phone(data.ContactDetailsData)
        self.address_page.add_phone_number(data.ContactDetailsData)
        self.address_page.add_whats_number(data.ContactDetailsData)
        self.address_page.add_the_additional_numbers(data.ContactDetailsData)
        self.address_page.country_code(data.ContactDetailsData)
        self.address_page.housing_details(data.ResidenceDetailsData)
        self.address_page.housing_Conditions(data.ResidenceDetailsData)
        self.address_page.Nationality(data.ResidenceDetailsData)
        self.address_page.Address_ZipCode(data.ResidenceDetailsData)
        self.address_page.Continue_address()
