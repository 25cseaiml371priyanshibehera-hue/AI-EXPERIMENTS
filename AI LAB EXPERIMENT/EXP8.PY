from collections import deque

#function to solve water jug problem using bfs
def water_jug(capacity1,capacity2,target):
   visited=set()
   queue=deque()

#initial state:both jugs are empty
   queue.append((0,0,[]))

   while queue:
       jug1 , jug2 , path= queue.popleft()

#skip if the state has already been visited
       if(jug1,jug2) in visited:
          continue

       visited.add((jug1,jug2))
#add current state to path
       current_path=path+[(jug1,jug2)]

       if jug1==target or jug2==target:
          return current_path

#generate all possible next states
       next_states=[
     #fill jug1
           (capacity1,jug2),
     #fill jug2
           (jug1,capacity2),
     #empty jug1
           (0,jug2),
     #empty jug2
           (jug1,0),
     #pour jug1>jug2
           (

               jug1-min(jug1,capacity2-jug2),
               jug2+min(jug1,capacity2-jug2)
           ),
     #pour jug2>jug1
          (
               jug1+min(jug2,capacity1-jug1),
               jug2-min(jug2,capacity1-jug1)
          )
      ]

 #add unvisited states to the queue
       for state in next_states:
          if state not in visited:
             queue.append((state[0],state[1],current_path))

#no solution found
   return None
#main program
jug1_capacity=int(input("enter capacity of jug1: "))
jug2_capacity=int(input("enter capacity of jug2: "))
target_amount=int(input("enter target amount: "))

solution=water_jug(jug1_capacity,jug2_capacity,target_amount)

if solution:
   print("\n steps to reach the target ")
   for step in solution:
     print(step)
else:
   print("no solution exists")