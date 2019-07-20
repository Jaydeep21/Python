from collections import defaultdict

#lets take the number of edges our graph has
n = int(input("Specify the number of branches: "))
#making a graph with default value of list
graph = defaultdict(list)
#taking vertices of edges
for i in range(n):
    nodes = list(map(int,input().split()))
    #adding it to graph list
    graph[nodes[0]].append(nodes[1])
#taking the initial or starting point of the search    
s = int(input("Specify the starting node: "))
#initializing a visited array with false i.e. 0 values according to the number of nodes in graph
visited = [False] * (len(graph))
#initailizing queue
queue = []
#appending values in queue
queue.append(s) 
#marking true to the values that are visited
visited[s] = True
while queue: 
    #running the loop until the queue ends
    s = queue.pop(0) 
    #removing the first value i.e. the 0th position of the queue
    print (s, end = " ")        
    #visit all graph nodes 
    for i in graph[s]:
        #if node is not visited i.e. false then append the value to the queue and mark it as True
        if visited[i] == False: 
            queue.append(i) 
            visited[i] = True
 
