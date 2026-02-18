conjunto1 = {1,2,3,4}
conjunto2 = set([1,2,3,4])

conjunto1.add(5)
print(conjunto1)

conjunto2.discard(1)
print(conjunto2)


conjunto3 = conjunto1.union(conjunto2)
print(conjunto3)

conjunto4 = conjunto1.intersection(conjunto2)
print(conjunto4)

