from pydantic import BaseModel

class EducationDetailsData(BaseModel):
    additional_education: int
    education_level: list
    University_Institution: list
    degree: list
    starting_Date: list
    graduation_Date: list

class OnlineStudyExperienceData(BaseModel):
    online_mode_study: int
    training_type_university: int
    training_type_employment: int
    training_type_second_language: int

class OtherExpertiseData(BaseModel):
    Other_Expertise: str

class AcademicRecordsPageModel(BaseModel):
    EducationDetailsData: EducationDetailsData
    OnlineStudyExperienceData: OnlineStudyExperienceData
    OtherExpertiseData: OtherExpertiseData