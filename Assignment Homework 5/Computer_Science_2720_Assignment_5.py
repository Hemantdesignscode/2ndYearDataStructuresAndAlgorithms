
""" 
Student: Hemant Kosaraju
Computer Science 2720 Assignment 5
Date: April 14, 2024
"""

""" Assignment 5 Question 1 Determining if a list of nodes is considered to be A Binary Search Tree or not """

def ISConsideredBinarySearchTree(LST): # A function named if ISConsideredBinarySearchTree taking the LST list as a parameter 
    for root in range(len(LST)): # the root temporary variable iterates for the range of len(LST) # Time: O(n), Space: O(1)
        left = 2*root + 1 # the left nodes of the tree within the list could be seen from applying this logic where each 1 index away from 2 * the root temporary variable are each of the left nodes 
        right = 2*root + 2 # the right nodes of the tree within the list could be seen from applying this logic where each 2 index away from 2 * root temporary variable are each of the right nodes 

        if left < len(LST) and LST[root] <= LST[left]: 
            """ The if condition first checks the left variable being less than the length of the list and then checks the LST at the root index of the iteration 
            to see if it is less than or equal to the left variable index and if it is it should output or return False because root is supposed to be greater than its
            left child node"""
            return False # returns False 
        
        if right < len(LST) and LST[root] >= LST[right]:
            """ The if condition first checks the right variable being less than the length of the lsit and then checks the LST at the root index of the iteration
            to see if it is greater than or equal to the right variable index and if it is it should output or return False because root is supposed to be less than its
            right child node """
            return False # returns False 
        """ If all conditions are false and the if conditions are not executed then the return True statement would execute indicating the LST of nodes to be 
        a Binary Search Tree algorithm if it was made into a binary search tree since child nodes to the left of parent node would be less than parent and child nodes
        to the right of parent node would be greater than parent node """
    return True # returns True 

print("\nNot a Test Case List: {}\n".format(ISConsideredBinarySearchTree(LST = [10, 5, 15, 2, 7, 11, 25, 1]))) # This is the default given list from assignment 
print("Test Case 1: {}".format(ISConsideredBinarySearchTree(LST = [2, 4, 5]))) # test case 1 with a value of the root node being less than left node causing if statement 1 to execute 
print("Test Case 2: {}".format(ISConsideredBinarySearchTree(LST = [3, 9, 0, 8, 14, 17, 19, 11]))) # test case 2 with left node being greater than root and right node being less than root 
print("Test Case 3: {}".format(ISConsideredBinarySearchTree(LST = []))) # test case 3 with empty list which has been found to output tree to be a binary search tree 
print("Test Case 4: {}".format(ISConsideredBinarySearchTree(LST = [3, 2, 12, 1, 13, 10, 20]))) # Test case 4 to have root node with less value left node and great value right node, then follows the same child left less and child right greater for each parent node 


""" Assignment 5 Question implementation task 1 of 2 using sorting algorithm """

LST = [1,2,1,3,2,2] # The initial list storing n values into LST with or without duplicates # Time: O(1), Space: O(n)

""" Selection sort algorithm below """
for j in range(len(LST)): # the for loop iterates a temporary variable j for the range of the length of the LST variable # Time: O(n^2), Space: O(1)
    first_index = j # The first index variable name is set to j # Time: O(1), Space: O(1)
    for r in range(j+1, len(LST)): # the for loop iterates another temporary variable r for the range starting at previous temporary variable + 1, to the length of the LST # Time: O(n), Space: O(1)
        if LST[r] < LST[first_index]: # The if statement checks to see if the index of the list at the second temporary variable is less than the index of the list at the first index variable # Time: O(1), Space: O(1)
            first_index = r # if statement would cause first_index variable to set or assign to r (our second temporary variable) # Time: O(1), Space: O(1)
    
    if first_index != j: # this is statement is what would cause the swap of elements if it executes the condition to be true # Time: O(1), Space: O(1)
        (LST[j], LST[first_index]) = (LST[first_index], LST[j]) # the index at j in the list will switch places with the index at the first_index in the list # Time: O(1), Space: O(1)

def kfrequency(LST, k): # the function to find the kfrequency or k most frequent elements and takes LST list and k value of an integer as parameters # Time: O(n), Space: O(k)
    count = 0 # the count variable to keep count initially assinged to 0 # Time: O(1), Space: O(1)
    current_value = LST[0] # the current value variable will store the first index from the initial list # Time: O(1), Space: O(1)
    the_maximum_count = [0]*k # the maximum_count variable will create a list to store the most frequent elements by creating an array of 0 initially of size k # Time: O(k), Space: O(k)
    The_frequent_list = [None]*k # the frequent_list variable will create a similar list to count frequency however instead of creating an array of 0 it will create array of None with size k # Time: O(k), Space: O(k)
    for c in range(1, len(LST)): # the for loop iterates a temporary variable c for the range starting at 1 and then iterating for the length of the LST (list) # Time: O(n), Space: O(1)
        if LST[c] == current_value: # if statement that shows what should happend if LST[c] is equal with the element current_value # Time: O(1), Space: O(1)
            count += 1 # count would increment by 1  # Time: O(1), Space: O(1)
        else: # else statement condition # Time: O(1), Space: O(1)
            min_index_for_max_count = 0 # a variable called the min_index_for_max_count would be initialized with 0 # Time: O(1), Space: O(1)
            for l in range(len(the_maximum_count)): # for loop iterating with temporary variable l in the range of the len of the variable list the_maximum_count # Time: O(k), Space: O(1)
                if the_maximum_count[l] < the_maximum_count[min_index_for_max_count]: # if condition to check the index at variable l for the maximum_count list being less than the index at variable min_index_for_max_count for the maximum_count list # Time: O(1), Space: O(1)
                    min_index_for_max_count = l # the min_index_for_max_count would be assigned to l if the condition were to be executed # Time: O(1), Space: O(1)
            if count > the_maximum_count[min_index_for_max_count]: # the if statement that checks to see if the variable count is higher than the_maximum_count[min_index_for_max_count] list element at that index # Time: O(1), Space: O(1)
                the_maximum_count[min_index_for_max_count] = count # the_maximum_count[min_index_for_max_count] variable would be assigned to count if condition is executed # Time: O(1), Space: O(1)
                The_frequent_list[min_index_for_max_count] = current_value # the_frequent_list[min_index_for_max_count] would be assigned to the current_value if condition is executed # Time: O(1), Space: O(1)
            current_value = LST[c] # the current value is set to the value of LST[c] for the iteration of  temporary variable c in the original for loop of range(1, to the length list)  # Time: O(1), Space: O(1)
            count = 1 # the count is assigned back to 1 for the for loop iteration # Time: O(1), Space: O(1)

    min_index_for_max_count = 0 # the min_index_for_max_count variable stays assigned to 0 # Time: O(1), Space: O(1)
    for l in range(len(the_maximum_count)): # the for loop iteration for the temporary variable l which iteration for the length of the maximum count # Time: O(k), Space: O(1)
        if the_maximum_count[l] < the_maximum_count[min_index_for_max_count]: # the if statement condition is for the_maximum_count at index l is less than the_maximum_count at index min_index_for_max_count # Time: O(1), Space: O(1)
            min_index_for_max_count = l # min_index_for_max_count is assigned to l # Time: O(1), Space: O(1)
    if count > the_maximum_count[min_index_for_max_count]: # the count variable is being compared to being greater than the_maximum_count at index min_index_for_max_count where this if statement condition executes # Time: O(1), Space: O(1)
        the_maximum_count[min_index_for_max_count] = count # the if condition causes the_maximum_count[min_index_for_max_count] to be assigned to count # Time: O(1), Space: O(1)
        The_frequent_list[min_index_for_max_count] = current_value # the if condition causes the_frequent_list[min_index_for_max_count] to be assigned to the current_value variable # Time: O(1), Space: O(1)

    return The_frequent_list # returns or outputs the frequent list # Time: O(1), Space: O(1)


print("\nThe k most frequent element[s] is/are {}\n".format(kfrequency(LST, k = 2))) # print statement # Time: O(1), Space: O(1)
print("The k most frequent element[s] is/are {}\n".format(kfrequency(LST, k = 1))) # Test case 1 with different k value # Time: O(1), Space: O(1)
print("The k most frequent element[s] is/are {}\n".format(kfrequency(LST = [5, 0, 0, 0, 2, 5, 6], k = 2))) # Test case 2 with different LST # Time: O(1), Space: O(1)
print("The k most frequent element[s] is/are {}\n".format(kfrequency(LST = [5, 0, 0, 0, 2, 5, 6], k = 1))) # Test case 2 with different k value # Time: O(1), Space: O(1)
print("The k most frequent element[s] is/are {}\n".format(kfrequency(LST = [2, 3, 4, 4, 4, 9, 9, 10], k = 2))) # Test case 2 with different LST # Time: O(1), Space: O(1)

""" The time complexity of the overall program algorithm would be O(n) for the function and because of the nested for loop in the sorting algorithm the algorithm's run time
would be O(n^2), because the total program to get the k most frequent elements depends on sorting algorithm also and the sorting algorithm has a time complexity higher
than the function's time complexity therefore total program would have O(n^2) time complexity. The space complexity of the sorting algorithm is constant because it only uses 
the amount of memory the list has without creating extra memory therefore its space is constant O(1) and the kfrequency function's space would be O(k) because there are 
new memory lists created for an unknown and undetermined size of k for what ever value k might be therefore total space complexity for program would be O(n + k). """

""" Assignment 5 Question implementation task 2 of 2 using priority queue also called a heap data structure """

import heapq # imported module heapq # Time: O(1), Space: O(1)

def Kmostfrequentelements(LST, k): # K most frequent elements defined function which takes arguments LST and k # Time: O(n log k), Space: O(n)
    
    element_hashtable_count = {} # a hashtable implemented to store frequencies and elements by key, value pairs # Time: O(1), Space: O(n)
    for element in LST: # for loop iterates for the elements in LST variable with temporary variable called element # Time: O(n), Space: O(1) 
        if element not in element_hashtable_count: # the if condition checks the element each iteration to see if it is or is not in hashtable for which if it is not # Time: O(1), Space: O(1)
            element_hashtable_count[element] = 0 # the element is created and set to having a frequency of 0 for when the value does not repeat or appear again # Time: O(1), Space: O(1)
        element_hashtable_count[element] += 1 # the element previous created will have its frequency which is its value increment by 1 each time that value has already appeared and it is in element_hashtable_count # Time: O(1), Space: O(1)

    frequencyelement = [] # the frequencyelement variable is created and assigned to an empty list # Time: O(1), Space: O(n)
    for key in element_hashtable_count: # the for loop which iterates for each key that exists with in the hashtable # Time: O(n), Space: O(1)
        frequencyelement.append((element_hashtable_count[key], key)) # every iteration would append a tuple containing (frequency, element) as an element to the frequencyelement list # Time: O(1), Space: O(1)
    
    heap = [] # the heap empty list to store k values in the following lines # Time: O(1), Space: O(k)
    for elements, counts in frequencyelement[:k]: # the for loop iterates for temporary variable elements and counts in the frequencyelement list which only indexes up to user inputted k value # Time: O(k log k), Space: O(1)
        heapq.heappush(heap, (elements, counts)) # the heapq.heappush function would push the (elements, counts) tuple to the heap # Time: O(log k), Space: O(1)

    for elements, counts in frequencyelement[k:]: # the for loop iterates for temporary variabel elements and counts however this time it is for the frequencyelement list indexes up to the end of the list starting the index from user inputted k value # Time: O((n-k) log k), Space: O(1)
        if elements > heap[0][0]: # the if statement checks elements variable being greater than the element on the heap which is indexes by heap[0][0] # Time: O(1), Space: O(1)
            heapq.heapreplace(heap, (elements, counts)) # if the if condition executes the heapq.heapreplace(heap, (elements, counts)) would replace the current value on top of the heap with the elements with the higher frequency # Time: O(log k), Space: O(1)
        
    output_list = [heap_value[1] for heap_value in heap] # the output list variable is optional however it shows the output as a list of only the elements that are most frequent instead of showing tuples showing elements and their frequencies  # Time: O(k), Space: O(k)
    return output_list # this statement returns the output_list variable # Time: O(1), Space: O(1)

print("The most frequent elements in this list is/are: {}".format(Kmostfrequentelements(LST = [1,2,1,3,2,2], k = 2))) # print statement with k value being 1 most frequent element[s] # Time: O(1), Space: O(1)
print("The most frequent elements in this list is/are: {}\n".format(Kmostfrequentelements(LST = [1,2,1,3,2,2], k = 1))) # print statement with k value being 2 most frequent elements[s] # Time: O(1), Space: O(1)
print("The most frequent elements in this list is/are: {}\n".format(Kmostfrequentelements(LST = [4, 2, 2, 3, 6, 2, 8, 1], k = 1))) 
print("The most frequent elements in this list is/are: {}\n".format(Kmostfrequentelements(LST = [0, 1, 1, 7, 7, 0, 7, 4], k = 3)))

""" The time complexity of the overall program algorithm would be O(n log k) because functions of heap such as heapify or pushing a value onto a heap would have time 
complexities of O(log n) and because of the two heap functions being used which are heapq.heappush and heapq.heapreplace which are each O(log k) and that would make them
have an overall complexity of O(n log k), the run time also is impacted by the output_list variable because for each heap_value variable or element in the heap list
the program has to iterate and index the first value from each tuple which outputs the element and appends it into the list. The space complexity of the overall program algorithm
would be O(n) because we have had constant time for most of the code logic statements only we have created O(n) space when assigning the hashtable, frequencyelement list, 
and the heap list. """