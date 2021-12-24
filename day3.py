data = []

f = open("day3_input.txt", "r")
for x in f:
  data.append(x.replace('\n', ''))
f.close()

print(data)
print(len(data[0]))
print(len(data))

res = [0] * 12
for i in range(len(data)):
  res[0] = res[0] + int(data[i][0])
  res[1] = res[1] + int(data[i][1])
  res[2] = res[2] + int(data[i][2])
  res[3] = res[3] + int(data[i][3])
  res[4] = res[4] + int(data[i][4])
  res[5] = res[5] + int(data[i][5])
  res[6] = res[6] + int(data[i][6])
  res[7] = res[7] + int(data[i][7])
  res[8] = res[8] + int(data[i][8])
  res[9] = res[9] + int(data[i][9])
  res[10] = res[10] + int(data[i][10])
  res[11] = res[11] + int(data[i][11])

print(res)

for i in res:
  if(i > 500): 
    print(1)
  else: print(0)

#part2
print("---part2---")

res = [0] * 12


for i in range(12):
  for j in range(len(data)):
    res[i] = res[i] + int(data[j][i])
  print(int(res[i] > len(data)))
  commen = int(res[i] >= (len(data)/2))

  new_data0 = []
  for j in range(len(data)):
    if(int(data[j][i]) == commen):
      new_data0.append(data[j])
  print(len(new_data0))
  data = new_data0
  print(data)


print(data)
