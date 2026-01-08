cost = int(input())
discount = 0

if cost >= 200:
    discount = cost / 100 * 20
elif cost >= 100:
    discount = cost / 100 * 15
else:
    discount = cost / 100 * 10

print(cost - discount)