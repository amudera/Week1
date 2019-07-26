from pprint import pprint 

def read_matrix(matrix):
    """ loads a text file of a grid of integers and creates a list of lists
    of integers representing the matrix. matrix[r][c] is the element on
    row #r and column #c """
    with open('testmatrix0.txt', 'r') as input_file:
        return [[int(column) for column in row.split()] for row in input_file]

matrix = read_matrix('testmatrix0.txt')

listmatrix = list(matrix)
        
def rowsum():
        for i in listmatrix:
                print(sum(i))
rowsum()

transpose_matrix = zip(*matrix)
transmatrix = list(transpose_matrix)

print(transmatrix)

def colsum():
        for col in transpose_matrix:
                print(sum(col))

colsum()

#colums = list(map(sum,zip(*matrix)))
#print(columns)

print(sorted(listmatrix, key=sum))
print(sorted(transmatrix,key=sum))

