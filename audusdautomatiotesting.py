from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.tradingview.com/chart/?symbol=FX%3AAUDUSD")
driver.implicitly_wait(5000)

# searchbox = driver.find_element_by_xpath('//*[@id="search"]')
# searchbox.send_keys('Feroz Ghauri')

#searchButton = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div/div/div')
driver.find_element_by_class_name('button-9U4gleap').click()
print("hamburger clicked")
driver.implicitly_wait(5000)
driver.find_element_by_xpath('//*[@id="overlap-manager-root"]/div/span/div[1]/div/div/div[2]').click()
print("export data clicked")
driver.implicitly_wait(5000)
driver.find_element_by_xpath('//*[@id="overlap-manager-root"]/div/div/div[1]/div/div[3]/div/span/button').click()
print("export button clicked clicked")


#searchButton.Click()

#Hamburger Click
#<div data-role="button" class="button-9U4gleap button-2ioYhFEY isInteractive-20uLObIc"><svg width="28" height="28" xmlns="http://www.w3.org/2000/svg"><g fill="currentColor"><path d="M6 7h16a1 1 0 1 1 0 2H6z" class="line-O3ltjpHc"></path><path d="M6 13h16a1 1 0 1 1 0 2H6z" class="line-O3ltjpHc"></path><path d="M6 19h16a1 1 0 1 1 0 2H6z" class="line-O3ltjpHc"></path><path d="M6 9a1 1 0 1 1 0 -2zM6 15a1 1 0 1 1 0 -2zM6 21a1 1 0 1 1 0 -2z"></path></g></svg></div>

#Export Data option Click
#<div class="label-3Xqxy756">Export chart data...</div>
