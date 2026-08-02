# username is no longer or shorter than 3< < 12
# username has no digits
# username must not contain spaces

while True:
    username = input("username: ")
    if not username.isalpha():
        print("Invalid")
    elif username.count(" ") > 0:
        print("Invalid")
    elif 3> len(username) or len(username)>12:
        print("Invalid")
    else:
        print("Username accepted")
        break
