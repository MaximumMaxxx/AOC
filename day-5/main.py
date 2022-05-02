import matplotlib.pyplot as plt
import time

# Importing and formatting input.txt
input_obj = open("input.txt","r")
input_raw_text = input_obj.read()

input_lines_lst = input_raw_text.split('\n')

for i in range(len(input_lines_lst)):
    input_lines_lst[i] = input_lines_lst[i].split(" -> ")

for i in range(len(input_lines_lst)):
    for j in range(2):
        input_lines_lst[i][j] = input_lines_lst[i][j].split(",")

# Ignoring any non-print(pair)
ignore_diag = False
if ignore_diag:
    new = [pair for pair in input_lines_lst if bool(pair[0][1] != pair[1][1]) ^ bool(pair[0][0] != pair[1][0])]
    input_lines_lst=new
     



print(input_lines_lst)
print(len(input_lines_lst))


# Calculating the dimensions of the table
maxX = 0 
maxY = 0

for l1 in input_lines_lst:
    for l2 in l1:
        if int(l2[0]) > maxX:
            maxX = int(l2[0])
        if int(l2[1]) > maxY:
            maxY = int(l2[1])
old_input_lines_lst = input_lines_lst

# Defining the 2d array for data storage

# https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/
arr = [[0 for i in range(maxY+1)] for j in range(maxX+1)]

print(maxX)
print(maxY)

for pair in input_lines_lst:
    # All changes are relative to the first pair
    y = int(pair[0][1])
    x = int(pair[0][0])
    if int(pair[0][0]) == int(pair[1][0]):
        # Change by Y
        if int(pair[0][1]) > int(pair[1][1]):
            # Need to go down by y
            arr[x][y] += 1
            while True:
                y -= 1
                arr[x][y] += 1
                if y == int(pair[1][1]):
                    break
        elif int(pair[0][1]) < int(pair[1][1]):
            # Need to go up by y
            arr[x][y] += 1
            while True:
                y += 1
                arr[x][y] += 1
                if y == int(pair[1][1]):
                    break
        else:
            print("Something probably broke")
    elif int(pair[0][1]) == int(pair[1][1]):
        # Change by X
        if int(pair[0][0]) > int(pair[1][0]):
            # Need to go down by X
            arr[x][y] += 1
            while True:
                x -= 1
                arr[x][y] += 1
                if x == int(pair[1][0]):
                    break
        elif int(pair[0][0]) < int(pair[1][0]):
            # Need to go up by X
            arr[x][y] += 1
            while True:
                x += 1
                arr[x][y] += 1
                if x == int(pair[1][0]):
                    break
                
        else:
            print("Something probably broke")


    elif int(pair[0][0]) > int(pair[1][0]) and int(pair[0][1]) < int(pair[1][1]):
        # Top left -> Bottom right line
        arr[x][y] += 1
        while True:
            
            x -= 1
            y += 1
            print(pair)
            print(f"{x}:{y}")
            arr[x][y] += 1
            # Since it's only 45 deg angles we shouldn't need to check y as well
            if x == int(pair[1][0]):
                break
    elif int(pair[0][0]) < int(pair[1][0]) and int(pair[0][1]) > int(pair[1][1]):
        # Bottom right -> Top left line
        arr[x][y] += 1
        while True:
            x += 1
            y -= 1
            print(pair)
            print(f"{x}:{y}")
            arr[x][y] += 1
            # Since it's only 45 deg angles we shouldn't need to check y as well
            if x == int(pair[1][0]):
                break
    elif int(pair[0][0]) > int(pair[1][0]) and int(pair[0][1]) > int(pair[1][1]):
        # Bottom left -> top right line
        arr[x][y] += 1
        while True:
            x -= 1
            y -= 1
            print(pair)
            print(f"{x}:{y}")
            arr[x][y] += 1
            # Since it's only 45 deg angles we shouldn't need to check y as well
            if x == int(pair[1][0]):
                break
    elif int(pair[0][0]) < int(pair[1][0]) and int(pair[0][1]) < int(pair[1][1]):
        # Top left -> Bottom right line
        arr[x][y] += 1
        while True:
            x += 1
            y += 1
            print(pair)
            print(f"{x}:{y}")
            arr[x][y] += 1
            # Since it's only 45 deg angles we shouldn't need to check y as well
            if x == int(pair[1][0]):
                break
    else:
        print("Something is broken lol")

final_count = 0
for row in arr:
    for col in row:
        if col > 1:
            final_count += 1

for pair in input_lines_lst:
    plt.plot((pair[0][0],pair[1][0]),(pair[0][1],pair[1][1]))

out = open("/home/maximummaxx/Documents/Coding/Python/aoc-2021/day-5/output.txt","w")
out.writelines(str(arr).replace("], [","]\n[").replace("0"," "))

print(f"The total number of overlapping points is {final_count}")
plt.savefig("vents.png")