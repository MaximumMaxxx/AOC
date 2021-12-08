
main_list = []
with open("input.txt","r") as input:
    inputlst = [[item.split("|")[0].strip().split(" "),item.split("|")[1].strip().split(" ")] for item in input.read().split("\n")]

print(inputlst[0])

uniquelinecounts = [2, 4, 3, 7]

thing_count = 0

for item in inputlst:
    for thing in item[1]:
        if len(thing) in uniquelinecounts:
            thing_count +=1
            print(thing)

print(f"There are {thing_count} instances of number with a unique number of line segments")

#  6666
# 5    4
# 5    4
#  3333
# 2    1
# 2    1
#  0000

setindex = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6}
setindexinverse = ["a","b","c","d","e","f","g"]
for item in inputlst:
    final_letters = ["","","","", "","",""]
    number_codes  = ["","","","", "","","","","",""]
    uncatagorized = []

    # Sorting the letters 
    for set in enumerate(item[0]):
        if len(set[1]) in uniquelinecounts:
            if len(set[1]) == 2: number_codes[1] = set[1]
            if len(set[1]) == 3: number_codes[3] = set[1]
            if len(set[1]) == 4: number_codes[4] = set[1]
            if len(set[1]) == 7: number_codes[7] = set[1]

        else:
            uncatagorized.append(set[1])
    letters = [0,0,0,0, 0,0,0]

    # Getting the top part of the code (6)
    for letter in number_codes[7]:
        if letter not in number_codes[1]:
            difference = letter

    final_letters[6] = difference

    