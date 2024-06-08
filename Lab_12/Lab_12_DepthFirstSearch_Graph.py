
""" 
Student: Hemant Kosaraju
Computer Science 2720 Lab 12
Lab Time: Wednesday April 3 2024 Location: Langdale Hall 405 2:00 PM to 2:50 PM
Due Time: Sunday April 7 2024 11:59 PM
References I had to use:
    https://github.com/esethuraman/Problems/blob/a88f2eeaffcc107603a092203a943220ccc88a72/graphs/GraphAdjacencyList.py
    YouTube Video - Depth First Search Algorithm | Graph Theory - Channel: WilliamFiset
    YouTube Video - Depth First Search (DFS) Explained: Algorithm, Examples, Code
"""

class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = {}
        """ We have implmented a class called Graph and use a constructor function with __init__(self, V) to take the Number of vertexes or nodes as input and assign
        to self.V, the instance attribute self.adj = {} is represented as a dictionary here storing as a key-value pair similar to a hash table or linked list"""

        for i in range(V):
            self.adj[i] = []
        """ The for loop iterates for the range of the value of vertexes or nodes V and the node at that particular index represented by self.adj[i] is being assigned
        to an empty list so that each node connection of the graph that the node connects to is connected to the node e.g., node 0 connects to node 1 then to node 2
        therefore the self.adj[0] at 0 would connect to the elements [1, 2] which store in this empty list, this occurs for each node """

    def add_edge(self, v, w):
        if v not in self.adj:
            self.adj[v] = []
        """ The add_edge function is taking three argument parameters self, v, w and the if condition checks that if v not in self.adj then self.adj[v] at that value which is
        not in self.adj would be assigned to an empty list """

        self.adj[v].append(w)
        """ If v is found to be in self.adj then to that list of self.adj[v] at node v the connection of that node which is passed in as the third argument w is appended
        to the value at that index e.g., we have a value like 2 and if 2 was not in self.adj then self.adj[2] would be an empty list and since 2 is a part of our edges
        then the values passed in along side 2 being v were 3 for w and 4 for w therefore the function would connect elements [3, 4] to node 2 """

    def outputgraph(self):
        for node in self.adj:
            connection = ", ".join(map(str, self.adj[node]))
            print("{} 🠖 {}".format(node, connection))
    """ This function lets us print the graph like a graph in order of the nodes connections and it shows that in self.adj when we check for each node the variable node
    would be the actual value which is the starting position for each connection and the connection variable we are defining is using a comma separator between each element
    to split each element connected to a node and changes it to a string which is an optional task, then it indexes the elements by indexing the dictionary self.adj[node]
    using the node key identifier to get the values connected to it and then finally prints or ouptuts like a graph showing the connection with arrows """

    def DFS(self, first_node):

        node_alreadyvisited = set()
            
        stack = [first_node]

        while stack:
            node = stack.pop() # gets the element on top of stack
            if node not in node_alreadyvisited: # if condition to see if the value popped from the stack and assigned to node variable is not in the node_alreadyvisited list
                node_alreadyvisited.add(node) # if it is true that the node popped from stack is not in the node_alreadyvisited list it will append the popped value to the list
                stack.extend(v for v in self.adj[node] if v not in node_alreadyvisited) # stack.extend would add each value or connected edge of the root node key to the stack if v is not in the node_alreadyvisited list, it is different from append which would have added all elements at once to the visited list and made it look like one value

        print ("\nThe order of the Depth First Traversal is: {}\n".format(node_alreadyvisited), "\n")
        
        """ Edits from previous submission """   
        # node_alreadyvisited.append(first_node) Changed this part by commenting it since it appended more elements to the node_alreadyvisited list
        #         for next_node in self.adj.get(node, []): 
        #             if not node_alreadyvisited[next_node]:
        #                 stack.append(next_node)


        """ The Depth First Search Traversal is just taking self, first_node as argument parameters and then instead of going for node_alreadyvisited being assigned
        to set to make it easier, because this is data structures and algoirthms I decided to deduplicate the list of nodes my self using a list and one for statement
        and one if statement, which then I assigned the dedeuplicated list of elements to node_alreadyvisited variable. Then I created a stack variable with the element of 
        the first node being the starting variable. for while the stack is true with elements, I have assigned the node variable to the element on top of the Last In First
        Out Stack and then had an if condition that states if the node was not a part of the node_alreadyvisited list then append that value to node already visited
        and for the next_node in self.adj[node] if that next node is not in node_alreadyvisited then it will append that next_node value to the stack using append function
        finally the print statement prints the order of the Depth First Search traversal """
            

g = Graph(6)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(4, 5)
g.add_edge(1, 3)
g.add_edge(3, 5)

g.outputgraph()

g.DFS(0)

""" Test Cases """

""" Test Case 1 """

g1 = Graph(6)
g1.add_edge(2, 3)
g1.add_edge(3, 2)
g1.add_edge(3, 4)
g1.add_edge(10, 11)
g1.add_edge(5, 6)
g1.add_edge(8, 9)
g1.add_edge(8, 10)

g1.outputgraph()

g1.DFS(2)

""" Test Case 2 """

g2 = Graph(7)
g2.add_edge(0, 1)
g2.add_edge(0, 4)
g2.add_edge(1, 5)
g2.add_edge(5, 6)
g2.add_edge(6, 8)
g2.add_edge(8, 10)
g2.add_edge(10, 11)
g2.add_edge(11, 0)

g2.outputgraph()

g2.DFS(0)