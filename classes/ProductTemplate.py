class ProductTemplate:

    def __init__(self, brand, category, name, color, price):
        self.__brand = brand
        self.__category = category
        self.__name = name
        self.__color = color
        self.__price = price

    def getBrand(self):
        return self.__brand

    def getCategory(self):
        return self.__category

    def getName(self):
        return self.__name

    def getColor(self):
        return self.__color

    def getPrice(self):
        return self.__price

    def change(self, brand, category, name, color, price):
        if brand != "":
            self.__brand = brand

        if category != "":
            self.__category = category

        if name != "":
            self.__name = name

        if color != "":
            self.__color = color

        if price != 0:
            self.__price = price
