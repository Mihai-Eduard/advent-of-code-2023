mat = [line.strip() for line in open('file.in', 'r').readlines()]
N, M = len(mat), len(mat[0])
dp = [[0 for i in range(M)] for j in range(N)]

start = (0, 0)
for i in range(N):
    for j in range(M):
        if mat[i][j] == 'S':
            start = (i, j)
            break

prev = {}
prev['|'] = {(-1, 0), (1, 0)}
prev['-'] = {(0, -1), (0, 1)}
prev['F'] = {(1, 0), (0, 1)}
prev['L'] = {(-1, 0), (0, 1)}
prev['7'] = {(1, 0), (0, -1)}
prev['J'] = {(-1, 0), (0, -1)}

next = {}
next['|'] = {(-1, 0), (1, 0)}
next['-'] = {(0, -1), (0, 1)}
next['F'] = {(1, 0), (0, 1)}
next['L'] = {(-1, 0), (0, 1)}
next['7'] = {(1, 0), (0, -1)}
next['J'] = {(-1, 0), (0, -1)}
next['S'] = {(-1, 0), (1, 0), (0, -1), (0, 1)}

print(mat)
print(start)

current = start
dp[start[0]][start[1]] = 1
q = [start]

dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while len(q) > 0:
    x, y = q.pop(0)
    for dx, dy in next[mat[x][y]]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and mat[nx][ny] != '.' and dp[nx][ny] == 0:
            if (x-nx, y-ny) in prev[mat[nx][ny]]:
                dp[nx][ny] = dp[x][y] + 1
                q.append((nx, ny))
                break

sol = max([max(row) for row in dp])

print(sol-1)

print('\n'.join([str([str(x) if x>9 else '0'+str(x) for x in row]) for row in dp]))

inside_mat = [[0 for i in range(M)] for j in range(N)]

mx = max([max(row) for row in dp])

print(start)
next_start = set()
for dx, dy in dir:
    nx, ny = start[0] + dx, start[1] + dy
    print(nx, ny, dp[nx][ny])
    if 0 <= nx < N and 0 <= ny < M and (dp[nx][ny] == 2 or dp[nx][ny] == mx):
        next_start.add((-dx, -dy))

if next_start == next['|']:
    start_sign = '|'
elif next_start == next['-']:
    start_sign = '-'
elif next_start == next['F']:
    start_sign = 'F'
elif next_start == next['L']:
    start_sign = 'L'
elif next_start == next['7']:
    start_sign = '7'
elif next_start == next['J']:
    start_sign = 'J'

for i in range(N):
    angle_pipe_up = None
    inside = False
    for j in range(M):
        if dp[i][j] > 0:
            tile = mat[i][j]
            if tile == 'S':
                tile = start_sign
            if tile == '|':
                inside = not inside
            elif tile == 'L':
                angle_pipe_up = True
            elif tile == 'F':
                angle_pipe_up = False
            elif tile == 'J':
                if angle_pipe_up == False:
                    inside = not inside
                angle_pipe_up = None
            elif tile == '7':
                if angle_pipe_up == True:
                    inside = not inside
                angle_pipe_up = None
        if inside and dp[i][j] == 0:
            inside_mat[i][j] = 1

print()
print("\n".join([str(row) for row in inside_mat]))

print(sum([sum(row) for row in inside_mat]))

print(mat[start[0]][start[1]])
print(start_sign)