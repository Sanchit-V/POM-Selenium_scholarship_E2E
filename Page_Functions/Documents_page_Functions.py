from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import time

from Page_Object.Documents_Page import DocumentsPage

class Documents_Page(DocumentsPage):

    def ID_Passport(self, Passport_File):
        try:
            upload_Id_passport = self.driver.find_element(*self.bttn_id_passport)
            upload_Id_passport.click()
            time.sleep(2)

            pyautogui.write(Passport_File)
            time.sleep(1)
            pyautogui.press("enter")
            time.sleep(1)


        except:
            print("Not able to click the upload option.")

    time.sleep(1)

    def Curriculum(self,Curriculum_File):
        try:
            curriculum_File = self.driver.find_element(*self.bttn_curriculum)
            curriculum_File.click()
            time.sleep(2)

            pyautogui.write(Curriculum_File)
            time.sleep(1)
            pyautogui.press("enter")
            time.sleep(1)


        except:
            print("Not able to click the upload option.")

    time.sleep(1)

    def Letter_of_moTive(self,Letter_Of_Motive):
        try:
            LoM = self.driver.find_element(*self.bttn_letter_of_motive)
            LoM.click()
            time.sleep(2)

            pyautogui.write(Letter_Of_Motive)
            time.sleep(1)
            pyautogui.press("enter")
            time.sleep(1)


        except:
            print("Not able to click the upload option.")

    time.sleep(1)

    def other_Document(self,Other_Document):
        try:
            LoM = self.driver.find_element(*self.bttn_other_document)
            LoM.click()
            time.sleep(2)

            pyautogui.write(Other_Document)
            time.sleep(1)
            pyautogui.press("enter")
            time.sleep(1)


        except:
            print("Not able to click the upload option.")

    time.sleep(1)

    def Have_degree_checkbox(self, have_degree_checkbox):
        try:
            unchecked_degree = self.driver.find_element(*self.unchecked_degree_box)
            if unchecked_degree:
                try:
                    if have_degree_checkbox == 0:
                        checkbox = self.driver.find_element(*self.checkbox_no_degree)
                        checkbox.click()
                        time.sleep(1)

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
                        time.sleep(1)

                    else:
                        print('Applicant does not have a degree')

                except:
                    print('Already checked.')

        except:
            print('Web element not found.')

    time.sleep(1)


    def deGree(self,Degree):
        try:
            LoM = self.driver.find_element(*self.bttn_degree)
            LoM.click()
            time.sleep(2)

            pyautogui.write(Degree)
            time.sleep(1)
            pyautogui.press("enter")
            time.sleep(1)


        except:
            print("Not able to click the upload option.")

    time.sleep(1)

    def transCript(self,Transcript):
        try:
            LoM = self.driver.find_element(*self.transcript)
            LoM.click()
            time.sleep(2)

            pyautogui.write(Transcript)
            time.sleep(1)
            pyautogui.press("enter")
            time.sleep(1)


        except:
            print("Not able to click the upload option.")

    time.sleep(1)

    def graDuation(self,Graduation_Certificate):
        try:
            LoM = self.driver.find_element(*self.graduate_certificate)
            LoM.click()
            time.sleep(2)

            pyautogui.write(Graduation_Certificate)
            time.sleep(1)
            pyautogui.press("enter")
            time.sleep(1)


        except:
            print("Not able to click the upload option.")

    time.sleep(1)

    def LoM(self,Letter_Of_Commitment):
        try:
            LoM = self.driver.find_element(*self.letter_of_commitment)
            LoM.click()
            time.sleep(2)

            pyautogui.write(Letter_Of_Commitment)
            time.sleep(1)
            pyautogui.press("enter")
            time.sleep(1)


        except:
            print("Not able to click the upload option.")

    time.sleep(1)





    def delete_documents(self):
        try:
            del_Id_pass = self.driver.find_element(*self.bttn_delete_id_passport)
            del_Id_pass.click()
            time.sleep(1)

        except:
            print("No file to be deleted.")

        try:
            del_Curriculum  = self.driver.find_element(*self.bttn_delete_curriculum)
            del_Curriculum.click()
            time.sleep(1)

        except:
            print("No file to be deleted.")

        try:
            del_Letter_of_motive  = self.driver.find_element(*self.bttn_delete_letter_of_motive)
            del_Letter_of_motive.click()
            time.sleep(1)

        except:
            print("No file to be deleted.")

        try:
            del_other_files  = self.driver.find_element(*self.bttn_delete_other_documents)
            del_other_files.click()
            time.sleep(1)

        except:
            print("No file to be deleted.")

        try:
            del_degree = self.driver.find_element(*self.bttn_delete_degree)
            del_degree.click()
            time.sleep(1)

        except:
            print("No file to be deleted.")

        try:
            del_transcript = self.driver.find_element(*self.bttn_delete_transcript)
            del_transcript.click()
            time.sleep(1)

        except:
            print("No file to be deleted.")

        try:
            del_graduation = self.driver.find_element(*self.bttn_delete_graduation_certificate)
            del_graduation .click()
            time.sleep(1)

        except:
            print("No file to be deleted.")

        try:
            del_commitment = self.driver.find_element(*self.bttn_delete_letter_of_commitment)
            del_commitment.click()
            time.sleep(1)

        except:
            print("No file to be deleted.")

    time.sleep(1)



    def continue_documents(self):
        time.sleep(3)
        continue_bttn_document = self.driver.find_element(*self.bttn_continue_documents)
        continue_bttn_document.click()







