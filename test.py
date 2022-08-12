import csv
import datetime
import time

def winput(title, sentence):
    import tkinter as tk
    from tkinter import simpledialog
    tk.Tk().withdraw()
    y = simpledialog.askinteger(title, sentence)
    return y

sn1 = winput("Handle Scanning Sequence", "Scan Barcode 1")
print(sn1)

def winput(title, sentence):
    import tkinter as tk
    from tkinter import simpledialog
    tk.Tk().withdraw()
    y = simpledialog.askinteger(title, sentence)
    return y
sn2 = winput("Handle Scanning Sequence", "Scan Barcode 2")
print(sn2)
def winput(title, sentence):
    import tkinter as tk
    from tkinter import simpledialog
    tk.Tk().withdraw()
    y = simpledialog.askinteger(title, sentence)
    return y
sn3 = winput("Handle Scanning Sequence", "Scan Barcode 3")
print(sn3)
def winput(title, sentence):
    import tkinter as tk
    from tkinter import simpledialog
    tk.Tk().withdraw()
    y = simpledialog.askinteger(title, sentence)
    return y
sn4 = winput("Handle Scanning Sequence", "Scan Barcode 4")
print(sn4)
def winput(title, sentence):
    import tkinter as tk
    from tkinter import simpledialog
    tk.Tk().withdraw()
    y = simpledialog.askinteger(title, sentence)
    return y
sn5 = winput("Handle Scanning Sequence", "Scan Barcode 5")
print(sn5)
def winput(title, sentence):
    import tkinter as tk
    from tkinter import simpledialog
    tk.Tk().withdraw()
    y = simpledialog.askinteger(title, sentence)
    return y
sn6 = winput("Handle Scanning Sequence", "Scan Barcode 6")
print(sn6)
def winput(title, sentence):
    import tkinter as tk
    from tkinter import simpledialog
    tk.Tk().withdraw()
    y = simpledialog.askinteger(title, sentence)
    return y

with open('C:/Users/15754/PycharmProjects//Barcode/test.csv', mode='a') as csv_file:
    fieldnames = ['SN', 'Time', 'Data', 'File Location']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'SN': sn1, 'Time': 'TBD', 'Data': 'TBD', 'File Location': 'TBD'})
    writer.writerow({'SN': sn2, 'Time': 'TBD', 'Data': 'TBD', 'File Location': 'TBD'})
    writer.writerow({'SN': sn3, 'Time': 'TBD', 'Data': 'TBD', 'File Location': 'TBD'})
    writer.writerow({'SN': sn4, 'Time': 'TBD', 'Data': 'TBD', 'File Location': 'TBD'})
    writer.writerow({'SN': sn5, 'Time': 'TBD', 'Data': 'TBD', 'File Location': 'TBD'})
    writer.writerow({'SN': sn6, 'Time': 'TBD', 'Data': 'TBD', 'File Location': 'TBD'})




