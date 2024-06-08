
""" 
Student: Hemant Kosaraju
Computer Science 2720 Lab 11 CRN 17910
Lab Time: Wednesday March 27 2024 2:00 to 2:50 PM Langdale Hall Room 405
Due Time: Sunday March 31 2024 11:59 PM
"""

from collections import deque # imported module collections for creating a queue

class TreeNode: # the class name is Tree Node which will have three attributes being left, right, data [called root too]
    def __init__(self, data): # A constructor function which is the function that will begin the class with the three attributes listed above
        self.left = None
        self.right = None
        self.data = data # self.data is the only variable that has a variable set to it, while self.left and self.right are initialized with None

    def Levelorder_traversal(self): # The beginning of the LevelOrder_traversal(self) function which will create a queue and then append the root to the queue initially
        self.Queue = deque()
        self.Queue.append(root)
        
        while self.Queue: # This loop will run for until the Queue is empty of elements whenever there are elements the while self.Queue statement will be True
            Tree_access_FIFO = self.Queue.popleft() 
            """ This is a variable that will be holding the popped value and since we are popping first value because of First in First Out algorithm we will use 
            Queue.popleft() because we want to pop or receive the first element from Queue contrast from stack when stack used Last in First Out algorithm which was
            why we used pop() instead of popleft() and whywe are using popleft() now"""
            if Tree_access_FIFO is not None: # if statement checks the condition that the variable Tree_access_FIFO contains a value receives or holds a value at any given time
                if Tree_access_FIFO.left: # this condition checks if there are any elements on the left of the element received from the queue, if yes it appends it to the queue
                    self.Queue.append(Tree_access_FIFO.left)
                if Tree_access_FIFO.right: # this condition checks if there are any elements on the right of the element received from the queue, if yes it appends it to the queue
                    self.Queue.append(Tree_access_FIFO.right)

            print(Tree_access_FIFO.data, end = " ")

        print("\n")
        """ The print statement for the Tree_access_FIFO.data is indented in the while loop because we do not just want the outermost right value of the tree 
        we want all the values to print for each execution of the while loop"""


""" The nodes of the tree - beginning from the root and going from left to right and subtree nodes """
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

""" Statment to access the function Levelorder_traversal() from the class and print the tree nodes as a list in level order """
print()
root.Levelorder_traversal()

""" Test Cases """

""" Test Case 1 """

root = TreeNode(12)
root.left = TreeNode(27)
root.right = TreeNode(90)
root.left.left = TreeNode(47)
root.left.right = TreeNode(15)
root.right.left = TreeNode(9)
root.right.right = TreeNode(25)

print("Test Case 1:\n")
root.Levelorder_traversal()

""" Test Case 2 """

root = TreeNode(34)
root.left = TreeNode(66)
root.right = TreeNode(37)
root.left.left = TreeNode(10)
root.left.right = TreeNode(15)
root.right.left = TreeNode(19)
root.right.right = TreeNode(29)

print("Test Case 2:\n")
root.Levelorder_traversal()

""" Test Case 3 """

root = TreeNode(76)
root.left = TreeNode(33)
root.right = TreeNode(45)
root.left.left = TreeNode(26)
root.left.right = TreeNode(87)
root.right.left = TreeNode(91)
root.right.right = TreeNode(94)

print("Test Case 3:\n")
root.Levelorder_traversal()