import random
import os
from dotenv import load_dotenv, dotenv_values
from Model.Documents_Page_Model import DocumentUploadData

time_long = int(os.getenv("TIME_LONG"))  # Default to 5 seconds if not set
time_med = int(os.getenv("TIME_MED"))  # Default to 2 seconds if not set
time_short = int(os.getenv("TIME_SHORT"))  # Default to 1 second if not set

have_degree_checkbox = random.randint(0, 1)

class DocumentPageMother:
    @staticmethod
    def get() ->  DocumentUploadData:
        return DocumentUploadData(have_degree_checkbox = have_degree_checkbox)
    