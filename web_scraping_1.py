from bs4 import BeautifulSoup
import requests
import urllib.request
from urllib.request import Request, urlopen
import re
import dateutil
File= open('File.txt','w')

req = Request("https://www.itaq.nl/vacatures/vacature-senior-app-ontwikkelaar-668487-11.html")
result = urlopen(req).read()
doc = BeautifulSoup(result,'html.parser')
title= doc.find(attrs={'class':'hookItemTitle fhlItemTitle chlItemTitle'})
email= doc.find(attrs={'class':'hookItemWord fhlItemWord chlItemWord chlEmail'})

Name=title.text
Email=email.text

print(Name,Email)

File.write(Name)
File.write(Email)
File.close()
