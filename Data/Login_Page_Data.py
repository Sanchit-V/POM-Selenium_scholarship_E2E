import os

url = os.getenv("URL")  #"https://sales-scholarship-application-requests-develop-iymj66chvq-uc.a.run.app/"
selected_language = os.getenv("SELECTED_LANGUAGE")
time_long = int(os.getenv("TIME_LONG"))  # Default to 5 seconds if not set
time_med = int(os.getenv("TIME_MED"))  # Default to 2 seconds if not set
time_short = int(os.getenv("TIME_SHORT"))


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
print(selected_language)

access_code = os.getenv("ACCESS_CODE")    #json_data['access_code']
previous_access_code = os.getenv("PREVIOUS_ACCESS_CODE")       #json_data['previous_access_code']

print(access_code)
print(previous_access_code)