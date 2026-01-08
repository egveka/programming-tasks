children = int(input())

tall = 0
for i in range(children):
    height = float(input())
    if height >= 1.2:
        tall += 1
print(tall)