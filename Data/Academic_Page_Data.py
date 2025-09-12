import os
from dotenv import load_dotenv, dotenv_values
import random
import string
from datetime import datetime
from datetime import date
from deep_translator import GoogleTranslator
from faker import Faker
from Model.Academic_Records_Page_Model import AcademicRecordsPageModel, EducationDetailsData, OnlineStudyExperienceData, OtherExpertiseData
import json

from dateutil.relativedelta import relativedelta

load_dotenv()
fake = Faker()

with open('Data/user_details.json') as f:
     json_data = json.load(f)

time_long = int(os.getenv("TIME_LONG"))  # Default to 5 seconds if not set
time_med = int(os.getenv("TIME_MED"))  # Default to 2 seconds if not set
time_short = int(os.getenv("TIME_SHORT"))  # Default to 1 second if not set
selected_language = os.getenv("SELECTED_LANGUAGE")

def get_language_code(selected_language):
    # Normalize input (lowercase and remove accents for consistency)
    normalized = selected_language.strip().lower()

    language_map = {
        0: {"spanish", "español", "espana", "españa"},
        1: {"english", "inglés", "united states", "estados unidos"},
    }

    for code, variants in language_map.items():
        if normalized in variants:
            return code

    print("Please select a valid language option.")
    return None

selected_language = get_language_code(selected_language)

additional_education = 2 #random.randint(0, 2)

education_level = [random.randint(1, 4) for _ in range(3)]
University_Institution = [fake.company() + " University" for _ in range(3)]
degree = [random.choice(json_data['Degree']) for _ in range(3)]

starting_Date = []
graduation_Date = []
for _ in range(3):
    fake_date = fake.date_between(start_date='-10y', end_date='-5y')
    start_str = fake_date.strftime("%m%Y")
    grad_str = (datetime.strptime(start_str, "%m%Y") + relativedelta(years=5)).strftime("%m%Y")

    starting_Date.append(start_str)
    graduation_Date.append(grad_str)



online_mode_study = random.randint(0, 1)
training_type_university = random.randint(0, 1)
training_type_employment = random.randint(0, 1)
training_type_second_language =  1 #random.randint(0, 1)

Other_Expertise = random.choice(json_data['Other_Expertise'])


class AcademicRecordsPageMother:
    @staticmethod
    def get() -> AcademicRecordsPageModel:
        return AcademicRecordsPageModel(
            EducationDetailsData=EducationDetailsData(
                additional_education=additional_education,
                education_level=education_level,
                University_Institution=University_Institution,
                degree=degree,
                starting_Date=starting_Date,
                graduation_Date=graduation_Date),

            OnlineStudyExperienceData=OnlineStudyExperienceData(
                online_mode_study=online_mode_study,
                training_type_university=training_type_university,
                training_type_employment=training_type_employment,
                training_type_second_language=training_type_second_language),

            OtherExpertiseData=OtherExpertiseData(
                Other_Expertise=Other_Expertise
            )
        )





