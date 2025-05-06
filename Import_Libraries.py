
import os
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
class Import_libraries:
    
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    import time
    from google.cloud import translate_v2 as translate
    from selenium.webdriver import Remote
    
    
    driver = None

    @staticmethod
    def initialize_driver():
        """
        Initialize a Selenium Remote WebDriver, reading the Grid hub URL
        from the SELENIUM_HUB_URL environment variable (with default).
        """
        # Read hub URL from environment, fallback to 'selenium' for Docker Compose
        hub_url = os.getenv("SELENIUM_HUB_URL", "http://selenium:4444/wd/hub")

        # Configure Chrome options
        options = Options()
        options.add_argument('--headless')       # run without GUI
        options.add_argument('--no-sandbox')     # needed in many Linux CI environments
        options.add_argument('--disable-dev-shm-usage')  # avoid shared memory issues
        options.add_argument('--window-size=1920,1080')

        # Instantiate Remote WebDriver
        Import_libraries.driver = webdriver.Remote(
            command_executor=hub_url,
            options=options
        )
        return Import_libraries.driver




# class Import_libraries:
#     from selenium import webdriver
#     from selenium.webdriver.common.by import By
#     from selenium.webdriver.support.ui import WebDriverWait
#     from selenium.webdriver.support import expected_conditions as EC
#     import time
#     from google.cloud import translate_v2 as translate

#     # Initialize driver as None for explicit control
#     driver = None

#     @staticmethod
#     def initialize_driver():
#         Import_libraries.driver = Import_libraries.webdriver.Chrome()
#         return Import_libraries.driver
