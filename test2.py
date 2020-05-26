from Secure import *

username = input("Username: ")
password = input("Password: ")

user_reg = Register(username, password, 12, 12)
user = Login(username, password, 12, 12)

choice = int(input("Login(1) or register(2): "))

if choice == 1:
    user.verification()
elif choice == 2:
    user_reg.create_acc()
else:
    print("none")
