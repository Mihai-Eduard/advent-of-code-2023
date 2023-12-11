from functools import cmp_to_key

input = open('file.in', 'r').read().split('\n')

chars = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

def cmp_lex(a, b):
    for i in range(len(a)):
        if chars.index(a[i]) < chars.index(b[i]):
            return 1
        elif chars.index(a[i]) > chars.index(b[i]):
            return -1
    return 0

def get_type(hand):
    cnt = {}
    for char in hand:
        cnt[char] = cnt.get(char, 0) + 1
    if len(cnt) == 1:
        return 6
    elif len(cnt) == 2:
        if 4 in cnt.values():
            return 5
        else:
            return 4
    elif len(cnt) == 3:
        if 3 in cnt.values():
            return 3
        else:
            return 2
    elif len(cnt) == 4:
        return 1
    else:
        return 0

def cmp(a, b):
    a = a[0]
    b = b[0]
    if get_type(a) < get_type(b):
        return -1
    elif get_type(a) > get_type(b):
        return 1
    else:
        return cmp_lex(a, b)

hands = [(hand.split(' ')[0], int(hand.split(' ')[1])) for hand in input]

print(hands)

hands.sort(key=cmp_to_key(cmp))

print(hands)

sol = 0
for i in range(len(hands)):
    sol += hands[i][1] * (i + 1)

print(sol)

def get_type_special(a):
    cnt = {}
    cnt_J = 0
    for char in a:
        if char != 'J':
            cnt[char] = cnt.get(char, 0) + 1
        else:
            cnt_J += 1
    if len(cnt) == 0:
        return 6
    if len(cnt) == 1:
        return 6
    elif len(cnt) == 2:
        if cnt_J == 3 or cnt_J == 2:
            return 5
        elif cnt_J == 1:
            if 3 in cnt.values():
                return 5
            else:
                return 4
        if 4 in cnt.values():
            return 5
        else:
            return 4
    elif len(cnt) == 3:
        if cnt_J == 2 or cnt_J == 1:
            return 3
        if 3 in cnt.values():
            return 3
        else:
            return 2
    elif len(cnt) == 4:
        return 1
    else:
        return 0

def cmp_special(a, b):
    a = a[0]
    b = b[0]
    if get_type_special(a) < get_type_special(b):
        return -1
    elif get_type_special(a) > get_type_special(b):
        return 1
    else:
        return cmp_lex(a, b)

hands = [(hand.split(' ')[0], int(hand.split(' ')[1])) for hand in input]

print(hands)

hands.sort(key=cmp_to_key(cmp_special))

print(hands)

sol = 0
for i in range(len(hands)):
    sol += hands[i][1] * (i + 1)

print(sol)
