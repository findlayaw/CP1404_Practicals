def main():
    numbers = []
    for i in range(5):
        number = int(input("Enter a number: "))
        numbers.append(number)

    print(f"The first number is {numbers[0]}")
    print(f"The Last number is {numbers[4]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average number is {sum(numbers) / len(numbers)}")

    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    username = input("Enter username: ")
    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")


main()

