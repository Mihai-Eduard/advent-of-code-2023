input = open('file.in').read().split('\n\n')

def getVertical(mat):
    N = len(mat)
    M = len(mat[0])
    for k in range(1, M):
        cnt = 0
        for i in range(N):
            for j in range(min(k, M-k)):
                if mat[i][k-j-1] != mat[i][k+j]:
                    cnt += 1
        if cnt == 1:
            return k
    return -1

def getHorizontal(mat):
    N = len(mat)
    M = len(mat[0])
    for k in range(1, N):
        cnt = 0
        for i in range(M):
            for j in range(min(k, N-k)):
                if mat[k-j-1][i] != mat[k+j][i]:
                    cnt += 1
        if cnt == 1:
            return k
    return -1

verticals = []
horizontals = []

for mat in input:
    mat = mat.split('\n')
    print(mat)
    ver = getVertical(mat)
    hor = getHorizontal(mat)
    print(ver, hor)
    if ver != -1:
        verticals.append(ver)
    if hor != -1:
        horizontals.append(hor)

print(sum(horizontals) * 100 + sum(verticals))
        
