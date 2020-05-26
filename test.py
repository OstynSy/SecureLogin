from Secure import Login
from Secure import Register


user = Login("Billie", "Jean", 12, 12)

user_reg = Register("Billie", "Jean", 12, 12)
user_reg1 = Register("23weJoe", "Jay", 12, 12)

print("Login:")
print("Username: " + user.get_username())
print("Password: " + user.get_password())

print("\n")

print("Register:")
print("Username: " + user_reg.get_username())
print("Password: " + user_reg.get_password())

print("\n")

print("false = account not created, true = account created")
print("reg account create")
print(user_reg.create_acc())

print("\n")

print("reg account create1")
print(user_reg1.create_acc())

print("\n")
print("is there an account with this username and pass?")
print(user.verification())

print("\n")
print("is there an account with this username and pass?")
user = Login("Billied", "Joee", 12, 12)
print(user.verification())