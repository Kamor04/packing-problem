from Packer import Packer
from Item import Item
from Bin import Bin

from tkinter import *
import sqlite3

# Database

conn = sqlite3.connect('packingProblem.db')
curr = conn.cursor()

# curr.execute("""CREATE TABLE bin (
#         id integer PRIMARY KEY,
#         bin_name text,
#         bin_width integer,
#         bin_height integer,
#         bin_depth integer
#         )""")
#
# curr.execute("""CREATE TABLE items (
#         id integer PRIMARY KEY,
#         item_name text,
#         item_width integer,
#         item_height integer,
#         item_depth integer
#         )""")
#
# curr.execute("""CREATE TABLE packed_items (
#         id integer PRIMARY KEY,
#         item_name text,
#         item_width integer,
#         item_height integer,
#         item_depth integer
#         )""")
#
# curr.execute("""CREATE TABLE unpacked_items (
#         id integer PRIMARY KEY,
#         item_name text,
#         item_width integer,
#         item_height integer,
#         item_depth integer
#         )""")

def exit(e):
    root.destroy()

root = Tk()
root.geometry("700x600+0+0")

root.title("Bin-packing")
root.configure(background='white')
root.bind("<Escape>", exit)

binName = StringVar()
binWidth = IntVar()
binWidth = int(binWidth.get())
binHeight = IntVar()
binHeight = int(binHeight.get())
binDepth = IntVar()
binDepth = int(binDepth.get())


itemName = StringVar()
itemWidth = IntVar()
itemWidth = int(itemWidth.get())
itemHeight = IntVar()
itemHeight = int(itemHeight.get())
itemDepth = IntVar()
itemDepth = int(itemDepth.get())


lblBinName = Label(root, font=('georgia', 16, 'bold'), text="Bin name", fg='black', width=15, bd=10, anchor='w')
lblBinName.grid(row=3, column=0)
txtBinName = Entry(root, font=('arial', 16, 'bold'), bd=2, width=24, bg='white', justify='left', textvariable=binName)
txtBinName.grid(row=3, column=1)


lblBinWidth = Label(root, font=('georgia', 16, 'bold'), text="Bin Width", fg='black', width=15, bd=10, anchor='w')
lblBinWidth.grid(row=4, column=0)
txtBinWidth = Entry(root, font=('arial', 16, 'bold'), bd=2, width=24, bg='white', justify='left', textvariable=binWidth)
txtBinWidth.grid(row=4, column=1)

lblBinHeight = Label(root, font=('georgia', 16, 'bold'), text="Bin Height", fg='black', width=15, bd=10, anchor='w')
lblBinHeight.grid(row=5, column=0)
txtBinHeight = Entry(root, font=('arial', 16, 'bold'), bd=2, width=24, bg='white', justify='left', textvariable=binHeight)
txtBinHeight.grid(row=5, column=1)

lblBinDepth = Label(root, font=('georgia', 16, 'bold'), text="Bin Depth", fg='black', width=15, bd=10, anchor='w')
lblBinDepth.grid(row=6, column=0)
txtBinDepth = Entry(root, font=('arial', 16, 'bold'), bd=2, width=24, bg='white', justify='left', textvariable=binDepth)
txtBinDepth.grid(row=6, column=1)

##

lblItemName = Label(root, font=('georgia', 16, 'bold'), text="Item name", fg='black', width=15, bd=10, anchor='w')
lblItemName.grid(row=8, column=0)
txtItemName = Entry(root, font=('arial', 16, 'bold'), bd=2, width=24, bg='white', justify='left', textvariable=itemName)
txtItemName.grid(row=8, column=1)


lblItemWidth = Label(root, font=('georgia', 16, 'bold'), text="Item Width", fg='black', width=15, bd=10, anchor='w')
lblItemWidth.grid(row=9, column=0)
txtItemWidth = Entry(root, font=('arial', 16, 'bold'), bd=2, width=24, bg='white', justify='left', textvariable=itemWidth)
txtItemWidth.grid(row=9, column=1)

lblItemHeight = Label(root, font=('georgia', 16, 'bold'), text="Item Height", fg='black', width=15, bd=10, anchor='w')
lblItemHeight.grid(row=10, column=0)
txtItemHeight = Entry(root, font=('arial', 16, 'bold'), bd=2, width=24, bg='white', justify='left', textvariable=itemHeight)
txtItemHeight.grid(row=10, column=1)

lblItemDepth = Label(root, font=('georgia', 16, 'bold'), text="Item Depth", fg='black', width=15, bd=10, anchor='w')
lblItemDepth.grid(row=11, column=0)
txtItemDepth = Entry(root, font=('arial', 16, 'bold'), bd=2, width=24, bg='white', justify='left', textvariable=itemDepth)
txtItemDepth.grid(row=11, column=1)





def submitData():

    packer.addItem(item1)
    packer.pack()
    root.destroy()

def saveToDb():
    conn = sqlite3.connect('packingProblem.db')

    entry_binName = txtBinName.get()
    entry_binWidth = txtBinWidth.get()
    entry_binHeight = txtBinHeight.get()
    entry_binDepth = txtBinDepth.get()
    conn.execute('insert into bin values (NULL,?,?,?,?)',
                 (str(entry_binName), str(entry_binWidth), str(entry_binHeight), str(entry_binDepth)))
    curr = conn.execute("SELECT * FROM bin")
    print(curr.fetchone())

    entry_itemName = txtItemName.get()
    entry_itemWidth = txtItemWidth.get()
    entry_itemHeight = txtItemHeight.get()
    entry_itemDepth = txtItemDepth.get()
    conn.execute('insert into items values (NULL,?,?,?,?)',
                 (str(entry_itemName), str(entry_itemWidth), str(entry_itemHeight), str(entry_itemDepth)))
    curr = conn.execute("SELECT * FROM items")
    print(curr.fetchone())

    conn.commit()
    conn.close()



submitButton = Button(pady=8, bd=2, fg='black', font=('arial', 10, 'bold'), width=10, text="Submit", bg='white', command=saveToDb).grid(row=13, column=2)


bin1 = Bin("Box", 200.0, 200.0, 200.0)
item1 = Item(itemName, itemWidth, itemHeight, itemDepth)
item2 = Item("Item 2", 20.0, 20.0, 2.0)
item3 = Item("Item 3", 3000.0, 2000.0, 2.0)
item4 = Item("Item 4", 10.0, 8.0, 2.0)
item5 = Item("Item 5", 10.0, 10.0, 2.0)
item6 = Item("Item 6", 20.0, 14.0, 2.0)
item7 = Item("Item 7", 2.0, 20.0, 2.0)
item8 = Item("Item 8", 10.0, 8.0, 4.0)
item9 = Item("Item 9", 1.0, 1.0, 2.0)
item10 = Item("Item 10", 10.0, 14.0, 2.0)
item11 = Item("Item 11", 1.0, 1.0, 2.0)
item12 = Item("Item 12", 1.0, 1.0, 2.0)
item13 = Item("Item 13", 2.0, 1.0, 2.0)



root.mainloop()

packer = Packer()

packer.addBin(bin1)
packer.addItem(item1)
# packer.addItem(item2)
# packer.addItem(item3)
# packer.addItem(item4)
# packer.addItem(item5)
# packer.addItem(item6)
# packer.addItem(item7)
# packer.addItem(item8)
# packer.addItem(item9)
# packer.addItem(item10)

# pack items into bin1
# packer.pack()
#
# # item1
# print(bin1.items)
#
# # items will be empty, all items was packed
# print("Packer items")
# # print(packer.items)
# print(*packer.bins[0].items)
#
# print("Unfitted items")
# # unfitItems will be empty, all items fit into bin1
# print(*packer.unfitItems)
