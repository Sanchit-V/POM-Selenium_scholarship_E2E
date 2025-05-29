import os
import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import user_details


from Page_Object.Documents_Page import DocumentsPage
from pyvirtualdisplay import Display
import Xlib.display

# Timeouts from user_details
time_short = user_details.time_short
time_med = user_details.time_med

time_long = user_details.time_long

class Documents_Page(DocumentsPage):
    """
    Extends DocumentsPage to handle file uploads via PyAutoGUI
    in a headless environment using a virtual display.
    """
    # def __init__(self, driver):
    #     super().__init__(driver)
    #     # Start virtual X display for PyAutoGUI
    #     self._disp = Display(visible=False, size=(1920, 1080), backend="xvfb")
    #     self._disp.start()
    #     os.environ['DISPLAY'] = self._disp.new_display_var

    # def _get_pyautogui(self):
    #     # Import and attach PyAutoGUI to the virtual display
    #     import pyautogui
    #     pyautogui._pyautogui_x11._display = Xlib.display.Display(os.environ['DISPLAY'])
    #     return pyautogui

    def ID_Passport(self, Passport_File):
        try:
            # Optional: click upload button to make sure any animation finishes
            self.driver.find_element(By.CSS_SELECTOR, "[data-test-id='upload-btn-documents-id/passport']").click()

            # Wait until the hidden <input type="file"> is in the DOM
            wait = WebDriverWait(self.driver, 10)
            file_input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-test-id='input-documents-id/passport']"))
            )

            # Path to the file inside Docker container
            full_path = "/home/seluser/Upload_Files/1.pdf"
            file_input.send_keys(full_path)

            time.sleep(time_short)

        except Exception as e:
            print("Not able to upload ID/Passport file:", e)

    def Curriculum(self, curriculum_file_name):
        try:
            # Optional: Click the upload button to trigger file input visibility/activation
            self.driver.find_element(By.CSS_SELECTOR, "[data-test-id='upload-btn-documents-curriculum-vitae']").click()

            # Wait for the hidden input[type=file] to appear in the DOM
            wait = WebDriverWait(self.driver, 10)
            file_input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-test-id='input-documents-curriculum-vitae']"))
            )

            # Construct the full file path inside the Docker container
            full_path = "/home/seluser/Upload_Files/2.pdf"

            # Upload the file directly
            file_input.send_keys(full_path)

            time.sleep(time_short)

        except Exception as e:
            print("Not able to upload Curriculum file:", e)

    def Letter_of_moTive(self, Letter_Of_Motive):
        try:
            # Click the upload button to trigger the file input
            self.driver.find_element(By.CSS_SELECTOR, "[data-test-id='upload-btn-documents-letter-of-motive']").click()

            # Wait for the file input to be present in the DOM
            wait = WebDriverWait(self.driver, 10)
            file_input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-test-id='input-documents-letter-of-motive']"))
            )

            # Full path to the file inside Docker container
            full_path = "/home/seluser/Upload_Files/3.pdf"

            # Upload the file
            file_input.send_keys(full_path)

            time.sleep(time_short)

        except Exception as e:
            print("Not able to upload Letter of Motive file:", e)

    def other_Document(self, Other_Document):
        try:
            # Click the upload button
            self.driver.find_element(By.CSS_SELECTOR, "[data-test-id='upload-btn-documents-other']").click()
    
            # Wait until the file input becomes present
            wait = WebDriverWait(self.driver, 10)
            file_input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-test-id='input-documents-other']"))
            )
    
            # Full path to the file inside Docker container
            full_path = "/home/seluser/Upload_Files/4.pdf"
    
            # Upload the file
            file_input.send_keys(full_path)
    
            time.sleep(time_short)
    
        except Exception as e:
            print("Not able to upload 'Other' document:", e)


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
                    print('Already un-checked.')

        except:
            print('Web element not found.')

    time.sleep(time_short)

    def deGree(self, Degree):
        try:
            # Wait until the input becomes enabled and clickable
            wait = WebDriverWait(self.driver, 10)
            upload_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test-id='upload-btn-documents-degree']"))
            )
    
            # Click the upload button
            upload_button.click()
    
            # Wait for file input to be present
            file_input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-test-id='input-documents-degree']"))
            )
    
            # Send file path
            file_input.send_keys("/home/seluser/Upload_Files/5.pdf")
    
            time.sleep(time_short)
    
        except Exception as e:
            print("Could not upload Degree document:", e)
            self._take_screenshot("Degree document")


    def transCript(self, Transcript):
        try:
            wait = WebDriverWait(self.driver, 10)
            upload_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test-id='upload-btn-documents-transcript-of-records']"))
            )

            upload_button.click()

            file_input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-test-id='input-documents-transcript-of-records']")))

            file_input.send_keys("/home/seluser/Upload_Files/6.pdf")
            time.sleep(time_short)

        except Exception as e:
            print("Could not upload Transcript document:", e)
            self._take_screenshot("Transcript document")

    def graDuation(self, Graduation_Certificate):
        try:
            wait = WebDriverWait(self.driver, 10)
            upload_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test-id='upload-btn-documents-graduation-certificates']"))
            )

            upload_button.click()

            file_input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-test-id='input-documents-graduation-certificates']")))

            file_input.send_keys("/home/seluser/Upload_Files/7.pdf")
            time.sleep(time_short)

        except Exception as e:
            print("Could not upload Graduation document:", e)
            self._take_screenshot("Graduation document")



    def LoM(self, Letter_Of_Commitment):
        try:
            wait = WebDriverWait(self.driver, 10)
            upload_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test-id='upload-btn-documents-letter-of-commitment']"))
            )

            upload_button.click()

            file_input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-test-id='input-documents-letter-of-commitment']")))

            file_input.send_keys("/home/seluser/Upload_Files/8.pdf")
            time.sleep(time_short)

        except Exception as e:
            print("Could not upload Letter_Of_Commitment document:", e)
            self._take_screenshot("Letter_Of_Commitment")


    def delete_documents(self):
        try:
            del_Id_pass = self.driver.find_element(*self.bttn_delete_id_passport)
            del_Id_pass.click()
            time.sleep(time_short)

        except:
            print("No file to be deleted(Passport).")

        try:
            del_Curriculum  = self.driver.find_element(*self.bttn_delete_curriculum)
            del_Curriculum.click()
            time.sleep(time_short)

        except:
            print("No file to be deleted(Curriculum).")

        try:
            del_Letter_of_motive  = self.driver.find_element(*self.bttn_delete_letter_of_motive)
            del_Letter_of_motive.click()
            time.sleep(time_short)

        except:
            print("No file to be deleted(LOM).")

        try:
            del_other_files  = self.driver.find_element(*self.bttn_delete_other_documents)
            del_other_files.click()
            time.sleep(time_short)

        except:
            print("No file to be deleted(Other Files).")

        try:
            del_degree = self.driver.find_element(*self.bttn_delete_degree)
            del_degree.click()
            time.sleep(time_short)

        except:
            print("No file to be deleted(Degree).")

        try:
            del_transcript = self.driver.find_element(*self.bttn_delete_transcript)
            del_transcript.click()
            time.sleep(time_short)

        except:
            print("No file to be deleted(Transcript).")

        try:
            del_graduation = self.driver.find_element(*self.bttn_delete_graduation_certificate)
            del_graduation .click()
            time.sleep(time_short)

        except:
            print("No file to be deleted(Graduation).")

        try:
            del_commitment = self.driver.find_element(*self.bttn_delete_letter_of_commitment)
            del_commitment.click()
            time.sleep(time_short)

        except:
            print("No file to be deleted.(Commitment)")

    time.sleep(time_short)


    def continue_documents(self):
        time.sleep(time_long)
        self.driver.find_element(*self.bttn_continue_documents).click()

    def _take_screenshot(self, name_prefix):
        folder = "screenshots"
        os.makedirs(folder, exist_ok=True)
        ts = time.strftime("%Y%m%d-%H%M%S")
        path = f"{folder}/{name_prefix}-{ts}.png"
        self.driver.save_screenshot(path)
        print(f"Screenshot saved: {path}")

    def quit(self):
        # Stop virtual display when done
        if hasattr(self, '_disp') and self._disp:
            self._disp.stop()
