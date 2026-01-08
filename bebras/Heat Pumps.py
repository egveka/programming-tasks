import math

house = int(input())
garden = int(input())
pipes = 0

if garden / 2.5 < house:
    # if house <= 100:
    #     pipes += 1
    # elif house > 100 and house <= 200:
    #     pipes += 2
    # elif house > 200 and house <= 300:
    #     pipes += 3
    pipes = math.ceil(house / 100)
    print("Vertical")
    print(pipes)
else:
    print("Horizontal")

print("examples:")
print(math.ceil(0.4))
print(math.ceil(1.0))
print(math.ceil(100))
print(math.ceil(10/100))
print(math.ceil(100/100))
print(math.ceil(101/100))
print(math.ceil(200/100))