import re
 
class TextStatistical:
    def __init__(self, text):
        self.__symbols = len(text)
        self.__words = len(re.findall(r'[a-zA-Z-\']+', text))
        self.__sentences = len(re.split(r'[.!?]+', text))

    def __str__(self):
        return f'symbols: {self.__symbols}\nword: {self.__words}\nsentences: {self.__sentences}'

def main(path):
    try:
        with open(path, "r") as file:
            text = file.read()
            file.close()
        info = TextStatistical(text)
        print(info)
    except:
        print('Something went wrong!')

main("/Users/mac/Desktop/OOP-python/Lab 2/text.txt")