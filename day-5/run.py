def converter(mappings, list):
    sol = []
    for x in list:
        y = x
        for rel in mappings:
            if x >= rel[0] and x <= rel[1]:
                y = rel[2] + (x - rel[0])
        sol.append(y)
    return sol


with open("file.in", "r") as file:
    seeds = [int(number) for number in file.readline().split(": ")[1].split()]
    file.readline()
    mappings = []
    current_mapping = []
    for line in file:
        line = line.strip()
        if line.find(':') != -1:
            continue
        if line:
            nums = [int(number) for number in line.split()]
            current_mapping.append((nums[1], nums[1] + nums[2] - 1, nums[0]))
        else:
            mappings.append(current_mapping)
            current_mapping = []
    mappings.append(current_mapping)


from queue import Queue


q = Queue()
for i in range(0, len(seeds), 2):
    q.put((seeds[i], seeds[i] + seeds[i + 1] - 1))


print(list(q.queue))


for mapping in mappings:
    new_q = Queue()
    while not q.empty():
        start, end = q.get()
        ok = False
        for rel in mapping:
            if ok == True:
                break
            if rel[1] < start or rel[0] > end:
                continue
            st = max(start, rel[0])
            en = min(end, rel[1])
            ok = True
            new_q.put((rel[2] + st - rel[0], rel[2] + en - rel[0]))
            if st > start:
                q.put((start, st - 1))
            if en < end:
                q.put((en + 1, end))
        if ok == False:
            new_q.put((start, end))
    q = new_q

    print(list(new_q.queue))


print(min(list(q.queue)))
