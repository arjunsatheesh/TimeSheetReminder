# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 21:35:47 2020

@author: AS050739
"""

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

import win10toast
from win10toast import ToastNotifier

from selenium import webdriver
import time

toaster = ToastNotifier()

opt = Options()
opt.headless = True
opt.add_experimental_option('excludeSwitches', ['enable-logging'])
#driver=webdriver.Chrome(r"C:\TimeSheet\chromedriver.exe",options=opt)
driver=webdriver.Chrome(executable_path=r"C:\TimeSheet\chromedriver.exe",options=opt)
driver.get("https://mytime.cerner.com/")
time.sleep(20)

try:
    element = driver.find_element_by_xpath("//div[@id='status-text']//*[contains(text(),'Pending')]")
    if element:
        toaster.show_toast("Time Sheet","Please Submit Your Time Sheet!",duration=10)    

except NoSuchElementException:
    toaster.show_toast("Time Sheet","Thanks for Submitting your Time Sheet.",duration=5)
    
    
driver.close()
