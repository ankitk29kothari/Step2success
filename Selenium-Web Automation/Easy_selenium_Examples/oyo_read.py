from easyselenium import *

open_browser(browser='chrome',debug=True)
open_url("https://www.oyorooms.com/search?location=Delhi%2C%20India&city=Delhi&searchType=city&coupon=&checkin=17%2F11%2F2019&checkout=18%2F11%2F2019&roomConfig%5B%5D=1&showSearchElements=false&country=india&guests=1&rooms=1&filters%5Bcity_id%5D=2")

hotel_name=read_text(xpath='class="listingHotelDescription__hotelName d-textEllipsis"')


hotel_price=read_text(xpath='class="listingPrice__finalPrice"')



for i,j in zip(hotel_name,hotel_price):
	print('Hote name: {} and its price is{}'.format(i[0],j[0]))


