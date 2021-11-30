try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")


"""
#When will a ValueError occur?
 When something that is not a number is inputted

#When will a ZeroDivisionError occur?
 When the denominator is 0

#Could you change the code to avoid the possibility of a ZeroDivisionError?
 
"""