input = open("input.txt","r")
input_raw = input.read()

inputlst = [item for item in input_raw.split('\n')]

def count_bits(arr):
    output_lst = []
    for bit_index in range(len(arr[0])):
        temp_lst = [0,0]
        for item in arr:
            if item[bit_index] == '0':
                temp_lst[0] += 1
            else:
                temp_lst[1] += 1
        output_lst.append(temp_lst)
    
    return output_lst

print(count_bits(inputlst))

gamma = ''
for i in count_bits(inputlst):
    if i[0] > i[1]:
        # more 0's
        gamma += "0"
    else:
        # more 1's
        gamma += "1"

epsilon = int("1"*len(count_bits(inputlst)))-int(gamma)

gamma= int(gamma,2)
epsilon = int(str(epsilon),2)

print(f"Gamma: {gamma}")
print(f"Epsilon: {epsilon}")
print(f"Total power: {gamma*epsilon}")

# Oxygen Crap
oxy_list = inputlst
bit = 0
while len(oxy_list) != 1:
    print(len(oxy_list))
    bit_count = count_bits(oxy_list)
    check_bit = 0 if bit_count[bit][0] > bit_count[bit][1] else 1

    oxy_list = [item for item in oxy_list if item[bit] == str(check_bit)]
    bit+=1

# Co2 Crap
co2_list = inputlst
bit = 0
while len(co2_list) != 1:
    print(len(co2_list))
    bit_count = count_bits(co2_list)
    check_bit = 1 if bit_count[bit][0] > bit_count[bit][1] else 0

    co2_list = [item for item in co2_list if item[bit] == str(check_bit)]
    bit+=1

co2= int(co2_list[0],2)
oxy = int(oxy_list[0],2)

print(f"Co2: {co2}")
print(f"Oxygen: {oxy}")
print(f"Total lifesupport: {co2*oxy}")