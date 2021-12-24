import sys

f = open("day12_input.txt", "r")
data = []
for x in f:
    data.append(x.replace('\n', ''))
f.close()
print(data)


sys.setrecursionlimit(1000000000)

#dic
graph = dict()

for c in data:
    caves = c.split("-")
    cave1 = caves[0]
    cave2 = caves[1]
    graph[cave1] = []
    graph[cave2] = []

for c in data:
    caves = c.split("-")
    cave1 = caves[0]
    cave2 = caves[1]
    graph[cave1].append(cave2)
    graph[cave2].append(cave1)

print(graph)

path_list = []

path = []
visited = dict()
for c in data:
    caves = c.split("-")
    cave1 = caves[0]
    cave2 = caves[1]
    visited[cave1] = False
    visited[cave2] = False

print(visited)
#u start node
#d end node
def getAllPaths(u, d, visited, path):

    #big cave can be visited multiple times
    if(u.isupper() == False): visited[u] = True
    path.append(u)

    if u == d:
        path_list.append(path)
    else:
        for i in graph[u]:
            if(visited[i] == False):
                getAllPaths(i, d, visited, path)
    path.pop()
    visited[u] = False

getAllPaths("start", "end", visited, path)

print("part 1")
print(path_list)
print(len(path_list))

#part2

def paths2(cur: str, seen: set, dup:str) -> int:
    if cur == 'end':
        return 1
    if cur == "start" and seen:
        return 0
    if cur.islower() and cur in seen:
        if dup is None:
            dup = cur
        else:
            return 0
    seen = seen | {cur}
    out = 0
    for a in graph[cur]:
        out += paths2(a, seen, dup)
    return out

out = paths2("start", set(), dup=None)

print("part 2")
print(out)
