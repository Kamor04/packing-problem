from Packer import Packer
from Item import Item
from Bin import Bin

bin1 = Bin("Box", 200.0, 200.0, 200.0)
item1 = Item("Item 1", 20.0, 20.0, 2.0)
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
# packer.addItem(item2)
# packer.addItem(item3)
# packer.addItem(item4)
# packer.addItem(item5)
# packer.addItem(item6)
# packer.addItem(item7)
packer.addItem(item8)
# packer.addItem(item9)
# packer.addItem(item10)

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
