file = open("file.in", "r")
lines = file.readlines()

times = [int(time) for time in lines[0].strip().split(" ")[1:] if time != ""]
distances = [int(distance) for distance in lines[1].strip().split(" ")[1:] if distance != ""]

print(times, distances)

product = 1
for time, distance in zip(times, distances):
    cnt = 0
    for i in range(0, time + 1):
        if i * (time - i) > distance:
            cnt += 1
    product *= cnt

print(product)

time = int("".join([str(time) for time in times]))
distance = int("".join([str(distance) for distance in distances]))

print(time, distance)

cnt = 0
for i in range(0, time + 1):
    if i * (time - i) > distance:
        cnt += 1

print(cnt)