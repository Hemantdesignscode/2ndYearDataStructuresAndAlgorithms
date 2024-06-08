# Name: Hemant Kosaraju
# Computer Science 2720 Lab 4 Section: 014 CRN: 17910
# Lab Time: Wednesday January 31 2024 2:00 PM to 2:50 PM Langdale Hall Room 405
# Due Time: February 4 2024 at 11:59 PM

# Big-O time complexity analysis Insertion Sort

def Insertion_Sort(Listarray):
    for c in range(0, len(Listarray)): # n times
        key = Listarray[c] # 1 time
        e = c - 1 # 1 time
        while e >= 0 and Listarray[e] > key: # n times
            Listarray[e + 1] = Listarray[e] # 1 time
            e = e - 1 # 1 time
        Listarray[e + 1] = key # 1 time

    return Listarray # 1 time

print("\n{}\n".format(Insertion_Sort([50, 11, 33, 21, 40, 50, 40, 40, 21]))) # 1 time

""" The Insertion Sort algorithm has a time complexity of n∗1∗1∗n∗1∗1 + 1 + 1 + 1 = n∗n + 3 = O(n²) Quadratic runtime """

# Big-O space complexity analysis Insertion Sort

def Insertion_Sort(Listarray): # input size n
    for c in range(0, len(Listarray)): # 1 space unit for c
        key = Listarray[c] # no space, assignment uses no new space
        e = c - 1 # no space, assignment uses no new space
        while e >= 0 and Listarray[e] > key: # no space, because while loop uses variables that have already been declared and no new variables are being stored not even temporarily
            Listarray[e + 1] = Listarray[e] # no space, assignment uses no new space
            e = e - 1 # no space, assignment uses no new space
        Listarray[e + 1] = key # no space, assignment uses no new space

    return Listarray # no space, returns value therefore no extra space

print("\n{}\n".format(Insertion_Sort([50, 11, 33, 21, 40, 50, 40, 40, 21]))) # 1 space

""" The Insertion Sort algorithm has a space complexity of 1 + 1 = 2 = O(1) Constant Space allocated """

# Big-O time complexity analysis Selection Sort

def Selection_Sort(values):
    for j in range(0, len(values) - 1): # n times
        first_index = j # 1 time
        for l in range(j+1, len(values)): # n times
            if values[l] < values[first_index]: # 2 times
                first_index = l # 1 time
            
        if first_index != j: # 1 time
            (values[j], values[first_index]) = (values[first_index], values[j]) # 2 times

    return values  # 1 time

print("\n{}\n".format(Selection_Sort([50, 11, 33, 21, 40, 50, 40, 40, 21]))) # 1 time

""" The Selection Sort algoirthm has a time complexity of n∗1∗n + 2 + 1 + 1 + 2 + 1 + 1 = n² + 8 = O(n²) Quadratic runtime """

# Big-O space complexity analysis Selection Sort

def Selection_Sort(values): # input size n 
    for j in range(0, len(values) - 1): # 1 space unit for j, because a temporary space is utilized to store the variable each iteration
        first_index = j # no space, assignment
        for l in range(j+1, len(values)): # 1 space unit for l, because a temporary space is utilized to store the variable each iteration
            if values[l] < values[first_index]: # no space, because if statement uses no new space these variables are within the program and have been declared
                first_index = l # no space, because assignment uses no new space
            
        if first_index != j: # no space, because if statement uses no new space these variables are within the program and have been declared
            (values[j], values[first_index]) = (values[first_index], values[j]) # no space, because assignment uses no new space

    return values # no space, returns value therefore no extra space

print("\n{}\n".format(Selection_Sort([50, 11, 33, 21, 40, 50, 40, 40, 21]))) # 1 space

""" The Selection Sort algorithm has a space complexity of 1∗1 + 1 = 1 + 1 = 2 = O(1) Constant Space allocated """