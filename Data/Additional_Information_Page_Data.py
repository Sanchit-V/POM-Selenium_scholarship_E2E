import random
from faker import Faker
import os
from dotenv import load_dotenv, dotenv_values
from Model.Additional_Information_Page_Model import AdditionalInformationDetailsModel, AdditionalTypeData

time_long = int(os.getenv("TIME_LONG"))  # Default to 5 seconds if not set
time_med = int(os.getenv("TIME_MED"))  # Default to 2 seconds if not set
time_short = int(os.getenv("TIME_SHORT"))  # Default to 1 second if not set
fake = Faker()
additional_type = 4 #random.randint(1, 8)
description = ' '.join(fake.words(nb=30))
Text_Additional_field=description

class AdditionalInformationMother:
    @staticmethod
    def get()-> AdditionalInformationDetailsModel:
        return AdditionalInformationDetailsModel(
            AdditionalTypeData = AdditionalTypeData(additional_type = additional_type,Text_Additional_field = Text_Additional_field))
