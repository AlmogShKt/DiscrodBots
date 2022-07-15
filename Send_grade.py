import os
import time
import warnings
from datetime import datetime

from dotenv import load_dotenv


import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def getLS():
    def clearConsole():
        command = 'clear'
        if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'
        os.system(command)

    clearConsole()

    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument("--log-level=0")
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    browser = webdriver.Chrome(options=chrome_options ,\
        executable_path=r'/Users/almogshtaigmann/Downloads/chromedriver')

    webpage = 'https://sheilta.apps.openu.ac.il/pls/dmyopt2/course_info.courses?p_from=1'
    browser.get(webpage)

    clearConsole()

    load_dotenv()

    username = os.getenv('openU_username')
    password = os.getenv('openU_password')
    id = os.getenv('openU_id')

    browser.find_element("id", 'p_user').send_keys(username)

    browser.find_element("id","p_sisma").send_keys(password)

    browser.find_element("id","p_mis_student").send_keys(id)

    browser.find_element("xpath",'//*[@id="login_sso"]/fieldset/input[1]').click()

    while True:
        browser.get(webpage)
        html = browser.page_source
        soup = BeautifulSoup(html,'html.parser')
        tr_table=soup.find("table", {'class':'content_tbl'}).text
        items=tr_table.split('\n')
        print(items)
        course_id = '20441'
        for i in range(len(items)):
            if course_id in items[i]:
                if items[i-9].isdigit():
                    result = "{0} Course {1} - Exam grade is: {2}".format(datetime.now().strftime('%d/%m/%Y %H:%M:%S'),course_id,items[i-9])
                    if items[i-12].isdigit():
                        result += "\n{0} Final grade in course {2} is: {1}".format(datetime.now().strftime('%d/%m/%Y %H:%M:%S'),items[i-12],course_id)
                    else:
                        result += "\n{0} Final grade not given yet - good luck MOED B".format(datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
                    print(result)
                    return  result
                    message= { "value1" : result }
                    IFTTT_KEY='KEY'
                    IFTTT_URL='https://maker.ifttt.com/trigger/{EVENT_NAME_IN_IFTTT}/with/key/'+IFTTT_KEY
                    requests.post(IFTTT_URL,data=message)
                    exit()
                else:
                    print("{0} No grade yet for Course {1}".format(datetime.now().strftime('%d/%m/%Y %H:%M:%S'),course_id))
                break

        time.sleep(120)
        browser.refresh()
        clearConsole()

    browser.quit()
