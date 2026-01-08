# km = int(input())

# water = 0
# for i in range(1, km + 1):
#     water += 30
#     if i % 3 == 0:
#         water += 10 
# print(water)

km = int(input())

water = km * 30
water += (km//3) * 10

print(water)