# Name: Hemant Kosaraju
# CSC 2720 Lab 01
# CRN 17910 Section 014 
# Lab Time: January 10 2024 2:00 to 2:50 PM
# Due Time: January 14 2024 11:59 PM

LST = [50, 11, 33, 21, 40, 50, 40, 40, 21] # This can be any input list 

""" Initializes a new list """
deduplicatelst = []

""" Assigns a variable named error_ for checking the list to see if only integers are passed to the list """
error_ = False

""" The for loop is used to get the elements included in the list named with variable LST """ 
for elements in LST:
    """ The if statement below shows how if the elements are any data type other than integers then the print statement showing an error will execute and the
    variable error_ previously initialized and assigned in line 9 will become True here if the if statement gets executed"""
    if not isinstance(elements, (int)):
        print("\nThere is an error no characters, strings, or decimals should be included within the list \n")
        error_ = True
        break # This is to stop the code from going any further if characters or strings are found to be within the user input list
    
    """ The code below says if elements are not already included at least once in the new list named deduplicate list, then append
        them to the new list if they have been included already at least once do not include them again, this will only work if all elements in the 
        user defined list are integer values """

    if elements not in deduplicatelst:
        deduplicatelst.append(elements)

def bubble_sort(deduplicatelst): # Function is defined here for sorting algorithm of bubble sort, though there are other sorting algorithms like quick sort or merge sort
    n = len(deduplicatelst) # The list's length is assigned to variable n

    if n <= 1: # If the list's length has less than or equal to one element this if statement will return the list as it is since there will be nothing to sort
        return deduplicatelst # return statement to return the list
    
    """ The lines below have a nested for loop which indicates a for loop within a for loop and the first for loop iterates for every element within the 
    given list's length """
    for e in range(n): 
        for c in range(n-e-1):
            if deduplicatelst[c] > deduplicatelst[c+1]:
                
                (deduplicatelst[c], deduplicatelst[c+1]) = (deduplicatelst[c+1], deduplicatelst[c])
    
    return deduplicatelst

sortedlist = bubble_sort(deduplicatelst)

# Binary Search for finding the user entered integer if it exists in the output deduplicate list

if not error_:
    n = int(input("\nEnter your integer that you would like to find: "))
    
    checks = 0
    def Binary_Search(sortedlist, n, low, high):
        global checks
        if high >= low:
            middle_value = (low + (high - low) // 2) # This would be the Optimal way compared to writing middle = (l + r) // 2 which could cause overflow
    
            if n == sortedlist[middle_value]:
                print("\nThe integer {} is found".format(n))
                checks += 1
                print("\nIt took {} checks to find this integer\n".format(checks))
            elif n > sortedlist[middle_value]:
                checks += 1
                return Binary_Search(sortedlist, n, middle_value + 1, high)
            elif n < sortedlist[middle_value]:
                checks += 1
                return Binary_Search(sortedlist, n, low, middle_value - 1)
        else:
            print("\nFailed to find the input number of {}\n".format(n))
    
    
    Binary_Search(sortedlist, n, 0, (len(sortedlist) - 1))