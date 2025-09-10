from pydantic import BaseModel

class LanguageSelectionData(BaseModel):
    selected_language: int

class AccessCodeData(BaseModel):
    access_code: str

class LoginPageData(BaseModel):
    LanguageSelectionData: LanguageSelectionData   
    AccessCodeData: AccessCodeData