from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# service = Service(executable_path = r"C:\geckodriver\geckodriver.exe") ---- no need for this
fp = webdriver.FirefoxProfile(r"C:\Users\tempe\AppData\Roaming\Mozilla\Firefox\Profiles\jm3tidl2.default")
driver = webdriver.Firefox(fp)
# driver.get("https://www.google.com/")
# input_element = driver.find_element(By.CLASS_NAME, "search-handoff-button")
# input_element.send_keys("hello")

    time.sleep(5)
driv    er.quit()
