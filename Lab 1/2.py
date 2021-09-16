import sys
import operator

def calculate(string):
    try:
        act = string[1]
        if act == 'add': return operator.add(int(string[2]), int(string[3]))
        elif act == 'sub': return operator.sub(int(string[2]), int(string[3]))
        elif act == 'mull': return operator.mul(int(string[2]), int(string[3]))
        elif act == 'div': return operator.truediv(int(string[2]), int(string[3]))
    except:
        return None

print(calculate(sys.argv[:]))
