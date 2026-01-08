num = int(input())
prev_height = 0

counter = 0
for i in range(num):
    height = int(input())
    if prev_height < height:
        if prev_height > 0:
            counter += 1
    prev_height = height
print(counter * 100)

# num = int(input())
# prev_height = 0

# counter = 0
# for i in range(num):
#     height = int(input())
#     if prev_height < height:
#         counter += 1
#     prev_height = height
# print((counter - 1) * 100)