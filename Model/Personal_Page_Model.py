from pydantic import BaseModel

class BasicData(BaseModel):
    document_type: int
    Document_number: str
    Martial_status: int
    Profession: str

class BirthData(BaseModel):
    Date_Of_Birth: str
    Country: str
    State: str
    City: str
    Nationality: str

class FinancialData(BaseModel):
    Currency: int
    Monthly_Income: str
    Monthly_Expense: str
    Financially_Dependent: int

class FamilyDetailsData(BaseModel):

    Has_Children: int
    Range_0to4: int
    Range_5to12: int
    Range_13to18: int
    Range_18plus: int

class PersonalDetailsPageModel(BaseModel):
    BasicData: BasicData
    BirthData: BirthData
    FinancialData: FinancialData
    FamilyDetailsData: FamilyDetailsData

