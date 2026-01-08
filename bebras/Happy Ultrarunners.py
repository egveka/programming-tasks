ultruners = int(input())

def is_happy(points):
    old_point = -1
    for point in points:
        if old_point >= point:
            return False
        else:
            old_point = point
    return True             

happy = 0
for i in range(ultruners):
    points = [int(i) for i in input().split()]
    if is_happy(points):
        happy += 1
print(happy)