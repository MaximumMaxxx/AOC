import math

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

