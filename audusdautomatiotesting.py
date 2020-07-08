from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep

# options = webdriver.ChromeOptions() 
# options.add_argument("download.default_directory=C:/Users/dell/Desktop/Selenium automation script")
res=1
while res <10:
    chrome_options = webdriver.ChromeOptions()
    prefs = {'download.default_directory' : r'C:\Users\dell\Desktop\Selenium automation script\\'}#Must Include double slash like \\ in the end of the path
    chrome_options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(chrome_options=chrome_options)

    #driver = webdriver.Chrome()
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

    driver.find_element_by_xpath('//*[@id="signin-form"]/div[1]/div[1]/input').send_keys("")
    print("username entered")
    driver.implicitly_wait(10000)

    driver.find_element_by_xpath('//*[@id="signin-form"]/div[2]/div/div[1]/input').send_keys("")
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

    sleep(10)
    driver.close()


