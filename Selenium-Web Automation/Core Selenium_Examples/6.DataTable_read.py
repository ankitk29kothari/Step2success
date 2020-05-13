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
driver.get("https://step2success.in/datable-demo/")
time.sleep(2)
table=driver.find_element_by_xpath('//*[@id="example"]')
#print(table.text)

# sending text on search box
#srch=driver.find_element_by_xpath('//*[@type="search"]')
#srch.send_keys('Airi')
table=driver.find_element_by_xpath('//*[@id="example"]')
#print(table.text)
rows=table.find_elements_by_tag_name('tr')
#print(rows)
for row in rows:
	try:
		cols=row.find_elements_by_tag_name('td')
		print(cols[0].text,cols[-1].text)
	except:
		pass

