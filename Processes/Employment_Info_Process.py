class Employement_Info_Process:
    def __init__(self, employment_info_page):
        self.employment_info_page = employment_info_page

    def run_processes(self, currently_working,Institution_Name, Position, Area,
                      work_category, Activity, seniority_position, Monthly_Salary, Emp_Country, Emp_State, Emp_City,Zip_Code,
                      Address, Landline_Phone, Phone_Mobile,Website, Landline_Nation, Mobile_Nation):

        self.employment_info_page.Currently_working(currently_working)

        self.employment_info_page.position_info(Institution_Name, Position, Area,
                      work_category, Activity, seniority_position, Monthly_Salary)

        self.employment_info_page.employment_country(Emp_Country, Emp_State, Emp_City, Zip_Code, Address)

        self.employment_info_page.employment_contact(Landline_Phone, Phone_Mobile,  Website)

        self.employment_info_page.nations(Landline_Nation, Mobile_Nation)

        self.employment_info_page.emp_info_continue()
