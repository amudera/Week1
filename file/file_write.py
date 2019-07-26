with open("outfile.txt", 'w') as file_object:
    file_object.write("first string\n")
    file_object.write("second string\n")
    file_object.write("third string\n")

with open("outfile2.txt", "w") as file_object:
    print("first string", file=file_object)
    print("second string", file=file_object)

# This uses the append method ('a')
with open("outfile2.txt", "a") as file_object:
    print("third line", file=file_object)
