from sys import argv
from os.path import exists

script, from_file, to_file = argv

print('Copy from %s to %s' % (from_file, to_file))

# we could do these two on one line too, how?
in_file = open(from_file)
indata = in_file.read()

print('The input file is %d bytes long' % len(indata))

print('Does the output file exist? %r' % exists(to_file))
print('Ready, hit RETURN to continue, CTRL-C to abort.')
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print('All right, all done.')

out_file.close()
in_file.close()

# --Output--
# $ python exe17.py test17_from.txt test17_to.txt
# Copy from test17_from.txt to test17_to.txt
# The input file is 21 bytes long
# Does the output file exist? True
# Ready, hit RETURN to continue, CTRL-C to abort.

# All right, all done.
