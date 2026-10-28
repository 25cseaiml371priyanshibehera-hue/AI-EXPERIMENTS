from collections import deque

def bfs(graph,start):
 visited=set()
 queue=deque([start])
 visited.add(start)
 print("bfs traversal:",end=" ")

 while queue:
    vertex =queue.popleft()
    print(vertex,end=" ")

    for neighbour in graph[vertex]:
      if neighbour not in visited:
        visited.add(neighbour)
        queue.append(neighbour)

graph={}

n=int(input("enter the vertices:"))

for i in range(n):
  vertex=input(f"enter vertex{i+1}:")
  neighbours=input(f"enter adjacent vertices of {vertex}(space-separated):").split()
  graph[vertex]=neighbours


start=input("enter the starting vertex:")
print("\ngraph:",graph)
bfs(graph,start)