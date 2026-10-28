#function to perfprm dfs
def dfs(graph,node,visited):
  if node not in visited:
        print(node,end=" ")
        visited.add(node)

        for neighbour in graph[node]:
            dfs(graph,neighbour,visited)

#main program
graph={}

n=int(input("enter the number oF vertices:"))

for i in range(n):
  vertex=input(f"enter vertex{i+1}: ")
  neighbours=input(f"enter adjascent vertices of {vertex} (space-separated): ").split()
  graph[vertex]=neighbours

start=input("enter the starting vertex: ")

print("\ngraph:",graph)
print("dfs traversal:",end=" ")


visited=set()
dfs(graph,start,visited)