flowers = input().split()

new_flowers = []
for flower in flowers:
    if flower not in new_flowers:
        new_flowers.append(flower)

print(*new_flowers)