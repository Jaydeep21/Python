from collections import defaultdict

n = int(input("Specify the number of branches: "))
graph = defaultdict(list)
for i in range(n):
    nodes = list(map(int,input().split()))
    graph[nodes[0]].append(nodes[1])
s = int(input("Specify the starting node: "))
#print(s)
def DFSUtil(s,visited): 
  
    # Mark the current node as visited and print it 
    visited[s]= True
    print (s, end=" ")
  
    # Recur for all the vertices adjacent to this vertex 
    for i in graph[s]: 
        if visited[i] == False: 
            DFSUtil(i, visited) 
  
  
    # The function to do DFS traversal. It uses 
    # recursive DFSUtil() 
def DFS(s): 
    #print(len(graph))
        # Mark all the vertices as not visited
    visited = [False]*(len(graph)) 
          
        # Call the recursive helper function to print 
        # DFS traversal 
    DFSUtil(s,visited)

DFS(s)
