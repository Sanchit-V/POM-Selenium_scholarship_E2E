from Model.Academic_Records_Page_Model import AcademicRecordsPageModel
class AcademicRecordsProcess:
    def __init__(self, academic_records_page):
        self.academic_records_page = academic_records_page

    def run_processes(self, data:AcademicRecordsPageModel):
        self.academic_records_page.del_added_edu()
        self.academic_records_page.education_details(data)
        self.academic_records_page.education_Level_1(data)
        self.academic_records_page.education_Level_2(data)
        self.academic_records_page.education_Level_3(data)
        self.academic_records_page.university_institute(data)
        self.academic_records_page.degree_details(data)
        self.academic_records_page.degree_date(data)
        self.academic_records_page.previous_online_mode(data)
        self.academic_records_page.other_expertise(data)
        self.academic_records_page.academic_continue()


