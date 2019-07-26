Romans = [
    (1000, "M"),
    ( 900, "CM"),
    ( 500, "D"),
    ( 400, "CD"),
    ( 100, "C"),
    (  90, "XC"),
    (  50, "L"),
    (  40, "XL"),
    (  10, "X"),
    (   9, "IX"),
    (   5, "V"),
    (   4, "IV"),
    (   1, "I"),
]
Num = input("Please input a number: ")
Number = int(Num)

print(type(Number))

def toroman(Number):
    Result = ""
    while Number >0:
        for x, y in Romans:
            while Number - x >= 0:
                Result += y
                Number = Number - x
        break
    print(Result)

toroman(Number)



            
