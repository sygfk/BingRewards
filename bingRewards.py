import os
import sys
import string
import time
import random, string

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options



# loginUrl = "http://www.bing.com/"
loginUrl ="https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1487226969&rver=6.7.6631.0&wp=MBI&wreply=https%3a%2f%2fwww.bing.com%2fsecure%2fPassport.aspx%3frequrl%3dhttp%253a%252f%252fwww.bing.com%252f%253fwlexpsignin%253d1&lc=1033&id=264960"
def main():
    global loginUsers
    loginUsers = {'email':'password','email2':'password'}
    login()


def login():

    global loginUsers
    global password 

    chromedriver = "C:\Program Files\BingReward\chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    chrome_options = Options()
    chrome_options.add_experimental_option('prefs', {
		'credentials_enable_service': False,
		'profile': {
			'password_manager_enabled': False
		}
	})
    driver = webdriver.Chrome(chrome_options=chrome_options)
	
	
    #driver = webdriver.Chrome(chromedriver)


    driver.get(loginUrl)
    
    
    
    for name in loginUsers.keys():
        box = driver.find_element_by_id('i0116');
        actions = ActionChains(driver)
        actions.move_to_element(box).send_keys(name).perform()
    
        driver.implicitly_wait(3)
    
        driver.find_element_by_id("idSIButton9").click()
        
        time.sleep(2)
    
        passwordBox =  driver.find_element_by_id('i0118');
        actions = ActionChains(driver)
        actions.move_to_element(passwordBox).send_keys(loginUsers[name]).perform()
        driver.implicitly_wait(3)
        driver.find_element_by_xpath('//*[@id="idSIButton9"]').send_keys("\n")
        driver.refresh()
        time.sleep(2)
    
        search(driver)
        driver.find_element_by_id("id_n").click();
        driver.find_element_by_class_name("id_link_text").click();
        time.sleep(3)
        driver.find_element_by_id("id_s").click();
        driver.find_element_by_class_name("id_link_text").click();

        
        

    # pause(driver)
    driver.quit()

def search(driver):
    
    
    for x in range(0,75):
        word = randomword(random.randint(2, 10))
        driver.find_element_by_id('sb_form_q').send_keys(word)
        driver.find_element_by_id('sb_form_go').click()
        driver.find_element_by_id('sb_form_q').clear()
        time.sleep(2)


def pause(webdriver):
    element = WebDriverWait(webdriver, 5).until(
            EC.presence_of_element_located((By.ID, "myDynamicElement")))

def randomword(length):
   return ''.join(random.choice(string.ascii_lowercase) for i in range(length))

if __name__ == '__main__':
    main()

