my_set = {1,2,3,3,4,5,6,3,4}
my_set.discard(3)
my_set.clear()
print(my_set)

#set union method
A = {1,2,3,4,5}
B= {4,5,6,7,8}

print(A | B)
print(A.union(B))


# Set difference
# here we use the -operator
A = {1,2,3,4,5}
B= {4,5,6,7,8}
print(A & B)
print(A.intersection(B))
print(B.intersection(A))

# Set Symmetric Difference
A = {1,2,3,4,5}
B= {4,5,6,7,8}
print(A^B)

print(A.symmetric_difference(B))
print(B.symmetric_difference(A))


# Frozensets
# initialize A and B
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])
print( A.difference(B))