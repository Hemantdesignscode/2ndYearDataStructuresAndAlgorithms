# Name: Hemant Kosaraju
# Computer Science 2720 Lab 4 CRN: 17910 Section: 014
# Lab Time: Wednesday February 7 2024 2:00 PM to 2:50 PM Langdale Hall 405
# Due Time: Sunday February 11 2024 at 11:59 PM
""" 
The sources I used: 
1. GeeksforGeeks Merge Sort - Data Structure and Algorithms Tutorials
"""

LST = [50, 11, 33, 21, 40, 50, 40, 40, 21] # This input list

def Merge_Sort(LST): # we have defined a function known as Merge Sort
    
    if len(LST) <= 1: # The len of list if it is less than or equal to 1 we can assume list had been already sorted to its basic format and return the list
        return LST
    

    middle_index = (len(LST) // 2) # The middle index is found by working with the length of the list and floor dividing by 2 which would choose the lower index value if there happens to be two middle values necessary to take average for them

    left_first_unsorted = LST[:middle_index] 
    """ The line above is the left half """
    right_second_unsorted = LST[middle_index:]
    """ The line above is the right half """

    i = 0 
    j = 0
    """ Variable of iteration for LST[:middle_index] which is left_first_unsorted """
    """ Variable of iteration for LST[middle_index:] which is right_first_unsorted"""
    
    while i < (len(LST) - 1): 
        i += 1
        if i < middle_index:
            left_first_unsorted[i] = LST[i]
            """ These previous lines have defined a while loop and within the list loop the variable i will increment until it increments to where it is greater than
            the length of the list or the last element's index, then if the i value is less than the middle index the left sliced array half will be implemented to include
            the LST value at the index value of i """

        else:
            right_second_unsorted[j] = LST[i]
            j += 1
        """ This is our other variable that we have defined and it is j, the same if happening as previously except these lines say that if the i index value is not less than the 
        middle value then the else statement gets executed which implements to include the LST value at index value of i to the right slided array half """

    Merge_Sort(left_first_unsorted) 
    Merge_Sort(right_second_unsorted)
    merge(LST, left_first_unsorted, right_second_unsorted)
    """ Two recursive calls to the merge_sort function, one for the left sliced array and another for the right sliced array """

    Output_list = [] # A new list to be able to dedeuplicate and append to

    for j in range(0, len(LST)): # a for loop to run through 0 to the length of the original input array
        if LST[j] not in Output_list: # within the for loop is the element at index j in the LST array input is not already appended or found within the Output_list then it will get appended to the list
            Output_list.append(LST[j]) # append function for the new list

    return Output_list # returns the deduplicated list after using the merge sort on the input

def merge(LST, left_first_unsorted, right_second_unsorted): # This is the merge function
    j, l, k = 0, 0, 0 # we have defined variables j, l, k to be 0

    left_index = len(LST) // 2 
    right_index = len(LST) - left_index
    """ These two variables were created to be temporary for the while loops to merge the sliced elements together """

    while l < left_index and k < right_index:
        if left_first_unsorted[l] < right_second_unsorted[k]:
            LST[j] = left_first_unsorted[l]
            j += 1
            l += 1

        else:
            LST[j] = right_second_unsorted[k]
            j += 1
            k += 1
    
    while l < left_index:
        LST[j] = left_first_unsorted[l]
        j += 1
        l += 1
    
    while k < right_index:
        LST[j] = right_second_unsorted[k]
        j += 1 
        k += 1

    """ These three while loops go thorugh the right index and left index to find any elements which are not sorted and checks them one by one by incrementing its index value by 1
    while the variables are less than either the right sliced index value or the left sliced index value """

print("\n{}\n".format(Merge_Sort(LST))) # Function call using print to return the output of the list
print("{}{}\n".format(Merge_Sort([89, 76, 40, 13, 2, 70, 84, 60, 60, 74, 2]), " Test Case ")) 
print("{}{}\n".format(Merge_Sort([37, 45, 20, 6, 14, 90, 125, 110, 66, 74, 2]), " Test Case "))