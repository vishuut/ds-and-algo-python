strings = ['a', 'b', 'c', 'd']

strings[2] # O(1)

strings.append('e') # O(1)

strings.pop() # O(1) (removes and returns the last element)

strings.insert(0, 'x') # O(n)

del strings[2] # O(n) (delets element at index 2 and shifts the elements after that element)

print(strings)
