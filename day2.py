data = []

f = open("day2_input.txt", "r")
for x in f:
  data.append(x.replace('\n', ''))
f.close()

print(data)

h_pos = 0
depth = 0

for i in data:
  d = i.split()
  dir = d[0]
  val = int(d[1])
  if(dir == "forward"): h_pos = h_pos + val
  if(dir == "down"): depth = depth + val
  if(dir == "up"): depth = depth - val

print(h_pos)
print(depth)
print(h_pos*depth)

#part2

aim = 0
h_pos = 0
depth = 0
for i in data:
  d = i.split()
  dir = d[0]
  val = int(d[1])
  if(dir == "forward"): 
    h_pos = h_pos + val
    depth = depth + (aim * val)

  if(dir == "down"):
    aim = aim + val

  if(dir == "up"):
    aim = aim - val
  print("aim", aim)

print(h_pos)
print(depth)
print(h_pos*depth)