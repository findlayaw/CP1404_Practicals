#1.
name = input("Enter your name: ")
file = open("name.txt", "w")
file.write(name)
file.close()

#2
with open("name.txt") as file_read:
    read_name = file_read.read()
    print(f"Your name is {read_name}")

#3.
numbers_read = open("numbers.txt","r")
first_number = int(numbers_read.readline())
second_number = int(numbers_read.readline())
result = first_number + second_number
print(result)
numbers_read.close()

#4
numbers_file = open("numbers.txt","r")
total = 0
for line in numbers_file:
    total += int(line)
print(total)