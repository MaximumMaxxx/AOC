with open("sampleinput.txt","r") as f:
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
    print(addon_stack)
    # Generating the math order like this: mathorder = ["]",")","}",">"]
    addon_stack_copy = addon_stack.copy()
    mathorder = []
    while len(addon_stack_copy) != 0:
        item = addon_stack_copy[0]
        mathorder.append(item)
        while item in addon_stack_copy: addon_stack_copy.remove(item)
    
    print(addon_stack)
    # Generating the local score
    for index,value in enumerate(mathorder):
        localscore *= 5
        if value in addon_stack: count = addon_stack.count(value)
        else: count = 0
        localscore += count * (index+1)
        print(localscore)



    scores.append(localscore)

scores.sort()

print(scores)

