correct_password = "Saf.the.great"
max_attempt = 3

for attempt in range(max_attempt):
    password = input("Enter the password: \n")
    if password == correct_password:
        print("Access granted")
        break
    else:
        print("Access denied")
else:
        print('Too many failed attempts')