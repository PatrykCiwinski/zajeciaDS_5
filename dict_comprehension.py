var=34
dt={(1,2,3):['a','b','c'],
    3.14: 'pi',
    'e':2,
    1:'zero',
    var:'text'}

# for key in dt:
#     print(dt[key])

print(dt['e'])

#metoda get lepsza bo zwraca none nie keyerror, albo to co damy jak 2 argument

print(dt.get('y'))
print(dt.get('y', 'This key doesn\'t exist'))

dc=dict(zip(['x','y','z'],(1,2,3)))

print()
print(dc)
dc1=dict(zip([i for i in range(1,11)],('abcdefghij')))

dc2={k+10:v*2 for (k,v) in dc1.items() if v in['a','e','i','o']}

print()
print(dc1)

print()
print(dc2)
print()
for key,value in dc1.items():
    print(f"klucz: {key}, wartość: {value}")
print()
for key in dc1.keys():
    print(key)
print()
for value in dc1.values():
    print(value)
print()
for k in dc1:
    print(k,end=",")


