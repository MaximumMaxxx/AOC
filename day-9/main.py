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


rslt = []
i,j = (0,0)
def basin_check(arr:list):
    print("Recusion")
    arr = arr
    nomore= True
    for i,j in arr:
        # Left
        if j != 0 :
            if (i,j-1) not in arr and int(inputsplit[i][j-1]) != 9:
                arr.append((i,j-1))  
                nomore= False
        
        # Right
        if j != len(inputsplit[0])-1 :
            if (i,j+1) not in arr and int(inputsplit[i][j+1]) != 9:
                arr.append((i,j+1))  
                nomore= False
        # Up
        if i != 0 :
            if (i-1,j) not in arr and int(inputsplit[i-1][j]) != 9:
                arr.append((i-1,j))  
                nomore= False
        # Down
        if i != len(inputsplit)-1 :
            if (i+1,j) not in arr and int(inputsplit[i+1][j]) != 9 :
                arr.append((i+1,j))
                nomore= False

    if nomore:
        global rslt
        rslt = arr
        return
    else: arr = basin_check(arr=arr)

basins = []
for i,j in lows:
    basin_check(arr=[(i,j)])
    basins.append(rslt)

sorted_basins = sorted(basins, key=len)
sorted_basins.reverse()

print(f"The three largest basins are {len(sorted_basins[0])}, {len(sorted_basins[1])}, and {len(sorted_basins[2])} meaning the final answer is {len(sorted_basins[0])*len(sorted_basins[1])*len(sorted_basins[2])}")