import os
import timeit

f = open("sample.txt", "w")
while (os.path.getsize('sample.txt')/(1000*1000)) < 50:
    f.write('4352556726456542\n')
f.close()

s = """
open1 = open("sample.txt", "r")
res = 0
for line in open1.readlines():
    if line.strip().isdigit():
        res+=1
open1.close()
"""
print(timeit.timeit(s, number=10))

s = """
open2 = open("sample.txt", "r")
res = 0
for line in open2:
    if line.strip().isdigit():
        res+=1
open2.close()
"""
print(timeit.timeit(s, number=10))

s = """
open3 = open("sample.txt", "r")
res = sum(int(line.strip().isdigit()) for line in open3)
open3.close()
"""
print(timeit.timeit(s, number=10))