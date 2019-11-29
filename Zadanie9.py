input_file = open("input_file.txt", "w")
input_file.writelines("I chose to write this line 1\n")
input_file.writelines("I chose to write this line 2\n")
input_file.writelines("I chose to write this line 3\n")
input_file.writelines("I chose to write this line 4\n")
input_file.writelines("I chose to write this line 5\n")
input_file.close()

try:
    with open("input_file.txt", "r") as input_file:
        with open("output_file.txt", "w") as output_file:
            for row in input_file:
                output_file.write(row)
except (IOError, ZeroDivisionError):
    print("I/O Error or dividing by zero")

output_file_read = open("input_file.txt", "r")
print(output_file_read.read())
output_file_read.close()