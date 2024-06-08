
""" 
Student: Hemant Kosaraju
Computer Science 2720 Lab 9 
Lab Time: Wednesdays March 8 2024 Langdale Hall 405
Due Time: Sundays March 10 2024 at 11:59 PM
"""

class MinStack: 
    """ We implemented the class called MinStack """
    def __init__(self):
        """ The def __init__(self) is a definition function constructor with the __init__ and
        the self would be the instance attribute """
        self.stack = []
        """ This is a stack variable created using the instance attribute which is self and is intialized as a list """
        self.minimumstack = []
        """ This is a minimumstack variable created using the instance attribute which is self and is initialized as another list """

    def push(self, stack):
        self.stack.append(stack)
        if not self.minimumstack or stack <= self.minimumstack[-1]:
            self.minimumstack.append(stack)
        """ The defined function for push which takes the instance attribute self and the stack variable, to the self.stack.append(stack) would append the pushed integer value stack to 
        the self.stack list, the if statement line checks two expressions to check if they are true or false which are if the element or int variable stack is not already in the minimumstack
        and the second expression if stack int var is less than or equal to the last element of the minimumstack after both these expressions are verified or represent true it will append
        the variable that was previously appended to the self.stack list as the minimum value of the minimumstack """

    def pop(self):
        if self.stack:
            pop_element = self.stack.pop()
            if pop_element == self.minimumstack[-1]:
                self.minimumstack.pop()
        """ The defined function for pop which starts with an if statement and evaluates if self.stack then a variable called pop_element is assigned to self.stack.pop() which can be used because
        the self.stack is a list, and the next if statement evaluates if the pop_element is equal to the last element of the minimumstack then it will pop that mininmum value from the minimumstack
        list too """

    def top(self):
        if self.stack:
            return self.stack[-1]
        raise IndexError ("No elements are assigned to stack")
    """ The defined function for top which starts with an if statement similar to the pop function and then it will get the current latest updated value which was push to the self.stack
    list and it does this by returning self.stack[-1] which is the latest element from the list, and if no elements are found at all in the self.stack list it should raise an IndexError """
    
    def get_min(self):
        if self.minimumstack:
            return self.minimumstack[-1]
        raise IndexError ("No elements are assigned to stack")
    """ The defined function for get_min follows with the same logic of the top function however the if statement checks to see if self.minimumstack: and then because this function should
    get the minimum element it returns self.minimumstack[-1] which is the lowest value from the stack """
    
elements = MinStack()
elements.push(10)
elements.push(27)
elements.push(12)
elements.push(16)
elements.push(36)
elements.push(20)
elements.push(78)
elements.push(100)
elements.push(89)
elements.push(77)
elements.push(70)
""" The elements is a variable which are assigned to MinStack() class
then it will append the values which are integer values using the 
function push """

elements.pop()
elements.pop()
""" Removes the two recently updated values
from the stack list """

print("\nThe current top of the stack: {}\n".format(elements.top()))
print("The minimum value from the stack: {}\n".format(elements.get_min()))
""" elements.top gets the top or latest updated value from the stack
and elements.get_min gets the minimum value from the minimumstack """

""" Test Cases """

""" Test Case 1 """
elements.push(7)
elements.push(89)
elements.push(45)
elements.push(98)
elements.push(76)
elements.push(58)
elements.push(34)
""" The elements is a variable which are assigned to MinStack() class
then it will append the values which are integer values using the 
function push """

elements.pop()
""" Removes one recently updated value
from the stack list """

print("\nThe current top of the stack: {}\n".format(elements.top()))
print("The minimum value from the stack: {}\n".format(elements.get_min()))
""" elements.top gets the top or latest updated value from the stack
and elements.get_min gets the minimum value from the minimumstack """

""" Test Case 2 """
elements.push(89)
elements.push(21)
elements.push(43)
elements.push(32)
elements.push(77)
elements.push(23)
elements.push(4)
""" The elements is a variable which are assigned to MinStack() class
then it will append the values which are integer values using the 
function push """

print("\nThe current top of the stack: {}\n".format(elements.top()))
print("The minimum value from the stack: {}\n".format(elements.get_min()))
""" elements.top gets the top or latest updated value from the stack
and elements.get_min gets the minimum value from the minimumstack """

""" Test Case 3 [with empty push] """
try:
    elements.push()
except TypeError as t:
    print ("\nThere were no element int val being assigned to the stack using push function, please put an int val using push ")
""" The try and except to use and show what happens to give an error message for elements.push function """

print("\nThe current top of the stack: {}\n".format(elements.top()))
print("The minimum value from the stack: {}\n".format(elements.get_min()))
""" elements.top gets the top or latest updated value from the stack
and elements.get_min gets the minimum value from the minimumstack """