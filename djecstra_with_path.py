import sys

N, S, F = list(map(int, input().split()))

matrix = []
matrix.append([0] * (N + 1))
for i in range(N):
    n = list(map(int, input().split()))
    n = [0] + n
    matrix.append(n)

# 3 2 1
# 0 1 1
# 4 0 1
# 2 1 0

distance = [sys.maxsize] * (N + 1)
currentVertex = S
distance[currentVertex] = 0

path = [0] * (N + 1)
path[currentVertex] = -1

visited = [currentVertex]

def getNext(dist, vis):
    a_min = -1
    m = max(dist)
    for elem in range(len(dist)):
        if dist[elem] < m and elem not in vis and dist[elem] != 0:
            m = dist[elem]
            a_min = elem

    return a_min

while currentVertex != -1:
    neighbors = []
    for n in range(N+1):
        if matrix[currentVertex][n] > 0 and n not in visited:
            neighbors.append(n)
    for elem in neighbors:
        weight = distance[currentVertex] + matrix[currentVertex][elem]
        if weight < distance[elem]:
            distance[elem] = weight
            #if currentVertex not in path:
            path[elem] = currentVertex

    currentVertex = getNext(distance, visited)
    if currentVertex > 0:
        visited.append(currentVertex)


if distance[F] == sys.maxsize:
    print(-1)
else:
    otv = [F]
    elem = F

    while path[elem] != -1:
        elem = path[elem]
        otv.append(elem)
    # 95 24 75 27 93
    print(*otv[::-1])
