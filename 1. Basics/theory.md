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

### Arithmetic 
a=10
b=3
- print(a+b) #Addition: 13
- print(a-b) #Subtraction: 7
- print(a*b) #Multiplication: 30
- print(a/b) #True divison: 3.333333333335, true division will produce float. and why extra 5 bcz decimal numbers cannot be represented exactly in binary floating-point. same case with 0.1+0.2
- print(a//b) #Floor divison: 3, this will give only, in case of negative(-7//2 = 3.5 but it will give 4), it means goes till infinity
- print(a%b) #Modul0: 1, gives the remainder
- print(a**b) #Exponenation: 1000, 10^3
-  