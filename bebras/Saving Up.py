daily_earnings = [int(i) for i in input().split()]

_sum = 0
days = 0
for daily_earning in daily_earnings:
    _sum += daily_earning - 20
    days += 1
    if _sum >= 1000:
        break
print(days)