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
driver.get("https://www.oyorooms.com/search?location=Delhi%2C%20India&city=Delhi&searchType=city&coupon=&checkin=17%2F11%2F2019&checkout=18%2F11%2F2019&roomConfig%5B%5D=1&showSearchElements=false&country=india&guests=1&rooms=1&filters%5Bcity_id%5D=2")



# using find elements to get all data in list witin the same id
description=driver.find_elements_by_xpath('//*[@class="listingHotelDescription__hotelName d-textEllipsis"]')
rating=driver.find_elements_by_xpath('//*[@class="listingPrice__finalPrice"]')

#print ist of all elements	 present in id.
#print(description)

for i,j in zip(description,rating):
	print(i.text,j.text)
	print("\n\n")