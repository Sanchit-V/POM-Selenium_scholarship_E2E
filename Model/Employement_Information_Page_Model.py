from pydantic import BaseModel

class EmploymentStatusData(BaseModel):
    currently_working: int

class PositionInformationData(BaseModel):
    Institution_Name: str
    Position: str
    Area: str
    work_category: int
    Activity: str
    seniority_position: int
    Monthly_Salary: str
    Emp_Currency: int

class EmploymentAddressData(BaseModel):
    Emp_Country: str
    Emp_State: str
    Emp_City: str
    Zip_Code: str
    Address: str

class EmploymentContactData(BaseModel):
    Landline_Phone: str
    Phone_Mobile: str
    Website: str
    Mobile_Nation: str
    Landline_Nation: str

class EmploymentInformationPageData(BaseModel):
    EmploymentStatusData:EmploymentStatusData
    PositionInformationData:PositionInformationData
    EmploymentAddressData:EmploymentAddressData
    EmploymentContactData:EmploymentContactData