class Academic_Records_Process:
    def __init__(self, academic_records_page):
        self.academic_records_page = academic_records_page

    def run_processes(self, additional_education, education_level, University_Institution_1, degree_1, starting_Date_1, graduation_Date_1, online_mode_study,
                      training_type_university, training_type_employment, training_type_second_language, Other_Expertise, access_code, previous_access_code):
        self.academic_records_page.education_details(additional_education)
        self.academic_records_page.education_Level(education_level)
        self.academic_records_page.university_institute(University_Institution_1)
        self.academic_records_page.degree_details(degree_1)
        self.academic_records_page.degree_date(starting_Date_1, graduation_Date_1)
        self.academic_records_page.previous_online_mode(online_mode_study, training_type_university, training_type_employment, training_type_second_language, access_code, previous_access_code)
        self.academic_records_page.other_expertise(Other_Expertise)
        self.academic_records_page.academic_continue()


