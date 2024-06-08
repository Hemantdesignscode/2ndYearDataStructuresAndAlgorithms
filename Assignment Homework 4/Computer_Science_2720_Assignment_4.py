
""" 
Student: Hemant Kosaraju
Computer Science 2720 Data Structures and Algorithms CRN: 17910 Section: 014
"""

""" Computer Science Assignment 4 Question 1 - Replace and Delete Root Node """

class BinarySearchTreeNode: # A Binary Tree Class Created

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        """ The Binary Tree's constructor function consists of a def __init__(self) function and then include instance attributes for self.left set to none, self.right set
        to none, and self.data set to data variable """

    def inorder_traversal(self): # A function to inorder traverse the Binary Search Tree

        if self.left is not None:
            self.left.inorder_traversal()
        
        print(self.data, end = " ")

        if self.right is not None:
            self.right.inorder_traversal()
        """ Citation: #[1] Lab_10_BinaryTree, 
        The traversal for inorder is can be thought of as the root node having a higher value than the left subtree and a lower value than the right subtree therefore
        the order would be Left --> Root --> Right and that is shown in the code by if condition first checking for as long as the statement self.left is not None which 
        means it is True then self.left.inorder_traversal() would just keep passing the left subtree nodes to the inorder_traversal() recursively and after it has
        completed doing that the print self.data would output the root node and finally the other if condition checks to see if the statement self.right is not None which
        suggests it is True and it would recursively get the right subtree nodes passed to the inorder_traversal() because of the self.right.inorder_traversal() statement """

    def delete_replace_node(self): # A function to delete and replace a node of the Binary Search Tree
        
        if self.right:
            updatedroot = self.right
            while updatedroot.left:
                updatedroot = updatedroot.left
            """ The if statement checks to see if the parameter or argument instance that was passed in has right elements and if it does and the condition is True then
            a variable which I named the updatedroot would be assigned to the element which is the right child of the root [at this time it would be recommended to
            know that using the left child of the root node to find an inorder predecessor also would work similar to finding an inorder successor, in this example I 
            have chosen the inorder successor] from the right child of the root we will check for however many left nodes are connected to that right child using a while
            updatedroot.left statement and then the leftmost value of the right subtree [i.e. the lowest value of the right side of the binary search tree which is higher
            than the node] will be updated to be the updatedroot   """

            self.data = updatedroot.data
            """ This statement copies the data of the updatedroot we found using the code build above to the value of the root so after executing this line 
            the root node and the lowest value of the right subtree should be equal """
        
            if updatedroot != self.right:
                higherlevel_node = self.right
                while higherlevel_node.left != updatedroot:
                    higherlevel_node = higherlevel_node.left
                higherlevel_node.left = None
            """ if the updatedroot is not equal to the self.right the variable higherlevel_node would be set to the self.right subtree and then for each higherlevel_node 
            that has a left node which is not equal to the updatedroot then the higherlevel_node is being assigned to the place of the inorder successor which means the
            left most node of the right subtree and that inorder successor which has already been set as the root node will be removed from the left most node of the right subtree
            by updating the value of the higherlevel_node.left to None """

""" The Tree root node along with other Binary Search Tree nodes """
Tree = BinarySearchTreeNode(4)
Tree.left = BinarySearchTreeNode(2)
Tree.right = BinarySearchTreeNode(6)
Tree.left.left = BinarySearchTreeNode(1)
Tree.left.right = BinarySearchTreeNode(3)
Tree.right.left = BinarySearchTreeNode(5)
Tree.right.right = BinarySearchTreeNode(7)

""" The code calls the delete_replace_node() function here """
Tree.delete_replace_node()

""" The code calls the inorder_traversal() function to print the Binary Search Tree from Left Subtree --> Root --> Right Subtree """
print("The Inorder traversal after replacing the root node with inorder successor: ", end = " "), Tree.inorder_traversal(), print("\n")

""" Test Cases """

""" Test Case 1 """

Tree1 = BinarySearchTreeNode(55)
Tree1.left = BinarySearchTreeNode(30)
Tree1.right = BinarySearchTreeNode(70)
Tree1.left.left = BinarySearchTreeNode(18)
Tree1.left.right = BinarySearchTreeNode(52)
Tree1.right.left = BinarySearchTreeNode(65)
Tree1.right.right = BinarySearchTreeNode(81)

Tree1.delete_replace_node()

print("Test Case 1 - The Inorder traversal after replacing the root node with inorder successor: ", end = " "), Tree1.inorder_traversal(), print("\n")

""" Test Case 2 """

Tree2 = BinarySearchTreeNode(64)
Tree2.left = BinarySearchTreeNode(36)
Tree2.right = BinarySearchTreeNode(74)
Tree2.left.left = BinarySearchTreeNode(5)
Tree2.left.right = BinarySearchTreeNode(49)
Tree2.right.left = BinarySearchTreeNode(66)
Tree2.right.right = BinarySearchTreeNode(95)

Tree2.delete_replace_node()

print("Test Case 2 - The Inorder traversal after replacing the root node with inorder successor: ", end = " "), Tree2.inorder_traversal(), print("\n")


""" Computer Science Assignment 4 Question 2 - DNA Sequence """

def DNA_Sequence(DNA_Sequence_user_input):

    sequence = "" 
    """ A Sequence variable created and assigned to empty string to be of str type """
    sequence_in_ten_characters = []
    """ A list with the name sequence_in_ten_characters """
    for j in range(int(len(DNA_Sequence_user_input) / 10)):
        """ The for loop will iterate for the range of the length of the sequence divided by 10 times for example 36 characters / 10 = 3.6 and float type casted to int would
        be 3 therefore the for loop for a input with 36 characters would iterate 3 times """
        sequence = DNA_Sequence_user_input[j * 10 : (j + 1) * 10]
        """ The sequence variable is updated to be a ten character word for however many are found through out the string depending on the length of the user sequence given  """
        sequencereverse = sequence[::-1]
        """ This are the same ten character sequences found throughout the string however the sequences are just reversed therefore they will also occur in a backwards order
        e.g., AAAAACCCCC might become CCCCCAAAAA """
        sequence_in_ten_characters.append(sequence)
        """ This line above will append each standard 10 character sequence to the list with the name sequence_in_ten_characters """
        sequence_in_ten_characters.append(sequencereverse)
        """ This line above will append each reversed 10 character sequence to the list with the name sequence_in_ten_characters """
    print("\n{}".format(sequence_in_ten_characters)) # A print statement to print or show the output of the total output of each ten character sequence whether standard or outputted appended to the list sequence_in_ten_characters

    hashtable_word_count = {}
    """ A Hash Table which contains key-value pairs which can also be referred to as a hash set, hash map or commonly in programming a dictionary """

    for sub_statements in sequence_in_ten_characters: 
        """ for each 10 character word or sequence in the list sequence_in_ten_characters """
        if sub_statements in hashtable_word_count:
            hashtable_word_count[sub_statements] += 1
            """ the if condition if it is true that each 10 character sequence is in the hashtable_word_count and the condition is True it will do two things
            1. it will add the new key to the hashtable and 2. if that key is seen in the hashtable_word_count hashtable again then it will increment the key's value by
            """
        else:
            hashtable_word_count[sub_statements] = 1
            """ the else statement states that if the key is not seen again as a 10 character sequence whether it is standard or reversed it will keep the value for the key
            at 1 """

    print("\n{}".format(hashtable_word_count)) # A print statement to show the output of the hashtable and how if a key is detected again it has an incremented value pair

    sequences_that_appear_more_than_once = []
    """ This list is used to store the 10 character sequences that appear more than once """
    for char in hashtable_word_count:
        """ For each key in the hashtable named hashtable_word_count """
        if hashtable_word_count[char] > 1:
            sequences_that_appear_more_than_once.append(char)
            """ if the hashtable key has a value pair that is greater > than 1 then that key which is a specific 10 character sequence that appeared more than once is
            appended to the sequences_that_appear_more_than_once list """ 
        else:
            break
        """ The else statement would cause the keys that do not have a value pair greater > than 1 to be bypassed or left out with out being added to the final 
        sequences_that_appear_more_than_once list """ 

    print("\nThe DNA Sequence which occurs more than once: {}\n".format(sequences_that_appear_more_than_once)) # A print statement to output the final result of the sequences that appear more than once

DNA_Sequence(DNA_Sequence_user_input = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")

""" Test Cases 1,2,3 """
print("Test Case 1")
DNA_Sequence(DNA_Sequence_user_input = "CCAAAAAAAATTTTTTTTTTGATCGATC")
print("Test Case 2")
DNA_Sequence(DNA_Sequence_user_input = "GTGTTTGTTTCACACAACAAGTGTTTGTTT")
print("Test Case 3")
DNA_Sequence(DNA_Sequence_user_input = "AAAAAAAAAAAAA")