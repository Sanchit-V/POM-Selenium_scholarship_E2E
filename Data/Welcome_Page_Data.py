import os
from Model.Welcome_Page_Model import WelcomePageData, UserGreetingData, ExpectedMessageData
from dotenv import load_dotenv
time_long = int(os.getenv("TIME_LONG"))  # Default to 5 seconds if not set
time_med = int(os.getenv("TIME_MED"))  # Default to 2 seconds if not set
time_short = int(os.getenv("TIME_SHORT"))

raw_selected_language = os.getenv("SELECTED_LANGUAGE")

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

selected_language=get_language_code(raw_selected_language)

if raw_selected_language == 1:
    user_greeting = "Welcome to the online scholarship application form"
    expected_message = "Login successful"

else:
    user_greeting = "Bienvenido al formulario de solicitud de beca online"
    expected_message = "Inicio de sesión correcto"


class WelcomePageMother:
    @staticmethod
    def get() -> WelcomePageData:
        return WelcomePageData(
            UserGreetingData=UserGreetingData(user_greeting=user_greeting),
            ExpectedMessageData=ExpectedMessageData(expected_message=expected_message)
        )
