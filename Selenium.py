import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
'''
driver.maximize_window()
print(driver.title)
print(driver.current_url)
print(driver.name)

driver.find_element(By.NAME,"email").send_keys("hello@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("1234")
driver.find_element(By.ID,"exampleCheck1").click()
driver.find_element(By.XPATH,"//input[@type='submit']").click()
driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("Darvin")
message=driver.find_element(By.CLASS_NAME,"alert-success").text
print(message)
assert ("Success!" in message)
time.sleep(2)
data=driver.find_elements(By.XPATH,"//input[@type='checkbox']") # .classname also cssselector
for d in data:
    if d.text == "option2": # or below
        if d.get_attribute('value') == "option2"
            d.click() # d[1].click()
            assert d.is_selected() # is_displayed()
            break
assert d.text == "option2"'''
time.sleep(2)
driver.find_element(By.NAME,"bday").send_keys("22-04-1983")
time.sleep(2)


