class Customer:
    def __init__(self, fName, lName, pat, phone):
        if isinstance(fName, str) and isinstance(lName, str) and isinstance(pat, str) and isinstance(phone, str):
            self.firstName = fName
            self.lastName = lName
            self.__patronimic = pat
            self.__phone = phone
        else:
            raise TypeError("Uncorrect type")
    
    @property
    def firstName(self):
        return self.__firstName

    @firstName.setter
    def firstName(self, name):
        if not isinstance(name, str):
            raise TypeError("Uncorrect type")
        if not name:
            raise ValueError("Uncorrect value")
        self.__firstName = name

    @property
    def lastName(self):
        return self.__lastName 

    @lastName .setter
    def lastName(self, surname):
        if not isinstance(surname, str):
            raise TypeError("Uncorrect type")
        if not surname:
            raise ValueError("Uncorrect value")
        self.__lastName  = surname

    def __str__(self):
        return f'firstName: {self.__firstName}\nlast name: {self.__lastName}'
    
class Product:
    def __init__(self, price, description, dimension):
        if isinstance(price, int) and isinstance(description, str) and isinstance(dimension, str):
            if price > 0:
                self.__price = price
            else:
                raise ValueError("Uncorrect value")
            self.__description = description
            self.__dimension = dimension
        else:
            raise TypeError("Uncorrect type")

    def getPrice(self):
        return self.__price

class Order:
    def __init__(self, customer, products):
        if isinstance(customer, Customer) and isinstance(products[0], Product):
            self.__customer = customer
            self.__products = products
            self.__price = self.__orderPrice__()
        else:
            raise TypeError("Uncorrect type")

    def __orderPrice__(self):
        cost = 0
        for i in range(len(self.__products)):
            cost += self.__products[i].getPrice()
        return cost

    def __str__(self):
        return f'{self.__customer}\ntotal price: {self.__price}'

def main():
    serhiy = Customer('Serhiy', 'Buryakivskiy', 'Vitaliovich', '+380683389420')
    iPhone = Product(399, 'Nice phone!', 'w: 8, l: 15')
    iMac = Product(2399, 'Nice pc!', 'w: 45, l: 60')
    serhiyOrder = Order(serhiy, [iPhone, iMac])
    print(serhiyOrder)

main()