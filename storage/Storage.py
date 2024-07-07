from classes.Brand import Brand
from classes.StockedProduct import StockedProduct
from classes.ProductTemplate import  ProductTemplate
from classes.Category import Category


products = []


def create_product():
    brand = Brand("Apple")
    category = Category("Celular")
    template = ProductTemplate(brand, category, "Iphone 12 Pro", "Gray", 10000)
    stocked = StockedProduct(template, 10)
