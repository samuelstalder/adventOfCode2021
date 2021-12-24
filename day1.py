sig = []

f = open("day1_input.txt", "r")
for x in f:
  sig.append(int(x))
f.close()

print(sig)

increased = 0

#part 1
for i in range(len(sig)-1):
  if(sig[i] < sig[i+1]): increased = increased + 1

print(len(sig))
print(increased)

#part 2
sliding_window_increased = 0
for i in range(len(sig)-3):
  a = sig[i] + sig[i+1] + sig[i+2]
  b = sig[i+1] + sig[i+2] + sig[i+3]
  print(a, b)
  if(a < b): sliding_window_increased = sliding_window_increased + 1

print(sliding_window_increased)