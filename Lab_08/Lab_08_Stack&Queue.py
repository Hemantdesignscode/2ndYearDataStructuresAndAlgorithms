
""" 
Name: Hemant Kosaraju
Computer Science 2720 Lab 8 Section: 014 CRN: 17910
Lab Time: Wednesdays February 28 2024 2:00 to 2:50 PM Langdale Hall Room 405
Due Time: Sundays March 3 2024 11:59 PM
"""

""" This is an allowed library that we have discussed in class and the imported module is Double Ended Queue """
from collections import deque 

""" This is class declaration for the two queues and includes functions for both adding and removing values from the queue along with a function
to display the maximum value """
class TwoQueue:
    """ This is the initial function which is a constructor and has an instance self, because we have two queues the first instance attribute would be 
    instance self.mainqueue which is one of the double ended queues [deque] and the second instance attribute would be instance self.maxqueue which is the other double
    ended queue [deque] """
    def __init__(self):
        self.mainqueue = deque()
        self.maxqueue = deque()

    """ The addition to the queue function which has parameters (instance self, value) and instance self will append value to the main queue, however the while loop
    checks to see if the value passed in to the parameter is greater than or equal to the last element in the maxqueue, for which then it will pop the value from the
    maxqueue and append the value that was previously appended to the main queue to the maxqueue """
    def add_to_queue(self, value):
        self.mainqueue.append(value)

        while self.maxqueue and value >= self.maxqueue[-1]:
            self.maxqueue.pop()
        self.maxqueue.append(value)

    """ The remove pop queue function takes the parameter as the instance self and the if statement states that if there is a value that is not part of the main queue
    then the return would be None, the removed value would be assigned to the main queue's left removed value, and then the if statement states removed value is equal to 
    the max queue's first value then it will also pop the left removed value from the max queue and then finally, return the removed value """
    def removepop_queue(self):
        if not self.mainqueue:
            return None
        removed_val = self.mainqueue.popleft()
        if removed_val == self.maxqueue[0]:
            self.maxqueue.popleft()
        return removed_val
    
    """ The get maximum queue function will use the instance self as a parameter to check if a value is in the max queue and then return None, then it will return
    the first element or value from the max queue """
    def getmaximumqueue(self):
        if not self.maxqueue:
            return None
        return self.maxqueue[0]
    
""" The Queue variable is assigned to the TwoQueue class """
Queue = TwoQueue()
""" These next four lines use the add to queue function to add a value to the queue and then each time print the maximum value from the maximum queue """
Queue.add_to_queue(1)
print("\nMaximum Of Queue is: {}\n".format(Queue.getmaximumqueue()))
Queue.add_to_queue(4)
print("Maximum Of Queue is: {}\n".format(Queue.getmaximumqueue()))
Queue.add_to_queue(2)
print("Maximum Of Queue is: {}\n".format(Queue.getmaximumqueue()))
Queue.add_to_queue(3)
print("Maximum Of Queue is: {}\n".format(Queue.getmaximumqueue()))

""" Test Cases - While also using try and except to show what happens if add to queue function is called to add an empty value to the main queue """
Queue.add_to_queue(8)
print("Test Case 1 - Maximum Of Queue is: {}\n".format(Queue.getmaximumqueue()))

Queue.add_to_queue(6)
print("Test Case 2 - Maximum Of Queue is: {}\n".format(Queue.getmaximumqueue()))

Queue.add_to_queue(10)
print("Test Case 3 - Maximum Of Queue is: {}\n".format(Queue.getmaximumqueue()))

try:
    Queue.add_to_queue()
    print("Test Case 4 - Maximum Of Queue is: {}\n".format(Queue.getmaximumqueue()))

except TypeError:
    print("Test Case 4 - Please input at least one value within the parameters for adding to the queue\n")