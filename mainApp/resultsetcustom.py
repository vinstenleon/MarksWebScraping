#imports
from selenium import webdriver
import os
from time import sleep
import platform
#Setting up Chrome options
chrome_options = webdriver.ChromeOptions()
if platform.system() == 'Linux':
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])#to remove the "Chrome is being controlled by automated test software" notification
chrome_options.add_argument("--headless")#To make The Browser not appear / Headless Chrome
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
if not platform.system() == 'Linux':
    currentWorkingDirectory=os.path.dirname(os.path.abspath(__file__))
    if platform.system() == 'Linux':
        chromeDriverUrl=os.path.join(currentWorkingDirectory,"chromedriver_linux64")
        chromeDriverUrl=os.path.join(chromeDriverUrl,"chromedriver")
    else:
        chromeDriverUrl=os.path.join(currentWorkingDirectory,"chromedriver_win32")#use join function so that it works in any OS
        chromeDriverUrl=os.path.join(chromeDriverUrl,"chromedriver.exe")
    driver = webdriver.Chrome(executable_path=str(chromeDriverUrl),options=chrome_options)
else:
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),options=chrome_options)



def getrs(year,sem):
    for i in range(1,10):
        url="https://www.vtu4u.com/results/4so"+str(year)+"cs00"+str(i)+"?cbse=1"
        driver.get(url)
        sleep(1)
        allTables=driver.find_elements_by_class_name("table") #getting all tables i.e. all sem results including revaluation
        for tabletags in allTables:
            allTableRows=tabletags.find_elements_by_tag_name("tr")
            semester=allTableRows[1].find_elements_by_tag_name("td")[0].text
            sgpa=allTableRows[1].find_elements_by_tag_name("td")[3].text

            if int(semester)==sem and str(sgpa)!="N/A":
                hrefToMarks=allTableRows[1].find_elements_by_tag_name("td")[6].find_element_by_tag_name("a").get_attribute("href")
                rs=hrefToMarks[49:51]
                if rs[1]=="?":
                    resultSet=rs[0]
                else:
                    resultSet=rs
                return resultSet
