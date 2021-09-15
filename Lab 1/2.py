import sys

action = sys.argv[1]
operandOne = int(sys.argv[2])
operandTwo = int(sys.argv[3])

calculate = {
    'add' : operandOne + operandTwo,
    'sub' : operandOne - operandTwo,
    'myl' : operandOne * operandTwo,
    'div' : operandOne / operandTwo,
}

print(calculate[action])