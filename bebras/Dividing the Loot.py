# n = int(input())
# result = 0
# desi = 0
# loki = 0

# for j in range(n):
#     necklace = [int(i) for i in input().split()]
#     if necklace[0] > necklace[1] or desi < loki:
#         desi += 1
#     elif necklace[0] < necklace[1] or loki < desi:
#         result += necklace[1]
#         loki += 1
#     print(j, desi, loki, result)

n = int(input())
result = 0

dict = {}
loki_turn = False

for j in range(n):
    necklace = [int(i) for i in input().split()]
    dict[necklace[0]] = necklace[1]
# print(dict)

for x in range(n):
    if not loki_turn:
        # sort by key and delete from dict 
        # for desi
        max_rubies = max(list(dict.keys()))
        dict.pop(max_rubies)
        loki_turn = True
    else:
        # sort by value and delete from dict 
        # for loki with saphire counting
        max_saphires = max(list(dict.values()))
        result += max_saphires
        for key,value in dict.items():
            if max_saphires == value:
                dict.pop(key)
                break
        loki_turn = False
print(result)

# num_lines = int(input())
# loki_sapphires = 0

# # Make two arrays with with the correct number of spaces
# necklaces_rubies = [0] * num_lines
# necklaces_sapphires = [0] * num_lines

# # Fill both arrays with the correct numbers
# for i in range(num_lines):
#     necklace = input().split()
#     necklaces_rubies[i] = int(necklace[0])
#     necklaces_sapphires[i] = int(necklace[1])
    
# # Take turns choosing
# for x in range(num_lines):
#     if x%2 == 0:
#         max_saphires = max(necklaces_sapphires)
#         loki_sapphires += max_saphires
#         index = necklaces_sapphires.index(max_saphires)
#         del necklaces_sapphires[index]
#         del necklaces_rubies[index]
#     else: # Desi's choice
#         max_rubies = max(necklaces_rubies)
#         index = necklaces_rubies.index(max_rubies)
#         del necklaces_sapphires[index]
#         del necklaces_rubies[index]

# print(loki_sapphires)