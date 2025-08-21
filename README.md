# 🕸️ Selenium Web Automation with Python

## 🚀 Overview

This project uses **Selenium WebDriver** with **Python** to automate **Scholarship Platform** with **Dockerization**.

---

## ⚙️ Tech Stack

- Python
- Selenium
- WebDriver
- Pytest 
- Git-Bash
- Docker

---

## 🧪 Setup Instructions

### 1. Clone the Repo

```bash
  git clone https://github.com/your-username/selenium-python-automation.git

  branch --> docker-scholarship-finalized
```
### 2. Setup steps.

```
1. Most of the setup has been preset and covered.😉

2. Follow these steps for a better flow of the automation script:
    --> Create a ".env" file in the root directory of this folder.

    --> Copy the contents from the ".env.example" file to the ".env" file.

    --> Select the language for filling the form.

    --> Enter the URL.

    --> Copy the Same access code in both the "Previous Access Code" and "Access Code" Section.

    --> Open the Git-Bash terminal.

    --> Run the commnds:
        chmod +x run_tests_with_novnc.sh
        ./run_tests_with_novnc.sh

    --> Observe the output.
        
    

```
---

## 📃 Important Notes 
1. Once the **.env** file has been created accordingly, try keeping the **Access   Code** and the **Previous Access Code** as same as it will allow an individual to **re-use** the Access Code again and again with fresh inputs each time (depending upon the inputs determined by the program-script **randomly**), **unless or until the form is finally submitted**.

2. In the **Document_page_Functions.py** page the file paths have been hard-coded to maintain the proper functioning of the End-to-End process continuation, without any breakage in the determined flow.

3. In case of any breakge in the script **Kindly read the Exit logs** in the terminal, most of the time the docker machine might cause an internal delay which may cause the selenium script and further test-case suits to fail for no reason, for countering this re-run the script and observe. If the issue persists, then report the issue to be resolved.

4. The entire script covers just the **End-to-End** process, no negative or corner test cases have been included, for better understanding and sanity of the code for other members/reviewers.

5. The code comprises of certain sections of delebrate time-based stops to replicate real-time scenarios for conditions like Uploading documents and entering a long string of data, kindly refer to the respective QA member before making any changes.

6. Most of the Country, State or Cities have been added using a **.json** file due to related language and translation based constraints.

7. In the **Documents Upload Page** once the files are uploaded and the user is redirected to the **Additional Informations Page** please press the **Escape** Key manually, to close the OS interaction window.
