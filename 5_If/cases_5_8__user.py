users = ['Admin', 'Lory', 'Justin', 'Black']
# users = []
if users:
    for user in users:
        if user == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello " + user + ", thank you for logging in again")
else:
    print("We need to find some users")


print("\n\n\n5-10 检查用户名\n")

current_users = ['John', 'Alex', 'Paul', 'Shine', 'Scott']
new_users = ['Alex', 'Bingo', 'Ultra', 'Scott']
for user in new_users:
    if user.lower() not in [u.lower() for u in current_users]:
        print("Welcome " + user)
    else:
        print("Sorry this name (" + user + ") is already in use")


print("\n\n\n5-11 序数\n")

ordinals = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in ordinals:
    if number == 1:
        print(str(number) + "st")
    elif number == 2:
        print(str(number) + "nd")
    elif number == 3:
        print(str(number) + "rd")
    else:
        print(str(number) + "th")
