from Pydentic_Model.models import AddressDetailsData
class AddressPageProcess:
    def __init__(self, address_page):
        self.address_page = address_page

    def run_processes(self, data:AddressDetailsData):
        self.address_page.default_Email()
        self.address_page.delete_email(data)
        self.address_page.add_email(data)
        self.address_page.add_additional_emails(data)
        self.address_page.phone_number(data)
        self.address_page.delete_phone(data)
        self.address_page.add_phone_number(data)
        self.address_page.add_whats_number(data)
        self.address_page.add_the_additional_numbers(data)
        self.address_page.country_code(data)
        self.address_page.housing_details(data)
        self.address_page.housing_Conditions(data)
        self.address_page.Nationality(data)
        self.address_page.Address_ZipCode(data)
        self.address_page.Continue_address()
