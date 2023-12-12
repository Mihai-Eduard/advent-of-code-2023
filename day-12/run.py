import functools

input = open('file.in').read().split('\n')

@functools.cache
def getAllArrangements(mask, values):
    if(len(values) == 0):
        return int(sum(x == '#' for x in mask) == 0)
    if sum(values) > len(mask):
        return 0
    
    if mask[0] == '.':
        return getAllArrangements(mask[1:], values)

    num1, num2 = 0, 0
    if mask[0] == '?':
        num2 = getAllArrangements(mask[1:], values)
    if all(x != '.' for x in mask[:values[0]]) and (mask[values[0]] if len(mask) > values[0] else '.') != '#':
        num1 = getAllArrangements(mask[(values[0] + 1):], values[1:])
    return num1 + num2

sol = 0

for i, line in enumerate(input):
    print(f'{i}/{len(input)-1}')
    mask, values = line.split(' ')
    values = [int(x) for x in values.split(',')]

    mask = ((mask + '?') * 5)[:-1]
    values = values * 5

    sol += getAllArrangements(tuple(mask), tuple(values))

print(sol)