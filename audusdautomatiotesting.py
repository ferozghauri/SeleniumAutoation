from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.tradingview.com/chart/?symbol=FX%3AAUDUSD")
driver.implicitly_wait(5000)

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
_hamburger.click()
print("hamburger clicked")
driver.implicitly_wait(5000)

_exportChartData = driver.find_element_by_xpath('//*[@id="overlap-manager-root"]/div/span/div[1]/div/div/div[3]/div/div')
print(_exportChartData.get_attribute('innerHTML'))
_exportChartData.click()

print("export data clicked")
driver.implicitly_wait(5000)


driver.find_element_by_xpath('//*[@id="overlap-manager-root"]/div/div/div[1]/div/div[3]/div/span/button').click()
print("export button clicked clicked")

sleep(3)
#driver.close()
