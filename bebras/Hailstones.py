num = int(input())

odd_counter = 0
even_counter = 0

def iseven(num):
    if num % 2 == 0:
        return True
    else:
        return False

if iseven(num):
    even_counter += 1
else:
    odd_counter += 1


while num > 1:
    if iseven(num):
        num = num / 2
        even_counter += 1
    else:
        num = (num * 3) + 1
        odd_counter += 1

print(even_counter)
print(odd_counter)