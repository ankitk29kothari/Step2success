easySelenium [![Travis Status](https://travis-ci.com/SeleniumHQ/selenium.svg?branch=master)](//travis-ci.com/SeleniumHQ/selenium/builds) [![AppVeyor Status](https://ci.appveyor.com/api/projects/status/pg1f99p1aetp9mk9/branch/master?svg=true)](https://ci.appveyor.com/project/SeleniumHQ/selenium/branch/master)
========
<a href="https://selenium.dev"><img src="https://selenium.dev/images/selenium_logo_square_green.png" width="180" alt="Selenium"/></a>

easyselenium is write on the top of selenium to make selenium easier for begineers for ready built in funtions only they need to call the functions and pass the arguments.All extra thing time delay and webdriver wait select findping xpath will do in backend.
Get rid of using time delays

The project is made possible by volunteer contributors who've
generously donated thousands of hours in code development and upkeep.

Selenium's source code is made available under the [Apache 2.0 license](https://github.com/SeleniumHQ/selenium/blob/master/LICENSE).

## Documentation


## from easy selenium import *
## Open broswer()
```sh
with optional arguments

headless = True/False (to work without browser)
path = 'your drirectory by default is default directory'
browser = 'chrome'/'firefox'/ie
debug = True/False (to print what is happening inside the code)

Example
This is by default arguments

open_browser(headless=False,path="chromedriver.exe",browser='chrome',debug=False)
```