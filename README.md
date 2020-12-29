# FPT-Subject-Register-Bot
A Messenger automation bot that will check the subject availability status on FAP website (FPT University) using Selenium.  
  
To run this, you will need a facebook account that will represent your chatbot (clone account) If you hadn't have any, create one! Or you can just use your current account (not recommended because you can't recieve Messenger notifications)
  
## 1. Clone the project
> `git clone https://github.com/thieulong/FPT-Subject-Register-Bot.git`  

## 2. Install required Python packages
> `cd FPT-Subject-Register-Bot`  
> `python -m pip install requirement.txt`  

## 3. Download chromedriver.exe (Not necessary)
- Just in case the chromedriver.exe is outdated, check your browser version by following [***these steps***](https://www.businessinsider.com/what-version-of-google-chrome-do-i-have).  
- After that, you can download the lastest version [***here***](https://chromedriver.chromium.org/downloads) and remove the default one in this repo.   

## 4. Modify the config.json file
Open the file *config.json* in this repo and replace these content with your information:  
- **<Your FPT email password>**: Your FPT University account's email
- **<Your FPT email password>**: Your FPT University account's password
- <Subject to register>: The subject code you want to register
- <Your register option>: Your register option (Register extra courses, Register to improve mark, Register to repeat a course)
- <Chatbot facebook email>: The chatbot facebook email 
- <Chatbot facebook password>: The chatbot facebook password
- <Your facebook username>: Your facebook username 
- <attempt_limit>: The maximun number of attempts you want to retry in case any error occured.
- <break_time>: Time break between each loop

## 5. Run the script
> `python bot.py`
Any error occured, please check the log.txt file.
