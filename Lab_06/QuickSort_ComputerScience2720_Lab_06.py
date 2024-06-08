""" 
Name: Hemant Kosaraju
Computer Science 2720 Lab 06 Section: 014 CRN: 17910
Lab Time: Wednesdays February 14 2024 Langdale Hall
Due Time: Sunday February 18 2024 11:59 PM
"""

LST = [50, 11, 33, 21, 40, 50, 40, 40, 21] # This is the main input LIST 1 which is passed as input  

def quicksort(LST, low, high): # This is defining a function called quicksort taking parameters LST, low , and high

    if low >= high:
        return LST
    """ The code above states that if the low index is greater than the high index then the list is already sorted and paritioned causing it to return LST """

    position_index = partition(LST, low, high) # This is the recursive call to the function defined as partition which also takes LST, low, high as parameters

    quicksort(LST, position_index + 1, high) # This is the recursive call to the quick sort algorithm, however the low index starts from position index + 1
    quicksort(LST, low, position_index - 1) # This is a recursive call to the quick sort algorithm, however the high index is updated to be position index - 1
    
    """ The lines below is to deduplicated the sorted list and it initializes a new array then goes through a for loop from the range low to high and the if statement
    within the for loop is what tells the new array or list that if the element at that index in the LIST is not already found in the new list then it will append that element
    to the list though if it is already in the list it reiterates again until all elements have been iterated """
    Ouptutlist = [] 
    for l in range(low, high):
        if LST[l] not in Ouptutlist:
            Ouptutlist.append(LST[l])
    return Ouptutlist



def partition(LST, low = 0, high = len(LST) - 1): # This is defining a function called partition taking parameters LST, low index which equals zero, and high index which equals the len(LST) - 1

    pivot = LST[high] # This is the pivot which we will use to reference and sort elements either to the left or right of this value based on if the selected value is less than or greater than this pivot
    pi = low - 1 # This is the index that will go through the list with which will change its position within the list
    for j in range(low, high): # For each index in the range from 0 to the high value of len(LST) - 1
        if LST[j] < pivot: # This statement states that if the element in the list LST at that index is less than the pivot value it will [continues on line below]
            pi += 1 # increment this value by 1 for each iteration, while the if statement is true
        
            (LST[pi], LST[j]) = (LST[j], LST[pi]) # This line swaps the value from the list LST at the index pi and the value from the list LST at the index j 
        
        else: # This is the else statement for if the if statement does not get executed
            (LST[pi + 1], LST[high]) = (LST[high], LST[pi + 1]) # The line swaps the value from the list LST at the index pi + 1 and the value from the list LST at the index high
    return pi + 1 # returns the pi + 1 value index to be updated each time the partition function is recursively called in the quicksort function

print("\n{}\n".format(quicksort(LST, 0, len(LST) - 1))) # print function call for the quick sort algorithm
print("{}{}\n".format(quicksort([40, 90, 14, 20, 6, 9, 10, 30, 33, 67, 98, 76, 90, 6, 9, 10], 0, len([40, 90, 14, 20, 6, 9, 10, 30, 33, 67, 98, 76, 90, 6, 9, 10]) - 1), " Test Case ")) # Test Case
print("{}{}\n".format(quicksort([16, 17, 2, 30, 26, 89, 89, 0, 24, 25, 32, 34, 67, 68, 81, 79], 0, len([16, 17, 2, 30, 26, 89, 89, 0, 24, 25, 32, 34, 67, 68, 81, 79]) - 1), " Test Case ")) # Test Case