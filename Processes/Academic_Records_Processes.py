class Academic_Records_Process:
    def __init__(self, academic_records_page):
        self.academic_records_page = academic_records_page

    def run_processes(self, additional_education, education_level_1,education_level_2,education_level_3,University_Institution_1,
                      University_Institution_2,University_Institution_3,degree_1, degree_2, degree_3, starting_Date_1, graduation_Date_1,
                      starting_Date_2, graduation_Date_2,
                      starting_Date_0, graduation_Date_0, online_mode_study,
                      training_type_university, training_type_employment, training_type_second_language, Other_Expertise):
        self.academic_records_page.del_added_edu()
        self.academic_records_page.education_details(additional_education)
        self.academic_records_page.education_Level_1(education_level_1)
        self.academic_records_page.education_Level_2(education_level_2)
        self.academic_records_page.education_Level_3(education_level_3)
        self.academic_records_page.university_institute(University_Institution_1, University_Institution_2, University_Institution_3)
        self.academic_records_page.degree_details(degree_1, degree_2, degree_3)
        self.academic_records_page.degree_date(starting_Date_1, graduation_Date_1, starting_Date_2, graduation_Date_2, starting_Date_0, graduation_Date_0)
        self.academic_records_page.previous_online_mode(online_mode_study, training_type_university, training_type_employment, training_type_second_language)
        self.academic_records_page.other_expertise(Other_Expertise)
        self.academic_records_page.academic_continue()


