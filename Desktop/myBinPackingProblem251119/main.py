from Packer import Packer
from Item import Item
from Bin import Bin

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
itemWidth = int(itemWidth.get())
itemHeight = IntVar()
itemHeight = int(itemHeight.get())
itemDepth = IntVar()
itemDepth = int(itemDepth.get())


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
listbox = Listbox(root, width='36', yscrollcommand=scrollbar.set)
for itemRecord in itemsRecords:
    print_itemRecords = ''
    print_itemRecords += str(itemRecord[0]) + " " + "[" + str(itemRecord[1]) + ", " + str(itemRecord[2]) + ", " + str(itemRecord[3]) + "]" + "\n"
    listbox.insert(END, print_itemRecords)
listbox.grid(row=5, column=4)

scrollbar.config(command=listbox.yview)


lblunpackedItem= Label(root, font=('georgia', 14, 'bold'), text="Niezapakowane", fg='black', width=15, bd=10, anchor='w')
lblunpackedItem.grid(row=4, column=6)

scrollbar = Scrollbar(root)
scrollbar.grid(row=14, column=1, sticky=W+S+N)
listbox = Listbox(root, width='36', yscrollcommand=scrollbar.set)
for itemRecord in itemsRecords:
    print_itemRecords = ''
    print_itemRecords += str(itemRecord[0]) + " " + "[" + str(itemRecord[1]) + ", " + str(itemRecord[2]) + ", " + str(itemRecord[3]) + "]" + "\n"
    listbox.insert(END, print_itemRecords)
listbox.grid(row=5, column=6)

scrollbar.config(command=listbox.yview)


packButton = Button(pady=8, bd=2, fg='black', relief=GROOVE, font=('arial', 10, 'bold'), width=15, text="Pakuj", bg='white', command=saveItemToDb).grid(row=6, column=8)



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




packer = Packer()

packer.addBin(bin1)
packer.addItem(item1)
#packer.addItem(item2)
# packer.addItem(item3)
# packer.addItem(item4)
# packer.addItem(item5)
# packer.addItem(item6)
# packer.addItem(item7)
# packer.addItem(item8)
# packer.addItem(item9)
# packer.addItem(item10)

# pack items into bin1
packer.pack()
#
# # item1
print(bin1.items)
#
# items will be empty, all items was packed
print("Packer items")
# print(packer.items)
print(*packer.bins[0].items)

print("Unfitted items")
# unfitItems will be empty, all items fit into bin1
print(*packer.unfitItems)
root.mainloop()
