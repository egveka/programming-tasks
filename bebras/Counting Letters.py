sentence = input().lower()

consanant = "qwrtpsdfghjklzyxcvbnm"
vowel = "euioa"

v_counter = 0
c_counter = 0

for letter in sentence:
    if letter in consanant:
        c_counter += 1
    elif letter in vowel:
        v_counter += 1

print(f"{v_counter} {c_counter}")