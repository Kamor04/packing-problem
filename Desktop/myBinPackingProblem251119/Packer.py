from Item import StartPosition


class Packer:

    bins = []
    items = []
    unfitItems = []

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def addBin(self, binn):
        self.bins.append(binn)

    def addItem(self, item):
        self.items.append(item)

    def findFittedBin(self, item):
        for binn in self.bins:
            if not binn.putItem(item, StartPosition):
                continue

            if len(binn.items) == 1 and binn.items[0] == item:
                binn.items = []
            return binn

    def unfitItem(self):
        if len(self.items) == 0:
            return
        self.unfitItems.append(self.items[0])
        self.items.pop(0)

    def packToBin(self, binn, items):
        unpacked = []
        fit = binn.putItem(items[0], StartPosition)
        if not fit:
            return self.items

        # Pack unpacked items.
        for _i in range(1, len(self.items)):
            item = self.items[_i]
            for itemInBin in binn.items:
                pv = []
                fitted = False

                if itemInBin.position[1] + itemInBin.getHeight() > binn.getHeight() and itemInBin.position[2] + \
                        itemInBin.getDepth() > binn.getDepth():
                    pv = [itemInBin.position[0] + itemInBin.getWidth(), itemInBin.position[1], itemInBin.position[2]]
                    fitted = True
                elif itemInBin.position[0] + itemInBin.getWidth() > binn.getWidth() and itemInBin.position[2] + \
                        itemInBin.getDepth() > binn.getDepth():
                    pv = [itemInBin.position[0], itemInBin.getHeight() + itemInBin.position[1], itemInBin.position[2]]
                    fitted = True
                elif itemInBin.position[0] + itemInBin.getWidth() > binn.getWidth() and itemInBin.position[1] + \
                        itemInBin.getHeight() > binn.getHeight():
                    pv = [itemInBin.position[0], itemInBin.position[1], itemInBin.getDepth() + itemInBin.position[2]]
                    fitted = True
                else:
                    pv = [itemInBin.getWidth() + itemInBin.position[0], itemInBin.getHeight() + itemInBin.position[1],
                          itemInBin.getDepth() + itemInBin.position[2]]
                    fitted = True

                if fitted:
                    binn.putItem(item, pv)
                else:
                    unpacked.append(item)

        return unpacked

    def pack(self):

        while len(self.items) > 0:
            binn = self.findFittedBin(self.items[0])
            if binn is None:
                self.unfitItem()
                continue
            self.items = self.packToBin(binn, self.items)
        return None
