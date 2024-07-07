class StockedProduct:

    def __init__(self, product_template, stocked_value):
        self.__product_template = product_template
        self.__stocked_value = stocked_value
        self.__stocked = True
        self.__released_value = stocked_value
        self.__released = True

    @property
    def product_template(self):
        return self.__product_template

    @product_template.setter
    def product_template(self, product_template):
        self.__product_template = product_template
        self.__stocked = True
        self.__released = True

    @property
    def stocked_value(self):
        return self.__stocked_value

    @stocked_value.setter
    def stocked_value(self, stocked_value):
        self.__stocked_value = stocked_value
        self.__released = True

    @stocked_value.getter
    def stocked_value(self):
        return self.__stocked_value