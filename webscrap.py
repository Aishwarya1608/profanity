import requests
import csv
from bs4 import BeautifulSoup
import time
with open('rates.csv','w') as rates:
    rates.write("Date,Rate\n")
for m in range(8,12):
    for d in range(15,32):
        try:
            response=request.get('https://www.tripadvisor.in/Hotel_Review-g1154299-d2385702-Reviews-Ananth_Residency-Hubli_Dharwad_Dharwad_District_Karnataka.html'+str(m)+'&day='+str(d)+'&year=2015')
            if response.ok:
    soup=BeautifulSoup(response.text)
        except Exception e:
            print e
            time.sleep(.2)
        king=soup.find("table", {"summary":"rooms availiability"}).find("div","room")
        if king.find("div","comfort-room").text.strip()=="King":
            rate=king.find("div","roomAvail").find("div","value").strip() 
            rates.write("2020"+str(m)+"-"+str(d)+","+str(rate)+"\n")
    
