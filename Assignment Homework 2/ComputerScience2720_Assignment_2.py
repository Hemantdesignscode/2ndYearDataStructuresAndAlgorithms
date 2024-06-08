""" 
Name:Hemant Kosaraju
Computer Science 2720 Data strutures and Algorithms Assignment 2
February 20 2024 
"""

""" First Exercise of Assignment 2 """

def has_duplicates_word_finder(n, words): # We have defined a function to find if a list includes duplicates, and the input parameters taken are an integer and the list
    """ To make sure each the number entered matches the number of elements in the list words """
    count = 0 # This count variable is declared to keep track of the number of elements in the list
    for j in range(0, len(words)): # The for loop iterates through the range of the length of the list words
        count += 1 # For each index found; the count variable increases by 1
    if count != n: # This if statement functions as one of the test cases to check if the amount of elements checked with the count variable equals the user inputted integer of elements
        return ("\nThe number of elements in the list {} do not equal the entered number {}".format(count, n)) # This would be the custom error message that returns or prints if the if statement were to be executed
    if words == []: # This is another if statement that functions as a test case to check if the given list is empty when the count == the user inptutted integer
        return ("\nThere are no elements in the list it is an empty list, please enter strings") # This would be the custom error message that returns or prints if the user enters an empty list
    
    for e in range(0, len(words)): # The for loop iterates through the range of the length of the list words; with temporary storage e
        for l in range(e+1, len(words)): # The nested for loop iterates from range temporary storage of [e + 1] to the length of the list words; with temporary storage l
            if words[e] == words[l]: # The if statement checks to see if any of the elements [strings] within the same list at two different positions are equal to each other 
                return True # if strings are equal; return True
    else:
        return False # else; if strings are not equal; return False
        
print("\n{}\n".format(has_duplicates_word_finder(5, ["spring", "summer", "fall", "summer", "winter"]))) # A Test Case that functions normally as intended
print("{}\n".format(has_duplicates_word_finder(4, ["spring", "summer", "fall", "winter"]))) # A Test Case that functions normally as intended
print("{}\n".format(has_duplicates_word_finder(5, ["January", "January", "February", "March", "June"]))) # A Test Case that functions normally as intended
print("{}\n".format(has_duplicates_word_finder(4, ["spring", "summer", "fall"]))) # A Test Case that is intentionally created as a test case with unmatched value and list elements
print("{}\n".format(has_duplicates_word_finder(0, []))) # A Test Case that is intentionally created as a test case with 0 integer and empty list


""" Second Exercise of Assignment 2 """

def sort_flowers(n, flowers): # We have defined a function to sort a list of flower names by their first character, and the input parameters taken are an integer and the list
    """ To make sure each the number entered matches the number of elements in the list words """
    count = 0 # This count variable is declared to keep track of the number of elements in the list
    for f in range(0, len(flowers)): # The for loop iterates through the range of the length of the list flowers
        count += 1 # For each index found; the count variable increases by 1
    if count != n: # This if statement functions as one of the test cases to check if the amount of elements checked with the count variable equals the user inputted integer of elements
        return ("\nThe number of elements in the list {} do not equal the entered number {}".format(count, n))  # This would be the custom error message that returns or prints if the if statement were to be executed
    if flowers == []: # This is another if statement that functions as a test case to check if the given list is empty when the count == the user inptutted integer
        return ("\nThere are no elements in the list it is an empty list, please enter flower names in string format") # This would be the custom error message that returns or prints if the user enters an empty list
    
    for name_flower in range(0, len(flowers)): # The for loop iterates through the range from 0 to the length of the list flowers; with temporary storage name_flower
        for next_flower in range(name_flower + 1, len(flowers)): # The nested for loop iterates from range temporary storage [name_flower + 1] to the length of the list flowers; with temporary storage next_flower
            if flowers[name_flower][0] > flowers[next_flower][0]: # The if statement is a sorting algorithm which basically is comparing the ASCII values of the first character of the two strings it is comparing

                (flowers[name_flower], flowers[next_flower]) = (flowers[next_flower], flowers[name_flower]) # if the ASCII value of the first character is greater than the ASCII value of the second character; then the first string switches positions in the list flowers with the second string 
    if not (65 <= ord(flowers[name_flower][0]) <= 90 ): # This if statement is another test case that had to use ord unlike the if statement above because it has to compare integers with integers; therefore this if statement ensures that only CAPITAL letters for the first character of each string are accepted and lowercase letters will cause this if statement to execute 
        return ("The sorting algorithm had not correctly displayed output caused by a Lowercase starting letter of a string, please use an Uppercase CAPITAL letter for starting letter of each string") # This would be the custom error message that returns or prints if the user enters their strings starting with a lowercase letter in their input list

    return flowers # return the sorted List

print("\n{}\n".format(sort_flowers(3, ["Rose", "Lily", "Tulip"]))) # A Test Case that functions normally as intended
print("{}\n".format(sort_flowers(4, ["Magnolia", "Hibiscus", "Maple", "Amaranth"]))) # A Test Case that functions normally as intended
print("{}\n".format(sort_flowers(5, ["Loquat", "Fennel", "Palm", "Guava", "Lantana"]))) # A Test Case that functions normally as intended
print("{}\n".format(sort_flowers(5, ["Blueberry", "Pine", "Maple", "guava", "lavender"]))) # A Test Case that is intentionally created as a test case with lowercase starting letter
print("{}\n".format(sort_flowers(4, ["Magnolia", "Hibiscus", "Maple"]))) # A Test Case that is intentionally created as a test case with unmatched value and list elements
print("{}\n".format(sort_flowers(0, []))) # A Test Case that is intentionally created as an empty list and 0 integer


""" Third Exercise of Assignment 2 """

def reverse_list(LST): # A function defined with name reverse_list and takes the list as input parameter
    for j in range(len(LST) // 2): # A for loop is iterating through the range of the total length of the list // [floor divided] by 2 which can also be thought of as the middle index; with temporary storage j

        (LST[j], LST[len(LST) - j - 1]) = (LST[len(LST) - j - 1], LST[j])

        """ The lines above sorts this algorithm in a particular way to explain it let us take the List = [3, 4, 7, 6, 1] e.g. and when we get the 
        for j in range(len (LST) // 2) that would mean total length = 5 // 2 = 2.5 rounded down would be 2 index so the range would go through j being 0, 1, 2 
        then for the sorting algorithm when j is 0 it can be thought of as LST[0] = 3 and LST[len(LST) - 0 - 1] = 1 so the 1 and 3 switch positions or indexes, next
        for when j is 1 it can be thought of as LST[1] = 4 and LST[len(LST) - 1 - 1] = 6 so the 4 and 6 switch positions or indexes, and finally when j is 2 then
        LST[2] = 7 and LST[len(LST) - 2 - 1] = 7 because they are equal 7 is already thought of being sorted therefore it will remain in the middle index position """
        
    if LST == []: # Checks to see if the list passed is empty
        return ("The list is empty please make an array consisting of integers and try again") # The custom error message that returns or prints if the if statement executes

    return LST  # return the reversed list

print("\n{}\n".format(reverse_list(LST = [3, 4, 7, 6, 1]))) # A Test Case that functions as intended
print("{}\n".format(reverse_list(LST = [6, 16, 90, 14, 80, 78, 40]))) # Test case that functions as intended
print("{}\n".format(reverse_list(LST = [18, 56, 89, 76, 34, 29, 66]))) # Test case that functions as intended
print("{}\n".format(reverse_list(LST = [32, 76, 5, 45, 12, 69, 10]))) # Test case that functions as intended
print("{}\n".format(reverse_list(LST = []))) # A Test case intentionally created to be empty for test case