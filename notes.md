1. variable naming should meaning full
2. use underscore to separate words not space
3. put space arount = sign in variable


string 
1. used quote " " ' ' 
2. len = length of the string  
3. function () to use the function 


scape sequence 
1. second string is the end of the string so its like " " or ' ' or ' " " ' 
2. backslash \ to scape the double coat 
    . \ " 
    . \ ' 
    . \\ 
    . \n = new line 



formatted string 
1. defined 1 variable to set formatted string / concat


String methods 
1. len() length of strings
2. object are method that called access using the dot access . 
3. strip() its remove the white space
4. lstrip, rstrip its just left and right strip
5. find()
6. python is case sentivite language


numbers 
1. arithmetics maths operators

working with numbers 
1. round() roundoff
2. abs()  its absolute value 
3. pthon3 math module


type conversion 
1. first number and string cannot to converted directly in the compiler 
2. like the first one the string and number cannot be concatenated  " " + 1 



fundamentals of programming 
1. comparison operators 
2. conditional statements 
3. ternary operator 
4. short circuit evaluation
5. loops 
6. loops if else
7. nested loop
8. iterables
9. while loops
10. infinite loops


functions 
1. def => define 
2. arguments
3. types of function
    .perform a task
    .calculate the value




collections
1. list = order  []
2. set = unorder {}
3. tuple = ()


2d list
1. 2 dimen [] []
2. matrix and grid data [] []


dictionaries
1. collection types 
2. consist key value pairs
example : id : name, item : price




functions 
resuable collection
block of resuable code 








list comprehension = concise way to list in py, expression 
construction
variable = [expression for loop if condition]





match case statement - similar to switch case statement 



module = use import useful to break large program




variable scope = where it variable and accessible
scope resolution = local, enclosed B G E L 
B - built in
G - global 
E - enclosed
L - local

if __name__ == __main__  = this means function and classes can be reused













day 13:
PYTHON OBJECT Oriented programming 
object - bundle of related attributes
class - blueprint used to design the structure and layout

class varible = shared among all instances of a class defined outside the constructor allow you to share data among object 

note in class variable - it should be class not the construction so its should the capital one 












day 13: 
Inheritance - allows a class to inherit attributes and methods from another class

2 types of inheritancess
-multiple inheritance = inherit from more than one parent
-multilevel inheritance = inherit it from parent which is from another parent



day 13:
super() = function used in a child class to call methods from a parent class (superclass) it allows you to extend 



day 13:
polymorphism = poly = many , morphe = form
duck typing = another way to achieve polymorph beside inheritance

static method = method belong to class rather than any object from that class (instances)
instances methods = best for operations on instances of the class (object)
static methods = best for utility functions that do not need access to class data








day 14: 
class methods = Allow operations related to the class itself
              = take (self) as the first parameter
              = take (cls) as first parameter


magic methods = dunder methods (double underscore) like __init__ , __str__ , __eq__


property = decorator used to define method as project 
         = benefits add additional logic when read, write and delete attributes


decorator = a function that extends the behavior of another function w/o modifying the base function



exception = an event that interrupts the flow of program 
            1.try 2. except 3. finally





file detection 
2 types 
    1. relative path = iisang folder or same path with the main file kaya kahit name nalang ilagay
    2. absolute path = whole path location na mismo. mas direct location something like that


output handling
3 types 
    1. file path = text
    2. file path = json need i iterate/loop each to write each data
    3. file path = csv same as json need iterate/loop each 
        - each file path have try and execpt for security also for prevention of error 



day 14: 
    py reading file same as the output handling
    

day 14:
    date time = format variable name = import datetime.datetime.now = current date
              = variable name = import datetime.datetime("pass ng date pedeng year, month, day")

            
day 15: 
    multithreading = used to perform multi task concurrently (multitasking)
    good for i/o

    