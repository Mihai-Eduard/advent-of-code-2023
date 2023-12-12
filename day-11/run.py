mat = open('file.in').read().split('\n')
N, M = len(mat), len(mat[0])
print(mat, N, M)

expansion = 999999

lines = {}
cnt = 0
for i in range(N):
    contains = False
    for j in range(M):
        if mat[i][j] == '#':
            contains = True
            lines[(i, j)] = i + cnt
    if not contains:
        cnt += expansion

columns = {}
cnt = 0
for j in range(M):
    contains = False
    for i in range(N):
        if mat[i][j] == '#':
            contains = True
            columns[(i, j)] = j + cnt
    if not contains:
        cnt += expansion

print(lines)
print(columns)

points = []
for i, j in columns:
    points.append((lines[(i, j)], columns[(i, j)]))

sol = 0
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        sol += abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

print(sol)

        