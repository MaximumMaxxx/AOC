input = open("input.txt","r")
inputraw = input.read()

crabs = inputraw.split(",")

crabs = [int(crab) for crab in crabs]

max_crab = 0
for i in crabs:
    if i > max_crab:
        max_crab = i

print(max_crab)

best_fuel = 99999999999999999999999999999999999
for i in range(max_crab):
    print(i)
    total_fuel = 0
    for crab in crabs:
        crab_fuel_cost = 1
        while crab != i:
            if crab < i:
                total_fuel+=crab_fuel_cost
                crab += 1
                crab_fuel_cost += 1
            else:
                total_fuel+=crab_fuel_cost
                crab -= 1
                crab_fuel_cost += 1

    if total_fuel < best_fuel:
        best_fuel = total_fuel
    
print(f"The best fuel is {best_fuel}")