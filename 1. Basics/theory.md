## Programming is basically giving instructions to a computer in a language it can understand. Ex: Python
## Python 
- It is high level language
- Used in AIML/Automation/DSA/Data science/Webdev
- case sensitive
- dynamically tped language(no need to declare the data type)

## How python executes your code?
Your Python source => Python implementation => Bytecode/runtime execution => Computer => Output

## Variable 
- variable name in Python is a name that refers to an object.
- x = 10 (x is variable, 10 is object/value, = is assignment operator), read it as x refers to 10

## Datatypes
- A data type tells Python what kind of object it is dealing with and what operations make sense for that object.
Note: x=10, y=x, then x and y refers to 10, if x values is chanegd to 20, x=20, now x values is updated to 20 but y is still refering to 10
### Type: type() is a function that helps us to find the type of data type
- int => whole no(ex: 25)
- boolean => True/False
- float => decimal(3.4)
- Nonetype => absence of value(ex: none)
- str => sequence of char(ex: "srujan")

type coversion or type casting => changing of one data type to another

## Operators
- Arithmetic : +  -  *  /  //  %  **
- Comparison : ==  !=  >  <  >=  <=
- Logical : and  or  not
- Assignment : =  +=  -=  *=  /= 
Expressions => An expression is code that Python can evaluate to produce a value.
Operands => The things the operator works on are called operands.
Operators => An operator is a symbol or keyword that tells Python to perform an operation.(ex: +-*/)
Operator precedence

### Arithmetic operators
a=10
b=3
- print(a+b) #Addition: 13
- print(a-b) #Subtraction: 7
- print(a*b) #Multiplication: 30
- print(a/b) #True divison: 3.333333333335, true division will produce float. and why extra 5 bcz decimal numbers cannot be represented exactly in binary floating-point. same case with 0.1+0.2
- print(a//b) #Floor divison: 3, this will give only, in case of negative(-7//2 = 3.5 but it will give 4), Floor means: go toward negative infinity.
- print(a%b) #Modul0: 1, gives the remainder
- print(a**b) #Exponenation: 1000, 10^3

### Comparison operators
a=20
b=10
- print(a==b) => Returns True/False
- print(a>=b) => greater than or equal to
- print(a != b) => not equal to
- print(a<=b) => less than or equal to
Note: =(assignment) and ==(comparison) are different

### Logical operators
- and, or and not
a = True
b = False
- print(a and b) => both condition must be True
- print(a or b) => only one condition can be True
- print(not a) => negate the value(Reverses a Boolean value)

### Precedence of operators: 
() > (**) > (*) > (/) > (//) > (%) > (+) > (-)
ex: (2 + 3) * 4
=> 5 * 4
=> 20

## Input Output
- print("srujan", "loves", "python", sep="❤️")
- print("srujan", end="!@!")
- print("Hello\nWorld") => newline

## String
- string is simply sequence of characters
- immutable
- indexing in python starts from 0, bcz if P we can say, move 0 pos from starting, if y, we can say move 1 pos from starting and it is much more easy to calculate physical address.
Character:   P    y    t    h    o    n
Positive:    0    1    2    3    4    5
Negative:   -6   -5   -4   -3   -2   -1

### String manipulation techniques
word="SrujanPattar"
- print(len(word)) => length of string
- print(word[1:4]) => string slicing, end is not included
- print(word[1:8:2]) => start:end:step => end one place before end and step means how many positions to jump each time
- "Sr" in "Srujan" => in operator(memebership)
- print(word.startswith("S")) => True
- print(word.endswith("s")) => False
- print(name.find("Pattar")) => searches that substring

Cheat code for slicing of string:
word[2:5]  => index 2 → 4
word[:5]   => beginning → 4
word[2:]   => index 2 → end
word[:]    => entire string
word[::2]  => every 2nd character
word[::-1] => reverse

### Three types of errors:
- Syntax Error => "Python doesn't understand how you wrote it."
- Runtime Error => "Python understood it, but couldn't execute it."
- Logical Error => "Python executed it successfully, but the answer is wrong."
- NameError => The name/variable doesn't exist.
- TypeError => The operation doesn't work with those types.
- ValueError => The type is appropriate, but the value isn't valid.