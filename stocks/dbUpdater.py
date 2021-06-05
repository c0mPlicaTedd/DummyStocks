
## This code is meant to be run 24x7 as it updates the price of the stocks in realtime. Can turn this code off once the market working hours are over.


from selenium import webdriver
from dbHandler import update
from datetime import datetime
from datetime import date


option = webdriver.ChromeOptions()
option.add_argument('headless')
browser = webdriver.Chrome('C:\\Users\Jash\Downloads\chromedriver_win32\chromedriver.exe',options=option)


now = datetime.now()
current_time = now.strftime("%H:%M:%S")
opening_time = now.replace(hour=9, minute=0, second=0, microsecond=0)
closing_time = now.replace(hour=15, minute=30, second=0, microsecond=0)
day = date.today().strftime("%A")

if (str(current_time)>str(opening_time) and current_time<closing_time and day != "Saturday" and day!="Sunday" ):
    f= open("C:\\Users\Jash\DummyStocks\stocks\stocknames.txt",'r')
    for line in f: #automated updates
        shortname = line
        url = "https://www.google.com/search?q=NSE:"+shortname
        browser.get(url)
        price = browser.find_element_by_xpath("/html/body/div[7]/div/div[9]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/g-card-section/div/g-card-section/div[2]/div[1]/span[1]/span/span[1]").text
        price = price.replace(",",'')
        price = float(price)
        movement = browser.find_element_by_xpath("/html/body/div[7]/div/div[9]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/g-card-section/div/g-card-section/div[2]/div[1]/span[2]/span[1]").text 
        movement = movement.replace(",","")
        percentage = browser.find_element_by_xpath("/html/body/div[7]/div/div[9]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/g-card-section/div/g-card-section/div[2]/div[1]/span[2]/span[2]/span[1]").text
        percentage = percentage.replace("(","")
        percentage = percentage.replace(")","")
        
        update(shortname.rstrip("\n"),price,movement,percentage)
        c = c+1
        print(c)
    f.close()

else:
    print("The market working hours are over")






