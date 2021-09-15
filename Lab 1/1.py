from sys import argv

if (argv[2].find('.') == True):
    argv[2] = '*'
    
print(eval(argv[1]+argv[2]+argv[-1]))