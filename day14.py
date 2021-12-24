import sys
import numpy as np

f = open("day14_input.txt", "r")
data = []
for x in f:
    data.append(x.replace('\n', ''))
f.close()
print(data)

string_list = []
for i in data[0]:
    string_list.append(i)

rules = dict()
for i in range(2, len(data)):
    t = data[i].split(" -> ")
    rules[t[0]] = str(t[0][0] + t[1] + t[0][1])

bsl = string_list

for p in range(10):
    new_sl = []
    for i in range(len(string_list)-1):
        duo = string_list[i]+string_list[i+1]
        tri = rules[duo]
        new_sl.append(tri[0])
        new_sl.append(tri[1])
    new_sl.append(string_list[len(string_list)-1])
    string_list = new_sl

string_list.sort()
myset = set(string_list)
l = []
for i in myset:
    print(i, string_list.count(i))
    l.append(string_list.count(i))
l.sort()
print(l)


#part2
print(bsl)
rule_count = dict()
for r in rules:
    rule_count[r] = 0

rule_count["K"] = 0
rule_count["C"] = 0
rule_count["O"] = 0
rule_count["H"] = 0
rule_count["S"] = 0
rule_count["N"] = 0
rule_count["P"] = 0
rule_count["V"] = 0
rule_count["F"] = 0
rule_count["B"] = 0

print(rule_count)
for i in range(len(bsl)-1):
    duo = bsl[i]+bsl[i+1]
    rule_count[duo] += 1

for p in range(20):
    old_rule_count = rule_count
    for key in old_rule_count:
        if(len(key) == 2):
            tri = rules[key]
            rule_count[tri[0] + tri[1]] += old_rule_count[duo]
            rule_count[tri[1] + tri[2]] += old_rule_count[duo]
    #last_char = string_list[len(string_list)-1]
    #rule_count[last_char] += 1


for key in rule_count:
    if(len(key) == 2):
        rule_count[key[0]] += rule_count[key]
        rule_count[key[1]] += rule_count[key]

l = []
for key in rule_count:
    if(len(key) == 1):
        l.append(rule_count[key])

l.sort()
print(l)
print(l[9] - l[0])
print(rule_count)
