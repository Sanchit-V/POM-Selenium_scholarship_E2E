import os
from unittest import skipIf

from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

import Data.user_details as user_details
from Page_Objects.Address_Page import AddressPageObjects
from Pydentic_Model.models import AddressDetailsData

time_short = user_details.time_short
time_med = user_details.time_med
time_long = user_details.time_long

class AddressPageFunctions(AddressPageObjects):
    def default_Email(self):
        WebDriverWait(self.driver,12).until(EC.presence_of_element_located(self.default_email))
        try:
            default_email_element = self.driver.find_element(*self.default_email)
            Default_email = default_email_element.text or default_email_element.get_attribute("value")
            print(f"Default Email: {Default_email}")
        except :
            print(f"Error locating default email.")

    def add_email(self, data:AddressDetailsData):
        for email in range(data.additional_emails_to_be_added):
            added_emails = self.driver.find_element(*self.add_email_button)
            added_emails.click()
            time.sleep(time_short)

    def delete_email(self, data:AddressDetailsData):

        if data.access_code == data.previous_access_code:
            try:
                for delete in range(data.additional_emails_to_be_added + 5):

                    delete_box = self.driver.find_element(*self.delete_email_0)
                    delete_box.click()
                    time.sleep(1)

                    try:
                        self.driver.find_element(*self.confirm_delete).click()
                        time.sleep(1)

                    except:
                        print('Empty Email fields.')


            except:
                print("+++++++")

        else:
            print("No previously added emails found")

    def add_additional_emails(self, data:AddressDetailsData):
    # Map index to locators
        try:

            email_boxes = [
                    self.add_email_dialogue_box_0,
                    self.add_email_dialogue_box_1,
                    self.add_email_dialogue_box_2,
                    self.add_email_dialogue_box_3,
                    self.add_email_dialogue_box_4
            ]


                # Loop safely within available locators and provided emails
            for i, email in enumerate(data.email_Ids[:len(email_boxes)]):
                    box = self.driver.find_element(*email_boxes[i])
                    print(f"Adding email: {email}")
                    box.click()
                    box.send_keys(email)
        
        except:
            print("No Dialogue box found for additional emails")

        time.sleep(time_med)


    def phone_number(self, data:AddressDetailsData):   #number_of_additional_phone, number_of_additional_whatsapp, total_additionals
        Default_Phone = self.driver.find_element(*self.add_default_phone_number)
        Default_Phone.click()
        Default_Phone.send_keys(Keys.CONTROL + "a")
        Default_Phone.send_keys(Keys.DELETE)
        Default_Phone.send_keys(data.default_phone)
        time.sleep(time_short)

        Default_Whatsapp = self.driver.find_element(*self.add_default_whatsapp_number)
        Default_Whatsapp.click()
        Default_Whatsapp.send_keys(Keys.CONTROL + "a")
        Default_Whatsapp.send_keys(Keys.DELETE)
        Default_Whatsapp.send_keys(data.default_whatsapp)
        time.sleep(time_short)

    def delete_phone(self, data:AddressDetailsData):

        if data.access_code == data.previous_access_code:
            try:
                for delete in range(data.total_additionals + 3):

                    delete_box = self.driver.find_element(*self.delete_added_phone_number)
                    delete_box.click()
                    time.sleep(1)

                    try:
                        confirm_delete = self.driver.find_element(*self.delete_confirmation)
                        confirm_delete.click()
                        time.sleep(1)
                    except:
                        print('Empty phone number fields')



            except:
                print('Empty Email fields.')
                print("+++++++")

        else:
            print("No previously added phone numbers found")



    def add_phone_number(self, data:AddressDetailsData):
        add_new_number = self.driver.find_element(*self.add_additional_phone_number_button)

        for i in range (data.number_of_additional_phone):
            add_new_number.click()
            add_phone = self.driver.find_element(*self.add_additional_phone_option)
            add_phone.click()
            time.sleep(time_short)
            confirm_add = self.driver.find_element(*self.confirm_add_number)
            confirm_add.click()
            time.sleep(time_short)

        time.sleep(time_med)

    def add_whats_number(self, data:AddressDetailsData):
        add_new_number = self.driver.find_element(*self.add_additional_phone_number_button)

        for i in range(data.number_of_additional_whatsapp):
            add_new_number.click()
            add_whats = self.driver.find_element(*self.add_additional_whatsapp_option)
            add_whats.click()
            time.sleep(time_short)
            confirm_add = self.driver.find_element(*self.confirm_add_number)
            confirm_add.click()
            time.sleep(time_short)

        time.sleep(time_med)

    def add_the_additional_numbers(self, data:AddressDetailsData):
        try:
            add_1 = self.driver.find_element(*self.add_new_phone_2)
            add_1.click()
            add_1.send_keys(data.additional_numbers[0])
            time.sleep(time_short)

        except:
            print("No Dialogue box found")

        try:
            add_2 = self.driver.find_element(*self.add_new_phone_3)
            add_2.click()
            add_2.send_keys(data.additional_numbers[1])
            time.sleep(time_short)

        except:
            print("No Dialogue box found")

        try:
            add_3 = self.driver.find_element(*self.add_new_phone_4)
            add_3.click()
            add_3.send_keys(data.additional_numbers[2])
            time.sleep(time_short)

        except:
            print("No Dialogue box found")

        time.sleep(time_med)


    def country_code(self,data:AddressDetailsData):  #, country_1, country_2, country_3, country_4

        try:
            CC_0 = self.driver.find_element(*self.select_country_code_0)
            CC_0.click()
            time.sleep(time_short)
            CC_Box = self.driver.find_element(*self.country_code_box)
            CC_Box.click()
            CC_Box.send_keys(data.country[0])
            time.sleep(time_short)

            if data.country[0] != 'India':
                CC_LB = self.driver.find_element(*self.country_code_listbox)
                CC_LB.click()


            else:
                try:
                    CC_Ind = self.driver.find_element(*self.India_list_box)
                    CC_Ind.click()
                except:
                    print(' ** ')

        except:
            print('Not Required.')

        time.sleep(time_med)

        try:
            CC_1 = self.driver.find_element(*self.select_country_code_1)
            CC_1.click()
            time.sleep(time_short)
            CC_Box = self.driver.find_element(*self.country_code_box)
            CC_Box.click()
            CC_Box.send_keys(data.country[1])
            time.sleep(time_short)

            if data.country[1] != 'India':
                CC_LB = self.driver.find_element(*self.country_code_listbox)
                CC_LB.click()


            else:
                try:
                    CC_Ind = self.driver.find_element(*self.India_list_box)
                    CC_Ind.click()
                except:
                    print(' ** ')

        except:
            print('Not Required.')

        time.sleep(time_med)

        try:
            CC_2 = self.driver.find_element(*self.select_country_code_2)
            CC_2.click()
            time.sleep(time_short)
            CC_Box = self.driver.find_element(*self.country_code_box)
            CC_Box.click()
            CC_Box.send_keys(data.country[2])
            time.sleep(time_short)

            if data.country[2] != 'India':
                CC_LB = self.driver.find_element(*self.country_code_listbox)
                CC_LB.click()


            else:
                try:
                    CC_Ind = self.driver.find_element(*self.India_list_box)
                    CC_Ind.click()
                except:
                    print(' ** ')

        except:
            print("Not Required")

        time.sleep(time_med)

        try:
            CC_3 = self.driver.find_element(*self.select_country_code_3)
            CC_3.click()
            time.sleep(time_short)
            CC_Box = self.driver.find_element(*self.country_code_box)
            CC_Box.click()
            CC_Box.send_keys(data.country[3])
            time.sleep(time_short)

            if data.country[3] != 'India':
                CC_LB = self.driver.find_element(*self.country_code_listbox)
                CC_LB.click()


            else:
                try:
                    CC_Ind = self.driver.find_element(*self.India_list_box)
                    CC_Ind.click()
                except:
                    print(' ** ')

        except:
            print('Not Required.')

        time.sleep(time_med)

        try:
            CC_4 = self.driver.find_element(*self.select_country_code_4)
            CC_4.click()
            time.sleep(time_short)
            CC_Box = self.driver.find_element(*self.country_code_box)
            CC_Box.click()
            CC_Box.send_keys(data.country[4])
            time.sleep(time_short)

            if data.country[4] != 'India':
                CC_LB = self.driver.find_element(*self.country_code_listbox)
                CC_LB.click()


            else:
                try:
                    CC_Ind = self.driver.find_element(*self.India_list_box)
                    CC_Ind.click()
                except:
                    print(' ** ')

        except:
            print('Not Required')

        time.sleep(time_med)

    def housing_details(self, data:AddressDetailsData):
        housing_Type = self.driver.find_element(*self.housing_type)
        housing_Type.click()

        time.sleep(time_short)

        if data.housing_type == 1:
            Department = self.driver.find_element(*self.Department)
            Department.click()


        else:
            House = self.driver.find_element(*self.House)
            House.click()


        #housing_Type.send_keys(Keys.TAB)

        time.sleep(time_long)



    def housing_Conditions(self, data:AddressDetailsData):
        housing_Conditions = self.driver.find_element(*self.Housing_conditions)
        housing_Conditions.click()
        time.sleep(time_short)

        if data.housing_conditions == 1:
             Family = self.driver.find_element(*self.Family)
             Family.click()

        elif data.housing_conditions == 2:
             Own = self.driver.find_element(*self.Own)
             Own.click()

        else:
             Rented = self.driver.find_element(*self.Rented)
             Rented.click()

        time.sleep(time_med)


    def Nationality(self, data:AddressDetailsData):
        country_select = self.driver.find_element(*self.country_residence)
        country_select.click()

        country_select.send_keys(data.Country)

        if data.Country == 'India':
            for i in range (2):
                self.driver.find_element(*self.country_residence).send_keys(Keys.ARROW_DOWN)

            time.sleep(time_short)

            self.driver.find_element(*self.country_residence).send_keys(Keys.ENTER)

        else:
            self.driver.find_element(*self.country_residence).send_keys(Keys.ARROW_DOWN)
            self.driver.find_element(*self.country_residence).send_keys(Keys.ENTER)

        time.sleep(time_med)


        try :
            home_State = self.driver.find_element(*self.state_residence)
            home_State.click()
            time.sleep(time_short)
            print('\t')
            print('***************************************\t')
            print('Web Element found for home state.')
            home_State.send_keys(data.State)
            home_State.send_keys(Keys.ARROW_DOWN)
            home_State.send_keys(Keys.ENTER)

        except:
            print('No State')

        print('***************************************\t')
        time.sleep(time_med)

        try:
            home_City = self.driver.find_element(*self.city_residence)
            home_City.click()
            time.sleep(time_short)
            print('Web Element found for home city.\t')
            print('***************************************\t')

            home_City.send_keys(data.City)
            home_City.send_keys(Keys.ARROW_DOWN)
            home_City.send_keys(Keys.ENTER)
            
        except:
            print('No City')

        time.sleep(time_long)


    def Address_ZipCode(self, data:AddressDetailsData):

        address_box = self.driver.find_element(*self.address)
        address_box.click()
        address_box.send_keys(Keys.CONTROL + "a")
        address_box.send_keys(Keys.DELETE)

        time.sleep(time_short)
        address_box.send_keys(data.home_address)
        time.sleep(time_short)

        Zip_code = self.driver.find_element(*self.zipcode)
        Zip_code.click()
        time.sleep(time_short)
        Zip_code.send_keys(Keys.CONTROL + "a")
        Zip_code.send_keys(Keys.DELETE)

        Zip_code.send_keys(data.zip_code)
        time.sleep(time_long)

    def Continue_address(self):

        
        WebDriverWait(self.driver,12).until(EC.presence_of_element_located(self.continue_button))

        continue_bttn = self.driver.find_element(*self.continue_button)
        continue_bttn.click()
        time.sleep(time_long)























































































