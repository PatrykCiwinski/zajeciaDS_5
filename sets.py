odd =set([i for i in range(1,24) if i%2!=0])
primes=set([i for i in odd if all(i % j != 0 for j in range(2, i))])
print(primes)
print("___________________")
print(odd | primes) # dodajemy
print("___________________")
print(odd & primes) # części wspólne
print("___________________")
#pozbywamy się duplikatów, set ich nie ma
lst=list(set([1,1,2,2,3,3,4,4]))
print(lst)
