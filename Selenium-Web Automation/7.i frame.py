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
driver.get("https://step2success.in/iframe-demo/")

driver.switch_to.frame(0)

