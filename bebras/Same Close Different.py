num1 = int(input())
num2 = int(input())

if num1 == num2:
    print("same")
elif num1 + 1 == num2 or num1 - 1 == num2:
    print("close")
else:
    print("different")