from sys import argv
from os.path import exists

script, from_file, to_file =argv

# we could do these two on one line too, how?
in_file = open(from_file, 'r+')


out_file = open(to_file, 'w')
out_file.write(in_file.read())
out_file = open(to_file)
print out_file.read()


out_file.close()
in_file.close()