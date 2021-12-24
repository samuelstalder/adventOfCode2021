f = open("day11_input.txt", "r")
data = []
for x in f:
    data.append(x.replace('\n', ''))
f.close()
#print(data)

field = []
field.append([-1]*12)
for row in data:
    r = []
    r.append(-1)
    for n in row:
        r.append(int(n))
    r.append(-1)
    field.append(r)
field.append([-1]*12)



def getListofNeighbors(t):
    (x,y) = t
    l = []
    if(field[x+1][y] != -1): l.append((x+1,y))
    if(field[x-1][y] != -1): l.append((x-1,y))
    if(field[x][y+1] != -1): l.append((x,y+1))
    if(field[x][y-1] != -1): l.append((x,y-1))
    if(field[x+1][y-1] != -1): l.append((x+1,y-1))
    if(field[x-1][y+1] != -1): l.append((x-1,y+1))
    if(field[x+1][y+1] != -1): l.append((x+1,y+1))
    if(field[x-1][y-1] != -1): l.append((x-1,y-1))
    return l


counter = 0

for step in range(100):

    #all +1
    for x in range(1,11):
        for y in range(1,11):
            field[x][y]+=1

    flashed = []
    for p in range(20):
        flash_list = []
        for x in range(1,11):
            for y in range(1,11):
                if(field[x][y] > 9 and (x,y) not in flashed):
                    flash_list.append((x,y))

        for i in flash_list:
            (x,y) = i
            field[x][y]+=1
            neighbors = getListofNeighbors((x,y))
            for n in neighbors:
                (x,y) = n
                field[x][y]+=1

        for f in flash_list:
            flashed.append(f)
        #print(len(flash_list))
        flash_list = []

    #update 0
    for x in range(1,11):
        for y in range(1,11):
            if(field[x][y] > 9): 
                field[x][y] = 0
                counter+=1
    
    if(len(flashed) == 100):
        print("step: ",step+1)
        for i in field:print(i)
print(counter)