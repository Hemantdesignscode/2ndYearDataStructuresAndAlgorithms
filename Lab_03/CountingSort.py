# Name: Hemant Kosaraju
# Computer Science 2720 Lab_03 Section: 014 CRN: 17910
# Lab Time: Wednesdays Langdale Hall 405 at 2:00 PM to 2:50 PM
# Due Time: Sunday January 28 at 11:59 PM

def Counting_sort(user_defined_list): 
    maximum_value = user_defined_list[0]
    for e in user_defined_list:
        if e > maximum_value:
            maximum_value = e

    length_list = len(user_defined_list)
    output = [0] * length_list
    
    count = [0] * (maximum_value+1)

    for c in user_defined_list:
        count[c] += 1
    
    for j in range(1, maximum_value + 1):
        count[j] += count[j - 1]
    
    for l in range(length_list - 1, -1, -1):
        output[count[user_defined_list[l]] - 1] = user_defined_list[l]
        count[user_defined_list[l]] -= 1
    
    return (output)


print("\n{}\n".format(Counting_sort([50, 11, 33, 21, 40, 50, 40, 40, 21])))
print("\n{} {}\n".format(Counting_sort([90, 90, 39, 67, 89, 90, 39, 91, 100]), "Test case"))
print("\n{} {}\n".format(Counting_sort([-91, 45, 89, 76, 100, 34, 54, -16, 2]), "Test case with negative numbers"))