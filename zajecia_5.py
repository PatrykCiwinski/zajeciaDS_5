#list comprehension

cubes = [x**3 for x in range(1,9)]

print(cubes)

sequence = list(range(1,11))

print(sequence)

power = [i **4 for i in sequence if i%3 ==0]
print(power)

powers=[[i, i **2, i **3] for i in sequence ]
print(powers)

for p in powers:
    print(p)