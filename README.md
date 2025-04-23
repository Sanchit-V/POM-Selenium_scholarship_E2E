# 🕸️ Selenium Web Automation with Python

## 🚀 Overview

This project uses **Selenium WebDriver** with **Python** to automate **Scholarship Platform**.

---

## ⚙️ Tech Stack

- Python
- Selenium
- WebDriver
- Pytest 
- HTML reporting (e.g., pytest-html)

---

## 🧪 Setup Instructions

### 1. Clone the Repo

```bash
  git clone https://github.com/your-username/selenium-python-automation.git
  cd selenium-python-automation
```
### 2. Setup the User details file(user_details.py).

```
1. Most of the setup has been preset and most have been covered.😉

2. To add on to it, user needs to configure the following:
    a. Add the URL where the website is running (Front End functioning).
    
    b. Further select the Language, for which the entire website will be tested which
       is either English or Spanish till now.
       
    c. --> Later for the document uploading test cases, you shall create a 'Upload_Files' named folder
           which shall contain the number of .pdf file, in the serial named as 1, 2, 3 till as per requirement.
           eg. 1.pdf, 2.pdf, 3.pdf etc.
       --> For the .jpg files the format shall be a1.jpg, a2.jpg etc.
       --> Make sure the number of pdf and jpg are mentioned in the number_of_pdf and 
           number_of_jpg in the user_details.py before running the main_driver_code.py .
    
    d. And provide the base folder as per required.
     
3. And when the entire user details has been setup, run the user_details.py for double cross check.

4. When everything is fine run the main_driver_code.py.

5. For getting better logs, once the entire process is completed **(Best suited for Pycharm)**:
    a.Go to the 'Run' tab.
    b.Click on the 'More' (three dots).
    c.Click on the Export Test Results. 
    d.Browse the path where you want it to be placed. 
    e.Once it gets placed, right click on the logs file 
      and open it on the browser.
   
    
```
