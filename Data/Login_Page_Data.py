import os
import dotenv
from Model.Login_Page_Model import LoginPageData, LanguageSelectionData, AccessCodeData

url = os.getenv("URL")  #"https://sales-scholarship-application-requests-develop-iymj66chvq-uc.a.run.app/"
raw_selected_language = os.getenv("SELECTED_LANGUAGE")
time_long = int(os.getenv("TIME_LONG"))  # Default to 5 seconds if not set
time_med = int(os.getenv("TIME_MED"))  # Default to 2 seconds if not set
time_short = int(os.getenv("TIME_SHORT"))


def get_language_code(raw_selected_language):
    # Normalize input (lowercase and remove accents for consistency)
    normalized = raw_selected_language.strip().lower()

    language_map = {
        0: {"spanish", "español", "espana", "españa"},
        1: {"english", "inglés", "united states", "estados unidos"},
    }

    for code, variants in language_map.items():
        if normalized in variants:
            return code

    print("Please select a valid language option.")
    return None

class LoginPageMother:
    @staticmethod
    def get() -> LoginPageData:
        return LoginPageData(
            LanguageSelectionData=LanguageSelectionData(selected_language=get_language_code(raw_selected_language)) ,
            AccessCodeData=AccessCodeData(access_code= os.getenv("ACCESS_CODE")),
            #previous_access_code= os.getenv("PREVIOUS_ACCESS_CODE")  
            )     
        

