from Data.Academic_Page_Data import AcademicRecordsPageMother
class AcademicRecordsProcess:
    def __init__(self, academic_records_page):
        self.academic_records_page = academic_records_page

    def run_processes(self):
        data = AcademicRecordsPageMother.get()
        self.academic_records_page.del_added_edu()
        self.academic_records_page.education_details(data.EducationDetailsData)
        self.academic_records_page.education_Level_1(data.EducationDetailsData)
        self.academic_records_page.education_Level_2(data.EducationDetailsData)
        self.academic_records_page.education_Level_3(data.EducationDetailsData)
        self.academic_records_page.university_institute(data.EducationDetailsData)
        self.academic_records_page.degree_details(data.EducationDetailsData)
        self.academic_records_page.degree_date(data.EducationDetailsData)
        self.academic_records_page.previous_online_mode(data.OnlineStudyExperienceData)
        self.academic_records_page.other_expertise(data.OtherExpertiseData)
        self.academic_records_page.academic_continue()


