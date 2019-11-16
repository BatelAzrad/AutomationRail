import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

date = input("Enter full date (dd/mm/yyyy): ")
time = input("Enter time in 24h format (hh:mm): ")
fName = 'Bat-El'
lName = 'Azrad'
Id = '123456789'
add = 'Street name and number'
city = 'City'
phone = '052-2228896'
email = 'azradbatel@gmail.com'
ravKavNum = '123456789'
#dateTime = sys.argv[1] + sys.argv[2]
dateTime = date + ' ' + time
print(dateTime)

driver = webdriver.Chrome(r"C:\Users\chromedriver\chromedriver.exe")
driver.get("https://ilrail.wizsupport.com/chat/m/TDDD22T2S5")

myFirstName = driver.find_element_by_id("txt47")
myFirstName.send_keys(fName)
myLastName = driver.find_element_by_id("txt48")
myLastName.send_keys(lName)
myIdNum = driver.find_element_by_id("txt3234")
myIdNum.send_keys(Id)
myAdd = driver.find_element_by_id("txt52")
myAdd.send_keys(add)
myCity = driver.find_element_by_id("txt51")
myCity.send_keys(city)
myPhone = driver.find_element_by_id("txt58")
myPhone.send_keys(phone)
myEmail = driver.find_element_by_id("txt59")
myEmail.send_keys(email)

ravKav = Select(driver.find_element_by_id("sel61"))
ravKav.select_by_value("כן")

myRavKav = driver.find_element_by_id("txt49")
myRavKav.send_keys(ravKavNum)
date = driver.find_element_by_id("longstamp63")
date.send_keys(dateTime)

start = Select(driver.find_element_by_id("sel64"))
start.select_by_value("מגדל העמק- כפר ברוך")
end = Select(driver.find_element_by_id("sel65"))
end.select_by_value("חיפה- חוף הכרמל")

notes = driver.find_element_by_id("txt67")
notes.send_keys(".")
send = driver.find_element_by_id("finishForm")
send.click()
driver.close()