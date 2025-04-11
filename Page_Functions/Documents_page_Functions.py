from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import time

import user_details

time_short = user_details.time_short
time_med = user_details.time_med
time_long = user_details.time_long

from Page_Object.Documents_Page import DocumentsPage

class Documents_Page(DocumentsPage):

    def ID_Passport(self, Passport_File):
        try:
            upload_Id_passport = self.driver.find_element(*self.bttn_id_passport)
            upload_Id_passport.click()
            time.sleep(time_med)

            pyautogui.write(Passport_File)
            time.sleep(time_short)
            pyautogui.press("enter")
            time.sleep(time_short)


        except:
            print("Not able to click the upload option.")

    time.sleep(time_short)

    def Curriculum(self,Curriculum_File):
        try:
            curriculum_File = self.driver.find_element(*self.bttn_curriculum)
            curriculum_File.click()
            time.sleep(time_med)

            pyautogui.write(Curriculum_File)
            time.sleep(time_short)
            pyautogui.press("enter")
            time.sleep(time_short)


        except:
            print("Not able to click the upload option.")

    time.sleep(time_short)

    def Letter_of_moTive(self,Letter_Of_Motive):
        try:
            LoM = self.driver.find_element(*self.bttn_letter_of_motive)
            LoM.click()
            time.sleep(time_med)

            pyautogui.write(Letter_Of_Motive)
            time.sleep(time_short)
            pyautogui.press("enter")
            time.sleep(time_short)


        except:
            print("Not able to click the upload option.")

    time.sleep(time_short)

    def other_Document(self,Other_Document):
        try:
            LoM = self.driver.find_element(*self.bttn_other_document)
            LoM.click()
            time.sleep(time_med)

            pyautogui.write(Other_Document)
            time.sleep(time_short)
            pyautogui.press("enter")
            time.sleep(time_short)


        except:
            print("Not able to click the upload option.")

    time.sleep(time_short)

    def Have_degree_checkbox(self, have_degree_checkbox):
        try:
            unchecked_degree = self.driver.find_element(*self.unchecked_degree_box)
            if unchecked_degree:
                try:
                    if have_degree_checkbox == 0:
                        checkbox = self.driver.find_element(*self.checkbox_no_degree)
                        checkbox.click()
                        time.sleep(time_short)

                    else:
                        print('Applicant has degree')

                except:
                    print('Already checked.')

        except:
            print('Web element not found.')


        try:
            checked_degree = self.driver.find_element(*self.checked_degree_box)
            if checked_degree:
                try:
                    if have_degree_checkbox == 1:
                        checkbox = self.driver.find_element(*self.checkbox_no_degree)
                        checkbox.click()
                        time.sleep(time_short)

                    else:
                        print('Applicant does not have a degree')

                except:
                    print('Already checked.')

        except:
            print('Web element not found.')

    time.sleep(time_short)


    def deGree(self,Degree):
        try:
            LoM = self.driver.find_element(*self.bttn_degree)
            LoM.click()
            time.sleep(time_med)

            pyautogui.write(Degree)
            time.sleep(time_short)
            pyautogui.press("enter")
            time.sleep(time_short)


        except:
            print("Not able to click the upload option.")

    time.sleep(time_short)

    def transCript(self,Transcript):
        try:
            LoM = self.driver.find_element(*self.transcript)
            LoM.click()
            time.sleep(time_med)

            pyautogui.write(Transcript)
            time.sleep(time_short)
            pyautogui.press("enter")
            time.sleep(time_short)


        except:
            print("Not able to click the upload option.")

    time.sleep(time_short)

    def graDuation(self,Graduation_Certificate):
        try:
            LoM = self.driver.find_element(*self.graduate_certificate)
            LoM.click()
            time.sleep(time_med)

            pyautogui.write(Graduation_Certificate)
            time.sleep(time_short)
            pyautogui.press("enter")
            time.sleep(time_short)


        except:
            print("Not able to click the upload option.")

    time.sleep(time_short)

    def LoM(self,Letter_Of_Commitment):
        try:
            LoM = self.driver.find_element(*self.letter_of_commitment)
            LoM.click()
            time.sleep(time_med)

            pyautogui.write(Letter_Of_Commitment)
            time.sleep(time_short)
            pyautogui.press("enter")
            time.sleep(time_short)


        except:
            print("Not able to click the upload option.")

    time.sleep(time_short)





    def delete_documents(self):
        try:
            del_Id_pass = self.driver.find_element(*self.bttn_delete_id_passport)
            del_Id_pass.click()
            time.sleep(time_short)

        except:
            print("No file to be deleted.")

        try:
            del_Curriculum  = self.driver.find_element(*self.bttn_delete_curriculum)
            del_Curriculum.click()
            time.sleep(time_short)

        except:
            print("No file to be deleted.")

        try:
            del_Letter_of_motive  = self.driver.find_element(*self.bttn_delete_letter_of_motive)
            del_Letter_of_motive.click()
            time.sleep(time_short)

        except:
            print("No file to be deleted.")

        try:
            del_other_files  = self.driver.find_element(*self.bttn_delete_other_documents)
            del_other_files.click()
            time.sleep(time_short)

        except:
            print("No file to be deleted.")

        try:
            del_degree = self.driver.find_element(*self.bttn_delete_degree)
            del_degree.click()
            time.sleep(time_short)

        except:
            print("No file to be deleted.")

        try:
            del_transcript = self.driver.find_element(*self.bttn_delete_transcript)
            del_transcript.click()
            time.sleep(time_short)

        except:
            print("No file to be deleted.")

        try:
            del_graduation = self.driver.find_element(*self.bttn_delete_graduation_certificate)
            del_graduation .click()
            time.sleep(time_short)

        except:
            print("No file to be deleted.")

        try:
            del_commitment = self.driver.find_element(*self.bttn_delete_letter_of_commitment)
            del_commitment.click()
            time.sleep(time_short)

        except:
            print("No file to be deleted.")

    time.sleep(time_short)



    def continue_documents(self):
        time.sleep(time_long)
        continue_bttn_document = self.driver.find_element(*self.bttn_continue_documents)
        continue_bttn_document.click()







