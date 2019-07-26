from pprint import pprint
import re

FileName = input("Which File are you looking for? ")
print(FileName)

Search = str("X-DSPAM-Confidence:")

with open(FileName,'r') as file:
   lines = file.readlines()

def lineprint():
   convert = []
   for line in lines:
      if Search in line:
         convert.append(line.split())
   
   for i in convert:
          print(convert[i][1])
                 
   print(convert)

lineprint()
# integerconvert = lineprint()
# print(integerconvert)
# avg = mean(integerconvert)

# print(avg)

