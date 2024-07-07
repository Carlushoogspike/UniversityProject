class Category:

    def __init__(self, name):
        self.__name = name

    def changeName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def print(self):
        print(f"Categoria: {self.__name}")
