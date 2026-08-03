class Product:

    count = 0
    def __init__(self, name, price):
        self.name = name
        self.price =price
        Product.count +=1

    def get_info(self):
        print(f"price of {self.name} is {self.price}")

    @classmethod
    def get_count():
        print(f"total products are: {Product.count}")    

    @staticmethod 
    def get_discount(price,discount):
        print(f"discounted price of product = {price-(price * discount/100)}")

p1 =Product("iphone", 600000)
p2 = Product("watch", 5999)
p3 = Product("laptop", 60034)

p1.get_discount(p1.price, 30)