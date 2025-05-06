import os
import time
from selenium.webdriver import Keys
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
    def __init__(self, driver):
        super().__init__(driver)
        # Start virtual X display for PyAutoGUI
        self._disp = Display(visible=False, size=(1920, 1080), backend="xvfb")
        self._disp.start()
        os.environ['DISPLAY'] = self._disp.new_display_var

    def _get_pyautogui(self):
        # Import and attach PyAutoGUI to the virtual display
        import pyautogui
        pyautogui._pyautogui_x11._display = Xlib.display.Display(os.environ['DISPLAY'])
        return pyautogui

    def ID_Passport(self, Passport_File):
        WebDriverWait(self.driver,12).until(EC.presence_of_element_located(self.bttn_id_passport))
        try:
            self.driver.find_element(*self.bttn_id_passport).click()
            time.sleep(time_med)
            pag = self._get_pyautogui()
            pag.write(Passport_File)
            time.sleep(time_short)
            pag.press('enter')
            time.sleep(time_short)
        except Exception:
            print("Not able to click the upload option.")

    def Curriculum(self, Curriculum_File):
        try:
            self.driver.find_element(*self.bttn_curriculum).click()
            time.sleep(time_med)
            pag = self._get_pyautogui()
            pag.write(Curriculum_File)
            time.sleep(time_short)
            pag.press('enter')
            time.sleep(time_short)
        except Exception:
            print("Not able to click the upload option.")

    def Letter_of_moTive(self, Letter_Of_Motive):
        try:
            self.driver.find_element(*self.bttn_letter_of_motive).click()
            time.sleep(time_med)
            pag = self._get_pyautogui()
            pag.write(Letter_Of_Motive)
            time.sleep(time_short)
            pag.press('enter')
            time.sleep(time_short)
        except Exception:
            print("Not able to click the upload option.")

    def other_Document(self, Other_Document):
        try:
            self.driver.find_element(*self.bttn_other_document).click()
            time.sleep(time_med)
            pag = self._get_pyautogui()
            pag.write(Other_Document)
            time.sleep(time_short)
            pag.press('enter')
            time.sleep(time_short)
        except Exception:
            print("Not able to click the upload option.")

    def Have_degree_checkbox(self, have_degree_checkbox):
        # ... (unchanged) ...
        pass  # retain existing logic here

    def deGree(self, Degree):
        try:
            self.driver.find_element(*self.bttn_degree).click()
            time.sleep(time_med)
            pag = self._get_pyautogui()
            pag.write(Degree)
            time.sleep(time_short)
            pag.press('enter')
            time.sleep(time_short)
        except Exception:
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
