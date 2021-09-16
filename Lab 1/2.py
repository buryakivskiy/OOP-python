import sys

inputString = sys.argv[1:]

def calculate(inputString):
    try:
        action = inputString[0]
        operandOne = int(inputString[1])
        operandTwo = int(inputString[2])
        formul = {
            'add' : operandOne + operandTwo,
            'sub' : operandOne - operandTwo,
            'myl' : operandOne * operandTwo,
            'div' : operandOne / operandTwo,
        }
        return formul[action]
    except:
        return 'Something went wrong'
    

if len(inputString) > 3:
    print('Need only 3 arguments')
else:
    print(calculate(inputString))

# use operators i