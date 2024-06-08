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

    """ prints the deduplicated sorted list """
    print(deduplicatelst) 

""" Calls the defined bubble_sort() function to receive the print statement of the deduplicated sorted list when error_ is False and not True since the 
error_ variable is False by defult if the if statement at line 15 is not executed this statement would be if not error_ which is if not False == to if True 
the bubble sort function is executed whilst if error_ is True then if not error_ would make that if not True which is if False the bubble sort function is
not executed """
if not error_:
    bubble_sort(deduplicatelst)