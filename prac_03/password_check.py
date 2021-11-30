def main():
    password = input("Password: ")
    output = hidePassword(password)
    print(f"Password: {output}")


def hidePassword(password):
    new_password = (len(password) * "*")
    return new_password

main()