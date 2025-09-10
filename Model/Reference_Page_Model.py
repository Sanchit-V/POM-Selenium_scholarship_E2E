from pydantic import BaseModel

class PersonalOrEmploymentReferencesPage(BaseModel):
    additional_references: int
    ref_First_Name: list
    ref_Last_Name: list
    ref_Pos_Occupation: list
    ref_Emails: list
    ref_phone_numbers: list
    ref_landline_numbers: list
    ref_phone_CC: list
    ref_landline_CC: list

    