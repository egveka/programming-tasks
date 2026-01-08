numbers = [int(i) for i in input().split()]
# sum1 = 0

# for i in range(len(numbers)):
#     sum1 += numbers[i]

# for num in numbers:
#     sum1 += num

co2 = sum(numbers) * 0.0024
print(int(co2))

print(int(sum(list(map(int, input().split()))) * 0.0024))