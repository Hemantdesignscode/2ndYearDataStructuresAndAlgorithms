
""" 
Student: Hemant Kosaraju
Computer Science 2720 Lab 13 CRN: 17910 Section: 014
Lab Time: Computer Science 2720 2:00 PM to 2:50 PM Langdale Hall Room 405
Due Time: Sunday April 14 2024 11:59 PM
References: Had to ask search engine for help however test cases and handling values of k larger than the list indexes was what I implemented on my own and none of the
variables or the return statements were copied I have just used the search engine to get a better understanding of heaps and how both min heap and max heap work
"""

import heapq # should be used

LST = [9, 3, 6, 2, 1, 8] # A test list to use for the heap

def kBiggest(LST, k): # A definition function to find the kth biggest element from a list given what k is

    while k not in range(1, len(LST) + 1): # A while loop to make sure k value inputted to determine what the kth biggest value is-is within the available indexes of the length of the list 
        return "Please input a value for k which is either within or equal to the index values that are available based on the size of the list and Try Again\n" # return statement

    heap = LST[:k] # The heap variable is assigned to being the slice of the LST to what element k is therefore the value of k equals the amount of elements that are in the heap
    heapq.heapify(heap) # The heapq is the module imported to make a list into a heap and it is a data structure that had been made into a library and it converts the list assigned to heap variable to a heap using heapq.heapify( )

    for r in LST[k:]: # For r index in the range of k through the end, which are the remaining elements in the LST which are not assigned to heap
        if r > heap[0]: # if condition checks for if the element at the r element value from the range of k through the end of the remaining list is greater than the root element of heap
            heapq.heappushpop(heap, r) # The heapq module will use the heappushpop function to take argument 1 to be the popped element and the element value r to be the pushed element onto the heap
    
    return ("The {}[st,nd,rd,th] largest element from the heap is {}\n".format(k, heap[0])) # This is the return statement that returns what value of k was given and what the largest element at that k value for the heap would be
    

print("\n{}".format(kBiggest(LST, k = 1))) # print statement calling the kBiggest function taking the list variable as argument 1 and k value as argument 2
print("Test Case 1", kBiggest(LST, k = 10)) # print statement calling the kBiggest function with Test case being k is a value not within the index of the LST which should be 1-6
print("Test Case 2", kBiggest(LST = [10, 5, 3, 13, 21, 30, 18, 32], k = 2))
print("Test Case 3", kBiggest(LST = [10, 57, 43, 11, 31, 60, 29, 30], k = 1))
print("Test Case 4", kBiggest(LST = [11, 56, 63, 49, 39, 77, 29, 36], k = 4))
print("Test Case 5", kBiggest(LST = [11, 56, 63, 49, 39, 77, 29, 36], k = 12))

""" The Time Complexity and Space Complexity Explanation """

""" 
The time complexity of this program would be O(n * log k because the for loop would iterate for the length of the list - k times and that would mean it would be linear 
time either O(n) or O(k) and the if condition within it would cause the heapq.heappushpop(heap, r) statement to execute if the LST[k:] value at r is greater than the 
root value of the min heap which is represented by heap[0] then it would pop the heap smallest value and push the r largest value if it was greater than the root of the heap
onto the min heap. That heappushpop would combine functions of both heappush and heappop each of which have a time complexity of log k because of the heap's tree like structure
and that causes the total program time complexity to be O(n * log k). The Space complexity would just be O(n) because the space used in context of memory would depend on the size of the list we have created but we can also say it 
is related to the value of k because the min heap only stores value from the list upto the kth index and then does a loop over the remaining values from the list which
will check to see if any of those remaining values are greater than the root of the min heap which would be the smallest value of the min heap.
"""