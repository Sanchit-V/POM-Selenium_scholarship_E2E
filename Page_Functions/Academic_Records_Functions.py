import os

from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

import user_details

time_short = user_details.time_short
time_med = user_details.time_med
time_long = user_details.time_long

from Page_Object.Academic_Records_Page import AcademicRecords

class Academic_Records(AcademicRecords):
    def education_details(self, additional_education):
        WebDriverWait(self.driver,12).until(EC.presence_of_element_located(self.add_education))
        try:
            if 0 < additional_education <= 2:
                for add_education in range(additional_education):
                    added_education = self.driver.find_element(*self.add_education)
                    added_education.click()
                    time.sleep(time_med)

            elif additional_education == 0:
                print('0 as option is selected.')

            else:
                print("Wrong Input")

        except:

            print('No additional needed to be added.')


    def del_added_edu(self):
        try:
            del_Edu_2 = self.driver.find_element(*self.delete_edu_2)
            del_Edu_2.click()
            time.sleep(time_med)

        except:

            print('Edu 2 box not found')

        try:
            del_Edu_3 = self.driver.find_element(*self.delete_edu_2)
            del_Edu_3.click()
            time.sleep(time_med)

        except:

            print('Edu 3 box not found')


    def education_Level_1(self, education_level_1):#, education_level
        uni_inst_1 = self.driver.find_element(*self.Education_Level_1)
        uni_inst_1.click()
        time.sleep(time_short)

        if education_level_1 == 1:
            Postgraduate = self.driver.find_element(*self.postgraduate_1)
            Postgraduate.click()
            time.sleep(time_short)

        elif education_level_1 == 2:
            University = self.driver.find_element(*self.university_1)
            University.click()
            time.sleep(time_short)

        elif education_level_1 == 3:
            Technical = self.driver.find_element(*self.technical_1)
            Technical.click()
            time.sleep(time_short)

        elif education_level_1 == 4:
            High_School = self.driver.find_element(*self.high_school_1)
            High_School.click()
            time.sleep(time_short)

        else:
            print('Correct option not selected.')
        time.sleep(time_short)

    def education_Level_2(self, education_level_2):
        try:
            uni_inst_2 = self.driver.find_element(*self.Education_Level_2)
            uni_inst_2.click()
            time.sleep(time_short)

            if education_level_2 == 1:
                Postgraduate = self.driver.find_element(*self.postgraduate_2)
                Postgraduate.click()
                time.sleep(time_short)

            elif education_level_2 == 2:
                University = self.driver.find_element(*self.university_2)
                University.click()
                time.sleep(time_short)

            elif education_level_2 == 3:
                Technical = self.driver.find_element(*self.technical_2)
                Technical.click()
                time.sleep(time_short)

            elif education_level_2 == 4:
                High_School = self.driver.find_element(*self.high_school_2)
                High_School.click()
                time.sleep(time_short)

            else:
                print('Correct option not selected.')
            time.sleep(time_short)

        except:
            print('Education 2 not selected.')

    def education_Level_3(self, education_level_3):
        try:
            uni_inst_3 = self.driver.find_element(*self.Education_Level_3)
            uni_inst_3.click()
            time.sleep(time_short)

            if education_level_3 == 1:
                Postgraduate = self.driver.find_element(*self.postgraduate_3)
                Postgraduate.click()
                time.sleep(time_short)

            elif education_level_3 == 2:
                University = self.driver.find_element(*self.university_3)
                University.click()
                time.sleep(time_short)

            elif education_level_3 == 3:
                Technical = self.driver.find_element(*self.technical_3)
                Technical.click()
                time.sleep(time_short)

            elif education_level_3 == 4:
                High_School = self.driver.find_element(*self.high_school_3)
                High_School.click()
                time.sleep(time_short)

            else:
                print('Correct option not selected.')
            time.sleep(time_short)

        except:
            print('Education 3 not selected.')

    def university_institute(self, University_Institution_1, University_Institution_2, University_Institution_3):
        uni_name_1 = self.driver.find_element(*self.University_School_1)
        uni_name_1.click()
        time.sleep(time_short)
        uni_name_1.send_keys(Keys.CONTROL + "a")
        uni_name_1.send_keys(Keys.DELETE)
        time.sleep(time_short)
        uni_name_1.send_keys(University_Institution_1)
        time.sleep(time_med)

        try:
            uni_name_2 = self.driver.find_element(*self.University_School_2)
            uni_name_2.click()
            time.sleep(time_short)
            uni_name_2.send_keys(Keys.CONTROL + "a")
            uni_name_2.send_keys(Keys.DELETE)
            time.sleep(time_short)
            uni_name_2.send_keys(University_Institution_2)
            time.sleep(time_med)

        except:
            print('Other eduction level-2 not selected.')

        try:
            uni_name_3 = self.driver.find_element(*self.University_School_3)
            uni_name_3.click()
            time.sleep(time_short)
            uni_name_3.send_keys(Keys.CONTROL + "a")
            uni_name_3.send_keys(Keys.DELETE)
            time.sleep(time_short)
            uni_name_3.send_keys(University_Institution_3)
            time.sleep(time_med)

        except:
            print('Other eduction level-3 not selected.')


    def degree_details(self, degree_1, degree_2, degree_3):
        degree_name_1 = self.driver.find_element(*self.Degree_1)
        degree_name_1.click()
        time.sleep(time_short)
        degree_name_1.send_keys(Keys.CONTROL + "a")
        degree_name_1.send_keys(Keys.DELETE)
        time.sleep(time_short)
        degree_name_1.send_keys(degree_1)
        time.sleep(time_short)

        try:
            degree_name_2 = self.driver.find_element(*self.Degree_2)
            degree_name_2.click()
            time.sleep(time_short)
            degree_name_2.send_keys(Keys.CONTROL + "a")
            degree_name_2.send_keys(Keys.DELETE)
            time.sleep(time_short)
            degree_name_2.send_keys(degree_2)
            time.sleep(time_short)

        except:
            print('Other eduction level-2 not selected.')

        try:
            degree_name_3 = self.driver.find_element(*self.Degree_3)
            degree_name_3.click()
            time.sleep(time_short)
            degree_name_3.send_keys(Keys.CONTROL + "a")
            degree_name_3.send_keys(Keys.DELETE)
            time.sleep(time_short)
            degree_name_3.send_keys(degree_3)
            time.sleep(time_short)

        except:
            print('Other eduction level-3 not selected.')


    def degree_date(self, starting_Date_0, graduation_Date_0, starting_Date_1, graduation_Date_1, starting_Date_2, graduation_Date_2):
        starting_date_1 = self.driver.find_element(*self.Starting_Date__1)
        starting_date_1.click()
        time.sleep(time_short)
        # starting_date_1.send_keys(Keys.CONTROL + "a")
        # starting_date_1.send_keys(Keys.DELETE)
        # time.sleep(1)
        starting_date_1.send_keys(starting_Date_0)
        time.sleep(time_short)

        graduation_date_1 = self.driver.find_element(*self.Graduation_Date__1)
        graduation_date_1.click()
        time.sleep(time_short)
        # graduation_date_1.send_keys(Keys.CONTROL + "a")
        # graduation_date_1.send_keys(Keys.DELETE)
        # time.sleep(1)
        graduation_date_1.send_keys(graduation_Date_0)
        time.sleep(time_short)

        try:
            starting_date_2 = self.driver.find_element(*self.Starting_Date__2)
            starting_date_2.click()
            time.sleep(time_short)
            # starting_date_2.send_keys(Keys.CONTROL + "a")
            # starting_date_2.send_keys(Keys.DELETE)
            # time.sleep(1)
            starting_date_2.send_keys(starting_Date_1)
            time.sleep(time_short)

            graduation_date_2 = self.driver.find_element(*self.Graduation_Date__2)
            graduation_date_2.click()
            time.sleep(time_short)
            # graduation_date_2.send_keys(Keys.CONTROL + "a")
            # graduation_date_2.send_keys(Keys.DELETE)
            # time.sleep(1)
            graduation_date_2.send_keys(graduation_Date_1)
            time.sleep(time_short)

        except:
            print('Other eduction level-2 not selected.')

        try:
            starting_date_3 = self.driver.find_element(*self.Starting_Date__3)
            starting_date_3.click()
            time.sleep(time_short)
            # starting_date_3.send_keys(Keys.CONTROL + "a")
            # starting_date_3.send_keys(Keys.DELETE)
            # time.sleep(1)
            starting_date_3.send_keys(starting_Date_2)
            time.sleep(time_short)

            graduation_date_3 = self.driver.find_element(*self.Graduation_Date__3)
            graduation_date_3.click()
            time.sleep(time_short)
            # graduation_date_3.send_keys(Keys.CONTROL + "a")
            # graduation_date_3.send_keys(Keys.DELETE)
            # time.sleep(1)
            graduation_date_3.send_keys(graduation_Date_2)
            time.sleep(time_short)

        except:
            print('Other eduction level-2 not selected.')






    def previous_online_mode(self, online_mode_study, training_type_university, training_type_employment, training_type_second_language):

        if online_mode_study == 1:
            yes_online_mode = self.driver.find_element(*self.yes_previous_service)
            yes_online_mode.click()
            time.sleep(time_med)

            try:
                unchecked_uni = self.driver.find_element(*self.data_test_emp_box_uni)
                if unchecked_uni:
                    try:
                        if training_type_university == 1:
                            uni_train = self.driver.find_element(*self.university_training)
                            uni_train.click()
                            time.sleep(time_short)

                        else:
                            print('University training not selected.')

                    except:
                        print('*****Uni-Error already selected*****')
            except:
                print('Web element not found, unchecked_uni')

            try:
                unchecked_emp = self.driver.find_element(*self.data_test_emp_box_emp)
                if unchecked_emp:
                    try:
                        if training_type_employment == 1:
                            emp_train = self.driver.find_element(*self.employment_training)
                            emp_train.click()
                            time.sleep(time_short)

                        else:
                            print('Employment training not selected.')

                    except:
                        print('*****Emp-Error already selected*****')
            except:
                print('Web element not found, unchecked_emp')

            try:
                unchecked_sec_lang = self.driver.find_element(*self.data_test_emp_sec_lang)
                if unchecked_sec_lang:
                    try:
                        if training_type_second_language == 1:
                            sec_lang_train = self.driver.find_element(*self.second_language_training)
                            sec_lang_train.click()
                            time.sleep(time_short)

                        else:
                            print('Second language training not selected.')

                    except:
                        print('*****Sec-Lang already selected*****')

            except:
                print("Web element not found, unchecked_sec_lang")

            try:
                checked_uni = self.driver.find_element(*self.data_test_check_uni)
                if checked_uni:
                    try:
                        if training_type_university == 0:
                            uni_train = self.driver.find_element(*self.university_training)
                            uni_train.click()
                            time.sleep(time_short)

                        else:
                            print('University training still selected.')

                    except:
                        print('*****Uni-Error already not-selected*****')
            except:
                print("Web element not found, checked_uni")

            try:
                checked_emp = self.driver.find_element(*self.data_test_check_emp)
                if checked_emp:
                    try:
                        if training_type_employment == 0:
                            emp_train = self.driver.find_element(*self.employment_training)
                            emp_train.click()
                            time.sleep(time_short)

                        else:
                            print('Employment training still selected.')

                    except:
                        print('*****Emp-Error already not-selected*****')
            except:
                print("Web element not found, checked_emp")

            try:
                checked_sec_lang = self.driver.find_element(*self.data_test_check_sec_lang)
                if checked_sec_lang:
                    try:
                        if training_type_second_language == 0:
                            sec_lang_train = self.driver.find_element(*self.second_language_training)
                            sec_lang_train.click()
                            time.sleep(time_short)

                        else:
                            print('Second language training still selected.')

                    except:
                        print('*****Sec-Lang already not-selected*****')

            except:
                print("Web element not found, checked_sec_lang")

        elif online_mode_study == 0:
            no_online_mode = self.driver.find_element(*self.no_previous_service)
            no_online_mode.click()
            time.sleep(time_med)

        else:
            print('Correct option not selected.')

    def other_expertise(self, Other_Expertise):

        other_exp = self.driver.find_element(*self.other_lang_study_knowledge)
        other_exp.click()
        time.sleep(time_short)
        other_exp.send_keys(Keys.CONTROL + "a")
        other_exp.send_keys(Keys.DELETE)
        other_exp.send_keys(Other_Expertise)
        time.sleep(time_med)

    def academic_continue(self):
        academic_continue = self.driver.find_element(*self.academic_continue_button)
        academic_continue.click()
        time.sleep(time_med)




















