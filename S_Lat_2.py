# import webdriver 
from selenium import webdriver 
import time 
# import Action chains 
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.common.keys import Keys

# create webdriver object 
driver = webdriver.Firefox() 

# get geeksforgeeks.org 
driver.get("https://www.latam.com/pt-br/") 

driver.find_element_by_xpath('//*[@id="em__b-UID__booking-journeyType-ow"]').click()
# get element 
time.sleep(2)
driver.find_element_by_xpath('//*[@id="em__b-UID__booking-origin-selector-container"]/div/div[1]/div[1]').click()
element = driver.find_element_by_xpath('//*[@id="em__b-UID__booking-origin-selector-container"]/div/div[1]/div[1]')



# create action chain object 
action = ActionChains(driver) 
# click the item 
action.click(on_element = element) 
action.send_keys("Vix") 
#action.click(on_element = element) 
action.send_keys(Keys.TAB)
action.perform() 

driver.find_element_by_xpath('//*[@id="em__b-UID__booking-destination-selector-container"]/div').click()
element = driver.find_element_by_xpath('//*[@id="em__b-UID__booking-destination-selector-container"]/div')

# create action chain object 
action = ActionChains(driver) 
action.click(on_element = element) 
action.send_keys("FRA") 
action.send_keys(Keys.TAB)
action.perform() 


driver.find_element_by_xpath('//*[@id="em__b-UID__booking-departure"]').click()
time.sleep(0.5)
element = driver.find_element_by_xpath('//*[@id="em__b-UID__booking-departure"]')
element.clear()
action = ActionChains(driver)
# create action chain object 
# move the cursor 
action.click(on_element = element) 
action.send_keys(" 16/10/2021")
action.send_keys(Keys.TAB)
  
# perform the operation 
action.perform() 

