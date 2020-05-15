
from easyselenium import *
import time
driver=open_browser(browser='chrome',headless=False)
open_url(url="https://google.com/")
open_url(url='https://step2success.in/registration-page-demo/',new_tab=True)


window_handle(1)
click_on(id='register')

time.sleep(5)
alerts('accept')


time.sleep(5)
close_window(title='Registration Demo')
