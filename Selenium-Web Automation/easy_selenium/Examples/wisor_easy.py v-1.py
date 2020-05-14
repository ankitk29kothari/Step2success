from easyselenium import *

open_browser(headless=False,browser='firefox',debug=True)

open_url(url="https://vfoprod-elink.activationnow.com/login.jsp")


send_text(name='loginName',text=' your username')


send_text(name='password',text='your password ')
send_text(name='serviceRequestType',text='Access')

click_on(image='images/login.gif')


switch_frame(no=1)

read_text(title='View Last Notification')
click_on(image='images/filter.gif')
window_handle(no=1)


click_on(image='images/clear.gif')

select_dropdown(name='CCNA',option='MJC')
send_text(id='fromDateSent',text='01/19/2020')
send_text(id='toDateSent',text='04/19/2020')

click_on(image='images/ok.gif')

window_handle(no=0)
switch_frame(no=1)
click_on(image='images/icon_excel.gif')

#close_window(no=0)





