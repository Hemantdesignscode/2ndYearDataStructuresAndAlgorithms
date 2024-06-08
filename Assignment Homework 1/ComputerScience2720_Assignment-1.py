

LST1 = [1, 5, 6, 6, 9, 9, 9, 11, 11, 21] # The defined List 1
LST2 = [6, 6, 9, 11, 21, 21, 21] # The defined List 2

""" Section 1 Of Assignment 1 """

def loopjoin(LST1, LST2): 
    """ The line above defines a function with the name loopjoin which closely relates to how the program runs and takes list 1 and list 2 as parameters """
    Output_lst =  []
    """ The Output_lst variable is initialized and assigned to an empty list which is later used to store the elements in common between both lists """

    for i1 in range(len(LST1)): 
        """ The for loop above goes through n iteration times for the temporary variable i1 for the range being from 0 to the length indexes of LST1 variable which is a list """
        for j2 in range(len(LST2)):
            """ The for loop above goes through m iteration times for the temporary variable j2 for the range being from 0 to the length indexes of LST2 variable which is a list """
            """ This represents O(n ∗ m) or O(mn) """
            if LST1[i1] == LST2[j2] and LST1[i1] not in Output_lst:
                """ The if statement is checking to see if after each iterations the list indexes using i1 for list 1 and j2 for list 2 are equal while also including an AND operator to
                only execute after checking that list1[i1], i1 a temporary placeholder which changes with n iterations is not in the declared and assigned new Output_lst  """
                Output_lst.append(LST1[i1])
                """ This statement appends the LST[i1] element value at that index if it is not already in Output_lst, only executing if the if statement is executed """
                
    if LST1 and LST2 == []:
        print("{}\n".format("One or more lists look to be empty"))
        """ The purpose of this if statement and using and to check an empty list is a test case handler for tests whether either LST1 or LST2 are blank lists which causes
        the print statement to execute letting the user know they have put one or more empty lists to the program """

    return Output_lst
    """Returns the Output_lst after the common elements have been appended"""

print("\nLoopjoin: \n") # Indicates the start of the output screen for the first section of assignment 1 which is loopjoin
print("{}\n".format(loopjoin(LST1, LST2))) 
""" The loopjoin function is called with the original lists from the assignment and outputs the common elements """
print("{}{}\n".format(loopjoin([1, 2, 2, 3, 4, 8, 9, 11, 30, 40, 60, 60], [1, 2, 4, 5, 7, 20, 30, 60, 60]), " Test Case "))
print("{}{}\n".format(loopjoin([6, 6, 7, 8, 9, 10, 11, 13], [2, 4, 16, 20, 25, 74, 13, 6, 8]), " Test Case "))
print("{}{}\n".format(loopjoin([25,30,40, 60, 54, 34, 32, 30, 28, 24], []), " Test Case with Empty List "))
""" The three print statements above are test cases and have been tested to show only the elements in common between both lists and also shows the output for an empty list
these will print test case next to the output list to help the user better understand clearly that these are test cases  """

""" Section 2 Of Assignment 1 """

def Binary_Search(LST1, LST2):
    """ The line above defines a function with the name Binary_Search which closely relates to how the program runs and takes list 1 and list 2 as parameters """

    elementsinbothlists = []
    """ The elementsinbothlists variable is initialized and assigned to an empty list which is later used to store the elements in common between both lists """
    for l in range(0, len(LST2)):
        """ The for loop above goes through n iteration times for the temporary variable l for the range being from 0 to the length indexes of LST2 variable which is a list """
        element = LST2[l]
        """ The element variable is what stores not the indexes of length LST2 but uses those indexes to find the value of the list at each index """
        low, high = 0, len(LST1) - 1
        """ In binary search the implementation of high and low variables """
        while high >= low:
            """ This is a straightforward line that shows that this line will stay executing while the condition of the high variable is greater than or equal to the low variable and
            goes through log m iteration times, which represents n ∗ log m = O(n log(m))  """
            middle_index = ((low + high) // 2)
            """ middle index is found using binary search logic of taking high and low variables then adding them and their sum floor divided // by 2 """
        
            if LST1[middle_index] < element:
                low = middle_index + 1
                """ If the if statement is executed and the value indexed from the middle of list 1 is less than the element value of LST2 at the given index then the low value for the middle_index
                 should be updated to increment by 1 """
            elif LST1[middle_index] > element:
                high = middle_index - 1
                """ If the if statement is executed and the value indexed from the middle of list 1 is greater than the element value of LST2 at the given index then the high value for the middle_index
                 should be updated to decrement by 1 """
            else:
                if element not in elementsinbothlists:
                    elementsinbothlists.append(element)
                break
            """ This else statement shows that if the element actually is not less or greater than the value of list 1 at the given index when the middle_index is updated then the element will
             append to the declared and initialized list elementsinbothlists and then have a break statement to break out of the program without going into an infinite loop """

    if LST1 and LST2 == []:
        print("{}\n".format("One or more lists look to be empty"))
        """ The purpose of this if statement and using and to check an empty list is a test case handler for tests whether either LST1 or LST2 are blank lists which causes
        the print statement to execute letting the user know they have put one or more empty lists to the program """

    return elementsinbothlists
    """Returns the elementsinbothlists after the common elements have been appended"""

print("Binary Search: \n") # Indicates the start of the output screen for the second section of assignment 1 which is Binary Search
print("{}\n".format(Binary_Search(LST1, LST2)))
print("{}{}\n".format(Binary_Search([1, 2, 2, 3, 4, 8, 9, 11, 30, 40, 60, 60], [1, 2, 4, 5, 7, 20, 30, 60, 60]), " Test Case "))
print("{}{}\n".format(Binary_Search([6, 6, 7, 8, 9, 10, 11, 13], [2, 4, 6, 8, 13, 16, 20, 25, 74]), " Test Case "))
print("{}{}\n".format(Binary_Search([25,30,40, 60, 54, 34, 32, 30, 28, 24], []), " Test Case with Empty List "))
""" The three print statements above are test cases and have been tested to show only the elements in common between both lists and also shows the output for an empty list
these will print test case next to the output list to help the user better understand clearly that these are test cases  """

""" Section 3 Of Assignment 1 """

""" Solution 2 can be improved to have a linear runtime of O(m + n) and that might be by using a merging algorithm (not exactly mergesort itself) to combine the 
two lists and then sort through them by finding the common elements between them. This would be possible to do after merging the lists because the logic would be 
to understand these lists when they were separetly searched had elements in common which were then sorted into one output list, the user has to understand that there had to be 
two or more occurances of the same elements which means e.g. if we had two lists and and in list 1 there was a 1 and list 2 also had an element 1 that would make two occurances when looked 
as a combined total number of occurances. Therefore if we were to merge the values which would create a linear runtime O(m + n) we could use binary search on just a single merged list
and look for where there are two or more occurances of a number that will likely represent the element is common in both lists which would make our program have a linear runtime O(n + m). """