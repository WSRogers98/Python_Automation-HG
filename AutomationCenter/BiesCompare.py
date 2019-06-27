from tkinter import *
import tkinter as tk
from pandas import *
import re
import requests
import math
from bs4 import BeautifulSoup
import urllib
from io import StringIO
from pdfminer3.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer3.converter import TextConverter
from pdfminer3.layout import LAParams
from pdfminer3.pdfpage import PDFPage
username = ""
password = ""
clinkurl = ""


# Setup to read a webpage
# does not work yet

# def webtotxt():
post = "https://clink.healthgrades.com/executelogin.cfm"
headers = {
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}
login_data = {
'return_url' : '/clinkhome.cfm?',
'loginusername' : 'DummyUsr', # replace with username
'loginpassword' : 'DummyPass', #replace with password
 'Login': 'Login'
}
with requests.Session() as s:
    r = s.post(post, data=login_data)
    print(r.content)
    r = s.get("https://clink.healthgrades.com/clinkhome.cfm?")
    soup = BeautifulSoup(r.content, features="lxml")
    print(soup.title.text)
    print(r.content)
    r = s.get("https://clink.healthgrades.com/clinkcounts/view.cfm?id=642025931735107374138627") #replace with Clink URL
    print(r.content)

# with requests.session() as s:
#   requrl = "https://clink.healthgrades.com/"
#  req = s.get(requrl, headers=headers)
# print(req.content)
# soupt = BeautifulSoup(req.content, 'html.parser')
# login_data["Login"] = soupt.find('input', attrs={'name': "Login"})['value']
# req = s.post(requrl, data=login_data, headers=headers)
# print(req.content)

# url = "https://clink.healthgrades.com/clinkcounts/view.cfm?id=642025931735107374138627"
# html = urllib.request.urlopen(url).read()
# soup = BeautifulSoup(html, features='html.parser')

# for script in soup(["script", "style"]):
    # script.extract()
# text = soup.get_text()
# lines = (line.strip() for line in text.splitlines())
# chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# text = '\n'.join(chunk for chunk in chunks if chunk)
    # test print
# print(text)
