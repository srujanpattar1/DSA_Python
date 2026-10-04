## Define python 
- Scripting language
- Dynamically typed language (no need to mention data type in prior)
- Automatic garbage collection 
- Used in AIML/automation/backend sys

## Variable
- It is name pointing to some data.

## Data types
- int 
- float
- boolean (True/False)
- str
- None

## Operators
- Add(+)
- Sub(-)
- Mul(*)
- Div(/)
- Floor Div(//)
- Rem(%)
- Power(**)

## Compariosn operators
- Greater than equal to(>=)
- Lesser than equal to (<=)
- Comparsion(==)
- Assignment(=)
- Less than, Greater than(< , >)

## Logical operators => always returns ans in boolean
- and 
- or
- not

Note: Falsy values(False, 0, 0.0, "", None)

## Conditional Statements
- if
- elif
- else

## Looping statements
- Repeat this piece of code until I tell you to stop.
- for => used when we know till what time we need to iterate 
- while => used when we don't know till what time we need to iterate
- break used to stop the loop
- continue used to skip that particular iteration 
- pass does nothing

## Data Structures 
- String
- List
- Tuple
- Set
- Dictionary

## Strings 
sequence of characters with each letters with index(how far from the beginning)

### String manipulation
name = " srujan pattar "
- name.lower() => loweercase
- name.upper() => uppercase
- name.replace("pattar", "m pattar") => replaces the words
- name.split() => separates each words into list
- name.strip() => removes unnecessary spaces at the beginning and end
- name[0] => access that index letter
- name[start:stop:step] => stop is not included
- name[::-1] => reverse the string 

## List 
- []
- it stores multiple values, it is mutable

### List manipulation
marks = [87, 98, 89, 93]
- print(marks[2]) => accessing particular index
- print(len(marks)) => length of the list
- print(marks.append(45)) => adds at the end of the list
- print(marks.pop(index)) => defaulty removes the last element, otherwise removes the specified index
- print(marks.remove(value)) => removes the ele
- print(marks.insert(pos,value)) => inserts the value in the specified pos
- for mark in marks: print(mark) => running of for loop inside marks
- print(90 in marks) => check is 90 present in marks and returns True/False

## Tuple
- ()
- it is not mutable
- Use tuples when the data shouldn't change.
marks1 = (56, 89)

## Set
- {}
- stores the unique values only
ex: set1={1,2,3,3,2,1}
it will store {1,2,3}

### Set manipulation
- print(set1.add(4)) => adds 4 at the end
- print(set1.remove(4)) => removes 4 from the set

## Dictionary
- exists in key value pair
example: 
student = {
  "name": "srujan",
  "age": 21, 
  "salary": 696969.69
}

### Dictionary manipulation
- print(student["name]) => accessing name key's value
- student["branch"]="cse => adds new key value into dict
- student["age"]=9 => modify the value
- for key, value in student.items(): print(key,value) => running for loop in dict
         