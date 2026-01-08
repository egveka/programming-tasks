search_sum = int(input())
search_diff = int(input())
found = False

for a in range(21):
    for b in range(21):
        _sum = a+b
        diff = a-b
        if search_sum == _sum and search_diff == diff:
            print(a, b)
            found = True

if not found:
    print("Impossible")