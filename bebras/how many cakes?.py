guests = int(input())
cakes = 0
result = guests//6

if guests % 6 != 0:
    result += 1
print(result)