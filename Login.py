from selenium import webdriver
from selenium.webdriver.common.keys import Keys #to type something in search in bar
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

tcpass=0
tcfail =0
totcse = 11

PATH="E:\Selenium\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("http://localhost:3000/")

if driver.title == "Amrita Classroom Booking":
    tcpass += 1
    print("Test case 1: Title matched.")
    tcpass += 1
    print("Test case 2: Navigation to Home page Successful")
else:
    tcfail += 1
    print("Test case 1: Title failed to match.")
    tcfail += 1
    print("Test case 2: Navigation to Home page Failed")

# print(driver.title)

# link=driver.find_element_by_link_text("Log In")
link=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.LINK_TEXT,"Log In")))
link.click()
log = driver.find_element_by_tag_name("h1")
# print(log.text)

if log.text == "Login":
    tcpass += 1
    print("Test case 3: Navigation to Login page Successful")
else:
    tcfail += 1
    print("Test case 3: Navigation to Login Page Failed ")
# print(tcpass)
# print("************")
# if link.title == "Amrita Classroom Booking":
#     tcpass += 1
# else:
#     tcfail += 1
# usr=driver.find_element_by_id("username")
usr=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"username")))
usr.clear()
usr.send_keys("user2")
# pwd=driver.find_element_by_id("pwd")
pwd=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"pwd")))
pwd.clear()
pwd.send_keys("login2")
time.sleep(3)
sbmt=driver.find_element_by_name("button")
sbmt.click()

wel = driver.find_element_by_tag_name("h1")

# print(wel.text)
s=wel.text.split()
if(s[0]=="Welcome"):
    # print("True")
    tcpass += 1
    print("Test case 4: Login 1 successful")
    time.sleep(3)
    lout = driver.find_element_by_class_name("log")
    lout.click()

    link=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.LINK_TEXT,"Log In")))
    link.click()    
    log = driver.find_element_by_tag_name("h1")

    if log.text == "Login":
        tcpass += 1
        print("Test case 5: Logout 1 Sucessful")
        tcpass += 1
        print("Test case 6: Navigation to Home page Successful")
        tcpass += 1
        print("Test case 7: Navigation to Login page Sucessful")
    else:
        tcfail += 1
        print("Test case 5: Logout 1 Failed")
        tcfail += 1
        print("Test case 6: Navigation to Home page Failed")
        tcfail += 1
        print("Test case 7: Navigation to Login Page Failed ")

    usr=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"username")))
    usr.clear()
    usr.send_keys("user1")
    pwd=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"pwd")))
    pwd.clear()
    pwd.send_keys("login1")
    time.sleep(3)
    sbmt=driver.find_element_by_name("button")
    sbmt.click()

    wel = driver.find_element_by_tag_name("h1")
    s=wel.text.split()
    if(s[0]=="Welcome"):
        tcpass += 1
        print("Test case 8: Login 2 Successful")
    else:
        tcfail += 1 
        print("Test case 8: Login 2 Failed")    
else:
    tcfail += 1 
    print("Test case 4: Login 1 Failed")

# print(tcpass)
menucircle = driver.find_element_by_class_name("circle")
# print(menu.text)
menucircle.click()
time.sleep(3)
lout = driver.find_element_by_class_name("log")
lout.click()

link=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.LINK_TEXT,"Log In")))
link.click()    
log = driver.find_element_by_tag_name("h1")

if log.text == "Login":
    tcpass += 1
    print("Test case 9: Logout 2 Sucessful")
    tcpass += 1
    print("Test case 10: Navigation to Home page Successful")
    tcpass += 1
    print("Test case 11: Navigation to Login page Successful")
else:
    tcfail += 1
    print("Test case 9: Logout 2 Failed")
    tcfail += 1
    print("Test case 10: Navigation to Home page Failed")
    tcfail += 1
    print("Test case 11: Navigation to Login Page Failed ")

print()
print("Total Number of testcases passed: ",tcpass)
print("Total Number of testcases failed: ",tcfail)
print("Total Number of testcases: ",totcse)
# menucircleopen = driver.find_element_by_class_name("circle open")

# reserve = driver.find_element_by_xpath("//html/body/div/div/div/a/Reservations")
# reserve = driver.find_element_by_id('2')
# reserve.click()

# reserv = menucircleopen.find_elements_by_link_text("Reservations")
# reserv.click()

# opts = menucircleopen.find_elements_by_tag_name("a")

# for opt in opts:
#     print(opt.text)

# print(reserve.text)
time.sleep(5)

# driver.quit() #toclose the browser