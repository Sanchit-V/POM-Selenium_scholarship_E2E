from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from Page_Object.Academic_Records_Page import AcademicRecords

class Academic_Records(AcademicRecords):
    def education_details(self, additional_education):
        if 0<=additional_education<=2:
            for add_education in range(additional_education):
                added_education = self.driver.find_element(*self.add_education)
                added_education.click()
                time.sleep(2)

        else:
            print("Wrong Input")

    def education_Level(self, education_level):#, education_level
        uni_inst_1 = self.driver.find_element(*self.Education_Level_1)
        uni_inst_1.click()
        time.sleep(1)

        if education_level == 1:
            Postgraduate = self.driver.find_element(*self.postgraduate)
            Postgraduate.click()
            time.sleep(1)

        elif education_level == 2:
            University = self.driver.find_element(*self.university)
            University.click()
            time.sleep(1)

        elif education_level == 3:
            Technical = self.driver.find_element(*self.technical)
            Technical.click()
            time.sleep(1)

        elif education_level == 4:
            High_School = self.driver.find_element(*self.high_school)
            High_School.click()
            time.sleep(1)

        else:
            print('Correct option not selected.')
        time.sleep(1)

    def university_institute(self, University_Institution_1):
        uni_name_1 = self.driver.find_element(*self.University_School_1)
        uni_name_1.click()
        time.sleep(1)
        uni_name_1.send_keys(Keys.CONTROL + "a")
        uni_name_1.send_keys(Keys.DELETE)
        time.sleep(1)
        uni_name_1.send_keys(University_Institution_1)
        time.sleep(1)

    def degree_details(self, degree_1):
        degree_name_1 = self.driver.find_element(*self.Degree_1)
        degree_name_1.click()
        time.sleep(1)
        degree_name_1.send_keys(Keys.CONTROL + "a")
        degree_name_1.send_keys(Keys.DELETE)
        time.sleep(1)
        degree_name_1.send_keys(degree_1)
        time.sleep(1)

    def degree_date(self, starting_Date_1, graduation_Date_1):
        starting_date_1 = self.driver.find_element(*self.Starting_Date_1)
        starting_date_1.click()
        time.sleep(1)
        starting_date_1.send_keys(Keys.CONTROL + "a")
        starting_date_1.send_keys(Keys.DELETE)
        time.sleep(1)
        starting_date_1.send_keys(starting_Date_1)
        time.sleep(1)

        graduation_date_1 = self.driver.find_element(*self.Graduation_Date_1)
        graduation_date_1.click()
        time.sleep(1)
        graduation_date_1.send_keys(Keys.CONTROL + "a")
        graduation_date_1.send_keys(Keys.DELETE)
        time.sleep(1)
        graduation_date_1.send_keys(graduation_Date_1)
        time.sleep(1)

    def previous_online_mode(self, online_mode_study, training_type_university, training_type_employment, training_type_second_language,
                             access_code, previous_access_code):

        if online_mode_study == 1:
            yes_online_mode = self.driver.find_element(*self.yes_previous_service)
            yes_online_mode.click()
            time.sleep(2)

            if access_code != previous_access_code:

                if training_type_university == 1:
                    uni_train = self.driver.find_element(*self.university_training)
                    uni_train.click()
                    time.sleep(1)
                else:
                    print('University training not selected.')

                if training_type_employment == 1:
                    emp_train = self.driver.find_element(*self.employment_training)
                    emp_train.click()
                    time.sleep(1)
                else:
                    print('Employment training not selected.')

                if training_type_second_language == 1:
                    sec_lang_train = self.driver.find_element(*self.second_language_training)
                    sec_lang_train.click()
                    time.sleep(1)
                else:
                    print('Second language training not selected.')

        elif online_mode_study == 0:
            no_online_mode = self.driver.find_element(*self.no_previous_service)
            no_online_mode.click()
            time.sleep(2)

        else:
            print('Correct option not selected.')

    def other_expertise(self, Other_Expertise):

        other_exp = self.driver.find_element(*self.other_lang_study_knowledge)
        other_exp.click()
        time.sleep(1)
        other_exp.send_keys(Keys.CONTROL + "a")
        other_exp.send_keys(Keys.DELETE)
        other_exp.send_keys(Other_Expertise)
        time.sleep(2)

    def academic_continue(self):
        academic_continue = self.driver.find_element(*self.academic_continue_button)
        academic_continue.click()
        time.sleep(4)




















