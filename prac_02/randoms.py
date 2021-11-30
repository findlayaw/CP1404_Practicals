import random
print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

"""
#What did you see on line 1?
#What was the smallest number you could have seen, what was the largest?
- it gave randoms numbers ranging from 5 to 20, 5 being the smallest
and 20 being the largest.

#What did you see on line 2?
#What was the smallest number you could have seen, what was the largest?
#Could line 2 have produced a 4?
- It gave the numbers 3, 5, 7, 9. 3 being the smallest and 9 being the
largest. It could not produce a 4

#What did you see on line 3?
#What was the smallest number you could have seen, what was the largest?
 - it gave 16 s.f numbers from 2.5 to 5.5, 2.5 being the smallest and 5.5 being the largest.

#Write code, not a comment, to produce a random number between 1 and 100 inclusive.
"""
print(random.randint(1, 100))