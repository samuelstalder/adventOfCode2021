f = open("day10_input.txt", "r")
data = []
for x in f:
    data.append(x.replace('\n', ''))
f.close()
#print(data)

counter = 0
#FIFO
for row in data:
    fifo = []
    for c in row:
        #in
        if(c == "(" or c == "[" or c == "{" or c == "<"):
            fifo.append(c)
        #out
        else:
            if(c == ")" and "(" == fifo[-1]): fifo.pop()
            elif(c == "]" and "[" == fifo[-1]): fifo.pop()
            elif(c == "}" and "{" == fifo[-1]): fifo.pop()
            elif(c == ">" and "<" == fifo[-1]): fifo.pop()
            else:
                if(c == ")"): counter+=3
                if(c == "]"): counter+=57
                if(c == "}"): counter+=1197
                if(c == ">"): counter+=25137
                break

print(counter)
            

#part2

data2 = []
#FIFO
for row in data:
    fifo = []
    for c in row:
        #in
        if(c == "(" or c == "[" or c == "{" or c == "<"):
            fifo.append(c)
        #out
        else:
            if(c == ")" and "(" == fifo[-1]): fifo.pop()
            elif(c == "]" and "[" == fifo[-1]): fifo.pop()
            elif(c == "}" and "{" == fifo[-1]): fifo.pop()
            elif(c == ">" and "<" == fifo[-1]): fifo.pop()
            else:
                if(c == ")"): counter+=3
                if(c == "]"): counter+=57
                if(c == "}"): counter+=1197
                if(c == ">"): counter+=25137
                data2.append(row)
                break


for i in data2:
    data.remove(i)
scores = []

for row in data:
    fifo = []
    for c in row:
        #in
        if(c == "(" or c == "[" or c == "{" or c == "<"):
            fifo.append(c)
        #out
        else:
            if(c == ")" and "(" == fifo[-1]): fifo.pop()
            elif(c == "]" and "[" == fifo[-1]): fifo.pop()
            elif(c == "}" and "{" == fifo[-1]): fifo.pop()
            elif(c == ">" and "<" == fifo[-1]): fifo.pop()
    fifo.reverse()
    counter = 0
    for i in fifo:
        counter *=5
        if(i == "("): counter+=1
        if(i == "["): counter+=2
        if(i == "{"): counter+=3
        if(i == "<"): counter+=4
    scores.append(counter)



scores.sort()
print("p", scores[25])