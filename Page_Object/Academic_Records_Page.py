from Import_Libraries import Import_libraries
By=Import_libraries.By

class AcademicRecords:
    def __init__(self, driver):
        self.driver = Import_libraries.driver

        self.add_education = By.CSS_SELECTOR, '[data-test-id="button-add-education-details-text"]'

        self.Education_Level_1 = By.CSS_SELECTOR, '[data-test-id="select-display-academic-education-level"]'
        self.postgraduate = By.CSS_SELECTOR, '[data-test-id="li-academic-education-level-Postgraduate"]'
        self.university = By.CSS_SELECTOR, '[data-test-id="li-academic-education-level-University"]'
        self.technical = By.CSS_SELECTOR, '[data-test-id="li-academic-education-level-Technical"]'
        self.high_school = By.CSS_SELECTOR, '[data-test-id="li-academic-education-level-High School"]'
        self.University_School_1 = By.CSS_SELECTOR, '[data-test-id="input-academic-education-institution"]'
        self.Degree_1 = By.CSS_SELECTOR, '[data-test-id="input-academic-education-degree"]'
        self.Starting_Date_1 = By.CSS_SELECTOR, '[data-test-id="date-picker-input-academic-education-start-date"]'
        self.Graduation_Date_1 = By.CSS_SELECTOR, '[data-test-id="date-picker-input-academic-education-graduation-date"]'

        self.no_previous_service = By.CSS_SELECTOR, '[data-test-id="radio-input-academic-online-study-experience-No"]'

        self.yes_previous_service = By.CSS_SELECTOR, '[data-test-id="radio-input-academic-online-study-experience-Yes"]'

        self.university_training = By.XPATH, "//input[@value='UNIVERSITY_TRAINING']"
        self.employment_training = By.XPATH, "//input[@value='EMPLOYMENT_TRAINING']"
        self.second_language_training = By.XPATH, "//input[@value='TRAINING_IN_SECOND_LANGUAGE']"

        # self.data_test_checkbox_uni = By.CSS_SELECTOR, '[data-test-id="uni_CheckBoxIcon"]'
        # self.data_test_checkbox_emp = By.CSS_SELECTOR, '[data-test-id="emp_CheckBoxIcon"]'
        # self.data_test_checkbox_sec_lang = By.CSS_SELECTOR, '[data-test-id="sec_lang_CheckBoxIcon"]'
        #
        # self.data_test_emp_box_uni = By.CSS_SELECTOR, '[data-test-id="uni_CheckBoxOutlineBlankIcon"]'
        # self.data_test_emp_box_emp = By.CSS_SELECTOR, '[data-test-id="emp_CheckBoxOutlineBlankIcon"]'
        # self.data_test_emp_sec_lang = By.CSS_SELECTOR, '[@data-test-id="sec_lang_CheckBoxOutlineBlankIcon"]'




        self.other_lang_study_knowledge = By.CSS_SELECTOR,'[data-test-id="input-academic-other-expertise"]'

        self.academic_continue_button = By.CSS_SELECTOR, '[data-test-id="btn-continue-academic"]'
        self.academic_back_button = By.CSS_SELECTOR, '[data-test-id="btn-back-academic"]'
        self.academic_cancel_button = By.CSS_SELECTOR, '[data-test-id="btn-cancel-academic"]'




