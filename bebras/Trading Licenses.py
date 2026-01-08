money = int(input())
profits = [int(i) for i in input().split()]

for i in range(len(profits)):
    half = money//2
    if profits[i] > half:
        money = money - half + profits[i]
print(money)