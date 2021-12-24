f = open("day8_input.txt", "r")
data = []
for x in f:
    data.append(x.replace('\n', ''))
f.close()

#print(data)


sig_list = []
out_list = []
for i in range(len(data)):
    d = data[i].split("|")
    sig = d[0].split(" ")
    sig_list.append(sig[:-1])
    out = d[1].split(" ")
    out_list.append(out[1:])

#print(sig_list)
#print(out_list)

counter = 0
for out in out_list:
    for i in range(4):
        le = len(out[i])
        if(le == 2 or le == 3 or le == 4 or le == 7): counter+=1

#print(counter)



#part2


def getNum(d, o):
    set_list = []
    for i in d:
        my_set = set()
        for st in i:
            my_set.add(st)
        set_list.append(my_set)

    out_set_list = []
    for i in o:
        my_set = set()
        for st in i:
            my_set.add(st)
        out_set_list.append(my_set)

    print(set_list)
    print(out_set_list)

    zero = set()
    one = set()
    two = set()
    three = set()
    four = set()
    five = set()
    six = set()
    seven = set()
    eight = set()
    nine = set()

    fiver = []
    sixer = []
    for s in set_list:
        if(len(s) == 2): one = s
        if(len(s) == 4): four = s
        if(len(s) == 3): seven = s
        if(len(s) == 7): eight = s
        if(len(s) == 5): fiver.append(s)
        if(len(s) == 6): sixer.append(s)
    A = fiver[0]
    B = fiver[1]
    C = fiver[2]

    #fiver are 2,3,5
    # 1 is subset 3
    if(one.issubset(A)): 
        three = A
        if(len(four & B) == 2): 
            two = B
            five = C
        else: 
            five = B
            two = C
    if(one.issubset(B)): 
        three = B
        if(len(four & A) == 2): 
            two = A
            five = C
        else: 
            five = A
            two = C
    if(one.issubset(C)): 
        three = C
        if(len(four & A) == 2): 
            two = A
            five = B
        else: 
            five = A
            two = B

    #sixer are 0,6,9
    X = sixer[0]
    Y = sixer[1]
    Z = sixer[2]

    # 4 is subset of 9
    if(four.issubset(X)): 
        nine = X
        # 1 is subset of 0
        if(one.issubset(Y)): 
            zero = Y
            six = Z  
        else:
            zero = Z
            six = Y
    if(four.issubset(Y)): 
        nine = Y
        # 1 is subset of 0
        if(one.issubset(X)): 
            zero = X
            six = Z  
        else:
            zero = Z
            six = X
    if(four.issubset(Z)): 
        nine = Z
        # 1 is subset of 0
        if(one.issubset(Y)): 
            zero = Y
            six = X 
        else:
            zero = X
            six = Y

    print("0", zero)
    print("1", one)
    print("2", two)
    print("3", three)
    print("4", four)
    print("5", five)
    print("6", six)
    print("7", seven)
    print("8", eight)
    print("9", nine)
    st = ""
    for s in out_set_list:
        if(s == zero): st += str(0)
        if(s == one): st += str(1)
        if(s == two): st += str(2)
        if(s == three): st += str(3)
        if(s == four): st += str(4)
        if(s == five): st += str(5)
        if(s == six): st += str(6)
        if(s == seven): st += str(7)
        if(s == eight): st += str(8)
        if(s == nine): st += str(9)
    return int(st)

counter = 0
for i in range(len(data)):

    counter += getNum(sig_list[i], out_list[i])

print(counter)