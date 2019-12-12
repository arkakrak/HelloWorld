my_file = open("my_file5.txt", "w")
my_file.writelines("I chose to write this line 1\n")
my_file.writelines("I chose to write this line 3\n")
my_file.writelines("I chose to write this line 2\n")
my_file.close()

with open("my_file5.txt", "r") as read_my_file:
    for row in read_my_file:
        read_my_file.read(3)

my_list = ["x", "y", "z"]
my_dictionary = {my_list[0]: "a", my_list[1]: "b", my_list[2]: "c"}