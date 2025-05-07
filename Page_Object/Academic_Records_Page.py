from Import_Libraries import Import_libraries
By=Import_libraries.By

class AcademicRecords:
    def __init__(self, driver):
        self.driver = Import_libraries._driver

        self.add_education = By.CSS_SELECTOR, '[data-test-id="button-add-education-details-text"]'

        self.Education_Level_1 = By.CSS_SELECTOR, '[data-test-id="select-display-academic-education-level-1"]'
        self.postgraduate_1 = By.CSS_SELECTOR, '[data-test-id="li-academic-education-level-1-Postgraduate"]'
        self.university_1 = By.CSS_SELECTOR, '[data-test-id="li-academic-education-level-1-University"]'
        self.technical_1 = By.CSS_SELECTOR, '[data-test-id="li-academic-education-level-1-Technical"]'
        self.high_school_1 = By.CSS_SELECTOR, '[data-test-id="li-academic-education-level-1-High School"]'
        self.University_School_1 = By.CSS_SELECTOR, '[data-test-id="input-academic-education-institution-1"]'
        self.Degree_1 = By.CSS_SELECTOR, '[data-test-id="input-academic-education-degree-1"]'
        self.Starting_Date__1 = By.CSS_SELECTOR, '[data-test-id="date-picker-input-academic-education-start-date-1"]'
        self.Graduation_Date__1 = By.CSS_SELECTOR, '[data-test-id="date-picker-input-academic-education-graduation-date-1"]'

        self.Education_Level_2 = By.CSS_SELECTOR, '[data-test-id="select-display-academic-education-level-2"]'
        self.postgraduate_2 = By.CSS_SELECTOR, '[data-test-id="li-academic-education-level-2-Postgraduate"]'
        self.university_2 = By.CSS_SELECTOR, '[data-test-id="li-academic-education-level-2-University"]'
        self.technical_2 = By.CSS_SELECTOR, '[data-test-id="li-academic-education-level-2-Technical"]'
        self.high_school_2 = By.CSS_SELECTOR, '[data-test-id="li-academic-education-level-2-High School"]'
        self.University_School_2 = By.CSS_SELECTOR, '[data-test-id="input-academic-education-institution-2"]'
        self.Degree_2 = By.CSS_SELECTOR, '[data-test-id="input-academic-education-degree-2"]'
        self.Starting_Date__2 = By.CSS_SELECTOR, '[data-test-id="date-picker-input-academic-education-start-date-2"]'
        self.Graduation_Date__2 = By.CSS_SELECTOR, '[data-test-id="date-picker-input-academic-education-graduation-date-2"]'

        self.Education_Level_3 = By.CSS_SELECTOR, '[data-test-id="select-display-academic-education-level-3"]'
        self.postgraduate_3 = By.CSS_SELECTOR, '[data-test-id="li-academic-education-level-3-Postgraduate"]'
        self.university_3 = By.CSS_SELECTOR, '[data-test-id="li-academic-education-level-3-University"]'
        self.technical_3 = By.CSS_SELECTOR, '[data-test-id="li-academic-education-level-3-Technical"]'
        self.high_school_3 = By.CSS_SELECTOR, '[data-test-id="li-academic-education-level-3-High School"]'
        self.University_School_3 = By.CSS_SELECTOR, '[data-test-id="input-academic-education-institution-3"]'
        self.Degree_3 = By.CSS_SELECTOR, '[data-test-id="input-academic-education-degree-3"]'
        self.Starting_Date__3 = By.CSS_SELECTOR, '[data-test-id="date-picker-input-academic-education-start-date-3"]'
        self.Graduation_Date__3 = By.CSS_SELECTOR, '[data-test-id="date-picker-input-academic-education-graduation-date-3"]'

        self.delete_edu_2 = By.CSS_SELECTOR,'[data-test-id="button-delete-education-details-2"]'
        self.delete_edu_3 = By.CSS_SELECTOR,'[data-test-id="button-delete-education-details-3"]'

        self.no_previous_service = By.CSS_SELECTOR, '[data-test-id="radio-input-academic-online-study-experience-no"]'

        self.yes_previous_service = By.CSS_SELECTOR, '[data-test-id="radio-input-academic-online-study-experience-yes"]'

        self.university_training = By.XPATH, "//input[@value='UNIVERSITY_TRAINING']"
        self.employment_training = By.XPATH, "//input[@value='EMPLOYMENT_TRAINING']"
        self.second_language_training = By.XPATH, "//input[@value='TRAINING_IN_SECOND_LANGUAGE']"

        self.data_test_check_uni = By.CSS_SELECTOR, '[data-test-id="UNIVERSITY_TRAINING_checked-icon"]'
        self.data_test_check_emp = By.CSS_SELECTOR, '[data-test-id="EMPLOYMENT_TRAINING_checked-icon"]'
        self.data_test_check_sec_lang = By.CSS_SELECTOR, '[data-test-id="TRAINING_IN_SECOND_LANGUAGE_checked-icon"]'

        self.data_test_emp_box_uni = By.CSS_SELECTOR, '[data-test-id="UNIVERSITY_TRAINING_unchecked-icon"]'
        self.data_test_emp_box_emp = By.CSS_SELECTOR, '[data-test-id="EMPLOYMENT_TRAINING_unchecked-icon"]'
        self.data_test_emp_sec_lang = By.CSS_SELECTOR, '[data-test-id="TRAINING_IN_SECOND_LANGUAGE_unchecked-icon"]'




        self.other_lang_study_knowledge = By.CSS_SELECTOR,'[data-test-id="input-academic-other-expertise"]'

        self.academic_continue_button = By.CSS_SELECTOR, '[data-test-id="btn-continue-academic"]'
        self.academic_back_button = By.CSS_SELECTOR, '[data-test-id="btn-back-academic"]'
        self.academic_cancel_button = By.CSS_SELECTOR, '[data-test-id="btn-cancel-academic"]'




