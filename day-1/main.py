input = open('input.txt',"r")
input_raw = input.read()


inputlst = [int(item) for item in input_raw.split('\n')]


output=[]
for i in range(len(inputlst)):
    if i == 0 or i == len(inputlst)-1:
        output.append("First")
    elif (inputlst[i]+inputlst[i+1]+inputlst[i-1]) > (inputlst[i-1]+inputlst[i]+inputlst[i-2]):
        
        output.append("Higher")
    else:
        output.append("Lower")

print(output)

heigher_count = 0
for height in output:
    if height == "Higher":
        heigher_count += 1

print(heigher_count)