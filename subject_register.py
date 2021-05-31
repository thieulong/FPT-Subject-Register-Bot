import json
import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from time import sleep
import datetime

with open('config.json') as file:
    config = json.load(file)

driver = webdriver.Chrome(config['chrome_driver_linux'])
fap_url = config['fap_url']
messenger_url = config['messenger_url']
fpt_email = config['fpt_email']
fpt_password = config['fpt_password']
subject_code = config['subject_code']
option = config['option']
facebook_email = config['facebook_email']
facebook_passwork = config['facebook_password']
user = config['facebook_user']
attempt_limit = config['attempt_limit']
breaktime = config['breaktime']

log = list()
message = list()
running = True
breaktime = breaktime*60
loop = 0


def fap_log_in():
    
    driver.get(fap_url)

    content = "[INFO] Opening FAP website"
    print(content)
    log_file.write(content+os.linesep)

    campus = Select(driver.find_element_by_id("ctl00_mainContent_ddlCampus"))
    campus.select_by_value('4')

    content = "[INFO] Select: FU-Hồ Chí Minh"
    print(content)
    log_file.write(content+os.linesep)

    mail = driver.find_element_by_class_name("abcRioButtonContents")
    mail.click()

    main_page = driver.current_window_handle[0]

    pop_up = driver.window_handles[1]
    driver.switch_to.window(pop_up)

    content = "[INFO] Opening login window"
    print(content)
    log_file.write(content+os.linesep)

    enter_email = True
    enter_password = True

    email_attempt = 0
    password_attempt = 0

    while enter_email:

        try:
            content = "[INFO] Entering email"
            print(content)
            log_file.write(content+os.linesep)

            try:
                email_box = driver.find_element_by_id("identifierId")
                email_box.click()
                email_box.send_keys(fpt_email)
                driver.find_element_by_id("identifierNext").click()

            except Exception:
                email_box = driver.find_element_by_id("Email")
                email_box.click()
                email_box.send_keys(fpt_email)
                driver.find_element_by_id("next").click()

            enter_email = False

        except Exception:
            email_attempt += 1

            if email_attempt == attempt_limit:
                content = "[ERROR] Moving to the next section"
                print(content)
                log_file.write(content+os.linesep)
                enter_email = False
            
            else:
                content = "[ERROR] Error occured! Trying again"
                print(content)
                log_file.write(content+os.linesep)
                sleep(2)

    sleep(2)

    while enter_password:

        try:
            content = "[INFO] Entering password"
            print(content)
            log_file.write(content+os.linesep)

            try:
                password_box = driver.find_element_by_name("password")
                password_box.click()
                password_box.send_keys(fpt_password)
                driver.find_element_by_id("passwordNext").click()
            
            except Exception:
                password_box = driver.find_element_by_id("password")
                password_box.click()
                password_box.send_keys(fpt_password)
                driver.find_element_by_id("submit").click()
            
            enter_password = False

        except Exception:
            password_attempt += 1

            if password_attempt == attempt_limit: 
                content = "[ERROR] Moving to the next section"
                print(content)
                log_file.write(content+os.linesep)
                enter_password = False

            else:
                content = "[ERROR] Error occured! Trying again"
                print(content)
                log_file.write(content+os.linesep)
                sleep(2)

    sleep(5)
    content = "[INFO] FAP login successful!"
    print(content)
    sleep(2)


def subject_registration():
    
    driver.switch_to.window(driver.window_handles[0])

    link = driver.find_element_by_link_text(option)
    link.click()

    content = "[INFO] Opening register extra courses"
    print(content)
    log_file.write(content+os.linesep)

    sleep(2)

    box = driver.find_element_by_id("ctl00_mainContent_txtSubjectCode")
    box.click()
    box.send_keys(subject_code)

    tick = driver.find_element_by_id("ctl00_mainContent_chkSubjectCode")
    tick.click()

    sleep(2)

    for elem in driver.find_elements_by_xpath('.//span[@id = "ctl00_mainContent_lblInvalidSubject"]'):
        message.append(elem.text)
        content = "[STATUS] {}".format(elem.text)
        print(content)
        log_file.write(content+os.linesep)


def messenger_log_in():
    
    content = "[INFO] Opening Messenger"
    print(content)
    log_file.write(content+os.linesep)

    driver.get(messenger_url)

    sleep(2)

    content = "[INFO] Entering username"
    print(content)
    log_file.write(content+os.linesep)
    
    username = driver.find_element_by_id('email')
    username.send_keys(facebook_email)

    content = "[INFO] Entering password"
    print(content)
    log_file.write(content+os.linesep)

    password = driver.find_element_by_id('pass')
    password.send_keys(facebook_passwork)

    login = driver.find_element_by_id('loginbutton')
    login.click()

    content = "[INFO] Messenger login successful!"
    print(content)
    log_file.write(content+os.linesep)


def send_message():
    
    sleep(2)
    
    search = driver.find_element_by_xpath('//input[@placeholder="Tìm kiếm trên Messenger"]')
    search.send_keys(user)

    sleep(2)

    choose = driver.find_element_by_xpath('//img[@class="k4urcfbm datstx6m s45kfl79 emlxlaya bkmhp75w spb7xbtv pzggbiyp bixrwtb6"]')
    choose.click()

    sleep(2)

    content = "[INFO] Found "+user+'!'
    print(content)
    log_file.write(content+os.linesep)

    message_box = driver.find_element_by_css_selector(".notranslate")
    message_box.send_keys("[AUTO] Phan Thieu Long - Subject: ",subject_code," | "+"\n".join(message)+"\n")

    content = '[INFO] Message sent!'
    print(content)
    log_file.write(content+os.linesep)


while running:

    log_file = open('log.txt', 'a')

    time = datetime.datetime.now()
    time = str(time)
    print(time)
    log_file.write(time+os.linesep)
    
    login = True
    register = True
    messenger = True
    send = True
    login_attempt = 0
    register_attempt = 0
    messenger_attempt = 0
    send_attempt = 0

    while login:
    
        try:
            if loop > 0:
                driver.get(fap_url)
                login = False
            else:
                fap_log_in()
                login = False

        except Exception:
            login_attempt += 1

            if login_attempt == attempt_limit: 
                content = "[ERROR] Log in attempt #{} failed! Aborting".format(login_attempt)
                print(content)
                log_file.write(content+os.linesep)

                content = "[ERROR] Please check your connection!"
                print(content)
                log_file.write(content+os.linesep)

                driver.quit()
                login = False
                register = False
                messenger = False
                send = False

            else:
                content = "[ERROR] Log in attempt #{} failed! Trying again".format(login_attempt)
                print(content)
                log_file.write(content+os.linesep)
                sleep(5)
        
    while register:

        try:
            subject_registration()
            register = False

        except Exception:
            register_attempt += 1

            if register_attempt == attempt_limit:
                content = "[ERROR] Register attempt #{} failed! Aborting".format(register_attempt)
                print(content)
                log_file.write(content+os.linesep)

                content = "[ERROR] There might be a problem with the website!"
                print(content)
                log_file.write(content+os.linesep)

                driver.quit()
                register = False
                messenger = False
                send = False
            
            else: 
                content = "[ERROR] Register attempt #{} failed! Trying again".format(register_attempt)
                print(content)
                log_file.write(content+os.linesep)
                sleep(5)

    while messenger:

        try:
            if loop > 0:
                driver.get(messenger_url)
                messenger = False
            else:
                messenger_log_in()
                messenger = False

        except Exception:
            messenger_attempt += 1

            if messenger_attempt == attempt_limit:
                content = "[ERROR] Log in Messenger attempt #{} failed! Aborting".format(messenger_attempt)
                print(content)
                log_file.write(content+os.linesep)

                content = "[ERROR] Please check your connection!"
                print(content)
                log_file.write(content+os.linesep)

                driver.quit()
                messenger = False
                send = False

            else:
                content = "[ERROR] Log in Messenger attempt #{} failed! Trying again".format(messenger_attempt)
                print(content)
                log_file.write(content+os.linesep)
                sleep(5)

    while send:

        try:
            send_message()
            send = False

        except Exception:
            send_attempt += 1

            if send_attempt == attempt_limit:
                content = "[ERROR] Sending message attempt #{} failed! Aborting".format(send_attempt)
                print(content)
                log_file.write(content+os.linesep)

                content = "[ERROR] Please check your connection!"
                print(content)
                log_file.write(content+os.linesep)

                driver.quit()
                send = False
            
            else:
                content = "[ERROR] Sending message attempt #{} failed! Trying again".format(send_attempt)
                print(content)
                log_file.write(content+os.linesep)
                sleep(5)

    content = "[INFO] Program terminated!"
    print(content)
    log_file.write(content+os.linesep)
    log_file.write("\n")
    log_file.close()
    sleep(breaktime)
    loop += 1
        
