##
#
##
##
#   main user interface b/w user and db (Starbucks Coffee System Ltd.)
##
##
#   blueprint : main window - search coffee, add coffee, lookup customer, make bill,
##

from tkinter import *
from tkinter import ttk
from ttkthemes import themed_tk as tk
import sys,os,sqlite3
from tkinter import messagebox as MsgBox

# (id_d, name_d, flavor_d, price_d)
global c_id
global c_name
global c_flavor
global c_price

global root
global starbucks_bg
starbucks_bg = "#D5EAFF"
try:
    root = Tk()
    root.title("Starbucks Coffee Ltd.")
    root.geometry("500x250")
    root.config(bg = starbucks_bg)
    root.iconbitmap(r'images/starbucks.ico')
    com = sqlite3.connect("starbucks.db")
    cur = com.cursor()
except:
    print("there was a problem, initializing program.")

c_id = IntVar()
c_name = StringVar()
c_flavor = StringVar()
c_price = IntVar()

def about_us():
    print("About_US")

def coffee_search():
    print("coffee seach")
def _addcoffee_final():
    print("reached destination")
    
def add_coffee():
    # (id_d, name_d, flavor_d, price_d)
    _addcoffee = Tk()
    _addL = Label(_addcoffee, text = "Enter details to add new coffee to data")
    _addL.grid(row = 0)
    
    _addL_D = Label(_addcoffee, text = "id: ")
    _addL_D.grid(row = 1, column = 0)
    _addE_D = Entry(_addcoffee, textvariable = c_id)
    _addE_D.grid(row = 1, column = 1)
    
    _addL_N = Label(_addcoffee, text = "name: ")
    _addL_N.grid(row = 2, column = 0)
    _addE_N = Entry(_addcoffee, textvariable = c_name)
    _addE_N.grid(row = 2, column = 1)
    
    _addL_F = Label(_addcoffee, text = "flavor: ")
    _addL_F.grid(row = 3, column = 0)
    _addE_F = Entry(_addcoffee, textvariable = c_flavor)
    _addE_F.grid(row = 3, column = 1)
    
    _addL_P = Label(_addcoffee, text = "price: ")
    _addL_P.grid(row = 4, column = 0)
    _addE_P = Entry(_addcoffee, textvariable = c_price)
    _addE_P.grid(row = 4, column = 1)
    
    _addSubmit = Button(_addcoffee, text = "SUBMIT", command = _addcoffee_final)
    _addSubmit.grid(row = 5)
    
    
def look_customer():
    def ph_clook():
        ph_entry = Entry(_look, textvariable = phone_number_c)
        ph_entry.bind("<return>") # might have issues, refer notes
        ph_entry.pack()
        cur.execute('select c_id, c_name, c_ph, c_usual from customer where c_ph = "{0}"'.format(phone_number_c))
        look_data = cur.fetchall()
        # for no just printing, change later
        print(look_data)
        
    def name_clook():
        nm_entry = Entry(_look, textvariable = name_c)
        nm_entry.bind("<return>") ##############
        nm_entry.pack()
        cur.execute('select c_id, c_name, c_ph, c_usual from customer where c_name = "{0}"'.format(name_c))
        look_data = cur.fetchall()
        print(look_data)
        
    print()
    
    _look = Tk()
    phone_number_c = StringVar()
    name_c = StringVar()
    _look_label = Label(_look, text = "How would you like to search?").pack(side = TOP)
    _look_ph = Button(_look, text = "Phone No.?", command = ph_clook).pack(side = LEFT)
    _look_nm = Button(_look, text = "Name.?", command = name_clook).pack(side = RIGHT)
    # enter details (c_id, c_name, c_ph , c_pay , c_usual)
    
def billing():
    print()

statusbar = ttk.Label(root, text="System Normal", relief=SUNKEN, anchor=W, font='Times 10 italic')
statusbar.grid(row = 3, column = 0)

menubar = Menu(root)
root.config(menu=menubar)

subMenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Exit", command=sys.exit)

subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=subMenu)
subMenu.add_command(label="About Us", command=about_us)




h_logo = PhotoImage(file = "images/Starbucks_Corporation_Logo_2011.png")
sub_hlogo = h_logo.subsample(6,6)
main_image = Label(root, image = sub_hlogo, bg = starbucks_bg)
main_image.grid(row = 1, column = 0)

title_logo = Label(root, text = "Starbucks Corporation (MasterUI) 0.0.1", bg = starbucks_bg)
title_logo.grid(row = 0, column = 2, columnspan = 8)

search_coffee = Button(root, text = "Search Coffee", bg = "blue", fg  = "white", command = coffee_search)
search_coffee.grid(row = 2, column = 2)

add_new_coffee = Button(root, text = "Add Coffee", bg = "blue", fg  = "white", command = add_coffee)
add_new_coffee.grid(row = 2, column = 4)

lookup_customer = Button(root, text = "Search Customer", bg = "blue", fg  = "white", command = look_customer)
lookup_customer.grid(row = 2, column = 6)

make_bill = Button(root, text = "Make Bill", bg = "blue", fg  = "white", command = billing)
make_bill.grid(row = 2, column = 8)

mainloop()
