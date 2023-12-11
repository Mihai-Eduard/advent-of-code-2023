input = open('file.in', 'r').read().split('\n')

print(input)

steps = input[0]
left_dir = {}
right_dir = {}
for i in range(2, len(input)):
    start = input[i].split(' ')[0]
    left, right = input[i].split(" = ")[1][1:-1].split(",")
    right = right[1:]
    left_dir[start] = left
    right_dir[start] = right

print(left_dir)
print(right_dir)
print(steps)

# current = "AAA"
# cnt = 0
# while current != "ZZZ":
#     if steps[cnt%len(steps)] == "L":
#         current = left_dir[current]
#     else:
#         current = right_dir[current]
#     cnt += 1

# print(cnt)

currents = set()
for node in left_dir:
    if node[-1] == "A":
        currents.add(node)
for node in right_dir:
    if node[-1] == "A":
        currents.add(node)

def verify(x):
    for el in x:
        if el[-1] != "Z":
            return False
    return True


print(currents)

cnts = []

for current in currents:
    print(current)
    cnt = 0
    while current[-1] != "Z":
        if steps[cnt%len(steps)] == "L":
            current = left_dir[current]
        else:
            current = right_dir[current]
        cnt += 1
    cnts.append(cnt)
    print(cnt)

print(cnts)

import math

print(math.lcm(*cnts))
