from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.tradingview.com/chart/?symbol=FX%3AAUDUSD")
driver.implicitly_wait(5000)

# searchbox = driver.find_element_by_xpath('//*[@id="search"]')
# searchbox.send_keys('Feroz Ghauri')

#searchButton = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div/div/div')
driver.find_element_by_class_name('button-9U4gleap').click()
print("hamburger clicked")
driver.implicitly_wait(5000)

driver.find_element_by_xpath('//*[@id="overlap-manager-root"]/div/span/div[1]/div/div/div[11]/div').click()
print("Sign In Button Clicked")
driver.implicitly_wait(5000)

driver.find_element_by_xpath('//*[@id="overlap-manager-root"]/div/div[2]/div/div/div/div/div/div[1]/div[6]/div/div[1]/div/span').click()
print("Email username button clicked")
driver.implicitly_wait(5000)

driver.find_element_by_xpath('//*[@id="signin-form"]/div[1]/div[1]/input').send_keys("GoodyErick")
print("username entered")
driver.implicitly_wait(10000)

driver.find_element_by_xpath('//*[@id="signin-form"]/div[2]/div/div[1]/input').send_keys("password1234")
print("password entered")
driver.implicitly_wait(10000)

driver.find_element_by_xpath('//*[@id="signin-form"]/div[3]/div[2]/button/span[2]').click()
print("Sign In Button Clicked")
driver.implicitly_wait(50000)
sleep(10)
print("now moving forward")


_hamburger = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div/div/div')
print(_hamburger.get_attribute('innerHTML'))
_hamburger.click()
print("hamburger clicked")
driver.implicitly_wait(5000)
#sleep(3)

# #code from previous version start
# driver.find_element_by_xpath('//*[@id="overlap-manager-root"]/div/span/div[1]/div/div/div[2]').click()
# print("export data clicked")
# driver.implicitly_wait(5000)
# driver.find_element_by_xpath('//*[@id="overlap-manager-root"]/div/div/div[1]/div/div[3]/div/span/button').click()
# print("export button clicked clicked")
# #code from previous version end

#code start
_exportChartData = driver.find_element_by_xpath('//*[@id="overlap-manager-root"]/div/span/div[1]/div/div/div[3]/div/div')
#driver.find_elements_by_xpath("//*[contains(text(), 'Export chart data...')]")
print(_exportChartData.get_attribute('innerHTML'))
_exportChartData.click()

print("export data clicked")
driver.implicitly_wait(5000)
# driver.find_element_by_class_name('item-3dBR9Pqb').click()
# print("export data clicked")
# driver.implicitly_wait(5000)
sleep(3)

driver.find_element_by_xpath('//*[@id="overlap-manager-root"]/div/div/div[1]/div/div[3]/div/span/button').click()
print("export button clicked clicked")
#code end

#searchButton.Click()

#Hamburger Click
#<div data-role="button" class="button-9U4gleap button-2ioYhFEY isInteractive-20uLObIc"><svg width="28" height="28" xmlns="http://www.w3.org/2000/svg"><g fill="currentColor"><path d="M6 7h16a1 1 0 1 1 0 2H6z" class="line-O3ltjpHc"></path><path d="M6 13h16a1 1 0 1 1 0 2H6z" class="line-O3ltjpHc"></path><path d="M6 19h16a1 1 0 1 1 0 2H6z" class="line-O3ltjpHc"></path><path d="M6 9a1 1 0 1 1 0 -2zM6 15a1 1 0 1 1 0 -2zM6 21a1 1 0 1 1 0 -2z"></path></g></svg></div>

#Export Data option Click
#<div class="label-3Xqxy756">Export chart data...</div>


#<div class="label-3Xqxy756">Export chart data...</div>

#document.evaluate('//*[@id="overlap-manager-root"]/div/div/div[2]/div[5]/div/div', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;

#<div class="apply-common-tooltip common-tooltip-vertical item-2xPVYue0 item-3dBR9Pqb"><div class="labelRow-3Q0rdE8-"><div class="label-3Xqxy756">Export chart data...</div></div></div>