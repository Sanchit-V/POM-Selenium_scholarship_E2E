from pydantic import BaseModel

class LoginData(BaseModel):
    selected_language: int   
    access_code: str

class WecomePageData(BaseModel):
    expected_message: str
    user_greeting: str

class PersonalDetailsData(BaseModel):
    document_type: int
    Document_number: str
    Martial_status: int
    Profession: str
    date_of_Birth: str
    Country: str
    State: str
    City: str
    Nationality: str
    Currency: int
    Monthly_Income: str
    Monthly_Expense: str
    Financially_Dependent: int
    Has_Children: int
    Range_0to4: int
    Range_5to12: int
    Range_13to18: int
    Range_18plus: int

class AddressDetailsData(BaseModel):
    additional_emails_to_be_added: int
    previous_access_code: str
    access_code:str
    email_Ids: list
    default_phone: str
    default_whatsapp: str
    total_additionals: int
    number_of_additional_phone: int
    number_of_additional_whatsapp: int
    additional_numbers: list
    country: list
    housing_type: int
    housing_conditions: int
    Country: str
    State: str
    City: str
    home_address: str
    zip_code: str

class AcademicRecordsData(BaseModel):
    additional_education: int
    education_level: list
    online_mode_study: int
    University_Institution: list
    degree: list
    starting_Date: list
    graduation_Date: list
    training_type_university: int
    training_type_employment: int
    training_type_second_language: int
    Other_Expertise: str

class EmploymentInfoData(BaseModel):
    currently_working: int
    Institution_Name: str
    Position: str
    Area: str
    work_category: int
    Activity: str
    seniority_position: int
    Monthly_Salary: str
    Emp_Currency: int
    Emp_Country: str
    Emp_State: str
    Emp_City: str
    Zip_Code: str
    Address: str
    Landline_Phone: str
    Phone_Mobile: str
    Website: str
    Mobile_Nation: str
    Landline_Nation: str

class ReferencePageData(BaseModel):
    additional_references: int
    ref_First_Name: list
    ref_Last_Name: list
    ref_Pos_Occupation: list
    ref_Emails: list
    ref_phone_numbers: list
    ref_landline_numbers: list
    ref_phone_CC: list
    ref_landline_CC: list

class DocumentUploadData(BaseModel):
    have_degree_checkbox: int

class AdditionalInfoData(BaseModel):
    additional_type: int
    Text_Additional_field: str

