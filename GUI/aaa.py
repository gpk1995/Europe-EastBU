from tkinter import *
import pandas as pd

data = pd.read_excel('C:\\Users\\user\\Desktop\\store-dataset.xlsx')

root = Tk()

Month = list(range(1,13))#{'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}
Year = [2014,2015,2016,2017]

yearLabel = Label(root,text='Select Year')
yearLabel.pack()

year = StringVar(root)
year.set(2014)
yearDropdown = OptionMenu(root,year,*Year)
yearDropdown.pack()
year.trace("w", getYear())

def getYear(*args):
    print(year.get())
    print(type(year.get()))
    print(yearDropdown)
    #return year.get()
     
def getMonth(*args):
    print(month.get())
    print(type(month.get()))
    print(monthDropdown)
    #return month.get()
# =============================================================================

monthLabel = Label(root,text='Select Month')
monthLabel.pack()
month = StringVar(root)
month.set(1)
monthDropdown = OptionMenu(root,month,*Month)
monthDropdown.pack()
month.trace("w",getMonth())

root.mainloop()
