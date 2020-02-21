from sys import argv

script, filename = argv

print('We are going to erase %r.' % filename)
print('If you dont want that, hit CTRL-C (^C).')
print('If you do want that, hit RETURN')

input('? ')

print('Opening the file...')
target = open(filename, 'w')

print('Truncating the file. Goodbye!')
target.truncate()

print('Now, Im going to ask you for three lines')

line1 = input('line 1: ')
line2 = input('line 2: ')
line3 = input('line 3: ')

print('Im going to write these to the file.')

target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')

# --Output--
# $ python exe16.py test16.txt
# We are going to erase 'test16.txt'.
# If you dont want that, hit CTRL-C (^C).
# If you do want that, hit RETURN
# ? 
# Opening the file...
# Truncating the file. Goodbye!
# Now, Im going to ask you for three lines
# line 1: Mary had a little lamb
# line 2: It's fleece was white as snow
# line 3: It was also tasty
# Im going to write these to the file.
