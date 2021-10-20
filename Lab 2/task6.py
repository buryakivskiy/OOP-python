
class Node:
    def __init__(self, code, number, price, left=None, right=None):
        self.code = code
        self.number = number
        self.price = price
        self.left = left
        self.right = right

    def totalPrice(self, current):
        if current.left == None and current.right == None:
            return current.number * current.price
        elif current.left and current.right:
            return current.number * current.price + self.totalPrice(current.left) + self.totalPrice(current.right)
        elif current.left and current.right == None:
            return current.number * current.price + self.totalPrice(current.left)
        elif current.right and current.left == None:
            return current.number * current.price + self.totalPrice(current.right)

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, code, number, price):
        if not isinstance(code, int) or not isinstance(number, int) or not isinstance(price, int):
            raise TypeError("Uncorrect type for inserting")
        if self.root == None:
            self.root = Node(code, number, price)
        else:
            current = self.root
            while 1:
                if code < current.code:
                    if current.left == None:
                        current.left = Node(code, number, price)
                        break
                    else:
                        current = current.left
                elif code > current.code:
                    if current.right == None:
                        current.right = Node(code, number, price)
                        break
                    else:
                        current = current.right
                else:
                    raise ValueError("Uncorrect code")

tree = BinarySearchTree()
tree.insert(1, 2, 2)
tree.insert(2, 2, 2)
tree.insert(3, 2, 2)
tree.insert(4, 2, 2)
tree.insert(5, 2, 2)

print('Total price is: ', tree.root.totalPrice(tree.root))