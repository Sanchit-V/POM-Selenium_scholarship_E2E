from pydantic import BaseModel

class ContactDetailsData(BaseModel):
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

class ResidenceDetailsData(BaseModel):
    housing_type: int
    housing_conditions: int
    Country: str
    State: str
    City: str
    home_address: str
    zip_code: str

class AddressPageDetailsModel(BaseModel):
    ContactDetailsData: ContactDetailsData
    ResidenceDetailsData: ResidenceDetailsData
