input = open('file.in').read().split('\n')
mat = [list(x) for x in input]

def rotate_90(mat):
    return [list(reversed(x)) for x in zip(*mat)]

def move(mat):
    N, M = len(mat), len(mat[0])
    new_mat = [list(x) for x in mat]
    col = [-1] * M
    for i in range(N):
        for j in range(M):
            if new_mat[i][j] == 'O':
                col[j] += 1
                new_mat[i][j] = '.'
                new_mat[col[j]][j] = 'O'
            elif new_mat[i][j] == '#':
                col[j] = i
    return new_mat

def getSum(mat):
    sol = 0
    for i in range(len(mat)):
        sol += (len(mat) - i) * sum([1 for x in mat[i] if x == 'O'])
    return sol

def printMat(mat):
    print("\n".join(["".join(x) for x in mat]))
    print()

def applyCycle(mat):
    for i in range(4):
        mat = move(mat)
        mat = rotate_90(mat)
    return mat

def printCycles(mat, k=10):
    for i in range(k):
        mat = applyCycle(mat)
        # print(i)
        # printMat(mat)
        # print()
    return mat

def findCycle(mat):
    mats = []
    for i in range(300):
        mat = applyCycle(mat)
        for j in range(len(mats)):
            if mats[j] == mat:
                return (j, i)
        mats.append(mat)
    return -1

i, j = findCycle(mat)
print(i, j)
num_cycles = 1000000000
remaining = (num_cycles - i) % (j - i)
print(remaining)

mat = printCycles(mat, i + remaining)
print(getSum(mat))