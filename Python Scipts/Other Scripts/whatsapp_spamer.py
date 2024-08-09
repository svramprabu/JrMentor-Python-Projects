#it4min
#t.me/LinuxArmy
from selenium import webdriver
import os, time
try:
    import selenium
    print ("selenium install")
except:
    os.system("pip install selenium")
    print("selenium installed")
time.sleep(4)
def cl():
    linux= 'clear'
    windows = 'cls'
    os.system([linux,windows][os.name=='nt'])
cl()
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
driver.maximize_window()
cl()
b = """


 __          ___           _                           _____                       
 \ \        / / |         | |     /\                  / ____|                      
  \ \  /\  / /| |__   __ _| |_   /  \   _ __  _ __   | (___  _ __   __ _ _ __ ___  
   \ \/  \/ / | '_ \ / _` | __| / /\ \ | '_ \| '_ \   \___ \| '_ \ / _` | '_ ` _ \ 
    \  /\  /  | | | | (_| | |_ / ____ \| |_) | |_) |  ____) | |_) | (_| | | | | | |
     \/  \/   |_| |_|\__,_|\__/_/    \_\ .__/| .__/  |_____/| .__/ \__,_|_| |_| |_|
                                       | |   | |            | |                    
                                       |_|   |_|            |_|                    

                    t.me/LinuxArmy
                                   @it4min

"""
print(b)
name = input("[+] Enter name of the group or contcat>>> ")
msg = input("[+] Enter your text>>> ")
count = int(input("[+]Enter the number of messages>>> "))
user= driver.find_element_by_xpath("//span[@title='{}']".format(name))
user.click()
msg_box = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
for index in range(count):
    msg_box.send_keys(msg)
    driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button").click()
    print("Message "+msg+" sent")
msg_box.send_keys('''All messages were sent
                     programmer: @it4min
                     channel: t.me/LinuxArmy''')
driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button").click()
print("Success:)")


#//span[@title=class gp]
#//*[@id="main"]/footer/div[1]/div[2]/div/div[2]
#//*[@id='main']/footer/div[1]/div[3]/button