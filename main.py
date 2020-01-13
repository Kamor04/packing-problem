from Packer import Packer
from Item import Item
from Bin import Bin

import itertools
import functools
from tkinter import *
import sqlite3

conn = sqlite3.connect('packingProblem.db')
curr = conn.cursor()

curr.execute('DROP TABLE bin')
curr.execute('DROP TABLE items')
curr.execute('DROP TABLE packed_items')
curr.execute('DROP TABLE unpacked_items')

curr.execute("""CREATE TABLE bin (
        id integer PRIMARY KEY,
        bin_name text,
        bin_width integer,
        bin_height integer,
        bin_depth integer
        )""")

curr.execute("""CREATE TABLE items (
        id integer PRIMARY KEY,
        id_bin integer NOT NULL,
        item_name text,
        item_width integer,
        item_height integer,
        item_depth integer,
        FOREIGN KEY(id_bin) REFERENCES bin (id) ON UPDATE CASCADE
        )""")

curr.execute("""CREATE TABLE packed_items (
        id integer PRIMARY KEY,
        item_name text,
        item_width integer,
        item_height integer,
        item_depth integer
        )""")

curr.execute("""CREATE TABLE unpacked_items (
        id integer PRIMARY KEY,
        item_name text,
        item_width integer,
        item_height integer,
        item_depth integer
        )""")

def exit(e):
    root.destroy()

root = Tk()
root.state('zoomed')


root.title("Bin packing problem")
root.configure(background='white')
root.bind("<Escape>", exit)

binName = StringVar()
binWidth = IntVar()
binHeight = IntVar()
binDepth = IntVar()


itemName = StringVar()
itemWidth = IntVar()
itemHeight = IntVar()
itemDepth = IntVar()


lblBinName = Label(root, font=('georgia', 14, 'bold'), text="Nazwa kontenera ", fg='black', width=15, bd=10, anchor='w')
lblBinName.grid(row=3, column=0)
txtBinName = Entry(root, font=('arial', 14, 'bold'),  bd=2, width=24, bg='white', justify='left', textvariable=binName)
txtBinName.grid(row=3, column=1)


lblBinWidth = Label(root, font=('georgia', 14, 'bold'), text="Szerokość", fg='black', width=15, bd=10, anchor='w')
lblBinWidth.grid(row=4, column=0)
txtBinWidth = Entry(root, font=('arial', 14, 'bold'), bd=2, width=24, bg='white', justify='left', textvariable=binWidth)
txtBinWidth.grid(row=4, column=1)

lblBinHeight = Label(root, font=('georgia', 14, 'bold'), text="Wysokość", fg='black', width=15, bd=10, anchor='w')
lblBinHeight.grid(row=5, column=0)
txtBinHeight = Entry(root, font=('arial', 14, 'bold'), bd=2, width=24, bg='white', justify='left', textvariable=binHeight)
txtBinHeight.grid(row=5, column=1)

lblBinDepth = Label(root, font=('georgia', 14, 'bold'), text="Głębokość", fg='black', width=15, bd=10, anchor='w')
lblBinDepth.grid(row=6, column=0)
txtBinDepth = Entry(root, font=('arial', 14, 'bold'), bd=2, width=24, bg='white', justify='left', textvariable=binDepth)
txtBinDepth.grid(row=6, column=1)

##

lblItemName = Label(root, font=('georgia', 14, 'bold'), text="Nazwa przedmiotu", fg='black', width=15, bd=10, anchor='w')
lblItemName.grid(row=8, column=0)
txtItemName = Entry(root, font=('arial', 14, 'bold'), bd=2, width=24, bg='white', justify='left', textvariable=itemName)
txtItemName.grid(row=8, column=1)


lblItemWidth = Label(root, font=('georgia', 14, 'bold'), text="Szerokość", fg='black', width=15, bd=10, anchor='w')
lblItemWidth.grid(row=9, column=0)
txtItemWidth = Entry(root, font=('arial', 14, 'bold'), bd=2, width=24, bg='white', justify='left', textvariable=itemWidth)
txtItemWidth.grid(row=9, column=1)

lblItemHeight = Label(root, font=('georgia', 14, 'bold'), text="Wysokość", fg='black', width=15, bd=10, anchor='w')
lblItemHeight.grid(row=10, column=0)
txtItemHeight = Entry(root, font=('arial', 14, 'bold'), bd=2, width=24, bg='white', justify='left', textvariable=itemHeight)
txtItemHeight.grid(row=10, column=1)

lblItemDepth = Label(root, font=('georgia', 14, 'bold'), text="Głębokość", fg='black', width=15, bd=10, anchor='w')
lblItemDepth.grid(row=11, column=0)
txtItemDepth = Entry(root, font=('arial', 14, 'bold'), bd=2, width=24, bg='white', justify='left', textvariable=itemDepth)
txtItemDepth.grid(row=11, column=1)


def saveBinToDb():
    conn = sqlite3.connect('packingProblem.db')

    entry_binName = txtBinName.get()
    entry_binWidth = txtBinWidth.get()
    entry_binHeight = txtBinHeight.get()
    entry_binDepth = txtBinDepth.get()
    conn.execute('insert into bin values (NULL,?,?,?,?)',
                 (str(entry_binName), str(entry_binWidth), str(entry_binHeight), str(entry_binDepth)))
    curr = conn.execute("SELECT * FROM bin")


    txtBinName.configure(state="disabled")
    txtBinWidth.configure(state="disabled")
    txtBinHeight.configure(state="disabled")
    txtBinDepth.configure(state="disabled")
    submitBinButton.configure(state="disabled")

    conn.commit()
    conn.close()


submitBinButton = Button(pady=8, bd=2, fg='black', relief=GROOVE, font=('arial', 10, 'bold'), width=15, text="Dodaj kontener", bg='white', command=saveBinToDb)
submitBinButton.grid(row=7, column=2)


def saveItemToDb():
    conn = sqlite3.connect('packingProblem.db')

    entry_itemName = txtItemName.get()
    entry_itemWidth = txtItemWidth.get()
    entry_itemHeight = txtItemHeight.get()
    entry_itemDepth = txtItemDepth.get()
    conn.execute('insert into items values (NULL,(SELECT max(id) from bin),?,?,?,?)',
                 (str(entry_itemName), str(entry_itemWidth), str(entry_itemHeight), str(entry_itemDepth)))
    curr = conn.execute("SELECT * FROM items")
    curr = conn.execute("SELECT item_name, item_width, item_height, item_depth FROM items")
    itemsRecords = curr.fetchall()

    itemRecordTitle = Label(root, font=('arial', 16, 'bold'), text="Przedmioty:", fg='black', width=15, bd=10, anchor='w')
    itemRecordTitle.grid(row=13, column=0)
    scrollbar = Scrollbar(root)
    scrollbar.grid(row=14, column=1, sticky=W+S+N)
    listbox = Listbox(root, width='36', yscrollcommand=scrollbar.set)
    for itemRecord in itemsRecords:
        print_itemRecords = ''
        print_itemRecords += str(itemRecord[0]) + " " + "[" + str(itemRecord[1]) + ", " + str(itemRecord[2]) + ", " + str(itemRecord[3]) + "]" + "\n"
        listbox.insert(END, print_itemRecords)
    listbox.grid(row=14, column=0)

    scrollbar.config(command=listbox.yview)

    conn.commit()
    conn.close()

    txtItemName.delete(0, END)
    txtItemWidth.delete(0, END)
    txtItemHeight.delete(0, END)
    txtItemDepth.delete(0, END)


submitItemButton = Button(pady=8, bd=2, fg='black', relief=GROOVE, font=('arial', 10, 'bold'), width=15, text="Dodaj przedmiot", bg='white', command=saveItemToDb).grid(row=12, column=2)


lblpackedItem = Label(root, font=('georgia', 14, 'bold'), text="Zapakowane ", fg='black', width=15, bd=10, anchor='w')
lblpackedItem.grid(row=4, column=4)
conn = sqlite3.connect('packingProblem.db')
curr = conn.execute("SELECT item_name FROM packed_items")
itemsRecords = curr.fetchall()
scrollbar = Scrollbar(root)
scrollbar.grid(row=14, column=1, sticky=W+S+N)
listboxPacked = Listbox(root, width='36', yscrollcommand=scrollbar.set)
for itemRecord in itemsRecords:
    print_itemRecords = ''
    print_itemRecords += str(itemRecord[0]) + " " + "[" + str(itemRecord[1]) + ", " + str(itemRecord[2]) + ", " + str(itemRecord[3]) + "]" + "\n"
    listboxPacked.insert(END, print_itemRecords)
listboxPacked.grid(row=5, column=4)

scrollbar.config(command=listboxPacked.yview)


lblunpackedItem= Label(root, font=('georgia', 14, 'bold'), text="Niezapakowane", fg='black', width=15, bd=10, anchor='w')
lblunpackedItem.grid(row=4, column=6)
conn = sqlite3.connect('packingProblem.db')
curr = conn.execute("SELECT item_name FROM unpacked_items")

scrollbar = Scrollbar(root)
scrollbar.grid(row=14, column=1, sticky=W+S+N)
listboxUnpacked = Listbox(root, width='36', yscrollcommand=scrollbar.set)
for itemRecord in itemsRecords:
    print_itemRecords = ''
    print_itemRecords += str(itemRecord[0]) + " " + "[" + str(itemRecord[1]) + ", " + str(itemRecord[2]) + ", " + str(itemRecord[3]) + "]" + "\n"
listboxUnpacked.grid(row=5, column=6)

scrollbar.config(command=listboxUnpacked.yview)


def packing():
    entry_binName = txtBinName.get()
    entry_binWidth = txtBinWidth.get()
    entry_binHeight = txtBinHeight.get()
    entry_binDepth = txtBinDepth.get()
    bin1 = Bin(str(entry_binName), int(entry_binWidth), int(entry_binHeight), int(entry_binDepth))
    conn = sqlite3.connect('packingProblem.db')
    curr1 = conn.execute("SELECT item_name, item_width, item_height, item_depth FROM items")
    itemShapesInBase = curr1.fetchall()
    ListOfItemsShapes = list(itertools.chain(*itemShapesInBase))
    packer = Packer()
    packer.addBin(bin1)
    item_list = []

    for i in range(0, len(ListOfItemsShapes), 4):
        obj = Item(ListOfItemsShapes[i], ListOfItemsShapes[i + 1], ListOfItemsShapes[i + 2], ListOfItemsShapes[i + 3])
        item_list.append(obj)
        packer.addItem(obj)
        packer.pack()
        conn = sqlite3.connect('packingProblem.db')
        if obj in packer.bins[0].items:
            conn.execute('insert into packed_items values (NULL,?,?,?,?)',
                         (str(ListOfItemsShapes[i]), str(ListOfItemsShapes[i + 1]), str(ListOfItemsShapes[i + 2]), str(ListOfItemsShapes[i + 3])))
        else:
            conn.execute('insert into unpacked_items values (NULL,?,?,?,?)',
                         (str(ListOfItemsShapes[i]), str(ListOfItemsShapes[i + 1]), str(ListOfItemsShapes[i + 2]), str(ListOfItemsShapes[i + 3])))
        conn.commit()
        conn.close()

    for i in range(len(packer.bins[0].items)):
        listboxPacked.insert(END, packer.bins[0].items[i].name)


    for el in range(len(packer.unfitItems)):
        listboxUnpacked.insert(END, packer.unfitItems[el].name)
    # volume = tuple(functools.reduce(lambda x, y: x * y, tp) for tp in itemShapesInBase)
    # sortedVolume = sorted(volume, reverse=True)
    packButton.configure(state="disabled")


packButton = Button(pady=8, bd=2, fg='black', relief=GROOVE, font=('arial', 10, 'bold'), width=15, text="Pakuj", bg='white', command=packing)
packButton.grid(row=6, column=8)

root.mainloop()
