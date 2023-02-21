#list comprehension

cubes = [x**3 for x in range(1,9)]

print(cubes)

sequence = list(range(1,11))

print(sequence)

power = [i **4 for i in sequence if i % 3 ==0]
print(power)

powers=[[i, i **2, i **3] for i in sequence ]
print(powers)


zeros = [[0 for i in range(8)] for i in range(8)]


for zero in zeros:
    print(zeros)

letters = ['a','b','y','v','o','y']
print(letters[:3])
#the same as print(letters[0:3])

print(letters[::-1])
#the same
print(list(reversed(letters)))

print(letters[-2::-1])