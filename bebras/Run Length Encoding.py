string = input()
prev = string[0]
counter = 1

for i in range(1, len(string)):
    curr = string[i]
    if prev == curr:
        # print(i, prev, curr,sep=", ")
        counter += 1
        # print()
    else:
        print(prev, counter, sep="", end=" ")
        counter = 1
    if i == len(string) - 1:
        print(curr, counter, sep="")
    prev = curr