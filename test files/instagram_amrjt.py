from time import sleep
from selenium import webdriver
from packaging import version
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pickle

#lpu = Options()
#lpu.headless = True
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
url = "http://www.instagram.com"
driver.get(url)

cookies = pickle.load(open("C:/Users/Mr Sultan/Desktop/intro_moment_1.2/intro_moment/test files/auth.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)
driver.get("https://www.instagram.com/")

k =[]
l = []
a ="/"
b = "/"
us = ["cristiano"]
for c in us:
    user = a+c+b
    driver.get(url + user)
    fi = driver.find_element(By.TAG_NAME, "ul")
    ki = fi.find_elements(By.TAG_NAME, "li")
    for i in ki:
        l.append(i.text)
    l.append(url+user)
#############################################
    y=1000

    SCROLL_PAUSE_TIME = 5
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(SCROLL_PAUSE_TIME)
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


    kii = driver.find_elements("xpath", "/html/body/div/div/div/div/div/div/div/div/div/div/div/section/main/div/div/article/div/div//a")
    for i in kii:
        k.append(i.get_attribute("href"))
print(l)
print(k)
print(len(k))