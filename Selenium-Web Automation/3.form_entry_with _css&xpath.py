#############################
#                            #
#      Step2success.in       #
#        copyright           #
##############################           
# Selenium is used for Gui testing as well as we can use it for web scrapping and web automation to fill up forms in complex sites and tools.
#pip install selenium        

#improting selenium driver(always copy paste all this function to minimse hassle)


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

driver.get("https://step2success.in/registration-page-demo/")
print('Opening URl in chrome driver')
time.sleep(5)




#you can use any of these method
f_name=driver.find_element_by_id("first_name")
#or
f_name=driver.find_element_by_xpath('//*[@data-role="tooltip"]')
#or
f_name=driver.find_element_by_xpath('//*[@id="first_name"]')


f_name=driver.find_element_by_xpath('//*[@class="form-control"]')
f_name=WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@class="form-control"]')))
f_name.send_keys("Ankit")
print('found id now sending keys')





submit_button=driver.find_element_by_id("register")

submit_button.click()
print('found id of submit button now clicking on it')




#For submit  l_name.click()

