import copy
import numpy as np
data = []

f = open("day7_input.txt", "r")
for x in f:
    data.append(x)
f.close()

num_str = data[0].split(",")

num_list = []
for i in num_str:
    num_list.append(int(i))

print(num_list)

input = num_list

tot = []
for x in range(10000):
    tots = 0
    for xx in input:
        diff = abs(xx-x)
        tots += diff
    tot.append(tots)
print(min(tot))

#part2
tot = []
for x in range(10000):
    tots = 0
    for xx in input:
        diff = abs(xx-x)
        #gauss-formel n•(n+1) / 2
        n = diff
        tots += (n*(n+1)/2)
    tot.append(tots)
print(min(tot))

