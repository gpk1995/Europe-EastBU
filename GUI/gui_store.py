from tkinter import *
import pandas as pd

data = pd.read_excel("C:/Users/user/Desktop/store-dataset.xlsx")
global y
global m
global product_list 
product_list = []
global mon
y,m = 2014,'Jan'
SalesReport = Tk()
SalesReport.title("Sales Report")
SalesReport.geometry("800x600")

def option_changed_year(*args):
    print("the user chose the value {}".format(year.get()))
    y = year.get()
    print(y)
    return y
    
year = StringVar()
#year.set('Select the Year')
year.set(2014)
year.trace("w", option_changed_year)
year_widget = OptionMenu(SalesReport, year, '2014', '2015', '2016', '2017')
year_widget.place(relx = 0.35,rely = 0.15)

def option_changed_month(*args):
    print("the user chose the value {}".format(month.get()))
    y = year.get()
    m = month.get()
    mon = 1
    if(True):
        if(m=='Jan'):
            mon = 1
        elif(m=='Feb'):
            mon = 2
        elif(m=='Mar'):
            mon = 3
        elif(m=='Apr'):
            mon = 4
        elif(m=='May'):
            mon = 5
        elif(m=='Jun'):
            mon = 6
        elif(m=='Jul'):
            mon = 7
        elif(m=='Aug'):
            mon = 8
        elif(m=='Sep'):
            mon = 9
        elif(m=='Oct'):
            mon = 10
        elif(m=='Nov'):
            mon = 11
        elif(m=='Dec'):
            mon = 12
    
    y,m = y,mon
    print(y,m)
    product_list = list(data[(data['Order Date'].dt.year==y) & (data['Order Date'].dt.month==m)]['Product Name'])
    print(len(product_list))
    return m

month = StringVar(SalesReport)
#month.set('Select the Month')
month.set('Jan')
month.trace("w", option_changed_month)
month_widget = OptionMenu(SalesReport,month,'Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec',command=option_changed_month(month))
month_widget.place(relx = 0.1,rely = 0.15)



'''y,m = int(y),int(m)
print(y,m)

product_list = list(data[(data['Order Date'].dt.year==y) & (data['Order Date'].dt.month==m)]['Product Name'])
print(product_list)
product = StringVar(SalesReport)
product.set('Select the Product')
product_widget = OptionMenu(SalesReport, product, *product_list)
product_widget.pack()
'''
mainloop()
