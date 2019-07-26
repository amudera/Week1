#input prompts the user for an input that could be used for computations. Print prints that input as a string 
word = input("What word would you like to print?")
print(word)

import math
math.isclose(.1 + .2, 0.3) #Returns TRUE if values a,b are close to eachother, false otherwise math.isclose(a,b)

varlist = [2,4,6,8,10] 
addition = sum(varlist) #prints the sum of elements 
rounded = round(addition) # rounds a number
Total = len(varlist) # counts the number of elements in a list 
Integer = int(addition) # makes the variable into an integer
decimals = float(addition) # make the variable into a number with decimal points
makestring = str(addition) # turns the variable into a string, which is a character, not a number

dict:{                      #A dictionary stores multiple values in key:value format. Each value is unique and doesnt need to be ordered
    Day: 20;
    Month: 'January';
    Year: 1990;
    Name: 'Puttu';
}
 #in contrast the dict() function can build dictionaries from sequences of key value pairs e.g
 dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
 dict{x: x**2 for x in (2, 4, 6)} # this returns {2: 4, 4: 16, 6: 36}
 
 tuple(), list(), set())