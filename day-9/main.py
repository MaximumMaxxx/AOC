with open("input.txt","r") as f:
    input = f.read().strip().split("\n")

inputsplit = []

for i,j in enumerate(input):
    inputsplit.append([])
    for char in j :
        inputsplit[i].append(int(char))



lows = []

point_crates = []
final_score = 0
for i in range(len(input)):
    for j in range(len(input[0])):

        left = True
        right = True
        up = True
        down = True

        if j == 0: left = False
        if j == len(input[0])-1: right = False
        if i == 0: up = False
        if i == len(input)-1: down = False

        lessnt = True

        if up == True: 
            if not int(input[i][j]) < int(input[i-1][j]): lessnt=False
        if down == True: 
            if  not int(input[i][j]) < int(input[i+1][j]): lessnt=False
        if left == True: 
            if not int(input[i][j]) < int(input[i][j-1]): lessnt=False
        if right == True: 
            if not int(input[i][j]) < int(input[i][j+1]): lessnt=False

        if lessnt:
            lows.append((int(i),int(j)))



print(lows)
i,j = (0,0)
def basin_check(arr):
    nomore= True
    for i,j in arr:
        # Left
        if j != 0 :
            if inputsplit[i][j-1] not in arr and int(inputsplit[i][j-1]) != 9:
                arr.append((i,j-1))  
                nomore= False
        
        # Right
        if j != len(inputsplit[0])-1 :
            if inputsplit[i][j+1] not in arr and int(inputsplit[i][j+1]) != 9:
                arr.append((i,j+1))  
                nomore= False
        # Up
        if i != 0 :
            if inputsplit[i-1][j] not in arr and int(inputsplit[i-1][j]) != 9:
                arr.append((i-1,j))  
                nomore= False
        # Down
        if i != len(inputsplit)-1 :
            if inputsplit[i+1][j] not in arr and int(inputsplit[i+1][j]) != 9:
                arr.append((i+1,j))
                nomore= False
        print(arr)

    if nomore:return arr
    else: arr = basin_check(arr=arr)

basins = []
for i,j in lows:
    basins.append(basin_check(arr=[(i,j)]))



print(basins)