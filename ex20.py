from sys import argv
from sys import argv
2 from os.path import exists
3
4 script, from_file, to_file = argv
5
6 print(f"Copying from {from_file} to {to_file}")
7
8 # we could do these two on one line, how?
9 in_file = open(from_file)
10 indata = in_file.read()
11
12 print(f"The input file is {len(indata)} bytes long")
13
14 print(f"Does the output file exist? {exists(to_file)}")
15 print("Ready, hit RETURN to continue, CTRL-C to abort.")
16 input()
17
18 out_file = open(to_file, 'w')
19 out_file.write(indata)
20
21 print("Alright, all done.")
22
23 out_file.close()
24 in_file.close()
11script, input_file = argv
def print_all(f):
print(f.read())
def rewind(f):
f.seek(0)
def print_a_line(line_count, f):
print(line_count, f.readline())
current_file = open(input_file)
print("First let's print the whole file:\n")
print_all(current_file)
print("Now let's rewind, kind of like a tape.")
rewind(current_file)
print("Let's print three lines:")
current_line = 1
print_a_line(current_line, current_file)
current_line = current_line + 1
print_a_line(current_line, current_file)
current_line = current_line + 1
print_a_line(current_line, current_file)
