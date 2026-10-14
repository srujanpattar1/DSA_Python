# Phase 3: Python Data Structures 🚀
- List
- Tuples
- Set
- Dictionaries


## List
- collection of elemenets of different data structure
- mutable 
- ordered

### List 
ex- numb=[10,20,30,40,50]
- len() tells you how many elements exist -> print(len(numb))
- Travsing => Traversal means visiting the elements one by one. -> for num in number: print(num)

### List methods:
- append() adds an element to the end -> print(numb.append(60))
- insert() adds an element at a specific index -> print(numb.insert(1,90))
- remove() removes the first matching occurence value, not all the values -> print(numb.remove(20))
- pop() uses a position to remove the element, if no pos is specified then last element is removed, only pop returns the value -> print(numb.pop(2))
- sort() -> modifies the list and returns none, sorted() -> creates a new list of sorted order and returns it, 
ex: x=numb.sort(numb) => returns none, modifies the original list and sorts it
    y=sorted(numb) => return new list of sorted order
- reverse() -> reverses the original list and returns None. numb[::-1] -> reverses the original list and returns list -> print(numb.reverse())

Note:
a=[1,2,3]
b=a
c=a.copy()
b.append(3)
print(a)
print(b)
print(c)
print(b is a)
- is checks whether two variables refer to the same object, not whether their contents are equal. 
- copy is used to take a copy of a list and store it independently

Note:
a=[1,2,3,4]
b=[1,2,3,4]
print(a==b) #checks are the values same
print(a is b) #both are pointing to different list with same value

### list[start:stop:step] #slicing
- Positive step: move left to right.
- Negative step: move right to left.
- The start index is included.
- The stop index is excluded.
- The step determines how many positions to move between selected elements.
- in checks whether a value exists in the list. not in checks whether a value does not exist. Both returns answers in boolean

Ex- 
a=[10,20,30,40]
print(a[::])