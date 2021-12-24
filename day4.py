import copy
data = []

f = open("day4_input.txt", "r")
for x in f:
    data.append(x.replace('\n', ''))
f.close()

print(data)

num_list_str = data[0].split(",")
num_list = []
for i in num_list_str:
    num_list.append(int(i))


board_list = []

for i in range(2,len(data)-2,6):
    board = []
    for anz in range(5):
        num_str = data[i+anz].split(" ")
        row = []
        for j in num_str:
            if (j != ''):
                row.append(int(j))
        board.append(row)
    board_list.append(board) 

print(board_list)

board_list_copy = copy.deepcopy(board_list)

for bingo_num in num_list:
    #boards ankreuzen: 40 -> -1
    for board in board_list:
        for x in range(5):
            for y in range(5):
                if(bingo_num == board[x][y]): board[x][y] = -1

    
    for i in range(len(board_list)):

        #col check
        b = board_list[i]
        for t in range(5):
            if(b[0][t] == -1 and b[1][t] == -1 and b[2][t] == -1 and b[3][t] == -1 and b[4][t] == -1):
                print("col bingo:", board_list_copy[i])
                print("col bingo:", board_list[i])
                print("col board index:", i)
                print("col: ", t)
                print("col last bingo num: ", bingo_num)

        #row check
        for t in range(5):
            if(b[t][0] == -1 and b[t][1] == -1 and b[t][2] == -1 and b[t][3] == -1 and b[t][4] == -1):
                print("row bingo:", board_list_copy[i])
                print("row bingo:", board_list[i])
                print("row board index:", i)
                print("row: ", t)
                print("row last bingo num: ", bingo_num)

        

#part2
print("part2-------")
for i in range(len(board_list_copy)):
    count = 0
    for x in range(5):
        for y in range(5):
            if(board_list_copy[i][x][y] == 36 or board_list_copy[i][x][y] == 54 or board_list_copy[i][x][y] == 59 or board_list_copy[i][x][y] == 43 or board_list_copy[i][x][y] == 87 or board_list_copy[i][x][y] == 39 or board_list_copy[i][x][y] == 67 or board_list_copy[i][x][y] == 81):
                count+=1
    if(count >= 5): print(board_list_copy[i])


board_list = copy.deepcopy(board_list_copy)
print(board_list)

for bingo_num in num_list:
    found_board = 0

    #boards ankreuzen: 40 -> -1
    for board in board_list:
        for x in range(5):
            for y in range(5):
                if(bingo_num == board[x][y]): board[x][y] = -1

    board_temp = []
    for i in range(len(board_list)):
        found = 0
        #col check
        b = board_list[i]
        for t in range(5):
            if(b[0][t] == -1 and b[1][t] == -1 and b[2][t] == -1 and b[3][t] == -1 and b[4][t] == -1):
                found += 1
        #row check
        for t in range(5):
            if(b[t][0] == -1 and b[t][1] == -1 and b[t][2] == -1 and b[t][3] == -1 and b[t][4] == -1):
                found += 1
        if (found >= 1): found_board+=1
        if(found == 0): board_temp = board_list[i]
    
    print(found_board)
    print(board_temp)
    print("bingo: ", bingo_num)

print(len(board_list))
