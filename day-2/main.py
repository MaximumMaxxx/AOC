input = open("input.txt","r")
input_raw = input.read()

inputlst = [item for item in input_raw.split('\n')]

for i in range(len(inputlst)):
    inputlst[i] = inputlst[i].split(' ')

horizontal = 0
vertical = 0
aim = 0

for movement in inputlst:
    if movement[0] == 'forward':
        horizontal+=int(movement[1])
        vertical+=int(movement[1])*aim
    elif movement[0] == 'backward':
        horizontal-=int(movement[1])
        vertical-=int(movement[1])*aim
    elif movement[0] == 'down':
        aim+=int(movement[1])
    elif movement[0] == 'up':
        aim-=int(movement[1])

print(f"The final horizontal postion is {horizontal}")
print(f"The final vertical postion is {vertical}")
print(f"The combined final position is {horizontal*vertical}")