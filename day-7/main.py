import math, time

start_time = time.time()
input = open("input.txt","r")
inputraw = input.read()

crabs = inputraw.split(",")

crabs = [int(crab) for crab in crabs]

max_crab = 0
for i in crabs:
    if i > max_crab:
        max_crab = i

print(max_crab)

def check_pos(pos,arr):
    total_fuel = 0
    for crab in arr:
        crab_fuel_cost = 1
        while crab != pos:
            if crab < pos:
                total_fuel+=crab_fuel_cost
                crab += 1
                crab_fuel_cost += 1
            else:
                total_fuel+=crab_fuel_cost
                crab -= 1
                crab_fuel_cost += 1
    return (total_fuel,pos)

minc = check_pos(1,crabs)
maxc = check_pos(max_crab,crabs)
midc = check_pos(math.floor(max_crab/2),crabs)

while minc[0] != midc[0]:
    if minc[0] < midc[0]:
        # Recalculate mid and find new max
        maxc = midc
        midc = check_pos(math.floor((maxc[1] + minc[1])/2),crabs)
    else:
        # Recalculate mid and find new max
        minc = midc
        midc = check_pos(math.floor((maxc[1] + minc[1])/2),crabs)
    print(midc)


print(f"The best fuel is {midc[0]}, Calculated in {time.time()-start_time}s")