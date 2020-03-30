# _.UTF8._
# modules
import os, sqlite3,time,sys

# connection.
com = sqlite3.connect("starbucks.db")
cur = com.cursor()

# formalities
print("booting...")
print("loading...",end=None)
time.sleep(2)
print(".....!")
time.sleep(1)
print("welcome to starbucks database creator")
print("author: ayushmaan karmokar")
time.sleep(3)

# declaration for verification of data addition.
global veri
veri = 0

# creation of table
try:
    print("\ntable not created...creating table...")
    cur.execute('create table drinks (id_d int(3), name_d varchar(150), flavor_d varchar(200), price_d int(3))')
    
    cur.execute('create table food (id_f int(3), name_f varchar(150), flavor_f varchar(200), price_f int(3))')
    
    cur.execute('create table athomecoffee (id_h int(3), name_h varchar(150), flavor_h varchar(200), price_h int(3))')
    
    cur.execute('create table customer (c_id int(5), c_name varchar(50), c_ph varchar(10), c_pay varchar(19), c_usual varchar(150))')
except:
    print("\n\ntable already created moving on.. ")

# feeding of table 1
time.sleep(1)
if (True):
    try:
        print("feeding data.. to drinks table")
        cur.execute('insert into drinks (id_d, name_d, flavor_d, price_d) '+
                            'values '+
                            '(001, "Caffe Americano", "water, brewed espresso", 150),'+                
                            '(002, "Caffe Misto", "Brewed Coffee, Milk", 120),'+
                            '(003, "Pike Place Roast", "Brewed Coffee", 99),'+          
                            '(004, "Cappuccino", "Milk, Brewed Espresso", 180),'+                
                            '(005, "Espresso", "Brewed Espresso", 40),'+                
                            '(006, "Flat White", "Milk, Brewed Espresso", 110),'+              
                            '(007, "Smoked Butterscotch Latte", "Milk, Smoked Butterscotch Sauce", 200),'+            
                            '(008, "Caffe Latte", "Milk, Brewed Espresso", 120),'+            
                            '(009, "Caramel Macchiato", "Milk, Brewed Espresso, Vanilla Syrup", 190),'+            
                            '(010, "Peppermint Mocha", "Milk, Mocha Sauce", 240),'+             
                            '(011, "White Chocolate Mocha", "Milk, White Chocolate Mocha Sauce", 220),'+                
                            '(012, "Chai Latte", "Milk, Water, Chai Tea Concentrate", 110),'+ 
                            '(013, "Emperors Clouds & Mist", "An Infusion Of Water, Green Tea", 110),'+ 
                            '(014, "Nitro Cold Brew", "Brewed Coffee", 40),'+ 
                            '(015, "Violet Drink", "Ice, Berry Refresher Base", 70),'+ 
                            '(016, "Dragon Drink", "Ice, Mango Dragonfruit Refreshers Base", 220)')
        print("16 DRINKS added successfully...")
        veri+=1
    except:
        print("somethings wrong with adding drinks")

# feeding of table 2
time.sleep(1)
if (True):
    try:
        print("feeding data to food table..")
        cur.execute('insert into food (id_f, name_f, flavor_f, price_f) '+
                    'values '+
                    '(001, "Classic Oatmeal", "Oatmeal", 350),'+
                    '(002, "Chicken Sausage & Bacon Biscuit", "Corn Biscuit", 550),'+
                    '(003, "Everything Bagel", "Enriched Wheat Flour", 90),'+
                    '(004, "Red Velvet Loaf Cake", "Sugar Enriched Wheat Flour", 450),'+
                    '(005, "Strawberries Lemon Cream", "Strawberries Lemon Cream", 440)')

        print("5 foods added successfully...")
        veri+=1
    except:
        print("somethings wrong with adding food")

# feeding of table 3
time.sleep(1)
if (True):
        try:
            print("feeding data to home table..")
            cur.execute('insert into athomecoffee (id_h, name_h, flavor_h, price_h) '+
                    'values '+
                    '(001, "Jamaica Blue Mountain", "citrus and a hint of cocoa", 800),'+
                    '(002, "Ethiopia Bitta Farm", "ripe banana and bittersweet chocolate", 900),'+
                    '(003, "Guatemala Santa Isabel", "Lemon and chocolate notes", 450)')

            print("3 home added successfully...")
            veri+=1
        except:
            print("somethings wrong with adding home")

# feeding of table 4
time.sleep(1)
if (True):
        try:
            print("feeding data to customer table..")
            cur.execute('insert into customer (c_id, c_name, c_ph , c_pay , c_usual) '+
                        'values '+
                        '(10001, "Ravi P", "9834512345", "card 1903", "Flat White 006"),'+
                        '(10002, "Carsi D", "9856512445", "cash", "Dragon Drink 016"),'+
                        '(10003, "Bison M", "9836514545", "card 8903", "Nitro Cold Brew 014"),'+
                        '(10004, "Carson Y", "9244512675", "upi 4290", "Cappuccino 004"),'+
                        '(10005, "Julia Z", "9896782345", "card 1100", "Caffe Misto 002"),'+
                        '(10006, "Fariq S", "9543512445", "cash", "Chai Latte 012"),'+
                        '(10007, "Corsair C", "9346712545", "cash", "Flat White 006"),'+
                        '(10008, "Samsung D", "9067812378", "card 8803", "Emperors Clouds & Mist 013"),'+
                        '(10009, "Garim D", "9780562345", "card 3333", "Espresso 005"),'+
                        '(10010, "Asim S", "9123456789", "upi 1001", "Caffe Americano 001")')

            print("10 customers added successfully...")
            veri+=1
        except:
            print("somethings wrong with adding customer data")

time.sleep(1)                  
# final_pass
if (veri == 4):
    print(" Great ! all tables and data are places nicely, you are ready to rock !")
    time.sleep(1)
    print("saving data........")
    com.commit()
    print("closing connections..")
    com.close()
    time.sleep(1)
    print("exitiing...")
    sys.exit()

else:
    print("one or more error have been commited, please see errors..\nYour data is not saved. closing program.")
    sys.exit()
    



