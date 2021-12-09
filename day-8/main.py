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

# 1,2,3,4,5

letters7 = ["012456","14","02346","01346","1345","01356","012356","146","0123456","013456"]

grand_total = 0

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
            if len(set[1]) == 3: number_codes[7] = set[1]
            if len(set[1]) == 4: number_codes[4] = set[1]
            if len(set[1]) == 7: number_codes[8] = set[1]

        else:
            uncatagorized.append(set[1])
    letters = [0,0,0,0, 0,0,0]

    # Getting the top part of the code (6)
    difference = [letter for letter in number_codes[7] if letter not in number_codes[1]]

    final_letters[6] = difference[0]

    # Generating a lsit of the counts + letters for the non-sorted numbers
    unsortedlettercounts = [[0,""],[0,""],[0,""],[0,""],[0,""],[0,""],[0,""]]
    for thing in uncatagorized:
        for letter in thing:
            unsortedlettercounts[setindex[letter]][0] += 1
            unsortedlettercounts[setindex[letter]][1] = letter

    # Getting letters based on the previous count
    for char in unsortedlettercounts:
        if char[0] == 3: final_letters[2] = char[1]
        if char[0] == 6 and char[1] != final_letters[6]: final_letters[0] = char[1]
        if char[0] == 5 and char[1] in number_codes[1]: final_letters[1] = char[1]
        if char[0] == 4 and char[1] in number_codes[1]: final_letters[4] = char[1]
        if char[0] == 5 and char[1] not in number_codes[1]: final_letters[3] = char[1]
        if char[0] == 4 and char[1] not in number_codes[1]: final_letters[5] = char[1]


    # Construct the numbers after the | in the original problem
    current_num = ""
    for num in item[1]:
        letterstr = ""
        for letter in num:
            letterstr += str(final_letters.index(letter))
        letterstr = "".join(str(sorted(letterstr)).translate(str.maketrans({"[":"","]":"",",":""," ":"","'":"",})))
        
        

        if letterstr in letters7:
            print("sucess")
            current_num = current_num+str(letters7.index(letterstr))
        else:
            print("error")
    grand_total += int(current_num)
    print("iter---------------------------------------")

print(f"The total of all numbers displayed on the 7 segments dislays is {grand_total}")