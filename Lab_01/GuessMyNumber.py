# Name: Hemant Kosaraju
# CSC 2720 Lab 01
# CRN 17910 Section 014
# Lab Time: January 10 2024 2:00 to 2:50 PM
# Due Time: January 14 2024 11:59 PM

n = int(input("\nEnter n: "))
while n == 0 or n < 0:
    n = int(input("Enter a positive integer for n: "))
print("Welcome to Guess My Number! ")
print("Please think of a number between 0 and {}".format(n-1))

""" The function below selects the middle value of the given range and the range would start from 0 to the end which would be the 
user entered number n"""
def middle_value(start, end):
    return (start + end) // 2

start = 0
end = n
middle = middle_value(start, end)

print("Is your number: {}?".format(middle))
print("Please enter C for correct, H for too high, L for too low. ")
user_response = input("Enter your response (H/L/C): ")

while user_response != "C":
    while user_response not in ["H","L","C"]:
        user_response = input("Enter your response (H/L/C): ") 
        """ This code was added to verify the user enters that the guessed number is Higher, Lower, or Correct although if the
        user enters other responses the code reexecutes the previous statement above to ask the user to re enter the response"""
    if user_response == "H": 
        """ The code written sets the range from 0 to the end which would be equal to the middle number if the selected number 
        is said to be too high from the user"""
        end = middle
    if user_response == "L":
        """ The code written sets the range from the starting number which is assigned to the middle number if the selected number
        is said to be too low from the user """
        start = middle
    middle = middle_value(start, end)
    """ The function above that decides the range to select the middle number from """
    print("Is your number: {}?".format(middle))
    print("Please enter C for correct, H for too high, L for too low. ")
    user_response = input("Enter your response (H/L/C): ")

print("Thank you for playing Guess My Number!\n")