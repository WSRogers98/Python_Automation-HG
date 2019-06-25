from tkinter import *
import tkinter as tk
from pandas import *
import re
import math
from beautifulsoup4 import *
import urllib5
from htmltopdf import *
from io import StringIO
from pdfminer3.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer3.converter import TextConverter
from pdfminer3.layout import LAParams
from pdfminer3.pdfpage import PDFPage


# Setup to read a webpage
url = "https://www.healthgrades.com/"
html = urllib5.urlopen(url).read()
soup = BeautifulSoup(html)

for script in soup(["script", "style"]):
    script.extract()
text = soup.get_text()
lines = (line.strip() for line in text.splitlines())
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
text = '\n'.join(chunk for chunk in chunks if chunk)

# test print
print(text)
