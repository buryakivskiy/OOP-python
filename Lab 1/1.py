from sys import argv

formula = argv[:]

def calculate(string):
    try:
        if string[2].find('.') == True:
            string[2] = '*'
        return eval(string[1]+string[2]+string[-1])
    except:
        return None

print(calculate(formula))