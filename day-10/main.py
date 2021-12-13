with open("input.txt","r") as f:
    input = f.read().strip().split("\n")

openchars = ["(","[","{","<"]
closecgars = ["Null",")","]","}",">"]
closecharmatches = {")":"(","}":"{","]":"[",">":"<"}

addon_stack_lookuptable = {"(":")","{":"}","<":">","[":"]"}

scorelookuptable = {")":3,"]":57,"}":1197,">":25137}
score = 0

for line in input:
    stack = []
    for char in line:
        if char in openchars: stack.append(char)
        else: 
            if closecharmatches[char] == stack[len(stack)-1]: stack.pop(len(stack)-1)
            else: 
                score += scorelookuptable[char]
                break

print(f"The final score for part 1 is {score}")

scores = []
for line in input:
    stack = []

    # Generating the stack
    for char in line:
        if char in openchars: stack.append(char)
        else: 
            if closecharmatches[char] == stack[len(stack)-1]: stack.pop(len(stack)-1)
            else:
                break
    addon_stack = []

    # Gnerating the add on stack
    for char in stack:
        addon_stack.append(addon_stack_lookuptable[char])
    localscore = 0


    addon_stack_copy = addon_stack.copy()
    mathorder = []

    # Generating the order of the elements
    for item in addon_stack_copy:
        print(addon_stack)
        mathorder.append(item)
        for i in addon_stack_copy:
            if i == item: addon_stack_copy.remove(item)
    localscore = 0
    print(mathorder)

    # Generating the local score
    for index,value in enumerate(mathorder):
        localscore *= 5
        try:tempscore = openchars[openchars.index(value)] * addon_stack.count(value)
        except: tempscore =0 
        print(tempscore)
        localscore += tempscore
        addon_stack.remove(value)
    print(localscore)
    scores.append(localscore)

scores.sort()

print(scores)

