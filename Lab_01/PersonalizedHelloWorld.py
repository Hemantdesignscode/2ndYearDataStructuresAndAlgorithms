# Name: Hemant Kosaraju
# CSC 2720 Lab 01
# CRN 17910 Section 014 
# Lab Time: January 10 2024 2:00 to 2:50 PM
# Due Time: January 14 2024 11:59 PM

print("\nWhat is your name? ")
users_name = input("Please enter your name: ")

while users_name == "":
    users_name = input("Please enter your name: ")

print("Hello, {}!\n".format(users_name))