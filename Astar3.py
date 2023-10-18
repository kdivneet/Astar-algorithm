start=[[2,8,3],
         [1,6,4],
         [7,0,5]
         ]
goal=[[1,2,3],
      [8,0,4],
      [7,6,5]]
cost=0
stack=[]
close=[]
stack_counter=-1
def push(item):
    global stack_counter
    stack_counter=stack_counter+1
    stack.append(item)
def pop():
    global stack_counter
    item=stack[stack_counter]
    stack.remove(stack[stack_counter])
    stack_counter=stack_counter-1
    return item
def heuristic(element,cost):
  for i in range(3):
    for j in range(3):
      if element[i][j]!=goal[i][j]:
        value=value+1
    return value+cost
def children(element1):
  prelist=[]
  rows = len(element1)
  cols = len(element1[0]) if rows > 0 else 0
  zero_position = None
  for i in range(rows):
     for j in range(cols):
       if element1[i][j] == 0:
         zero_position = (i, j)
         break
     if zero_position:
      break
  if not zero_position:
        return []
  x, y = zero_position
  neighbors = [
        (x, y-1),  # Left
        (x, y+1),  # Right
        (x-1, y),  # Up
        (x+1, y)   # Down
    ]
  for neighbor in neighbors:
        i, j = neighbor
        if 0 <= i < rows and 0 <= j < cols:
            # Create a deep copy of the matrix to store each result
            result_matrix = [row[:] for row in element1]
            # Swap zero with the current neighbor
            result_matrix[x][y], result_matrix[i][j] = result_matrix[i][j], result_matrix[x][y]
            prelist.append(result_matrix)

  return prelist
value=0
def heuristic2(element2,value):
  for i in range(3):
    for j  in range(3):
      if element2[i][j]!=goal[i][j]:
        value=value+1
  return value
def heuristic(pre1,cost1):
  openlist=[]
  for i in pre1:
    value=0
    value2=heuristic2(i,value)
    f=cost1+value2
    openlist.append([i,f])
  openlist.sort(key=lambda x: x[1])
  element3 = None
  if openlist:
        for item in openlist:
            if item[0] not in close:
                element3 = item[0]
                f1 = item[1]
                break
  return element3, f1

push(start)
open=[]
while(goal in stack)==False:
  if stack[stack_counter]==goal:
    print(stack[stack_counter])
  else:
    print("Traversing: \n")
    cost=cost+1
    dummy=pop()
    close.append(dummy)
    pre=children(dummy)
    value=0
    element4,f=heuristic(pre,cost)
    print(element4)
    if element4==goal:
      print("***************")
      print("Goal reached\n")
      print(element4)
      print("F: " , f)
      push(goal)
    elif f>=30:
      print("Not found!")
      push(goal)
      break
    else:
      push(element4)