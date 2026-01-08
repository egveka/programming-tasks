time_a = 0
time_b = 0

for i in range(4):
    results = input().split()
    if results[0] == "A":
        time_a += int(results[1]) - int(results[2]) * 3
    elif results[0] == "B":
        time_b += int(results[1]) - int(results[2]) * 3

if time_a < time_b:
    print("A")
elif time_b < time_a:
    print("B")
else:
    print("draw")