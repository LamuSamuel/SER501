def breadthfirst(graph, source):
    queue = [source]
    visited = set()

    
    while len(queue) >0:
        node = queue.pop(0)
        if node not in visited:
            print(node)
            visited.add(node)
        for neighbour in graph.get(node,[]):
            if neighbour not in visited:
                queue.append(neighbour)
graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': [],
    'e': ['b'],
    'f': ['d']
}

breadthfirst(graph,'a')

# what is all about breadthfirst?
# Breadth-First Search (BFS) is another fundamental graph traversal algorithm, but unlike Depth-First Search (DFS), which explores deeply along one path before backtracking,
# BFS explores the graph in all directions, starting from the source node. It explores all the neighbors of a node before moving on to the neighbors' neighbors. BFS is often used to find the shortest path in an unweighted graph or to explore the graph's structure systematically.
# in our above example , we have a grph and we are trying to perform BFS,so we are having a function breadthfirst which is accepting the defined graph and a starting node which is a starting with a node a , so we store that node in a list named queue and as the list is > 0 so our logic continues
# we are trying to pop out the 0th element of our queue. But here in our case our first iteration may have only one node , but as we go further come accross muliple nodes.
#so we pop a and add it in the visited list which doen't have duplicates. now as we seach for a neighbours we have b and c , we add them to our queue and again call recursive function.
# so now pop(0) makes  this algorithm different from the DFS
# BFS is all about FIFO (add back / remove front) . so it removes b and then gets the b neighbour to join c,here b neighbour is d so queue now has [d,c] now c is popped out in next recursive call and c neighbour e is added behind the list along with d and this process continues :) 
# Remember this is all about my understanding , i may be wrong at some point.
