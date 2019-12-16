RotationType_WHD = 0
RotationType_HWD = 1
RotationType_HDW = 2
RotationType_DHW = 3
RotationType_DWH = 4
RotationType_WDH = 5

WidthAxis = 0
HeightAxis = 1
DepthAxis = 2

StartPosition = [0, 0, 0]


class Item:

    name = ''
    width = 0
    height = 0
    depth = 0

    rotationType = RotationType_WHD
    position = []  # x, y, z

    def __init__(self, name, w, h, d):
        self.name = name
        self.width = w
        self.height = h
        self.depth = d

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getDepth(self):
        return self.depth

    def getVolume(self):
        return self.getWidth() * self.getHeight() * self.getDepth()

    def getRotationType(self):
        return self.rotationType

    def getDimension(self):
        if self.rotationType == RotationType_WHD:
            dimension = [self.getWidth(), self.getHeight(), self.getDepth()]
            return dimension
        elif self.rotationType == RotationType_HWD:
            dimension = [self.getHeight(), self.getWidth(), self.getDepth()]
            return dimension
        elif self.rotationType == RotationType_HDW:
            dimension = [self.getHeight(), self.getDepth(), self.getWidth()]
            return dimension
        elif self.rotationType == RotationType_DHW:
            dimension = [self.getDepth(), self.getHeight(), self.getWidth()]
            return dimension
        elif self.rotationType == RotationType_DWH:
            dimension = [self.getDepth(), self.getWidth(), self.getHeight()]
            return dimension
        elif self.rotationType == RotationType_WDH:
            dimension = [self.getWidth(), self.getDepth(), self.getHeight()]
            return dimension
        else:
            pass

    def intersect(self, i2):
        return rectIntersect(self, i2, WidthAxis, HeightAxis) and rectIntersect(self, i2, HeightAxis, DepthAxis) \
               and rectIntersect(self, i2, WidthAxis, DepthAxis)


def rectIntersect(item1, item2, x, y):
    dimension1 = item1.getDimension()
    dimension2 = item2.getDimension()
    cx1 = item1.position[x] + dimension1[x] / 2
    cy1 = item1.position[y] + dimension1[y] / 2
    cx2 = item2.position[x] + dimension2[x] / 2
    cy2 = item2.position[y] + dimension2[y] / 2

    ix = max(cx1, cx2) - min(cx1, cx2)
    iy = max(cy1, cy2) - min(cy1, cy2)

    return ix < (dimension1[x] + dimension2[x]) / 2 and iy < (dimension1[y] + dimension2[y]) / 2
