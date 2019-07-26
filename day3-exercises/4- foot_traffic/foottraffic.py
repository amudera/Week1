
def print_file(filename):
    printed_text = []
    with open(filename) as file_object:
        text = file_object.readlines()
    for line in text:
        printed_text.append(line.split())
    return printed_text

    #cleaning the data by separating the characters

dataset = print_file("traffic.txt")

def users_in(dataset):
    users_in = []
    for item in dataset:
        if item[2] == "I":
            users_in.append(item)
    return users_in

def users_out(dataset):
    users_out = []
    for item in dataset:
        if item[2] == "O":
            users_out.append(item)
    return users_out

users_coming = users_in(dataset)
users_going = users_out(dataset)

