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
        # ... (unchanged) ...
        pass  # retain existing logic here

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
            self.driver.find_element(*self.transcript).click()
            time.sleep(time_med)
            pag = self._get_pyautogui()
            pag.write(Transcript)
            time.sleep(time_short)
            pag.press('enter')
            time.sleep(time_short)
        except Exception:
            self._take_screenshot("Transcript document")

    def graDuation(self, Graduation_Certificate):
        try:
            self.driver.find_element(*self.graduate_certificate).click()
            time.sleep(time_med)
            pag = self._get_pyautogui()
            pag.write(Graduation_Certificate)
            time.sleep(time_short)
            pag.press('enter')
            time.sleep(time_short)
        except Exception:
            self._take_screenshot("Graduation document")

    def LoM(self, Letter_Of_Commitment):
        try:
            self.driver.find_element(*self.letter_of_commitment).click()
            time.sleep(time_med)
            pag = self._get_pyautogui()
            pag.write(Letter_Of_Commitment)
            time.sleep(time_short)
            pag.press('enter')
            time.sleep(time_short)
        except Exception:
            self._take_screenshot("LOM document")

    def delete_documents(self):
        # ... (unchanged) ...
        pass

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
