from tkinter import *
import tkinter as tk
from pandas import *
import re
import requests
import math
from bs4 import BeautifulSoup
import urllib
import selenium
from io import StringIO
from pdfminer3.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer3.converter import TextConverter
from pdfminer3.layout import LAParams
from pdfminer3.pdfpage import PDFPage
username = ""
password = ""


# Setup to read a webpage
# does not work yet

# def webtotxt():
headers = {
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}
login_data = {
'return_url' : '/clinkhome.cfm?',
'loginusername' : '$username',
'loginpassword' : '$password',
'Login': 'Login'
}
with requests.session() as s:
    requrl = "https://clink.healthgrades.com/"
    req = s.get(requrl, headers=headers)
    print(req.content)
    soupt = BeautifulSoup(req.content, 'html.parser')
    login_data[Login] = soupt.find('login_form')['value']
    req = s.post(requrl, data=login_data, headers=headers)

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
