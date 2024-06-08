
""" 
Student Name: Hemant Kosaraju
Homework Assignment 3
Computer Science 2720 
"""

""" Assignment 3 Coding Question 1 """

def hasBalancedParentheses(): # this is defined function for balanced parentheses which can be called
    user_input = input("\nEnter a string only consisting of ( { [ ] } ): ") # the user_input variable stores the input string of different types of parentheses


    stack = [] # the stack created as a list but functions as a stack with the methods we apply to it
    mapdictionary = {")" : "(", "}" : "{", "]" : "["} 
    """ A dictionary is used for the matching process of checking if the parentheses at the top of the stack and see if it has a value which matches with one of the keys
    of the key-value pair """

    def push(element): 
        stack.append(element)
    """ The push function was created to mimic the append execpt created for the stack as a method since stacks use functions or push and pop; think of 
    it as an append function for lists """

    for char in user_input:
        """ Iterates through the user input which consists of parentheses of ( { [ ] } ) """
        if char in mapdictionary.values():
            """ The if statement checks if the element being iterated is included as a value in the key-value dictionary named mapdictionary """
            push(char)
            """ The push function was called here with the argument char - also called the iterated element being passed in to function """
        elif char in mapdictionary:
            """ elif statement checks if the char element being iterated is included in the mapdictionary whether it is a key or a value does not have to just 
            be a value unlike the previous if statement """
            if not stack or stack.pop() != mapdictionary[char]:
                """ The if statement checks after the char element is found in the dictionary then this if statement checks if the char element is not in the stack and 
                the popped element in the stack or i.e. the top element using the Last-in-First-Out stack is not equal to the values of any values from the dictionary """
                return ("Balanced Parentheses: {}\n".format(False))
            """ The return statement shows False in this case if the element was not a parentheses defined in the dictionary and a matching open/close parenthesis """
    return ("Balanced Parentheses: {}\n".format(not stack))
""" The return statement shows True in this case if the element was not a parentheses defined in the dictionary and a matching open/close parenthesis """

print(hasBalancedParentheses()) # print statement takes the argument of function call to output the return statement in the terminal window
print("Test Case 1: {}".format(hasBalancedParentheses())) # print statement takes the argument of function call to output the return statement in the terminal window
print("Test Case 2: {}".format(hasBalancedParentheses())) # print statement takes the argument of function call to output the return statement in the terminal window
print("Test Case 3: {}".format(hasBalancedParentheses())) # print statement takes the argument of function call to output the return statement in the terminal window

""" Time Complexity is O(N) and Space Complexity is O(N) """

""" Assignment 3 Coding Question 2 """

def ReversePolishNotationCalculator(): # this is defined function for RPN ReversePolishNotationCalculator which can be called
    user_input2 = input("\nEnter character tokens consisting of number values preferably integers and + - * / operators [After appending all values please press Enter to finish]: ") # the user_input variable stores the input string of integers and different operators of + - / * 
    split_text_to_list = [] # This is initially an empty list and it is used in the code to store each value and operator as a string token list
    string_token_characters = "" 
    """ The string token characters will take in each character of the user_input before a space appears """

    for char in user_input2:
        """ The char variable temporarily holds each element iterating through the input taken from the user """
        if char == " ":
            """ The temporary char variable is compared to be equal to the space " " and if the char is a space-the space would act like a separator """
            if string_token_characters != "":
                split_text_to_list.append(string_token_characters)
            string_token_characters = ""
            """ The if statement checks to see if a string_token_characters is not equal to an empty string and if that is the case will append that section of the
            values or operator that appears before the space to be append to the created empty list split_text_to_list then the string_token_characters will be set 
            back to being empty string """
        else:
            string_token_characters += char
            """ The else statement to show what happens if the temporary char is not a space character " " and string_token_characters is set to being the entire 
            char value what ever the value is during the iteration so for example: user enters 10 2 then the code would work to do string_token_characters += char
            which would be string_token_characters = "1" there is no space after either therefore it will also add 0 to the 1 after; string_token_characters = "10" now
            a space is found; therefore the split_text_to_list will become ["10","2"] """
        
    if string_token_characters != "":
        split_text_to_list.append(string_token_characters)
        """ If string_token_characters is not equal to an empty string after the iteration of the loop of inputs is to check to see if there are any other remaining elements
        or operators at the end of the input """

    """ Character tokens to Reverse Polish Notation Expression using stack and a list """
    stack2 = [] # stack2 variable is created and again even though it is initialized as a list; the functions the user uses on it like push and pop are part of the stack architecture

    def push(element):
        stack2.append(element)
    """ The push function was created to mimic the append execpt created for the stack as a method since stacks use functions or push and pop; think of 
    it as an append function for lists """
    
    for token in split_text_to_list:
        """ The token is the temporary variable for each element that will be received by iterating over the split_text_to_list variable list which holds the character
        tokens """
        try:
            number = int(token)
            push(number)
        except ValueError:
            """ The try is used because the character tokens are string format and to be able to evaluate them we have to get them to integer number format by typecasting
            then using the user created push function which is basically just equivalent with append we push that number onto the stack; the except function is used
            for the ValueError and if that ValueError was executed the program build assumes that the character token must have been an operator which is why it is 
            used as a condition and when except is executed the lines below are executed """
            value1 = stack2.pop()
            value2 = stack2.pop()
            """ The value1 and value2 are the top most values of the stack and that is why they are each assigned with the stack2.pop() """
            if token == "+":
                result = value1 + value2
            elif token == "-":
                result = value1 - value2
            elif token == "*":
                result = value1 * value2
            elif token == "/":
                if value2 == 0:
                    raise ZeroDivisionError ("\nCan not divide by zero it is undefined")
                result = value2 // value1
            else:
                raise ValueError ("\nNo Corresponding operator found")
            push(result)
            """ The above lines are condition statements each checking the string equivalence of the operator and what I mean by that is if the string in the character token
            is "+" then the token which is "+" == "+" would be true hence causing the if statement for token == "+": to be executed and the result variable will be set 
            with value1 + value2 and that would be the same with the other conditional statements i.e. if operator is "-" it would subtract two values, if operator is "*"
            it would it would multiply value1 and value2 and furthermore, eventually calling the push function to append the total result to the stack2 stack """


    return ("\nThe RPN Expression {} is equal to = {}\n".format(split_text_to_list, stack2.pop())) 
""" The return statement returns the original reversepolishnotation expression and then the value it should be equal to once evaluated """
    

print(ReversePolishNotationCalculator()) # print statement takes the argument of function call to output the return statement in the terminal window
print("Test Case 1: {}".format(ReversePolishNotationCalculator())) # print statement takes the argument of function call to output the return statement in the terminal window
print("Test Case 2: {}".format(ReversePolishNotationCalculator())) # print statement takes the argument of function call to output the return statement in the terminal window
print("Test Case 3: {}".format(ReversePolishNotationCalculator())) # print statement takes the argument of function call to output the return statement in the terminal window

""" Time Complexity is O(N) and Space Complexity is O(N) """

""" Assignment 3 Coding Question 3 """

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    """ The code to first initialize a class Node so that is can be used to hold data and be called in another class to add to that data along with the variable
    to the next node as a pointer """

class MyLinkedLists:
    
    def __init__(self):
        self.head = None
    """ The code initializes the main class MyLinkedLists which creates a self.head node to indicate the beginning of the link list """

    def indexatstart(self, data):
        if not self.head:
            self.head = Node(data)

        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)
    """ indexatstart defined function is creating and arguments it accepts are self along with data next it checks to see condition if not self.head then it assigns 
    self.head to the Node(data) which will be set to the first instance that passes a number value into the Node class and the first value of the link lists [they should
    be the same value], if the else statement is executed then the current variable will hold self.head as the current node then while loop will be executed for the node
    after the self.head current node and the current variable updates to current.next, current.next is then assigned to Node(data) """

    def reverse_list(self):

        previous_node = None
        current = self.head
        while current:
            next = current.next
            current.next = previous_node
            previous_node = current
            current = next
        self.head = previous_node
    """ This is the function created to be called later on towards the end of the code to reverse the same linked list that was outputted without creating 
    another linked list, it uses three pointers which are the previous_node initially set to None, the current_node = self.head, then the next_node and we are updating them
    as the while loop is on the current pointer how we are doing that the next node where it shows current.next = is being assigned to previous_node which shows that logically
    thinking instead of moving forward using next we are moving in the backward direction causing the list to be in reverse order using this logic to where
    at last the self.head would be the last node from the original link list which would now appear in the front of the list"""


    def display(self):
        
        elements = []

        current_node = self.head

        while current_node:
            elements.append(str(current_node.data))
            current_node = current_node.next

        return " ".join(elements)
    """ This function called display uses only the self instance attribute to display the linked list and it then creates an empty list, then currentnode = the self.head
    first node and then while current_node is true: the current_node.data in the string format would be appended to the empty list that has been created while the second
    line sets the current_node to be current_node.next, and finally the last line would return a value of all the elements that will just have a space in between them when
    they are joined as a list """
    
linklist = MyLinkedLists()
linklist.indexatstart(5)
linklist.indexatstart(7)
linklist.indexatstart(1)
linklist.indexatstart(2)
linklist.indexatstart(3)
print("\nThe linked list before reverse: {}\n".format(linklist.display()))
""" The linklist variable assigns to the MyLinkedLists() class for the cause that it can be accessed by the class and def functions in the class
then it uses linklist.indexatstart to call that function and pass data as argument to the function for the data instance, hence the print statement linklist.display()
would output the linkedlist normally before it gets reversed """

linklist.reverse_list()
""" The linklist.reverse_list() would allow the list to access the defined function reverse_list() we created for the cause to reverse the order of
original link list """

print("The reversed linked list is: {}\n".format(linklist.display()))
""" Print linklist.display() again would cause the reversed list to be outputted """

""" Test Cases """

""" Test Case 1 """
linklist2 = MyLinkedLists()
linklist2.indexatstart(6)
linklist2.indexatstart(10)
linklist2.indexatstart(13)
linklist2.indexatstart(23)
linklist2.indexatstart(35)
print("\nTest Case 1 The linked list before reverse: {}\n".format(linklist2.display()))

linklist2.reverse_list()

print("Test Case 1 The reversed linked list is: {}\n".format(linklist2.display()))

""" Test Case 2 """
linklist3 = MyLinkedLists()
linklist3.indexatstart(70)
linklist3.indexatstart(20)
linklist3.indexatstart(7)
linklist3.indexatstart(26)
linklist3.indexatstart(57)
print("\nTest Case 2 The linked list before reverse: {}\n".format(linklist3.display()))

linklist3.reverse_list()

print("Test Case 2 The reversed linked list is: {}\n".format(linklist3.display()))

""" Time Complexity is O(N) and Space Complexity is O(1) """