class Brand:

    def __init__(self, brand_name):
        self.__brand_name = brand_name

    def changeBrandName(self, new_brand_name):
        self.__brand_name = new_brand_name

    def getBrandName(self):
        return self.__brand_name
