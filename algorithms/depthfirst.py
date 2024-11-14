def depthfirst(graph, source):
    stack = [source]
    visited = set()

    while len(stack) > 0:
        node = stack.pop()
        if node not in visited:
            print(node)
            visited.add(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                stack.append(neighbor)

graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': [],
    'e': ['b'],
    'f': ['d']
}

depthfirst(graph, 'a')


## what is all about DFA ?
#Depth-First Search (DFS) is a graph traversal algorithm used to explore nodes and edges of a graph. 
# It starts at a source node and explores as deeply as possible along each branch before backtracking. It is called "depth-first" because it explores the deepest nodes first before moving on to nodes at the same level.
# in the first step you declare the graph and a function , such that we will pass our graph and the first node to mine for the DFS
# We created initial stack with value 'a', which will be updated later , now we have while function which is active till the stack  has a value.
# We pop the a from the stack and we add it to the visited set , so the first value in DFS is a , next we get the neighbors of a which are b and c
# we append b and c to neighbour , it's up to the algorithm to choose one amonf them for the next mine . if it chose c , then c will be poped out and added to visited set. 
# next we add c neightbour e to the stack (remember we still have b in our stack)
# so now stack is of b and e (DFS is all about the add top / remove top so last in first out. 
# since e is now at top e will be removed and and we search for e neighbor  which is b (remember we still have previous b in our stack) and continues for an iternity :).
# Remember this is all about my understanding , i may be wrong at some point.
