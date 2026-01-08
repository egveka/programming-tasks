n = int(input())
error_nums = input().split()
m = int(input())

counter = 0
for i in range(m):
    num = input()
    for error_num in error_nums:
        if num.startswith(error_num):
            counter += 1
            break
print(counter)