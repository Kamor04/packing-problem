class Bin:
    name = ''
    width = 0
    height = 0
    depth = 0

    items = []

    def __init__(self, name, w, h, d):
        self.name = name
        self.width = w
        self.height = h
        self.depth = d

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def getName(self):
        return self.name

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getDepth(self):
        return self.depth

    def getItems(self):
        return self.items

    def getVolume(self):
        return self.getWidth() * self.getHeight() * self.getDepth()

    def putItem(self, itemToPutIn, itemPosition):
        box = self
        fit = False
        itemToPutIn.position = itemPosition
        for i in range(6):
            itemToPutIn.rotationType = i
            itemDimension = itemToPutIn.getDimension()
            if box.getWidth() >= itemPosition[0] + itemDimension[0] and box.getHeight() >= \
                    itemPosition[1] + itemDimension[1] and box.getDepth() >= itemPosition[2] + itemDimension[2]:
                fit = True
                for itemInBox in box.items:
                    if itemInBox.intersect(itemToPutIn):
                        fit = False
                        break
                if fit:
                    box.items.append(itemToPutIn)
                    break
                return fit
        return fit
