ten_things = 'Apples Oranges Crows Telephone Light Sugar'

print('Wait there\'s is not 10 things in that list, let\'s fix that.')

stuff = ten_things.split(' ')
more_stuff = ['Day', 'Night', 'Song', 'Frisbee', 'Corn', 'Banana', 'Girl', 'Boy']

while len(stuff) != 10:
    next_one  = more_stuff.pop()
    print('Adding: ', next_one)
    stuff.append(next_one)
    print('There is %d items now.' % len(stuff))

print('There we go: ', stuff)

print('Let\'s do something with stuff.')

print(stuff[1])
print(stuff[-1]) # whoa! fancy
print(stuff.pop())
print(' '.join(stuff)) # what? cool
print('#'.join(stuff[3:5])) # super stellar!

# --Output--
# Wait there's is not 10 things in that list, let's fix that.
# Adding:  Boy
# There is 7 items now.
# Adding:  Girl
# There is 8 items now.
# Adding:  Banana
# There is 9 items now.
# Adding:  Corn
# There is 10 items now.
# There we go:  ['Apples', 'Oranges', 'Crows', 'Telephone', 'Light', 'Sugar', 'Boy', 'Girl', 'Banana', 'Corn']
# Let's do something with stuff.
# Oranges
# Corn
# Corn
# Apples Oranges Crows Telephone Light Sugar Boy Girl Banana
# Telephone#Light
