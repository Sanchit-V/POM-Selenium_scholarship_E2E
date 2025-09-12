from pydantic import BaseModel

class AdditionalTypeData(BaseModel):
    additional_type: int
    Text_Additional_field: str
class AdditionalInformationDetailsModel(BaseModel):
    AdditionalTypeData:AdditionalTypeData




