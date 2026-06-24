correct_username = "admin"
correct_password = "password123"
attempts = 0
while attempts < 3:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username == correct_username and password == correct_password:
        print("Login successful!")
        break
    else:
        attempts += 1
        print(f"Incorrect credentials. You have {3 - attempts} attempts left.")