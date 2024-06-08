# Name: Hemant Kosaraju
# Computer Science 2720 Lab 4 Section: 014 CRN: 17910
# Lab Time: Wednesday January 31 2024 2:00 PM to 2:50 PM Langdale Hall Room 405
# Due Time: February 4 2024 at 11:59 PM


def Insertion_Sort(Listarray):
    """ define a function named Insertion_Sort(Listarray) with Listarray being a parameter for the function and is the variable name of the input list """
    for c in range(0, len(Listarray)):
        """ Similar to Selection sort except without the range being upto len(list) - 1, the for loop in Insertion Sort has a range starting from 0 and ending to the len(list) which is
        length of list """
        key = Listarray[c]
        """ The key is initialized and assigned to being the list variable (name could differ depending on the name of variable which stores the list) index of each temporary place holder of c
        which will change the value of c for each iteration of the range so a different index from the list will be chosen each time """
        e = c - 1
        """ This sets a variable named e i.e. is a placeholder for the arithmetic operation c - 1 which will subtract c from each iteration and the output value is set to variable e """
        while e >= 0 and Listarray[e] > key:
            """ This is like a nested for loop but since it is a while loop used here we can think of it as a nested for-while loop with for loop being main loop and while loop within for loop
            the comparison or program check here are two statements first the while loop is checking for e >= being greater than or equal to 0 but not below 0 and the second check is for 
            the list[temporary index] > being greater than key """
            Listarray[e + 1] = Listarray[e]
            """ Here the temporary value of e which is changing because of line 15 which is e = c - 1 is is getting indexed again with the pseudocode list_name[e + 1] where the temporary index position
            is added by 1 and that statement of list_name[e + 1] = is assigned to list_name[e] of the temporary index value at that index position in the list """
            e = e - 1
            """ e is now reassigned to a similar arithmetic operation just instead of e = c - 1 it is now e = e - 1 """
        Listarray[e + 1] = key 
        """ The statement above is out of the while loop but still in the for loop and it makes sure each value of the list index from 0 to len(list_name) is getting assigned to the key 
        using more detail it is like when we start at the index = 0 on c we can think of the key being the first value of the list key = list_name[c], then e is subtracted from c after that
        in the while loop e is subtracted by 1 which then checks to see if the temporary element of e which changes by iterating the while loop, list_name[e + 1] equals = key """

    return Listarray
    """ Return the list_name """

print("\n{}\n".format(Insertion_Sort([50, 11, 33, 21, 40, 50, 40, 40, 21])))
print("\n{}{}\n".format(Insertion_Sort([80, 67, 39, 22, 2, -1, 16, 75, 40]), " Test Case "))
print("\n{}{}\n".format(Insertion_Sort([90, 17, 49, 76, 23, 12, 34, 12, 78])," Test Case "))