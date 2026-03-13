A = {1, 2, 3, 4, 5}
B = {1, 2, 4, 6, 8}

# .union connect both sets with each other, but delete the redundant numbers
union = A.union(B)
print(union)

# .intersection prints all the variables in the sets wich are the same
intersection = A.intersection(B)
print(intersection)

# difference with the right direction show the numbers in the first set wich are not in the second set
# or shows first set - second set, all the same numbers are gone
difference1 = A.difference(B)
difference2 = B.difference(A)
print(difference1, difference2)

# symmetric_difference shows in one set wich numbers are not in both sets
sym_dif = A.symmetric_difference(B)
print(sym_dif)

C = {1, 2, 3, 4, 5}
D = {1, 2, 4}

# .issuperset means set C has all variables from D init
print(C.issuperset(D))
# is subset means in set D is a part of the set C
print(D.issubset(C))

# initial a new and empty set
S = set()

# add a value to a set
S.add(1)
print(S)

# remove this value from the set
S.remove(1)
print(S)

C = D.copy()
print(C, D)
C.clear()
print(C)
