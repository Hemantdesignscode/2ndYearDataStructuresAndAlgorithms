# Name: Hemant Kosaraju
# Computer Science Lab_03 Section: 014 CRN: 17910
# Lab Time: Wednesdays Langdale Hall 405 at 2:00 PM to 2:50 PM
# Due Time: Sunday January 28 at 11:59 PM


# Big-O Time Analysis for Bubble Sort

def Bubble_sort(unsorted_user_list):
    length_list = len(unsorted_user_list) # 1 step

    if length_list <= 1: # 1 time
        return unsorted_user_list # 1 step
    
    if unsorted_user_list == []: # 1 step
        print([]) # 1 step
    
    for e in range(length_list): # n times
        for c in range(length_list-e-1): # n times
            if unsorted_user_list[c] > unsorted_user_list[c+1]: # 2 steps

                (unsorted_user_list[c], unsorted_user_list[c+1]) = (unsorted_user_list[c+1], unsorted_user_list[c]) # 2 steps
            
    return(unsorted_user_list) # 1 step

Bubble_sort([50, 11, 33, 21, 40, 50, 40, 40, 21]) # 1 step

""" The time complexity for Bubble Sort should be 1 + 1 + 1 + 1 + n*n + 2 + 2 + 1 + 1 = n² + 10 = O(n²) Quadratic time because we drop constants """

# Big-O Space Analysis for Bubble Sort

def Bubble_sort(unsorted_user_list): # input size n
    length_list = len(unsorted_user_list)  # no space

    if length_list <= 1: # no space
        return unsorted_user_list # no space
    
    if unsorted_user_list == []: # no space
        print([]) # no space
    
    for e in range(length_list): # 1 space for e
        for c in range(length_list-e-1): # 1 space for c
            if unsorted_user_list[c] > unsorted_user_list[c+1]: # no space

                (unsorted_user_list[c], unsorted_user_list[c+1]) = (unsorted_user_list[c+1], unsorted_user_list[c]) # no space
            
    return (unsorted_user_list) # no space

Bubble_sort([50, 11, 33, 21, 40, 50, 40, 40, 21]) # 1 space

""" The Space Complexity for Bubble Sort should be 1*1 + 1 = 2 = O(1) Constant space allocated """

# Big-O Time Analysis for Counting Sort

def Counting_sort(user_defined_list): 
    maximum_value = user_defined_list[0] # 1 step
    for e in user_defined_list: # 1 step, for n times
        if e > maximum_value: # 1 step
            maximum_value = e # 1 step

    length_list = len(user_defined_list) # 1 step
    output = [0] * length_list # 1 step
    
    count = [0] * (maximum_value+1) # 1 step

    for c in user_defined_list: # 1 step, for n times
        count[c] += 1 # 1 step
    
    for j in range(1, maximum_value + 1): # n times
        count[j] += count[j - 1] # 1 step
    
    for l in range(length_list - 1, -1, -1): # n times
        output[count[user_defined_list[l]] - 1] = user_defined_list[l] # 3 steps
        count[user_defined_list[l]] -= 1 # 2 steps
    
    return (output) # 1 step


Counting_sort([50, 11, 33, 21, 40, 50, 40, 40, 21]) # 1 step

""" The time complexity for Counting Sort should be 1 + 1*n + 1 + 1 + 1 + 1 + 1 + 1*n + 1*n + 1*n + 5*n = 9n + 6 = O(n) Linear Time because we drop constants """

# Big-O Space Analysis for Counting Sort

def Counting_sort(user_defined_list): # input size n
    maximum_value = user_defined_list[0] # no space
    for e in user_defined_list: # 1 space for e
        if e > maximum_value: # no space
            maximum_value = e # no space

    length_list = len(user_defined_list) # no space
    output = [0] * length_list # n space - because of additional initialization of space
    
    count = [0] * (maximum_value+1) # n space - because of additional initialization of space

    for c in user_defined_list: # 1 space for c
        count[c] += 1 # no space
    
    for j in range(1, maximum_value + 1): # 1 space for j
        count[j] += count[j - 1] # no space
    
    for l in range(length_list - 1, -1, -1): # 1 space for l
        output[count[user_defined_list[l]] - 1] = user_defined_list[l] # no space
        count[user_defined_list[l]] -= 1 # no space
    
    return (output) # no space


Counting_sort([50, 11, 33, 21, 40, 50, 40, 40, 21]) # 1 space

""" The Space Complexity for Counting Sort should be 1 + n + n + 1 + 1 + 1 = 2n + 4 = O(n) Linear space allocated """

""" After calculating time complexities and spaces for both algorithms I have seen that both have different space and time complexities. I would say it is very close between both algorithms 
in terms of how they function, though if your hardware or software might be old or has less components that have fast processing speeds then Counting sort should be used over 
Bubble Sort because the running time of Counting Sort is linear which means the size of the data corresponds to the time taken to execute or sort the input. For Bubble Sort the time it 
takes to run the program is the square of the input passed which means the greater the data (input) the slower the time. When resources are low I would say to go with Counting Sort algorithm 
and when resources are already high end and have good processing speeds then it will be better to still use Counting Sort although using Bubble Sort will take near
to the same time while taking less space with an unnoticable difference. """