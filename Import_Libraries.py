class Import_libraries:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    import time

    # Initialize driver as None for explicit control
    driver = None

    @staticmethod
    def initialize_driver():
        Import_libraries.driver = Import_libraries.webdriver.Chrome()
        return Import_libraries.driver
