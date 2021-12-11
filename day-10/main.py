with open("input.txt","r") as f:
    input = f.read().strip().split("\n")

openchars = ["(","[","{","<"]
closechars = [")","]","}",">"]
scorelookuptable = {"(":3,"[":57,"{":1197,"<":25137}
score = 0

for line in input:
    squares,circles,curly,arrows = 0,0,0,0
    for char in line:
        if char == "(": circles += 1
        if char == ")": circles -= 1
        if char == "[": squares += 1
        if char == "]": squares -= 1
        if char == "{": curly += 1
        if char == "}": curly -= 1
        if char == "<": arrows += 1
        if char == ">": arrows -= 1
    print(circles,squares,curly,arrows)



print(f"The final score is {score}")