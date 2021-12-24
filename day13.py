import sys
import numpy as np

f = open("day13_input.txt", "r")
data = []
for x in f:
    data.append(x.replace('\n', ''))
f.close()
#print(data)

d1 = data[0:-13]
d2 = data[-12:]

pos_list = []
for pos in d1:
    p = pos.split(",")
    x = int(p[0])
    y = int(p[1])
    pos_list.append((x,y))


fold_list = []
for i in d2:
    d = i.split(" ")
    dd = d[2].split("=")
    fold_list.append((dd[0], int(dd[1])))


x_max = 1311
y_max = 895
letter = np.zeros(shape=(x_max,y_max))
for i in pos_list:
    x,y = i
    letter[x,y] = 1


for i in fold_list:
    (di, pos) = i
    print("di", di)
    if(di == "x"):
        x_max = int(x_max/2)
        fold1 = letter[:x_max, :y_max]
        fold2 = letter[-x_max:, :y_max]
        for x in range(x_max):
            for y in range(y_max):
                fold1[x,y] += fold2[x_max-1-x,y]
    else:
        y_max = int(y_max/2)
        fold1 = letter[:x_max, :y_max]
        fold2 = letter[:x_max, -y_max:]
        for x in range(x_max):
            for y in range(y_max):
                fold1[x,y] += fold2[x,y_max-1-y]

    fold1 = fold1 = letter[:x_max, :y_max]
    #count dots
    count = 0
    for x in range(x_max):
        for y in range(y_max):
            if(fold1[x,y] != 0): 
                fold1[x,y] = 1
                count+=1

    print("count", count)
    letter = fold1

print(letter.T.view())