import concurrent.futures
from concurrent.futures import ProcessPoolExecutor

def download(start_date,end_date,activity):
	from selenium import webdriver
	from selenium.webdriver.common.keys import Keys
	from selenium.webdriver.common.by import By
	from selenium.webdriver.common.action_chains import ActionChains
	from selenium.webdriver.support.ui import WebDriverWait
	from selenium.webdriver.support import expected_conditions as EC
	from selenium.common.exceptions import TimeoutException
	import pandas as pd
	import time
	from datetime import date
	from selenium.webdriver.support.select import Select
	#Driver set up
	driver = webdriver.Chrome("chromedriver.exe")
	driver.get("https://vfoprod-elink.activationnow.com/login.jsp")

	#login to the site
	user=driver.find_element_by_name("loginName").send_keys("ef654884")
	pwd=driver.find_element_by_name("password").send_keys("Ericsson@2019")
	module=driver.find_element_by_name("serviceRequestType").send_keys("Access")
	click=driver.find_element(By.XPATH, '/html/body/table/tbody/tr[2]/th/table/tbody/tr[3]/td[2]/table/tbody/tr[2]/th/form/table/tbody/tr[10]/th[3]/div/a/img').click()
	driver.maximize_window()

	#window manage
	time.sleep(2)
	main_page = driver.current_window_handle 
	element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//frame[@name="mainFrame"]')))
	driver.switch_to.frame(element)
	time.sleep(2)


	print(start_date,end_date)
	filter_img = driver.find_element_by_xpath('//a[img/@src="images/filter.gif"]').click()
	time.sleep(5)
	for handle in driver.window_handles: 
	    if handle != main_page: 
	        filter_win = handle

	driver.switch_to.window(filter_win)
	time.sleep(2)
	clear=driver.find_element_by_xpath('//*[@id="guiId"]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/a/img').click()

	date_sent_from=driver.find_element(By.XPATH,"//*[@id='fromDateSent']").send_keys(start_date)
	
	date_sent=driver.find_element(By.XPATH,"//*[@id='toDateSent']").send_keys(end_date)

	a=Select(driver.find_element_by_name("CCNA"))
	a.select_by_value('MJC')
	b=Select(driver.find_element_by_name("SERVICETYPE"))
	b.select_by_value(activity)
	c=Select(driver.find_element_by_name("ACTIVITY"))
	c.select_by_value('D')

	driver.find_element_by_xpath('//*[@id="guiId"]/table/tbody/tr[4]/td/table/tbody/tr/td[1]/a/img').click()
	time.sleep(5)
	driver.switch_to.window(main_page)
	driver.switch_to.frame(element)
	time.sleep(4)
	d=WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.XPATH, '//a[img/@src="images/icon_excel.gif"]')))
	time.sleep(2)
	d.click()
	return("done")

act_dict={'uni':'End User Switched Ethernet:SWITCHED_ETHERNET_SVC'}
end_dates=['04/19/2020','01/19/2020','10/19/2019','07/19/2019']
start_dates=['01/19/2020','10/19/2019','07/19/2019','04/19/2019']

#map(download,(start_dates),(end_dates))
for j,k in zip(start_dates,end_dates):
	download(j,k)

