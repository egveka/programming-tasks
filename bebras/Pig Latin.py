# word = str(input())

# vowel = "eyuioa"

# if word[0].lower() in vowel:
#     print(f"{word}-yay")
# else:
#     print(f"{word[1:]}-{word[0]}ay")

vowel = "eyuioa"

words = input().split()

def process_word(word):                                      
    if word[0].lower() in vowel:
        print(f"{word}-yay", end=" ")
    else:
        print(f"{word[1:]}-{word[0]}ay", end=" ")

for word in words:
    process_word(word)
print()