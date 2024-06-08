
""" 
Name: Hemant Kosaraju
Computer Science 2720 Lab 10 CRN 17910
Lab Time: Wednesday March 20 2024 2:00 to 2:50 PM at Langdale Hall Room 405
Due Time: Sunday March 24 2024 at 11:59 PM
References used: YouTube - viewed Binary Search Tree and Binary Tree Data Structures and Algoirthms video #10; to better understand the logic and how these trees work; channel: CodeBasics
"""

class TreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        """ The four [4] lines above are given in the lab assignment however a description for them is that there is a class created that has a constructor function
        with two arguments passed to it being the instance self and the variable data. Three instance attributes are created from instance self which are self.left assigned
        initially to None; self.right assigned initially to None; self.data assigned initially to data """


    """ To describe how I found out the logic to implement the Pre-Order, Post-Order, and In-Order traversals I used the understanding of the binary trees I learned from 
    lab when our lab instructor taught us how to distinguish the three types of traversals by thinking about the node structure they use e.g., for Pre-Order traversal
    in lab we learned the order would be Root Node --> Left Node --> Right Node, then for Post-Order traversal we learned the order was Left Node --> Right Node --> Root Node,
    then for In-Order we learned the order was Left Node --> Root Node --> Right Node """

    def preorder_traversal(self, level = 0):

        print("" * level, self.data, end = " ")
        
        if self.left is not None:
            self.left.preorder_traversal(level + 1)

        if self.right is not None:
            self.right.preorder_traversal(level + 1)
        """ The function preorder_traversal takes the instance self as one argument however the second argument is something that is optional and only useful to set
        spacing between elements and it would be more noticeable when trying to print the result of tree as tree structure rather than the list structure; however then the
        print("" * level, self.data, end=" ") would just access the Root Node because self.data is the main node we are focused on as being the root in this code situation,
        then using the order it means we have to now go to --> Left Node therefore that explains why is the left nodes exist and are not empty or none the if statement condition
        will traverse through the left section of the Binary tree lastly corresponding to the order --> Right Node which explains the if statement checking to see if 
        the instance attribute self.right is not empty and not none for which it exists and the binary tree will traverse through the right side of the tree and print 
        the values last. The idea has to be Root Node --> Left Node [elements from entire left side of Binary Tree] --> Right Node [elements from entire right side of Binary Tree] """

    def postorder_traversal(self, level = 0):
         
        if self.left is not None:
            self.left.postorder_traversal(level + 1)

        if self.right is not None:
            self.right.postorder_traversal(level + 1)
         
        print("" * level, self.data, end = " ")
        """ The function postorder_traversal takes the instance self as one argument however the second argument is something that is optional and only useful to set spacing
        between elements and it would be more noticeable when trying to print the result of tree as tree structure rather than the list structure in the situation of this lab;
        however instead of starting from the Root Node this time for the Post-Order traversal we will transfer the --> Left Node --> Right Node to infront of the Root Node causing
        the if statement which accesses the Left Node to be first and it checks to see that the left nodes are not empty and not None then it will output all the values of 
        the left nodes of the Binary tree, next we go to the --> Right Node and the same statement type executes the if statement checks to see this time that the right nodes
        are not empty and not None then it will output all the values of the right nodes of the Binary tree, lastly the --> Root Node is accessed and it will be outputted last
        in the list """

    def inorder_traversal(self, level = 0):

        if self.left is not None:
            self.left.inorder_traversal(level + 1)

        print("" * level, self.data, end = " ")

        if self.right is not None:
            self.right.inorder_traversal(level + 1)
        """ The function inorder_traversal takes the instance self as one argument however the second argument is something that is optional and only useful to set spacing
        between elements and it would be more noticeable when trying to print the result of tree as tree structure rather than the list structure in the situation of this lab;
        now first we started with Pre-Order which was Root Node --> Left Node --> Right Node then for Post-Order it changed to Left Node --> Right Node --> Root Node in this
        scenario the left and right nodes came in front of the Root Node in the same order as before, now for In-Order looking at Left Node --> Right Node --> Root Node
        switch the spots or locations of Right Node and Root Node and In-Order Traversal logic would be Left Node --> Root Node --> Right Node, then the if statement checks
        first if the left section of the binary tree is not empty and not None for which it will output the left section of binary tree, then the print(self.data) statement
        accesses and outputs the Root Node and lastly the if statement checks for the right sections of the binary tree being not empty and not None for which it will output
        the right section of binary tree """

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)
""" A Binary tree will start at a Root Node --> have two [2] split sub braches to it because binary trees are not general trees and they can only have two [2] child nodes
then after having two child nodes, each of those two child nodes have two child nodes connected to them """

print("\nThe Pre-Order Traversal: ", end = " "), root.preorder_traversal(), print("\n")
print("The In-Order Traversal: ", end = " "), root.inorder_traversal(), print("\n")
print("The Post-Order Traversal: ", end = " "), root.postorder_traversal(), print("\n")

""" These are print statements to first indicate the order they are and then the root instance is being used to call the traversal that is specified """

""" Test Cases """

root2 = TreeNode(16)
root2.left = TreeNode(25)
root2.right = TreeNode(10)
root2.left.left = TreeNode(5)
root2.left.right = TreeNode(4)
root2.right.left = TreeNode(20)
root2.right.right = TreeNode(19)

print("\nTest Case 1 The Pre-Order Traversal: ", end = " "), root2.preorder_traversal(), print("\n")
print("Test Case 1 The In-Order Traversal: ", end = " "), root2.inorder_traversal(), print("\n")
print("Test Case 1 The Post-Order Traversal: ", end = " "), root2.postorder_traversal(), print("\n")


root3 = TreeNode(3)
root3.left = TreeNode(14)
root3.right = TreeNode(70)
root3.left.left = TreeNode(15)
root3.left.right = TreeNode(47)
root3.right.left = TreeNode(16)
root3.right.right = TreeNode(29)

print("\nTest Case 2 The Pre-Order Traversal: ", end = " "), root3.preorder_traversal(), print("\n")
print("Test Case 2 The In-Order Traversal: ", end = " "), root3.inorder_traversal(), print("\n")
print("Test Case 2 The Post-Order Traversal: ", end = " "), root3.postorder_traversal(), print("\n")


root4 = TreeNode(12)
root4.left = TreeNode(33)
root4.right = TreeNode(49)
root4.left.left = TreeNode(23)
root4.left.right = TreeNode(10)
root4.right.left = TreeNode(24)
root4.right.right = TreeNode(1)

print("\nTest Case 3 The Pre-Order Traversal: ", end = " "), root4.preorder_traversal(), print("\n")
print("Test Case 3 The In-Order Traversal: ", end = " "), root4.inorder_traversal(), print("\n")
print("Test Case 3 The Post-Order Traversal: ", end = " "), root4.postorder_traversal(), print("\n")