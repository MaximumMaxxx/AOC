rolls = [67,3,19,4,64,39,85,14,84,93,79,26,61,24,65,63,15,69,48,8,82,75,36,96,16,49,28,40,97,38,76,91,83,7,62,94,21,95,6,10,43,17,31,34,81,23,52,60,54,29,70,12,35,0,57,45,20,71,78,44,90,2,33,68,53,92,50,73,88,47,58,5,9,87,22,13,18,30,59,56,99,11,77,55,72,32,37,89,42,27,66,41,86,51,74,1,46,25,98,80]
row_col_lst = [(0,5,10,15,20),(1,6,11,16,21),(2,7,12,17,22),(3,8,13,18,23),(4,9,14,19,24),(0,1,2,3,4),(5,6,7,8,9),(10,11,12,13,14),(15,16,17,18,19),(20,21,22,23,24)]
completed_boards_order = []
completed_boards_nummber = []

winning_index = 0
winning_number=0

inputtxt = open("/home/maximummaxx/Documents/Coding/Python/aoc-2021/day-4/boards.txt","r")
out = open("/home/maximummaxx/Documents/Coding/Python/aoc-2021/output.txt","w")

inputstr = inputtxt.read()

inputlst = inputstr.split("\n\n")
for i in range(len(inputlst)):
    inputlst[i] = inputlst[i].replace("\n"," ").split(" ")

for i in range(len(inputlst)):
    # https://www.delftstack.com/howto/python/python-list-remove-all/
    inputlst[i] = [int(value) for value in inputlst[i] if value != '']

def check_num(number,arr):
    for i in range(len(arr)):
        if number in arr[i]:
            for j in range(len(arr[i])):
                if arr[i][j] == number and i not in completed_boards_order: arr[i][j] = ' '

        for comb in row_col_lst:
            correct_perms = 0
            for perm in comb:
                if arr[i][perm] == ' ':
                    correct_perms+=1
            if correct_perms == 5 and i not in completed_boards_order:
                completed_boards_order.append(i)
                completed_boards_nummber.append(number)
    return(arr)


for roll in rolls:
    inputlst = check_num(roll,inputlst)

print(inputlst)
print(completed_boards_order)
print(completed_boards_nummber)

first_board = 0
last_board = 0

for item in inputlst[completed_boards_order[0]]:
    if item != ' ':
        first_board += item

for item in inputlst[completed_boards_order[len(completed_boards_order)-1]]:
    if item != ' ':
        last_board += item

first_board *= completed_boards_nummber[0]
last_board *= completed_boards_nummber[len(completed_boards_nummber)-1]

print(f"The first board to finish's score is {first_board}")
print(f"The last board to finish's score is {last_board}")