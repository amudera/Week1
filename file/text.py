
file_object = open('test.txt', 'r')

# some code here

file_object.close()

with open('test.txt', 'r') as file_object:
    print(file_object)
    for line in file_object:
        pass
        # print(line.split())

with open('test.txt', 'r') as file_object:
    line = file_object.readline()
    print(line)
    line2 = file_object.readline()
    print(line2)

with open('test.txt', 'r') as file_object:
    whole_text = file_object.read()
    # print(whole_text)
    print(type(whole_text))

with open('text.py', 'r') as file_object:
    for line in file_object:
        print(line, end='')
