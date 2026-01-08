# players = input().split()

# prev = ""
# a = 0
# b = 0
# c = 0
# d = 0

# for player in players:
#     if player == "A":
#         a += 1
#         if prev =="A":
#             a += 1
#     elif player == "B":
#         b += 1
#         if prev =="B":
#             b += 1
#     elif player == "C":
#         c += 1
#         if prev =="C":
#             c += 1
#     elif player == "D":
#         d += 1
#         if prev =="D":
#             d += 1

# if a == b:
#     print(a, b)
# elif a == c:
#     print(a, c)
# elif a == d:
#     print(a, d)
# elif b == c:
#     print(b, c)

players = input().split()

prev = ""
scores = {"A":0, "B": 0, "C":0, "D":0}


for player in players:
    score = scores[player]
    score += 1
    if prev == player:
        score += 1
    prev = player
    scores[player] = score

print(max(scores.values()))


# players = input().split()

# prev = ""
# who_won = [0,0,0,0]
#     if player == "A":
#         who_won[0] += 1 
#         if prev =="A":
#             who_won[0] += 1 
#         prev = "A"
#     elif player == "B":
#         who_won[1] += 1 
#         if prev =="B":
#             who_won[1] += 1 
#         prev = "B"
#     elif player == "C":
#         who_won[2] += 1 
#         if prev =="C":
#             who_won[2] += 1
#         prev = "C"
#     elif player == "D":
#         who_won[3] += 1 
#         if prev =="D":
#             who_won[3] += 1
#         prev = "D"

# print(max(who_won))