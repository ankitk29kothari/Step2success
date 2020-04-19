#############################
#                            #
#      Step2success.in       #
#        copyright           #
##############################           
# Selenium is used for Gui testing as well as we can use it for web scrapping and web automation to fill up forms in complex sites and tools.
#pip install selenium        

#improting selenium driver(always copy paste all this function to minimse hassle)


from selenium import webdriver
import time
import concurrent.futures
#importing chrome driver shuold be in same folder 

chrome_options = webdriver.ChromeOptions()


#path where driver is stored

def open(secs):

	driver=webdriver.Chrome(executable_path=r"chromedriver.exe")

	#url which nned to be open

	driver.get("https://step2success.in/registration-page-demo/")
	print('Opening URl in chrome driver')
	time.sleep(5)





	f_name=driver.find_element_by_id("first_name")
	f_name.send_keys(secs)
	print('found id now sending keys')


	l_name=driver.find_element_by_id("last_name")
	l_name.send_keys("Kothari")


	button=driver.find_element_by_id("register")
	button.click()
	print('found id of submit button now clicking on it')
	time.sleep(5)
	driver.close()
	return('done{}'.format(secs))
	


def main():
	secs=[1,2,3,4]
	
	t1=time.perf_counter()

	with concurrent.futures.ProcessPoolExecutor() as executor:
	#with concurrent.futures.ThreadPoolExecutor(max_workers = 10) as executor:
		
		results=executor.map(open, secs)
		for result in results:
			print(result)

		t2=time.perf_counter()
		print('Finsihed in',(t2-t1/2),'sec')






if __name__ == '__main__':
	main()