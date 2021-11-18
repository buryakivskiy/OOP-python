from datetime import datetime
import json
import os
import uuid

PEPPERONI_PRICE = 100
CHEESE_PRICE = 145
MARGHERITA_PRICE = 95
HAWAIIAN_PRICE = 125
CHICAGO_PRICE = 150
CHICKEN_PRICE = 110
VEGAN_PRICE = 90

class Pizza:
    def __init__(self, name, ingredients, extraIngredients, price):
        self.name = name
        self.inredients = ingredients + ', ' + extraIngredients
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def inredients(self):
        return self.__inredients

    @inredients.setter
    def inredients(self, inredients):
        self.__inredients = inredients

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    def __str__(self):
        return f"{self.__name}\n{self.__inredients}\nprice: {self.__price}"

class Pepperoni(Pizza):
    def __init__(self, extraIngredients):
        super().__init__('Pepperoni', 'pepperoni, chees, species', extraIngredients, PEPPERONI_PRICE)

class Cheese(Pizza):
    def __init__(self, extraIngredients):
        super().__init__('Cheese', '4 cheeses', extraIngredients, CHEESE_PRICE)

class Margherita(Pizza):
    def __init__(self, extraIngredients):
        super().__init__('Margherita', 'Mozzarella, tomatos, sauce', extraIngredients, MARGHERITA_PRICE)

class Hawaiian(Pizza):
    def __init__(self, extraIngredients):
        super().__init__('Hawaiian', 'Meet, pineapple, chees', extraIngredients, HAWAIIAN_PRICE)

class Chicago(Pizza):
    def __init__(self, extraIngredients):
        super().__init__('Chicago', 'Meet, chees, salami', extraIngredients, CHICAGO_PRICE)

class Chicken(Pizza):
    def __init__(self, extraIngredients):
        super().__init__('Chicken', 'Chicken meet, chees, tomatos', extraIngredients, CHICKEN_PRICE)

class Vegan(Pizza):
    def __init__(self, extraIngredients):
        super().__init__('Vegan', 'Chees, tomatos', extraIngredients, VEGAN_PRICE)

class Order():
    def __init__(self, name, extraIngredients = ''):
        if not isinstance(name, str) or not isinstance(extraIngredients, str):
            raise TypeError("Uncorrect type!")
        self.name = name
        self.pizza = self.generatePizzaDay(extraIngredients)
        self.writeOrder()

    def writeOrder(self):
        file = open(str(uuid.uuid1()) + '.json', 'w')
        dict = self.pizza.__dict__
        dict['name'] = self.name
        json.dump(dict, file, indent=2)
        file.close()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def pizza(self):
        return self.__pizza

    @pizza.setter
    def pizza(self, pizza):
        self.__pizza = pizza

    def generatePizzaDay(self, extraIngredients):
        day = datetime.now().weekday()
        pizzaType = {
            0: Pepperoni(extraIngredients),
            1: Cheese(extraIngredients),
            2: Margherita(extraIngredients),
            3: Hawaiian(extraIngredients),
            4: Chicago(extraIngredients),
            5: Chicken(extraIngredients),
            6: Vegan(extraIngredients),
        }
        return pizzaType[day]
    
    def openJSON(path):
        if not os.path.exists(path):
            raise FileNotFoundError
        file = open(path, "r")
        input = json.load(file)
        person = input['person']
        if 'extraIngredients' in input:
            extraIngredients = input['extraIngredients']
        else: extraIngredients = ''
        file.close()
        return Order(person, extraIngredients)
    
    def __str__(self):
        return f"{self.__name}\n{self.__pizza}"

order = Order.openJSON('order.json')
print(order)
