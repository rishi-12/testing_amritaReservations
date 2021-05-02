from selenium import webdriver
from selenium.webdriver.common.keys import Keys #to type something in search in bar
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

tcpass=0
tcfail =0
totcse = 10

PATH="E:\Selenium\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("http://localhost:3000/reserve")

print(driver.title)

try:
    rev = driver.find_element_by_tag_name("h1")
    if rev.text == "Make a Reservation":
        tcpass += 1
        print("Test case 1: Navigation Successful to Reservation page")
    else:
        tcfail += 1
        print("Test case 1: Navigation failed to Reservation page")
    # print(tcpass)
    # print("************")
    roomtype = driver.find_element_by_id("first")
    roomtype.send_keys("Lab")
    
    # print(roomtype.text)
    # print("************")
    time.sleep(2)
    roomcapacity = driver.find_element_by_id("last")
    roomcapacity.send_keys("65")
    # print(roomcapacity.text)
    # print("************")
    time.sleep(2)
    slot = driver.find_element_by_name("second")
    slot.send_keys("Second")
    
    # print(slot.text)
    # print("************")
    time.sleep(2)
    date1 = driver.find_element_by_id("when")
    date1.send_keys("04-04-2021")
    
    # print(date1.text)
    # print("************")
    time.sleep(2)
    reservebutton = WebDriverWait(driver,2).until(
        EC.presence_of_element_located((By.ID, "button-reserve"))
    )
    reservebutton.click()
    
    cards = driver.find_elements_by_class_name("card")
    f1=0
    f2=0
    f3=0
    f4=0
    f=0
    for card in cards:
        # req = card.find_element_by_tag_name("h1")
        # typ = card.find_elements_by_tag_name("h2")
        s=card.text.split("\n")
        # print(s)
        f1=0
        f2=0
        f3=0
        f4=0
        for i in range(len(s)):
            b=s[i].split()
            if(b[0]=="TYPE:"):
                if(b[1]=="Lab"):
                    f1=1
                    
                    
            if(b[0]=="SLOT"):
                if(b[1]=="2"):
                    f2=1
                    
                    
                
            if(b[0]=="DATE"):
                if(b[1]=="2021-04-04"):
                    f3=1
                    
            if(b[0]=="CAPACITY"):
                if(b[1]=="65"):
                    f4=1
                    
        if(f1==1 and f2==1 and f3==1 and f4==1):
            # print("True")
            tcpass += 4
            print("Test case 2: Selected Labs")
            print("Test case 3: Selected Slot")
            print("Test case 4: Selected Date")
            print("Test case 5: Filled capacity")
            tcpass += 1
            print("Test case 6: Reserved.")
            f=1
            break
        # print("****************")
    if(f==0):
        print("Test case 6: Reserve Failed.")
        tcfail += 1

    # print(tcpass)
    time.sleep(3)
    try:
        occ = driver.find_element_by_link_text("Occupancy chart")
        occ.click()
        pas = driver.find_element_by_id("cl")
        # print(pas.text)
        ps = pas.text.split("\n")
        # print(ps)
        # pas = pas[0]
        # print(pas)
        if(ps[0]=="Pick a FLOOR: "):
            tcpass+=1
            print("Test case 7: Navigated to Occupancy chart")
        else:
            tcfail+=1
            print("Test case 7: Navigation failed to Occupancy chart")
            
        
        time.sleep(3)
        fl = driver.find_element_by_id("movie")
        fl.click()
        # print(fl.text)
        fl.send_keys("GROUND")
        tcpass += 1
        print("Test case 8: Selected Floor")
        dy = driver.find_element_by_id("day")
        dy.click()
        dy.send_keys("Tuesday")
        tcpass += 1
        print("Test case 9: Selected Day")
        # print(dy.text)
        sl = driver.find_element_by_id("slot")
        sl.click()
        sl.send_keys("Second")
        sl.click()
        tcpass += 1
        print("Test case 10: Selected Slot")
        # print(sl.text)
    except:
        tcfail += 1

    print()
    print("Total Number of testcases passed: ",tcpass)
    print("Total Number of testcases failed: ",tcfail)
    print("Total Number of testcases: ",totcse)
except:
    driver.quit()

# driver.quit() #toclose the browser