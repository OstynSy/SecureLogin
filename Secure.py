from passlib.hash import pbkdf2_sha256


class Login:
    def __init__(self, u, p, ul, pl):
        self.username = u
        self.password = p
        self.username_length = ul
        self.password_length = pl

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def verification(self):
        verify_pass = False
        cur_username_len = len(self.username)
        cur_password_len = len(self.password)

        if cur_username_len not in range(1, self.username_length) and cur_password_len not in \
                range(1, self.password_length):
            print("Username and password length is not in range of (0 - length)")
            return False

        if cur_username_len not in range(1, self.username_length):
            print("Username length is not in range of (0 - length)")
            return False

        if cur_password_len not in range(1, self.password_length):
            print("Password length is not in range of (0 - length)")
            return False

        with open("Secret.txt", "r") as file:
            for line in file:
                if self.username in line:
                    if (self.username + " "*(self.username_length - len(self.username))) == line[0:self.username_length]:
                        data_password = line[self.username_length + 3:self.username_length + 90]
                        verify_pass = pbkdf2_sha256.verify(self.password, data_password)
                        break
                else:
                    print("sorry username does not exist")
                    break

            if verify_pass is True:
                file.close()
                print("acc verified")
                return True
            else:
                file.close()
                print("acc not verified")
                return False


class Register:
    def __init__(self, u, p, ul, pl):
        self.stored_username = u
        self.stored_password = pbkdf2_sha256.hash(p)
        self.username_length = ul
        self.password_length = pl

    def get_username(self):
        return self.stored_username

    def get_password(self):
        return self.stored_password

    def create_acc(self):
        st_username_len = len(self.stored_username)
        st_password_len = len(self.stored_password)

        if st_username_len not in range(1, self.username_length) and st_password_len not in \
                range(1, self.password_length):
            print("Username and password length is not in range of (0 - length)")
            return False

        if st_username_len not in range(1, self.username_length):
            print("Username length is not in range of (0 - length)")
            return False

        if st_password_len not in range(1, self.password_length):
            print("Password length is not in range of (0 - length)")
            return False

        with open("Secret.txt", "r") as file:
            for line in file:
                if self.stored_username in line:
                    if (self.stored_username + " " * (self.username_length - len(self.stored_username))) == line[
                                                                                            0:self.username_length]:
                        file.close()
                        print("acc not created bcus user already exists")
                        return False
            else:
                file.close()
                with open("Secret.txt", "a") as f:
                    line = [self.stored_username, self.stored_password]
                    f.writelines(line[0] + " "*(self.username_length - len(line[0])) + "|| " + line[1] + "\n")
                    f.close()
                    print("acc created successfully")
                return True

