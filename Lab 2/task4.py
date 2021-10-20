import re
import os.path
 
class TextStatistical:
    def __init__(self, path):
        if not isinstance(path, str):
            raise TypeError("Uncorrect type for path")
        elif not os.path.exists(path):
            raise FileNotFoundError("File not found")
        self.__path = path
        self.__symbols = self.getSymbols()
        self.__words = self.getWords()
        self.__sentences = self.getSentences()
    
    def getSymbols(self):
        file = open(self.__path, "r")
        result = len(file.read())
        file.close()
        return result

    def getWords(self):
        file = open(self.__path, "r")
        result = len(re.findall(r'[a-zA-Z-\']+', file.read()))
        file.close()
        return result

    def getSentences(self):
        file = open(self.__path, "r")
        result = len(re.split(r'[.!?]+', file.read()))
        file.close()
        return result

    def __str__(self):
        return f'symbols: {self.__symbols}\nword: {self.__words}\nsentences: {self.__sentences}'

def main(path):
    info = TextStatistical(path)
    print(info)

main("/Users/mac/Desktop/OOP-python/Lab 2/text.txt")