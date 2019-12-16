from Packer import Packer
from Item import Item
from Bin import Bin

from tkinter import *


def exit(e):
    root.destroy()


root = Tk()
root.geometry("700x300+0+0")

root.title("Bin-packing")
root.configure(background='white')
root.bind("<Escape>", exit)
itemName = StringVar()
Width = IntVar()
Height = IntVar()
Depth = IntVar()


lblItemName = Label(root, font=('georgia', 16, 'bold'), text="Item name", fg='black', width=15, bd=10, anchor='w')
lblItemName.grid(row=3, column=0)
txtItemName = Entry(root, font=('arial', 16, 'bold'), bd=2, width=24, bg='white', justify='left', textvariable=itemName)
txtItemName.grid(row=3, column=1)


lblWidth = Label(root, font=('georgia', 16, 'bold'), text="Width", fg='black', width=15, bd=10, anchor='w')
lblWidth.grid(row=4, column=0)
txtWidth = Entry(root, font=('arial', 16, 'bold'), bd=2, width=24, bg='white', justify='left', textvariable=Width)
txtWidth.grid(row=4, column=1)

lblHeight = Label(root, font=('georgia', 16, 'bold'), text="Height", fg='black', width=15, bd=10, anchor='w')
lblHeight.grid(row=5, column=0)
txtHeight = Entry(root, font=('arial', 16, 'bold'), bd=2, width=24, bg='white', justify='left', textvariable=Height)
txtHeight.grid(row=5, column=1)

lblDepth = Label(root, font=('georgia', 16, 'bold'), text="Depth", fg='black', width=15, bd=10, anchor='w')
lblDepth.grid(row=6, column=0)
txtDepth = Entry(root, font=('arial', 16, 'bold'), bd=2, width=24, bg='white', justify='left', textvariable=Depth)
txtDepth.grid(row=6, column=1)


bin1 = Bin("Box", 200.0, 200.0, 200.0)
item1 = Item("itemName", Width, Height, Depth)
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
#packer.addItem(item1)
packer.addItem(item2)
#packer.addItem(item3)
#packer.addItem(item4)
# packer.addItem(item5)
#packer.addItem(item6)
packer.addItem(item7)
packer.addItem(item8)
#packer.addItem(item9)
#packer.addItem(item10)

# pack items into bin1
packer.pack()

# item1
print(bin1.items)

# items will be empty, all items was packed
print("Packer items")
# print(packer.items)
print(*packer.bins[0].items)

print("Unfitted items")
# unfitItems will be empty, all items fit into bin1
print(*packer.unfitItems)



root.mainloop()
