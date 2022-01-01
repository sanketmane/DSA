strings = ['a', 'b', 'c', 'd']


"""
list is array like datastructure in python
the strings and numbers array above are stored somewhere in the memory and os knows about it.
"""

"""
array access/lookup
O(1)
"""
print(strings[2])

"""
add element at end of array
Since we are directly add 'e' at the end of array at a particular memory location, it is O(1)

Actually, this O(1) is called as "amortized O(1) for dynamic arrays". Read more about it here: https://en.wikipedia.org/wiki/Amortized_analysis
"""
strings.append('e')

"""
remove last element from array
O(1) because we are just accessing last memory location and not looping over the entire array
"""
strings.pop()

"""
insert element
O(n) - because we have to re-arrange indexes for the other elements which involves looping over them.
"""
strings.insert(1,'f')

"""
delete element from middle of the array
O(n) - just like insert, the indexes will need to rearranged
"""
strings.pop(1)

print(strings)


