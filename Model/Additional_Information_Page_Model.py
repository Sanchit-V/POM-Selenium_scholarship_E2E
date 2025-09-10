from pydantic import BaseModel

class AdditionalTypeData(BaseModel):
    additional_type: int

class TextFieldData(BaseModel):
    Text_Additional_field: str

class AdditionalInformationDetailsModel(BaseModel):
    AdditionalTypeData:AdditionalTypeData
    TextFieldData:TextFieldData



