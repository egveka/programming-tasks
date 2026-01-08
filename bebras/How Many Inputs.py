_sum = 0
counter = 0

while True:
    n = int(input())
    if n != -1:
        _sum += n
        counter += 1
    else:
        break

print(counter)
print(_sum)