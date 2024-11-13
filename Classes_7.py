class User:
    def __init__(self, username, email):
        """Initialize the user with a username, email, and login attempts."""
        self.username = username
        self.email = email
        self.login_attempts = 0

    def increment_login_attempts(self):
        """Increase the login attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the login attempts back to 0."""
        self.login_attempts = 0


user = User("john_doe", "john@example.com")


user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()


print(f"Login attempts for {user.username}: {user.login_attempts}")

user.reset_login_attempts()

print(f"Login attempts after reset for {user.username}: {user.login_attempts}")

class Admin(User):
    def __init__(self,username,email):
        self.privileges = ["can add post",
                      "can delete post",
                      "can ban user"]

        super().__init__(username,email)
        self.Admin = self.privileges

    def show_privileges(self):
        if self.Admin:
            print(f"The User is -> {self.username} : {self.email}")
            for get_value in self.Admin:
                print(" -" + get_value)
        else:
            print("Something Wrong")

value_Admin = Admin("adanielle","adanskie2555@gmail.com")
value_Admin.show_privileges()

class Privileges:
    def __init__(self):
        self.privileges = Admin("adanielle","adanskie2555@gmail.com")

    def show_privileges(self):
        print("privileges")
        for get_privileges in self.privileges.privileges:
            print(" -" + get_privileges)

print("\n")
result = Privileges()
result.show_privileges()
