# Name: Hemant Kosaraju
# Computer Science 2720 Lab 4 Section: 014 CRN: 17910
# Lab Time: Wednesday January 31 2024 2:00 PM to 2:50 PM Langdale Hall Room 405
# Due Time: February 4 2024 at 11:59 PM

def Selection_Sort(values): 
    """ define function named Selection_Sort with one parameter value of variable values which is a user defined list """
    for j in range(0, len(values) - 1): 
        """ for each value of the first to the last element - 1 this line will get j which is a temporary variable stored with each element from list one after the other """
        first_index = j 
        """ The variable called first index is initialized and assigned to the variable j """
        for l in range(j+1, len(values)): 
            """ for each value of l which starts its range from the element one after j to last element this line will get l which is a temporary variable stored with each element from list one after the other """
            if values[l] < values[first_index]: 
                """ This line is represented in english as showing that the program will check to see "if" the list element to the right of the temporary variable which is values[l] < is less than the value to the left of the temporary variable j and if it is it will set first_index variable to l """
                first_index = l 
                """ First_index variable is set to l here """
            
        if first_index != j: 
            """ This line is represented in english as showing that the program will check to see "if" the first_index variable which is now assigned to l is != not equal to j which we can see is true """
            (values[j], values[first_index]) = (values[first_index], values[j])  
            """ The line above shows how if the if statement gets executed then the lists right element for the temporary variable will swap places with the left element for the temporary variable
            which is shown in th line above by indexing the element from the list and assigning the reverse to it """

    return values 
    """ Returns the values """

print("\n{}\n".format(Selection_Sort([50, 11, 33, 21, 40, 50, 40, 40, 21])))
print("\n{}{}\n".format(Selection_Sort([89, 2, 47, 33, 17, 50, 40, 67, 6]), " Test Case "))
print("\n{}{}\n".format(Selection_Sort([16, 2, 75, 30, 17, 11, 29, 88, 10]), " Test Case "))