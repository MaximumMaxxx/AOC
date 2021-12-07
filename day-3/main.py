input = open("sampleinput.txt","r")
input_raw = input.read()

inputlst = [item for item in input_raw.split('\n')]


bit_count = len(inputlst[0])
bits_count = []

for i in range(bit_count):
    bits_count.append([0,0])


for set in inputlst:
    print(set)
    bit_index = 0
    for bit in set:
        bit = int(bit)
        if bit == 0:
            bits_count[bit_index][0]+=1
        else:
            bits_count[bit_index][1]+=1
        print(bits_count,bit_index,bit)
        bit_index+=1


gamma = ''
for i in range(len(bits_count)):
    if bits_count[i][0] > bits_count[i][1]:
        gamma += '0'
    else:
        gamma += '1'

epsilon = str(int('1'*bit_count) - int(gamma))


print(f"The gamma is {int(gamma,2)}")
print(f"The epsilon is {int(epsilon,2)}")

print(f"Meaning the power rating is {int(epsilon,2)*int(gamma,2)}")

print(bits_count)

# Calculating c02 scrubber

co2_list = inputlst
co2_index = 0

for set in bits_count:
    bits_count=[]
    for setc in co2_list:
        print(bits_count)
        bit_index = 0
        for bit in setc:
            bit = int(bit)
            if bit == 0:
                bits_count[bit_index][0]+=1
            else:
                bits_count[bit_index][1]+=1
            bit_index+=1

    current_bit = 0 if set[0] < set[1] else 1
    new_co2 = []
    co2_list = [bit_set for bit_set in co2_list if int(bit_set[co2_index]) == current_bit]
    co2_index +=1
    if len(co2_list) == 1: break

        

print(co2_list[0])




# Calculating Oxygen generator


oxy_list = inputlst
oxy_index = 0

for set in bits_count:
    bits_count=[]
    for seto in oxy_list:
        
        bit_index = 0
        for bit in seto:
            bit = int(bit)
            if bit == 0:
                bits_count[bit_index][0]+=1
            else:
                bits_count[bit_index][1]+=1
            bit_index+=1

    current_bit = 0 if set[0] > set[1] else 1
    new_oxy = []
    oxy_list = [bit_set for bit_set in oxy_list if int(bit_set[oxy_index]) == current_bit]
    oxy_index +=1
    if len(oxy_list) == 1: break



print(oxy_list[0])