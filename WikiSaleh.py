import os
from pyfiglet import Figlet
import requests
import re
f = Figlet()
print(f.renderText("WikISaleh"))
print("1.Figlet Text")
print("2.Url Shorter")
print("3.Sms Bomber")
print("4.Calculator")
select=input("Select Operation ---> ")
if select=="1":
	text=input("Enter Text ---> ")
	fig=Figlet()
	print(fig.renderText(text))
elif select=="2":
	link=input("Enter Site Link ---> ")
	url= "https://cleanuri.com/api/v1/shorten"
	job= {'url': link}
	urlshort= requests.post(url, data = job)
	print(urlshort.text)
elif select=="3":
	os.system("python3 Data/smsbomber.py")
elif select=="4":
	os.system("python3 Data/Calculator.py")
