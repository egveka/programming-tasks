coffees = int(input())
price = float(input())

if coffees >= 5:
    disc = price/10
    answ =(price - disc)*coffees
    print(f"{answ:.2f}")
else:
    answ = (round(price*coffees, 2))
    print(f"{answ:.2f}")