#from FrontEnd import *
#import FrontEnd as f
import re
from tkinter import *
import tkinter as tk
from io import StringIO
from pdfminer3.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer3.converter import TextConverter
from pdfminer3.layout import LAParams
from pdfminer3.pdfpage import PDFPage

txt10 = ""
pdf10 = ""
resultwindow = tk


def convert(fname):
    global txt10
    global pdf10
    pages = None
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = open(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close()
    return text


def write_to_text():

    global txt10
    global pdf10

    text_file = open("Output_1.txt", "w")
    text = re.sub("\s\s+", " ", convert(pdf10))
    text_file.write("%s" % text.encode("utf-8"))
    text_file.close()


def pdf_records_file():

    global txt10
    global pdf10

    text = convert(pdf10)

    regex = re.compile(
        r'(\d{1}.*) *\n(.*) *\n([A-Z]{1}[a-z]+) ([A-Z]{1}[a-z]+.*?) *\n(PO Box )?(\d{1,4}?.*?) *\n(\w+)(.*)')

    txt = regex.findall(text)
    new_txt = [tuple(filter(None, i))for i in txt]
    f1 = open('output_pdf.txt', 'w')
    count = 0
    list_0 = []
    list_1 = []
    list_2 = []
    list_3 = []
    for x in new_txt:
        list_0.append("Record #" + str(count + 1))
        name = ' '.join(map(str, x[2:4]))
        address_1 = ' '.join(map(str, x[4:-2]))
        address_2 = ' '.join(map(str, x[-2:]))
        list_1.append(address_1.replace("  ", " "))
        list_2.append(name.replace("  ", " ").strip('\n'))
        list_3.append(address_2.replace("  ", " ").replace(" ,", ",").strip(' '))
        count += 1
    temp_1 = {}
    for w, x, y, z in zip(list_0, list_2, list_1, list_3):
        temp_1.setdefault(w, []).append(x)
        temp_1.setdefault(w, []).append(y)
        temp_1.setdefault(w, []).append(z)
    f1.close()
    return temp_1


def records_in_text_file():

    global txt10
    global pdf10

    f = open(txt10, 'r')
    f1 = open('output_text.txt', 'w')
    count = 0
    list_0 = []
    list_1 = []
    list_2 = []
    list_3 = []
    list_4 = []
    list_5 = []
    list_6 = []
    list_7 = []

    for line in f:
        list_0.append("Record #" + str(count + 1))

        if "first = " in line:
            list_1.append(line.strip('first = ').strip('\n').replace('\"', '').replace("  ", " "))

        if "last = " in line:
            list_2.append(line.strip('last = ').strip('\n').replace('\"', '').replace("  ", " "))

        if "suffix = " in line:
            list_3.append(line.strip('suffix = ').strip('\n').replace('\"', '').replace("  ", " "))

        if "address = " in line:
            list_4.append(line.strip('address = ').strip('\n').replace('\"', '').replace("  ", " "))

        if "city = " in line:
            list_5.append(line.strip('city = ').strip('\n').replace('\"', '').replace("  ", " ").strip(' '))

        if " st = " in line:
            list_6.append(line.strip('st = ').strip('\n').replace('\"', '').replace("  ", " ").strip(' '))

        if "zip = " in line:
            list_7.append(line.strip('zip = ').strip('\n').replace('\"', '').replace("  ", " ").strip(' '))
        count += 1

    full_name = [a+" "+b for a, b in zip(list_1, list_2)]
    state_city_zip = [a+", "+b+" "+c for a, b, c in zip(list_5, list_6, list_7)]

    temp_2 = {}
    for v, w, x, y, z in zip(list_0, full_name, list_3, list_4, state_city_zip):
        temp_2.setdefault(v, []).append(w)
        temp_2.setdefault(v, []).append(x)
        temp_2.setdefault(v, []).append(y)
        temp_2.setdefault(v, []).append(z)

    for k in temp_2:
        if temp_2[k][1] == '<not set>':
            del temp_2[k][1]
        else:
            temp_2[k][0] = str(temp_2[k][0] + ", " + temp_2[k][1])
            del temp_2[k][1]

    return temp_2


def main2(textinput, pdfinput):
    #start_time = time.time()
    global resultwindow
    global txt10
    global pdf10
    txt10 = textinput
    pdf10 = pdfinput
    pdf_dict = pdf_records_file()
    text_dict = records_in_text_file()
    different = set()
    count = 0
    count1 = 0
    resultwindow = tk.Tk()
    resultwindow.title("Results")
    for key in sorted(set(pdf_dict.keys()) & set(text_dict.keys())):
        pdf_value = [x.upper() for x in pdf_dict[key]]
        text_value = [x.upper() for x in text_dict[key]]
        if pdf_value == text_value:
            count += 1
            # print()
            Label(resultwindow, text=key + " from pdf file " + str(pdf_dict[key])).grid(row=count1, column=0)
            Label(resultwindow, text="MATCHED", fg="green").grid(row=count1, column=1)
            Label(resultwindow, text=key + " from text file " + str(text_dict[key])).grid(row=count1, column=2)
            # print(key, "from pdf file", pdf_dict[key], colored("MATCHED", 'green', attrs=['bold']), key, "from text file"+text_dict[key])
            # print()
            count1 += 1
        else:
            different.add(key)
            Label(resultwindow, text=key + " from pdf file " + str(pdf_dict[key])).grid(row=count1, column=0)
            Label(resultwindow, text="DID NOT MATCH", fg="red").grid(row=count1, column=1)
            Label(resultwindow, text=key + " from text file " + str(text_dict[key])).grid(row=count1, column=2)
            # print(key, "from pdf file", pdf_dict[key], colored("DID NOT MATCH", 'red', attrs=['bold']), key, "from text file", text_dict[key])
            # print()
            count1 += 1

    # print()
    Label(resultwindow, text="The number of records matched = ").grid(row=count1, column=0)
    Label(resultwindow, text=count, fg="blue").grid(row=count1+1, column=1)
    # print("The number of records matched = ", colored(count, 'yellow', attrs=['bold']))
    # print()
    # print("Total time taken = ", colored(" %s seconds", 'yellow') % (time.time() - start_time))
    # write_to_text()


