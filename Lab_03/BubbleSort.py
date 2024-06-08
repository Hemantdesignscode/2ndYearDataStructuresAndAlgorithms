# Name: Hemant Kosaraju
# Computer Science 2720 Lab_03 Section: 014 CRN: 17910
# Lab Time: Wednesdays Langdale Hall 405 at 2:00 PM to 2:50 PM
# Due Time: Sunday January 28 at 11:59 PM



def Bubble_sort(unsorted_user_list):
    length_list = len(unsorted_user_list)

    if length_list <= 1:
        return unsorted_user_list
    
    if unsorted_user_list == []:
        print([])
    
    for e in range(length_list):
        for c in range(length_list-e-1):
            if unsorted_user_list[c] > unsorted_user_list[c+1]:

                (unsorted_user_list[c], unsorted_user_list[c+1]) = (unsorted_user_list[c+1], unsorted_user_list[c])
            
    return (unsorted_user_list)

print("\n{}\n".format(Bubble_sort([50, 11, 33, 21, 40, 50, 40, 40, 21])))
print("\n{} {}\n".format(Bubble_sort([-15, -90, 90, 80]), "Test case"))
print("\n{} {}\n".format(Bubble_sort([80, 67, 100, 35, 17, 2, 9, 16]), "Test case"))