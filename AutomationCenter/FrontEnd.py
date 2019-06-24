#!/usr/bin/env python
# imports
import re
from io import StringIO
from pdfminer3.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer3.converter import TextConverter
from pdfminer3.layout import LAParams
from pdfminer3.pdfpage import PDFPage
from DearNeighbor import main1
from NameOnPage import main2
from tkinter import filedialog
from tkinter import *
from functools import partial
import tkinter as tk


# Program by Will Rogers
# Enjoy my spaghetti code


# Global Variables
helpwindow = tk
bugwindow = tk
window = tk.Tk()
v = tk.IntVar()
quitb = Button
helpb = Button
lrcorner = Frame
llcorner = Frame
# Menu Buttons/Variables
direct = None
email = None
bies = None
# Radio Buttons
DirectButton0 = Radiobutton
DirectButton1 = Radiobutton
EmailButton0 = Radiobutton
EmailButton1 = Radiobutton
BiesButton0 = Radiobutton
BiesButton1 = Radiobutton
# Direct mail automation buttons/Variables
BoolNeighbor = None
BoolName = None
Neighbor0 = Button
Neighbor1 = Button
Name0 = Button
Name1 = Button
runButton = Button
boolRun = None
# PDF/TXT Search Variables/Buttons
txt0 = ""
txt1 = ""
pdf0 = ""
pdf1 = ""
Booltxt0 = None
Booltxt1 = None
Boolpdf0 = None
Boolpdf1 = None
warning = Label
pdfDis = Label
txtDis = Label
Boolwarning = None
# Functions


def submit():
    if BoolNeighbor:
        main1(txt0, pdf0)
    if BoolName:
        main2(txt1, pdf1)


def checker():
    global Booltxt0
    global Boolpdf0
    global BoolNeighbor
    global BoolName
    global Boolpdf1
    global Booltxt1
    global warning
    global Boolwarning
    global pdfDis
    global txtDis
    global runButton
    global boolRun
    
    if BoolNeighbor:
        if Boolpdf0 and Booltxt0:
            warning.pack_forget()
            if boolRun:
                runButton.destroy()
                boolRun = False
            runButton = Button(window, text="Run Test", command=partial(submit))
            runButton.pack()
            boolRun = True
        elif not Boolpdf0:
            if Boolwarning:
                warning.pack_forget()
                Boolwarning = False
            if boolRun:
                runButton.destroy()
                boolRun = False
            warning = Label(window, text="Missing .pdf file, please upload it.", fg="red")
            warning.pack()
            Boolwarning = True
        elif not Booltxt0:
            if Boolwarning:
                warning.pack_forget()
                Boolwarning = False
            if boolRun:
                runButton.destroy()
                boolRun = False
            warning = Label(window, text="Missing .txt file, please upload it.", fg="red")
            warning.pack()
            Boolwarning = True
    if BoolName:
        if Boolpdf1 and Booltxt1:
            warning.pack_forget()
            if boolRun:
                runButton.destroy()
                boolRun = False
            runButton = Button(window, text="Run Test", command=partial(submit))
            runButton.pack()
            boolRun = True
        elif not Boolpdf1:
            if Boolwarning:
                warning.pack_forget()
                Boolwarning = False
            if boolRun:
                runButton.destroy()
                boolRun = False
            warning = Label(window, text="Missing .pdf file, please upload it.", fg="red")
            warning.pack()
            Boolwarning = True

        elif not Booltxt1:
            if Boolwarning:
                warning.pack_forget()
                Boolwarning = False
            if boolRun:
                runButton.destroy()
                boolRun = False
            warning = Label(window, text="Missing .txt file, please upload it.", fg="red")
            warning.pack()
            Boolwarning = True


def pdfsearch0():
    global pdf0
    global Boolpdf0
    global Booltxt0
    global pdfDis
    global txtDis
    global warning
    global Boolwarning
    global boolRun
    
    window.fileName = filedialog.askopenfilename(initialdir="/", title="Select a pdf File", filetypes=[("pdf files", "*.pdf")])
    pdf0 = window.fileName
    if Boolpdf0:
        warning.pack_forget()
        pdfDis.destroy()
        Boolpdf0 = False
    if boolRun:
        runButton.destroy()
        boolRun = False
    if pdf0 != "":
        Boolpdf0 = True
        pdfDis = Label(window, text=".pdf= "+pdf0)
        pdfDis.pack()
        checker()


def pdfsearch1():
    global pdf1
    global Boolpdf1
    global Booltxt1
    global pdfDis
    global txtDis
    global warning
    global Boolwarning
    global boolRun

    window.fileName = filedialog.askopenfilename(initialdir="/", title="Select a pdf File", filetypes=[("pdf files", "*.pdf")])
    pdf1 = window.fileName
    if Boolpdf1:
        warning.pack_forget()
        pdfDis.destroy()
        Boolpdf1 = False
    if boolRun:
        runButton.destroy()
        boolRun = False
    if pdf1 != "":
        Boolpdf1 = True
        pdfDis = Label(window, text=".pdf= "+pdf1)
        pdfDis.pack()
        checker()


def txtsearch0():
    global txt0
    global Boolpdf0
    global Booltxt0
    global pdfDis
    global txtDis
    global warning
    global Boolwarning
    global boolRun

    window.fileName = filedialog.askopenfilename(initialdir="/", title="Select a txt File", filetypes=[("txt files", "*.txt")])
    txt0 = window.fileName
    if Booltxt0:
        txtDis.destroy()
        Booltxt0 = False
    if boolRun:
        runButton.destroy()
        boolRun = False
    if txt0 != "":
        warning.pack_forget()
        Booltxt0 = True
        txtDis = Label(window, text=".txt= "+txt0)
        txtDis.pack()
        checker()


def txtsearch1():
    global txt1
    global Boolpdf1
    global Booltxt1
    global Boolpdf0
    global Booltxt0
    global pdfDis
    global txtDis
    global warning
    global Boolwarning
    global boolRun

    window.fileName = filedialog.askopenfilename(initialdir="/", title="Select a txt File", filetypes=[("txt files", "*.txt")])
    txt1 = window.fileName
    if Booltxt1:
        warning.pack_forget()
        txtDis.destroy()
        Booltxt1 = False
    if txt1 != "":
        Booltxt1 = True
        txtDis = Label(window, text=".txt= "+txt1)
        txtDis.pack()
        checker()


def neighbortest():
    global BoolNeighbor
    global Neighbor0
    global Neighbor1
    global BoolName
    global Name0
    global Name1
    global boolRun
    global Boolpdf1
    global Booltxt1
    global Boolpdf0
    global Booltxt0

    if BoolNeighbor:
        Neighbor0.destroy()
        Neighbor1.destroy()
        BoolNeighbor = False
        if boolRun:
            runButton.destroy()
            boolRun = False
    if BoolName:
        Name0.destroy()
        Name1.destroy()
        BoolName = False
        if boolRun:
            runButton.destroy()
            boolRun = False
    if not BoolNeighbor:
        BoolNeighbor = True
        if boolRun:
            runButton.destroy()
            boolRun = False
        Neighbor0 = Button(window, text="Upload PDF", command=partial(pdfsearch0))
        Neighbor1 = Button(window, text="Upload TXT", command=partial(txtsearch0))
        Neighbor0.pack()
        Neighbor1.pack()


def nameonpagetest():
    global BoolNeighbor
    global Neighbor0
    global Neighbor1
    global BoolName
    global Name0
    global Name1
    global boolRun
    global Boolpdf1
    global Booltxt1
    global Boolpdf0
    global Booltxt0

    if BoolNeighbor:
        Neighbor0.destroy()
        Neighbor1.destroy()
        BoolNeighbor = False
        if boolRun:
            runButton.destroy()
            boolRun = False
    if BoolName:
        Name0.destroy()
        Name1.destroy()
        BoolName = False
        if boolRun:
            runButton.destroy()
            boolRun = False
    if not BoolName:
        if boolRun:
            runButton.destroy()
            boolRun = False
        Name0 = Button(window, text="Upload PDF", command=partial(pdfsearch1))
        Name1 = Button(window, text="Upload TXT", command=partial(txtsearch1))
        Name0.pack()
        Name1.pack()
        BoolName = True


def directfunction():
    global direct
    global email
    global bies
    global EmailButton0
    global EmailButton1
    global DirectButton0
    global DirectButton1
    global BiesButton0
    global BiesButton1
    global BoolNeighbor
    global BoolName
    global Neighbor0
    global Neighbor1
    global Name0
    global Name1

    if not direct:
        if bies:
            BiesButton0.destroy()
            BiesButton1.destroy()
            bies = False
        if email:
            EmailButton0.destroy()
            EmailButton1.destroy()
            email = False
        DirectButton0 = Radiobutton(window, variable=v, value=0, text="Dear Neighbor", command=partial(neighbortest))
        DirectButton1 = Radiobutton(window, variable=v, value=1, text="Name On Page", command=partial(nameonpagetest))
        DirectButton0.pack()
        DirectButton1.pack()
        direct = True
    else:
        if BoolNeighbor:
            Neighbor0.destroy()
            Neighbor1.destroy()
            BoolNeighbor = False
        if BoolName:
            Name0.pack_forget()
            Name1.pack_forget()
            BoolName = False
        direct = False
        DirectButton0.destroy()
        DirectButton1.destroy()
        DirectButton0 = Radiobutton(window, variable=v, value=0, text="Dear Neighbor", command=partial(neighbortest))
        DirectButton1 = Radiobutton(window, variable=v, value=1, text="Name On Page", command=partial(nameonpagetest))
        DirectButton0.pack()
        DirectButton1.pack()
        direct = True


def emailfunction():
    global direct
    global email
    global bies
    global EmailButton0
    global EmailButton1
    global DirectButton0
    global DirectButton1
    global BiesButton0
    global BiesButton1
    global BoolNeighbor
    global BoolName
    global Neighbor0
    global Neighbor1
    global Name0
    global Name1
    global boolRun
    global Boolpdf1
    global Booltxt1
    global Boolpdf0
    global Booltxt0

    if not email:
        if direct:
            DirectButton0.destroy()
            DirectButton1.destroy()
            if BoolNeighbor:
                Neighbor0.destroy()
                Neighbor1.destroy()
                BoolNeighbor = False
            if BoolName:
                Name0.pack_forget()
                Name1.pack_forget()
                BoolName = False
            direct = False
            if Boolpdf1:
                warning.pack_forget()
                pdfDis.destroy()
                Boolpdf1 = False
            if Boolpdf0:
                warning.pack_forget()
                pdfDis.destroy()
                Boolpdf0 = False
            if boolRun:
                runButton.destroy()
                boolRun = False
            if Booltxt0:
                txtDis.destroy()
                Booltxt0 = False
                if Booltxt1:
                    txtDis.destroy()
                    Booltxt1 = False
        if bies:
            BiesButton0.destroy()
            BiesButton1.destroy()
            bies = False
        EmailButton0 = Radiobutton(window, variable=v, value=2, text="Placeholder 0")
        EmailButton1 = Radiobutton(window, variable=v, value=3, text="Placeholder 1")
        EmailButton0.pack()
        EmailButton1.pack()
        email = True
    else:
        email = False
        EmailButton0.destroy()
        EmailButton1.destroy()
        EmailButton0 = Radiobutton(window, variable=v, value=2, text="Placeholder 0")
        EmailButton1 = Radiobutton(window, variable=v, value=3, text="Placeholder 1")
        EmailButton0.pack()
        EmailButton1.pack()
        email = True


def biesfunction():
    global direct
    global email
    global bies
    global EmailButton0
    global EmailButton1
    global DirectButton0
    global DirectButton1
    global BiesButton0
    global BiesButton1
    global BoolName
    global BoolNeighbor
    global Neighbor0
    global Neighbor1
    global Name0
    global Name1
    global boolRun
    global Boolpdf1
    global Booltxt1
    global Boolpdf0
    global Booltxt0

    if not bies:
        if email:
            EmailButton0.destroy()
            EmailButton1.destroy()
            email = False
        if direct:
            DirectButton0.destroy()
            DirectButton1.destroy()
            if BoolNeighbor:
                Neighbor0.destroy()
                Neighbor1.destroy()
                BoolNeighbor = False
            if BoolName:
                Name0.pack_forget()
                Name1.pack_forget()
                BoolName = False
            if Boolpdf1:
                warning.pack_forget()
                pdfDis.destroy()
                Boolpdf1 = False
            if Boolpdf0:
                warning.pack_forget()
                pdfDis.destroy()
                Boolpdf0 = False
            if boolRun:
                runButton.destroy()
                boolRun = False
            if Booltxt0:
                txtDis.destroy()
                Booltxt0 = False
                if Booltxt1:
                    txtDis.destroy()
                    Booltxt1 = False
            direct = False
        BiesButton0 = Radiobutton(window, variable=v, value=2, text="Placeholder 2")
        BiesButton1 = Radiobutton(window, variable=v, value=3, text="Placeholder 3")
        BiesButton0.pack()
        BiesButton1.pack()
        bies = True
    else:
        bies = False
        BiesButton0.destroy()
        BiesButton1.destroy()
        BiesButton0 = Radiobutton(window, variable=v, value=2, text="Placeholder 2")
        BiesButton1 = Radiobutton(window, variable=v, value=3, text="Placeholder 3")
        BiesButton0.pack()
        BiesButton1.pack()
        bies = True

# Main


def exitbugs():
    bugwindow.destroy()


def knownbugs():
    global bugwindow
    bugwindow = tk.Toplevel(window)
    Label(bugwindow, text="Below is a list of known bugs",  wraplength=599). grid(row=0, column=0)
    Label(bugwindow, text="Please email will.rogers@healthgrades.com if you find any more bugs or have a fix for some.", wraplength=599).grid(row=1, column=0)
    Label(bugwindow, text="• If you need to change the file you are uploading or change the QA, sometimes the text from the text from the previous upload or QA will  still display. if that happens, the program will still work and you just have to ignore the text or previous button.", wraplength=599, justify=LEFT, anchor=W).grid(row=2, column=0)
    Label(bugwindow, text="• If the Direct Mail QA is too long, the results can be cut off at the bottom of the screen", wraplength=599, justify=LEFT, anchor=W).grid(row=3, column=0)
    Button(bugwindow, text="Exit", command=partial(exitbugs)).grid(row=4, column=0)


def exitprogram():
    helpwindow.destroy()


def helpme():
    global helpwindow
    helpwindow = tk.Toplevel(window)
    helpwindow.title("Help Menu")
    Label(helpwindow, text="Welcome to the Healthgrades AutomationCenter 0.2", wraplength=599, justify=LEFT, anchor=W).grid(row=0, column=0)
    Label(helpwindow, text="This program was created by William Rogers, a quality assurance intern.", wraplength=599, justify=LEFT, anchor=W).grid(row=1, column=0)
    Label(helpwindow, text=" ", wraplength=599, justify=LEFT, anchor=W).grid(row=2, column=0)
    Label(helpwindow, text="• While this intern has never made a GUI before, has never used Python and barely knows how this works, he will do his best to walk you through it in this help section.", wraplength=599, justify=LEFT, anchor=W).grid(row=3, column=0)
    Label(helpwindow, text="• To get started, use the dropdown menu to select what QA type you are doing. Currently, only automation for DirectMail is available.", wraplength=599, justify=LEFT, anchor=W).grid(row=5, column=0)
    Label(helpwindow, text="• This will then present you with the buttons to select what autmation you need for this QA. If the button appears clicked when you first see the option you still have to click it again.", wraplength=599, justify=LEFT, anchor=W).grid(row=7, column=0)
    Label(helpwindow, text="• You will then be presented with buttons to upload the files needed for this QA automation. Please upload all files asked for in order to continue.", wraplength=599, justify=LEFT, anchor=W).grid(row=9, column=0)
    Label(helpwindow, text="• All that is left is to hit the submit button and the automation will do the work for you! If you are having troble reading the results, be sure to put the window in full screen.", wraplength=599, justify=LEFT, anchor=W).grid(row=10, column=0)
    Label(helpwindow, text=" ", wraplength=599, justify=LEFT, anchor=W).grid(row=11, column=0)
    Label(helpwindow, text="Thank you for using my program :)", wraplength=599, justify=CENTER, anchor=N).grid(row=12, column=0)
    Button(helpwindow, text="Known Bugs", command=partial(knownbugs)).grid(row=13, column=0)
    Button(helpwindow, text="Exit", command=partial(exitprogram)).grid(row=14, column=0)


def quitprogram():
    window.destroy()


window.geometry("600x450")
window.title("AutomationCenter for HealthGrades 0.2")
Label(window, text="AutomationCenter").pack()
Label(window, text="By Will Rogers").pack()
Label(window, text="Select the Automation you would Like:").pack()

mb = Menubutton(window, text="QA type")
mb.menu = Menu(mb)
mb["menu"] = mb.menu
mb.menu.add_command(label="DirectMail", command=partial(directfunction))
mb.menu.add_command(label="Email", command=partial(emailfunction))
mb.menu.add_command(label="BIES", command=partial(biesfunction))
mb.pack()

lrcorner = Frame(padx=0, pady=0)
llcorner = Frame(padx=0, pady=0)
lrcorner.pack(side="left", expand=True)
llcorner.pack(side="right", expand=True)
quitb = Button(llcorner, text="Quit", anchor=SW, command=partial(quitprogram))
helpb = Button(lrcorner, text="Help", anchor=SE, command=partial(helpme))
quitb.pack()
helpb.pack()

window.mainloop()
