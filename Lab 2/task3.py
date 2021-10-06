class Customer:
    def __init__(self, fName, lName, pat, phone):
        self.__firstName = fName
        self.__lastName = lName
        self.__patronimic = pat
        self.__phone = phone

    def __str__(self):
        return f'firstName: {self.__firstName}\nlast name: {self.__lastName}'
    
class Product:
    def __init__(self, price, description, dimension):
        self.__price = price
        self.__description = description
        self.__dimension = dimension
    
    def getPrice(self):
        return self.__price

class Order:
    def __init__(self, customer, products):
        self.__customer = customer
        self.__products = products
        self.__price = self.__orderPrice__()

    def __orderPrice__(self):
        cost = 0
        for i in range(len(self.__products)):
            cost += self.__products[i].getPrice()
        return cost

    def __str__(self):
        return f'{self.__customer}\ntotal price: {self.__price}'

def main():
    try:
        serhiy = Customer('Serhiy', 'Buryakivskiy', 'Vitaliovich', '+380683389420')
        iPhone = Product(399, 'Nice phone!', 'w: 8, l: 15')
        iMac = Product(2399, 'Nice pc!', 'w: 45, l: 60')
        serhiyOrder = Order(serhiy, [iPhone, iMac])
        print(serhiyOrder)
    except:
        print('Something went wrong!')

main()