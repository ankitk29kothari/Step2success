from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

import time


#importing chrome driver shuold be in same folder 

chrome_options = webdriver.ChromeOptions()


#path where driver is stored

driver=webdriver.Chrome(executable_path=r"chromedriver.exe")

#url which nned to be open

driver.get("https://www.google.com/")
print('Opening URl in chrome driver')
time.sleep(3)


f_name=driver.find_element_by_xpath('//*[@class="NKcBbd"]')
f_name.click()
time.sleep(3)


f_name=driver.find_element_by_xpath('//*[@class="kp-tabcontent"]')
print(f_name.text)
time.sleep(5)
