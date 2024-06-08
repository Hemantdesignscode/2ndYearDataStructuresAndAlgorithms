
""" 
Name: Hemant Kosaraju
Computer Science 2720 Lab 7 Section: 014 CRN: 17910
Lab Time: Wednesdays February 21 2024 Langdale Hall Room: 405
Due Time: Sundays February 25 2024 at 11:59 PM
"""

class Node: # A Node class
    def __init__(self, data): # An def function that is acting as a constructor and instance for the class
        self.data = data # The data value that will be stored in the node
        self.next = None # The next is a pointer connect to the next node

class LinkedList: # Linked List is the leading [Main] class

    """ The constructor definition using self to construct the leading Node which is also referred to by the head Node """
    def __init__(self): 
        self.head = None

    """ The definition of a function to use self and data that will insert a new node at the beginning of the linked list """
    """ Start by creating a new node """
    def indexatstart(self, data):
        """ An if statement that shows what the do which is assigning the head instance to the data that will go in Node class
        the else statement says that if the index at start is the self.head then it will assign current variable to self.head and the loop iterates
        to where current.next lengthens to which assigns the variable current from self.head to current.next and finally the current.next = Node(data) assigns itself
        the data coming from the Node class call """
        if not self.head:
            self.head = Node(data)
        
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)
    
    """ A def function that receives the length of the list to use with other function instances """
    def get_length(self):
        """ The length of the linked list """
        current_node = self.head
        length = 0
        while current_node:
            length += 1
            current_node = current_node.next
        return length

    """ The function definition of deleting a node """
    def delete_node(self, N):
    
        list_length = self.get_length() # gets the list length 
        
        """ N here is being assigned with the length of the list minus N so that it would be equivalent to getting the index starting from the end to the beginning """
        N = list_length - N 

        """ Because it will be out of bound or range for which it will return False """
        if N < 0 or N >= list_length:
            return False

        """ If self.head is None and there is no value for which it will return False """
        if self.head is None:
            return False
        
        """ If N is equal in comparison to 0 then the self.head node would be equal to the node next to it, i.e. the deleted node would be the head if n index is value 0 """
        if N == 0:
            self.head = self.head.next
            return True
        
        """ A previous node would be assigned to the node that would be deleted because then after the next node's deletion the previous node would take the position of the
        deleted node """
        previous_node = self.head
        for _ in range(N - 1):
            previous_node = previous_node.next

        previous_node.next = previous_node.next.next

        return True

    """ The definition of a function to display the output list """
    def display(self): 
        """ The elements variable is an empty list that will hold values within them """
        elements = []
        """ the current node is getting assigned to the head position node """
        current_node = self.head
        """ While there is a current node this while loop will continue iterating until it hits the tail node or end of the links of nodes """
        while current_node:
            """ elements are getting appended to the empty list however, they are appended as strings due to the type casting though this type casting to string [str] is an
            option and not a requirement unless instructed differently """
            elements.append(str(current_node.data))
            current_node = current_node.next
            """ The elements are joined in the return statement using join which is used for strings and characters and includes a comma [,] in betweeb each element """
        return ", ".join(elements) 

""" The linklist variable is assigned to the class LinkedList call """
linklist = LinkedList() 
""" The head to tail of the list with the nodes in between are assigned and defined in the lines below """
head = 50
node1 = 11
node2 = 33
node3 = 21
node4 = 40
tail = 71
""" node to be deleted is set to a variable """
node_del = 2
""" The lines below are instance calls for the indexatstart and delete_node functions that both insert a value in the place in a list and the delete_node function instance
would delete the element at that index which is given which starts not from the beginning though from the ending - per instruction to do so """
linklist.indexatstart(head)
linklist.indexatstart(node1)
linklist.indexatstart(node2)
linklist.indexatstart(node3)
linklist.indexatstart(node4)
linklist.indexatstart(tail)
linklist.delete_node(2)

""" Test Cases """
""" The head to tail nodes with nodes in between that link to each other """
head = 30
node1 = 60
node2 = 67
node3 = 72
node4 = 88
tail = 12
""" deletes last index """
node_del = 1
""" below lines are instance calls """
test_linklist1 = LinkedList()
test_linklist1.indexatstart(head)
test_linklist1.indexatstart(node1)
test_linklist1.indexatstart(node2)
test_linklist1.indexatstart(node3)
test_linklist1.indexatstart(node4)
test_linklist1.indexatstart(tail)
test_linklist1.delete_node(node_del)

""" The head to tail nodes with nodes in between that link to each other """
head = 45
node1 = 57
node2 = 27
node3 = 32
node4 = 16
tail = 64
""" deletes last index """
node_del = 3
""" below lines are instance calls """
test_linklist2 = LinkedList()
test_linklist2.indexatstart(head)
test_linklist2.indexatstart(node1)
test_linklist2.indexatstart(node2)
test_linklist2.indexatstart(node3)
test_linklist2.indexatstart(node4)
test_linklist2.indexatstart(tail)
test_linklist2.delete_node(node_del)


""" This final line calls the Linked List class' display instance to show the output of the list after inserting elements and deleting an element at a specific index """
print("\n{}\n".format(linklist.display()))
print("{}\n".format(test_linklist1.display()))
print("{}\n".format(test_linklist2.display()))