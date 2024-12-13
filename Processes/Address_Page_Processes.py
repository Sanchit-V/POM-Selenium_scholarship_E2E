class Address_Page_Process:
    def __init__(self, address_page):
        self.address_page = address_page

    def run_processes(self, additional_emails_to_be_added, email_Ids, default_phone, default_whatsapp,total_additionals,
                      number_of_additional_phone, number_of_additional_whatsapp,
                      additional_1, additional_2, additional_3,
                      country_0,country_1, country_2, country_3, country_4,
                      housing_type, housing_conditions,Country, State, City, home_address, zip_code):
        self.address_page.default_Email()
        self.address_page.delete_email(additional_emails_to_be_added)
        self.address_page.add_email(additional_emails_to_be_added)
        self.address_page.email_add(email_Ids, additional_emails_to_be_added)
        self.address_page.phone_number(default_phone, default_whatsapp)
        self.address_page.delete_phone(total_additionals)
        self.address_page.add_phone_number(number_of_additional_phone)
        self.address_page.add_whats_number(number_of_additional_whatsapp)
        self.address_page.add_the_additional_numbers(additional_1, additional_2, additional_3)
        self.address_page.country_code(country_0,country_1, country_2, country_3, country_4)
        self.address_page.housing_details(housing_type)
        self.address_page.housing_Conditions(housing_conditions)
        self.address_page.Nationality(Country,State,City)
        self.address_page.Address_ZipCode(home_address, zip_code)
        self.address_page.Continue_address()
