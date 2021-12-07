import time
start_time = time.time()
input = open("input.txt","r")
inputraw = input.read()
fishes = [0,0,0,0,0,0,0,0,0]
for item in inputraw.split(","):
    fishes[int(item)] += 1

for i in range(256):
    index_0 = fishes.pop(0)
    fishes.append(index_0)
    fishes[6] += index_0

print(fishes)
total_fishes = 0
for fish in fishes: total_fishes += fish

print(f"Found a total of {total_fishes} in {time.time()-start_time}s")