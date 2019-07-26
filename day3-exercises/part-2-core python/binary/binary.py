binary = input("Please input a binary number: ")

def binary_decimal(binary):
    start = 0
    for x in binary:
        start = start*2 + int(x)
    print(str(start))

binary_decimal(binary)

decimal = int(input("Please input a decimal: "))

def decimal_binary(decimal):
    x = decimal
    y = []
    while (decimal > 0):
        a = int(float(decimal % 2))
        y.append(a)
        decimal = (decimal - a)/2
    string = ""
    for z in y[::-1]:
        string=string+str(z)
    print(string)

decimal_binary(decimal)