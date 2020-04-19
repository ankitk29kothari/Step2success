#############################
#                            #
#      Step2success.in       #
#        copyright           #
##############################   


#Program to show you all the hotel available in Laxmi Nagar & its price.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

chrome_options = webdriver.ChromeOptions()
import time
 
driver = webdriver.Chrome(executable_path="chromedriver.exe",chrome_options=chrome_options)
driver.get("https://step2success.in/courses/python-deepdive/")

time.sleep(5)
des=driver.find_element_by_xpath('//div[@id="learn-press-course-tabs"]/ul/li[2]/a')
des.click()

time.sleep(3)


# using find elements to get all data in list witin the same id
description=driver.find_elements_by_xpath('//*[@class="lesson-title course-item-title button-load-item"]')



#print ist of all elements	 present in id.
#print(description)

for i in (description):
	print(i.text)
	print("....\n\n")