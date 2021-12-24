import copy
import numpy as np
data = []

f = open("day6_input.txt", "r")
for x in f:
    data.append(x.replace('\n', ''))
f.close()

print(data)

swarm = []

num_str = data[0].split(",")

for i in num_str:
    swarm.append(int(i))

print(swarm)

for i in range(10):
    for f in range(len(swarm)):
        swarm[f] = swarm[f] -1

    for f in range(len(swarm)):
        if(swarm[f] == -1): 
            swarm.append(8)
            swarm[f] = 6

print("final: ", len(swarm))


#part2
l = [int(x) for x in data[0].split(",")]
l = np.array(l)
d = dict()

for i in range(9):
    d[i] = 0

for i in l:
    d[i] += 1

print(d)

def doday(d :dict) -> dict:
    z = d[0]
    d[0] = d[1]
    d[1] = d[2]
    d[2] = d[3]
    d[3] = d[4]
    d[4] = d[5]
    d[5] = d[6]
    d[6] = d[7] + z
    d[7] = d[8]
    d[8] = z
    return d

for i in range(256):
    d = doday(d)

print(sum(d.values()))