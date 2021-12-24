import copy
data = []

f = open("day5_input.txt", "r")
for x in f:
    data.append(x.replace('\n', ''))
f.close()

#print(data)

ee_points = [] #x1, y1, x2, y2
for i in data:
    items_str = i.split(" ")
    start = items_str[0].split(",")
    end = items_str[2].split(",")
    x1 = int(start[0])
    y1 = int(start[1])
    x2 = int(end[0])
    y2 = int(end[1])
    ee_points.append([x1,y1,x2,y2])

#print(ee_points)

field = []
for i in range(1000):
    row = [0] * 1000
    field.append(row)

#print(field)

#fill field with vents
for ee in ee_points:
    x1 = ee[0]
    y1 = ee[1]
    x2 = ee[2]
    y2 = ee[3]
    if(y1 == y2 and x1 != x2):
        mi = min(x1, x2)
        ma = max(x1, x2)
        for x in range(mi, (ma+1), 1): 
            field[x][y1] += 1
    if(x1 == x2 and y1 != y2):
        mi = min(y1, y2)
        ma = max(y1, y2)
        for y in range(mi, (ma+1), 1): 
            field[x1][y] += 1
    
    #part2 diagonal
    if(y1 != y2 and x1 != x2):
        min_x = min(x1, x2)
        max_x = max(x1, x2)
        min_y = min(y1, y2)
        max_y = max(y1, y2)
        diff = max_x - min_x
        for i in range(0, (diff+1), 1):
            if(x1 < x2 and y1 < y2): field[x1+i][y1+i] +=1
            if(x1 > x2 and y1 < y2): field[x1-i][y1+i] +=1
            if(x1 < x2 and y1 > y2): field[x1+i][y1-i] +=1
            if(x1 > x2 and y1 > y2): field[x1-i][y1-i] +=1

    if(x1 == x2 and y1 == y2): print("omg")
    print("---")

#print(field)
counter = 0
for x in range(1000):
    for y in range(1000):
        if(field[x][y] >= 2): counter+=1

print(counter)
