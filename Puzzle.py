start = [['P', '_', '_', '*', '*'],
         ['*', '_', '_', '_', '_'],
         ['*', '*', '_', '*', '*']]
goal = [['_', '_', '_', '*', '*'],
         ['*', '_', '_', '_', '_'],
         ['*', '*', 'P', '*', '*']]
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
def children(element1):
    prelist = []
    rows = len(element1)
    cols = len(element1[0]) if rows > 0 else 0
    P_position = None

    # Find the position of 'P'
    for i in range(rows):
        for j in range(cols):
            if element1[i][j] == 'P':
                P_position = (i, j)
                break
        if P_position:
            break

    if not P_position:
        return []

    x, y = P_position
    neighbors = [
        (x, y - 1),  # Left
        (x, y + 1),  # Right
        (x - 1, y),  # Up
        (x + 1, y)   # Down
    ]

    for neighbor in neighbors:
        i, j = neighbor
        if 0 <= i < rows and 0 <= j < cols and element1[i][j] == '_':
            # Create a deep copy of the matrix to store each result
            result_matrix = [row[:] for row in element1]
            # Move 'P' to the current neighbor
            result_matrix[x][y], result_matrix[i][j] = result_matrix[i][j], result_matrix[x][y]
            prelist.append(result_matrix)

    return prelist
def heuristic2(element2,cost2):
    x, y = None, None
    for i in range(3):
        for j in range(3):
            if element2[i][j] == 'P':
                x, y = i, j

    if x is not None and y is not None:
        target_x, target_y = 2, 2  # Target position
        value = abs(x - target_x) + abs(y - target_y)  # Calculate Manhattan distance
        value1=value+cost2
        return value1
    else:
        return float('inf') 

def heuristic(prelist,cost):
    openlist = []
    for i in prelist:
        f = heuristic2(i,cost)
        openlist.append((i, f))

    openlist.sort(key=lambda x: x[1])
    element3 = None
    f1= None
    if openlist:
        for item in openlist:
            if item[0] not in close:
                element3 = item[0]
                f1= item[1]
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
    elif f >= 30:
      print("Not found!")
      push(goal)
      break
    else:
      push(element4)