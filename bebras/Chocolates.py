packets = [int(i) for i in input().split()]

result = 0
packets.sort()

for i in range(len(packets)):
    if i % 2 == 0:
        result += packets[i]

print(result)