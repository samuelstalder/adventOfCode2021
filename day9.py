f = open("day9_input.txt", "r")
data = []
for x in f:
    data.append(x.replace('\n', ''))
f.close()
#print(data)

field = []
field.append([10] * 102)
for row in data:
    r = []
    r.append(10)
    for n in row:
        r.append(int(n))
    r.append(10)
    field.append(r)
field.append([10] * 102)

#for i in field: print(i)
#print(len(field))
#print(len(field[1]))

sum = 0
for x in range(1,101):
    for y in range(1,101):
        cur = field[x][y]
        if(cur < field[x+1][y] and cur < field[x][y+1] and cur < field[x-1][y] and cur < field[x][y-1]): 
            sum += (cur+1)

print(sum)

#part2


def findbasain(x,y, pos_set):
    cur = field[x][y]
    if(cur >= 9 or ((x,y) in pos_set)):
        return pos_set
    else:
        pos_set.add((x,y))
        if(cur < field[x+1][y]):
            findbasain(x+1,y, pos_set)
        if(cur < field[x][y+1]):
            findbasain(x,y+1, pos_set)
        if(cur < field[x-1][y]):
            findbasain(x-1,y, pos_set)
        if(cur < field[x][y-1]):
            findbasain(x,y-1, pos_set)
        return pos_set



basin_size_list = []
for x in range(1,101):
    for y in range(1,101):
        cur = field[x][y]
        if(cur < field[x+1][y] and cur < field[x][y+1] and cur < field[x-1][y] and cur < field[x][y-1]): 
            #print(x,y)
            pos_set = set()
            c = findbasain(x,y,pos_set)
            basin_size_list.append(len(c))


for i in field: print(i)

basin_size_list.sort()

print("---")
print(basin_size_list)
