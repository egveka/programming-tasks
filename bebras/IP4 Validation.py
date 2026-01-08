# ip = [int(i) for i in input().split(".")]

# if len(ip) == 4:
#     if ip[0] <= 255 and ip[1] <= 255 and ip[2] <= 255 and ip[3] <= 255:
#         if ip[0] >= 0 and ip[1] >= 0 and ip[2] >= 0 and ip[3] >= 0:
#             print("Valid IP adress")
#         else: 
#             print("Invalid IP adress")
#     else: 
#         print("Invalid IP adress")
# else: 
#     print("Invalid IP adress")

ip = input().split(".")

if len(ip) != 4:
    print("Invalid IP address")
else:
    if ip[0].isnumeric() == False or ip[1].isnumeric() == False or ip[2].isnumeric() == False or ip[3].isnumeric() == False:
        print("Invalid IP address")
    else:
        if int(ip[0]) > 255 or int(ip[0]) < 0 or int(ip[1]) > 255 or int(ip[1]) < 0 or int(ip[2]) > 255 or int(ip[2]) < 0 or int(ip[3]) > 255 or int(ip[3]) < 0:
            print("Invalid IP address")
        else:
            print("Valid IP address")