min = int(input())
essay = input()

lessay = essay.split(" ")

if len(lessay) < min:
    print(f"{min-len(lessay)} below target")
else:
    print("target met")