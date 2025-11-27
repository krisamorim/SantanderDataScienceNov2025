set_a = {1,2,3}
set_b = {2,3,4}

print(f'set_a after union with set_b: {set_a.union(set_b)}')  # # using methods union (returns a new set with elements from both sets)

print(f'set_a after intersection with set_b: {set_a.intersection(set_b)}')  # using methods intersection (returns a new set with elements common to both sets)

print(f'set_a after difference with set_b: {set_a.difference(set_b)}')  # using methods difference (returns a new set with elements in set_a but not in set_b)
print(f'set_b after difference with set_a: {set_b.difference(set_a)}')  # using methods difference (returns a new set with elements in set_b but not in set_a)

print(f'set_a after difference symmetric with set_b: {set_a.symmetric_difference(set_b)}')  # using methods symmetric_difference (returns a new set with elements in either set_a or set_b but not in both)

set_c = {1,2,3}
set_d = {4,1,2,5,6,3}

print(f'Is set_c a subset of set_d? {set_c.issubset(set_d)}') # using methods issubset (returns True if set_c is a subset of set_d)
print(f'Is set_d a subset of set_c? {set_d.issubset(set_c)}') # using methods issubset (returns True if set_d is a subset of set_c)

print(f'Is set_c a superset of set_d? {set_c.issuperset(set_d)}') # using methods issuperset (returns True if set_c is a superset of set_d)
print(f'Is set_d a superset of set_c? {set_d.issuperset(set_c)}') # using methods issuperset (returns True if set_d is a superset of set_c)

set_e = {9,10,11,12}

set_e.add(13)  # using methods add (adds an element to the set)
print(f'set_e after adding 13: {set_e}') #set_e after adding 13: {9, 10, 11, 12, 13}

set_e.remove(13)  # using methods remove (removes an element from the set; raises KeyError if not found)
print(f'set_e after removing 13: {set_e}') #set_e after removing 12: {9, 10, 11, 12}

set_e.discard(12)  # using methods discard (removes an element from the set; does nothing if not found)
print(f'set_e after discarding 12: {set_e}') #set_e after discarding 12: {9, 10,11}

#isdisjoint
print(f'Is set_a disjoint with set_b? {set_a.isdisjoint(set_b)}') # using methods isdisjoint (returns True if set_a has no elements in common with set_b)
print(f'Is set_a disjoint with set_e? {set_a.isdisjoint(set_e)}') # using methods isdisjoint (returns True if set_a has no elements in common with set_e)

#using pop
set_e.pop()  # using methods pop (removes and returns an arbitrary element from the set)
print(f'set_e after popping an element: {set_e}') #set_e after popping an element: {10, 11}