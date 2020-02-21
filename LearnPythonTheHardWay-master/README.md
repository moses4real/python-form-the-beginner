# Learn Python the Hard Way 

All Exercises in learnpythonthehardway book

**Link:** https://learnpythonthehardway.org/book/

**Note:** The book in the website use python 2, but these files are written in python 3. There should not be much difference though

### Exercise 1: A Good First Program
```python
print("Hello World!")
print ("Hello Again")
print("I like typing this.")
print("This is fun.")
print('Yay! Printing.')
print("I'd much rather you 'not'.")
print('I "said" do not touch this.')

print('this command will print one line')
print('this\n command\n will\n print\n multiple\n lines')
# print('nevermind')
```
```
Hello World!
Hello Again
I like typing this.
This is fun.
Yay! Printing.
I'd much rather you 'not'.
I "said" do not touch this.
this command will print one line
this
 command
 will
 print
 multiple
 lines
```

### Exercise 2: Comments and Pound Character
```python
# A comment, this is so you can read your program later.
# Anything after the # is ignored by python.

print ("I could have code like this.") # and the comment after is ignored

# You can also use a comment to "disable" or comment out a piece of code:
# print "This won't run."

print ("This will run.")
```
```
I could have code like this.
This will run.
```

### Exercise 3: Numbers and Math
```python
print ("I will now count my chickens:")

print ("Hens", 25 + 30 / 6)
print ("or")
print ("Hens", int(25 + 30 / 6))
print ("Roosters", 100 - 25 * 3 % 4)

print ("Now I will count the eggs:")

print (3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

print ("Is it true that 3 + 2 < 5 - 7?")

print (3 + 2 < 5 - 7)

print ("What is 3 + 2?", 3 + 2)
print ("What is 5 - 7?", 5 - 7)

print ("Oh, that's why it's False.")

print ("How about some more.")

print ("Is it greater?", 5 > -2)
print ("Is it greater or equal?", 5 >= -2)
print ("Is it less or equal?", 5 <= -2)
```
```
will now count my chickens:
Hens 30.0
or
Hens 30
Roosters 97
Now I will count the eggs:
6.75
Is it true that 3 + 2 < 5 - 7?
False
What is 3 + 2? 5
What is 5 - 7? -2
Oh, that's why it's False.
How about some more.
Is it greater? True
Is it greater or equal? True
Is it less or equal? False
```

### Exercise 4: Variables and Names
```python
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print ("There are", cars, "cars available.")
print ("There are only", drivers, "drivers available.")
print ("There will be", cars_not_driven, "empty cars today.")
print ("We can transport", carpool_capacity, "people today.")
print ("We have", passengers, "to carpool today.")
print ("We need to put about", average_passengers_per_car, "in each car.")
```
```
There are 100 cars available.
There are only 30 drivers available.
There will be 70 empty cars today.
We can transport 120.0 people today.
We have 90 to carpool today.
We need to put about 3.0 in each car.
```

### Exercise 5: More Variables and Printing
```python
my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'
a_random_floating_point = 3.0

print ("Let's talk about %s." % my_name)
print ("He's %d inches tall." % my_height)
print ("He's %d pounds heavy." % my_weight)
print ("Actually that's not too heavy.")
print ("He's got %s eyes and %s hair." % (my_eyes, my_hair))
print ("His teeth are usually %s depending on the coffee." % my_teeth)

# this line is tricky, try to get it exactly right
print ("If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight))
print ("Btw here is a floating point: %f." % a_random_floating_point)
print ("Btw here is a floating point: %r" % "haha")
```
```
Let's talk about Zed A. Shaw.
He's 74 inches tall.
He's 180 pounds heavy.
Actually that's not too heavy.
He's got Blue eyes and Brown hair.
His teeth are usually White depending on the coffee.
If I add 35, 74, and 180 I get 289.
Btw here is a floating point: 3.000000.
Btw here is a floating point: 'haha'
```

### Exercise 6: Strings and Text
```python
x = "There are %d types of people" % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s" % (binary, do_not)

print (x)
print (y)

print ("I said %r." % x)
print ("I also said: '%s'." % y)

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print (joke_evaluation % hilarious)

w = "This is the left side of..."
e = "a string with a right side"

print (w + e)
```
```
There are 10 types of people
Those who know binary and those who don't
I said 'There are 10 types of people'.
I also said: 'Those who know binary and those who don't'.
Isn't that joke so funny?! False
This is the left side of...a string with a right side
```

### Exercise 7: More Printing
```python
print ("Mary had a little lamp.")
print ("Its fleece was white as %s." % "snow")
print ("And everywhere that Mary went.")
print ("." * 10)

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

print (end1 + end2 + end3 + end4 + end5 + end6, end=" ")
print (end7 + end8 + end9 + end10 + end11 + end12)

print (end1 + end2 + end3 + end4 + end5 + end6, end=" - ")
print (end7 + end8 + end9 + end10 + end11 + end12)

print (end1 + end2 + end3 + end4 + end5 + end6, end="")
print (end7 + end8 + end9 + end10 + end11 + end12)

print (end1 + end2 + end3 + end4 + end5 + end6)
print (end7 + end8 + end9 + end10 + end11 + end12)
```
```
Mary had a little lamp.
Its fleece was white as snow.
And everywhere that Mary went.
..........
Cheese Burger
Cheese - Burger
CheeseBurger
Cheese
Burger
```

### Exercise 8: Printing Printing
```python
formatter = "%r %r %r %r"

print(formatter % (1, 2, 3, 4))
print(formatter % ("one", "two", "three", "four"))
print(formatter % (True, False, False, True))
print(formatter % (formatter, formatter, formatter, formatter))
print(formatter % (
    "I had this things.",
    "That you could type up right.",
    "But it didn't sing.",
    "So i said goodbye."
    ))
```
```
1 2 3 4
'one' 'two' 'three' 'four'
True False False True
'%r %r %r %r' '%r %r %r %r' '%r %r %r %r' '%r %r %r %r'
'I had this things.' 'That you could type up right.' "But it didn't sing." 'So i said goodbye.'
```

### Exercise 9: Printing Printing Printing
```python
# Here's some new strange stuff, remember type it exactly

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug\nSep\nOct\nNov\nDec"

print('Here are the days: ', days)
print('Here are the months: ', months)

print("""
There is something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")
```
```
Here are the days:  Mon Tue Wed Thu Fri Sat Sun
Here are the months:  Jan
Feb
Mar
Apr
May
Jun
Jul
Aug
Sep
Oct
Nov
Dec

There is something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
```

### Exercise 10: What Was That?
```python
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
```
```
        I'm tabbed in.
I'm split
on a line.
I'm \ a \ cat.

I'll do a list:
        * Cat food
        * Fishies
        * Catnip
        * Grass
```

### Exercise 11: Asking Questions
```python
print('How old are you?', end=' ')
age = input()
print('How tall are you?', end=' ')
height = input()
print('How much do you weigh?', end=' ')
weight = input()

print('So, you are %r old, %r tall and %r heavy.' % (age, height, weight))
```
```
How old are you? 38
How tall are you? 6'2"
How much do you weigh? 180lb
So, you are '38' old, '6\'2"' tall and '180lbs' heavy.
```

### Exercise 12: Prompting People
```python
age = input('How old are you? ')
height = input('How tall are you? ')
weight = input('How much do you weigh? ')

print('So, you are %r old, %r tall and %r height' % (age, height, weight))
```
```
How old are you? 38
How tall are you? 6'2"
How much do you weigh? 180lbs
So, you are '38' old, '6\'2"' tall and '180lbs' height
```

### Exercise 13: Parameters, Unpacking, Variables
```python
import sys

script, first, second, third = sys.argv

print('The script is called:', script)
print('Your first variable is:', first)
print('Your second variable is:', second)
print('Your third variable is:', third)
```
```
$ python exe13.py first 2nd 3rd
The script is called: exe13.py
Your first variable is: first
Your second variable is: 2nd
Your third variable is: 3rd
```

### Exercise 14: Prompting and Passing
```python
from sys import argv

script, user_name = argv
prompt = '> '

print("Hi %s, I'm the %s script." % (user_name, script))
print("I'd like to ask you a few questions.")
print("Do you like me %s?" % user_name)
likes = input(prompt)

print("Where do you live %s?" % user_name)
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print("""
Alright, so you said %r about liking me.
You live in %r.  Not sure where that is.
And you have a %r computer.  Nice.
""" % (likes, lives, computer))
```
```
$ Hi near, I'm the exe14.py script.
$ I'd like to ask you a few questions.
$ Do you like me near?
$ > Yes
$ Where do you live near?
$ > LA
$ What kind of computer do you have?
$ > quantum

Alright, so you said 'Yes' about liking me.
You live in 'LA'.  Not sure where that is.
And you have a 'quantum' computer.  Nice.
```

### Exercise 15: Reading Files
```python
from sys import argv

script, filename = argv

txt = open(filename)

print("Here's your file %r: " % filename)
print(txt.read())

print("Type the filename again:")
file_again = input('> ')

txt_again = open(file_again)

print(txt_again.read())
```
```
$ python exe15.py test15.txt
Here's your file 'test15.txt': 
This is stuff I typed into a file.
It is really cool stuff.
Lots and lots of fun to have in here.

Type the filename again:
> Exe15_sample.txt
This is stuff I typed into a file.
It is really cool stuff.
Lots and lots of fun to have in here.
```

### Exercise 16: Reading and Writing Files
```python
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
```
```
$ python exe16.py test.txt
We are going to erase 'test.txt'.
If you dont want that, hit CTRL-C (^C).
If you do want that, hit RETURN
? 
Opening the file...
Truncating the file. Goodbye!
Now, Im going to ask you for three lines
line 1: Mary had a little lamb
line 2: It's fleece was white as snow
line 3: It was also tasty
Im going to write these to the file.
```

### Exercise 17: More Files
```python
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
```
```
--Output--
$ python exe17.py test17_from.txt test17_to.txt
Copy from test17_from.txt to test17_to.txt
The input file is 21 bytes long
Does the output file exist? True
Ready, hit RETURN to continue, CTRL-C to abort.

All right, all done.
```

### Exercise 18: Names, Variables, Code, Functions
```python
# this one is like your script with argv
def print_two(*args):
    arg1, arg2 = args
    print('arg1: %r, arg2: %r' % (arg1, arg2))

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print('arg1: %r, arg2: %r' % (arg1, arg2))

# this just takes one argument
def print_one(arg1):
    print('arg1: %r' % arg1)

# this one takes no argument
def print_none():
    print("I got nothin'.")

print_two('Zed', 'Shaw')
print_two_again('Zed', 'Shaw')
print_one('First!')
print_none()
```
```
arg1: 'Zed', arg2: 'Shaw'
arg1: 'Zed', arg2: 'Shaw'
arg1: 'First!'
I got nothin'.
```

### Exercise 19: Functions and Variables
```python
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print('You have %d cheeses!' % cheese_count)
    print('You have %d boxes of crackers!' % boxes_of_crackers)
    print("Man that's enough for a party!")
    print('Get a blanket.\n')


print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
```
```
We can just give the function numbers directly:
You have 20 cheeses!
You have 30 boxes of crackers!
Man that's enough for a party!
Get a blanket.

OR, we can use variables from our script:
You have 10 cheeses!
You have 50 boxes of crackers!
Man that's enough for a party!
Get a blanket.

We can even do math inside too:
You have 30 cheeses!
You have 11 boxes of crackers!
Man that's enough for a party!
Get a blanket.

And we can combine the two, variables and math:
You have 110 cheeses!
You have 1050 boxes of crackers!
Man that's enough for a party!
Get a blanket.
```

### Exercise 20: Functions and Files
```python
from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

print('First lets print the whole file:\n')
print_all(current_file)

print('Now lets rewind, kind of like a tape.')
rewind(current_file)

print('Lets print three lines:')

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
```
```
$ python exe20.py test20.txt
First lets print the whole file:

This is line 1
This is line 2
This is line 3

Now lets rewind, kind of like a tape.
Lets print three lines:
1 This is line 1

2 This is line 2

3 This is line 3
```

### Exercise 21: Functions Can Return Something
```python
def add(a, b):
    print("ADDING %d + %d" % (a, b))
    return a + b

def subtract(a, b):
    print("SUBTRACTING %d - %d" % (a, b))
    return a - b

def multiply(a, b):
    print("MULTIPLYING %d * %d" % (a, b))
    return a * b

def divide(a, b):
    print("DIVIDING %d / %d" % (a, b))
    return a / b

print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print("Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq))

# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")
```
```
Let's do some math with just functions!
ADDING 30 + 5
SUBTRACTING 78 - 4
MULTIPLYING 90 * 2
DIVIDING 100 / 2
Age: 35, Height: 74, Weight: 180, IQ: 50
Here is a puzzle.
DIVIDING 50 / 2
MULTIPLYING 180 * 25
SUBTRACTING 74 - 4500
ADDING 35 + -4426
That becomes:  -4391.0 Can you do it by hand?
```

### Exercise 24: More Practice
```python
print('Lets practice everything.')
print('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------")
print(poem)
print("--------------")

five = 10 - 2 + 3 - 6
print('This should be five: %s' % five)

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

print('With a starting point of: %d' % start_point)
print("We'd would have %d beans, %d jars and %d crates." % secret_formula(start_point))
```
```
Lets practice everything.
You'd need to know 'bout escapes with \ that do 
 newlines and 	 tabs.
--------------

	The lovely world
with logic so firmly planted
cannot discern 
 the needs of love
nor comprehend passion from intuition
and requires an explanation

		where there is none.

--------------
This should be five: 5
With a starting point of: 10000
We'd would have 5000000 beans, 5000 jars and 50 crates.
```

### Exercise 25: Even More Practice
```python
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full setence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
 ```
 ```
$ python
Python 3.6.2 (default, Jul 20 2017, 03:52:27) 
[GCC 7.1.1 20170630] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import exe25
>>> sentence = 'All good things come to those who wait.'
>>> words = exe25.break_words(sentence)
>>> words
['All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait.']
>>> sorted_words = exe25.sort_words(words)
>>> sorted_words
['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
>>> exe25.print_first_word(words)
All
>>> exe25.print_last_word(words)
wait.
>>> words
['good', 'things', 'come', 'to', 'those', 'who']
>>> exe25.print_first_word(sorted_words)
All
>>> exe25.print_last_word(sorted_words)
who
>>> sorted_words
['come', 'good', 'things', 'those', 'to', 'wait.']
>>> sorted_words = exe25.sort_sentence(sentence)
>>> sorted_words
['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
>>> exe25.print_first_and_last(sentence)
All
wait.
>>> exe25.print_first_and_last_sorted(sentence)
All
who
```

### Exercie 26: Congratulations, Take a Test!

Fix the broken code

```python
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words)
    """Prints the first word after popping it off."""
    word = words.poop(0)
    print(word)

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""


print("--------------")
print(poem)
print("--------------")

five = 10 - 2 + 3 - 5
print("This should be five: %s" % five)

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans \ 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates == secret_formula(start-point)

print("With a starting point of: %d" % start_point)
print("We'd have %d jeans, %d jars, and %d crates." % (beans, jars, crates))

start_point = start_point / 10

print("We can also do that this way:")
print("We'd have %d beans, %d jars, and %d crabapples." % secret_formula(start_pont)


sentence = "All god\tthings come to those who weight."

words = exe26.break_words(sentence)
sorted_words = exe26.sort_words(words)

print_first_word(words)
print_last_word(words)
.print_first_word(sorted_words)
print_last_word(sorted_words)
sorted_words = exe26.sort_sentence(sentence)
prin(sorted_words)

print_irst_and_last(sentence)

   print_first_a_last_sorted(senence)

```

Solution:

```python
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""


print("--------------")
print(poem)
print("--------------")

five = 10 - 2 + 3 - 5
print("This should be five: %s" % five)

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

print("With a starting point of: %d" % start_point)
print("We'd have %d jeans, %d jars, and %d crates." % (beans, jars, crates))

start_point = start_point / 10

print("We can also do that this way:")
print("We'd have %d beans, %d jars, and %d crabapples." % secret_formula(start_point))


sentence = "All god\tthings come to those who weight."

words = exe26_fixed.break_words(sentence)
sorted_words = exe26_fixed.sort_words(words)

print_first_word(words)
print_last_word(words)
print_first_word(sorted_words)
print_last_word(sorted_words)
sorted_words = exe26_fixed.sort_sentence(sentence)
print(sorted_words)

print_first_and_last(sentence)

print_first_and_last_sorted(sentence)

```

### Exercise 28: Boolean Practice
```python
# True and True
# False and True
# 1 == 1 and 2 == 1
# "test" == "test"
# 1 == 1 or 2 != 1
# True and 1 == 1
# False and 0 != 0
# True or 1 == 1
# "test" == "testing"
# 1 != 0 and 2 == 1
# "test" != "testing"
# "test" == 1
# not (True and False)
# not (1 == 1 and 0 != 1)
# not (10 == 1 or 1000 == 1000)
# not (1 != 10 or 3 == 4)
# not ("testing" == "testing" and "Zed" == "Cool Guy")
# 1 == 1 and not ("testing" == 1 or 1 == 0)
# "chunky" == "bacon" and not (3 == 4 or 3 == 3)
# 3 == 3 and not ("testing" == "testing" or "Python" == "Fun")
```
```
$ python
Python 3.6.2 (default, Jul 20 2017, 03:52:27) 
[GCC 7.1.1 20170630] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> True and True
True
>>> False and True
False
>>> 1 == 1 and 2 == 1
False
>>> "test" == "test"
True
>>> 1 == 1 or 2 != 1
True
>>> True and 1 == 1
True
>>> False and 0 != 0
False
>>> True or 1 == 1
True
>>> "test" == "testing"
False
>>> 1 != 0 and 2 == 1
False
>>> "test" != "testing"
True
>>> "test" == 1
False
>>> not (True and False)
True
>>> not (1 == 1 and 0 != 1)
False
>>> not (10 == 1 or 1000 == 1000)
False
>>> not (1 != 10 or 3 == 4)
False
>>> not ("testing" == "testing" and "Zed" == "Cool Guy")
True
>>> 1 == 1 and not ("testing" == 1 or 1 == 0)
True
>>> "chunky" == "bacon" and not (3 == 4 or 3 == 3)
False
>>> 3 == 3 and not ("testing" == "testing" or "Python" == "Fun")
False
```

### Exercise 29: What If
```python
people = 20
cats = 30
dogs = 15

if people < cats:
    print('Too many cats! The world is doomed!')

if people > cats:
    print('Not many cats! The world is saved!')

if people < dogs:
    print('The world is drooled on!')

if people > dogs:
    print('The world is dry!')

dogs += 5

if people >= dogs:
    print('People are greater than or equal to dogs.')

if people <= dogs:
    print('People are less than or equal to dogs')

if people == dogs:
    print('People are dogs.')
```
```
Too many cats! The world is doomed!
The world is dry!
People are greater than or equal to dogs.
People are less than or equal to dogs
People are dogs.
```

### Exercise 30: Else and If
```python
people = 30
cars = 40
buses = 15

if cars > people:
    print('We should take the cars.')
elif cars < people:
    print('We should not take the cars.')
else:
    print('we can\'t decide.')

if buses > cars:
    print('That\'s too many buses.')
elif buses < cars:
    print('Maybe we could take the buses.')
else:
    print('We still can\'t decide.')

if people > buses:
    print('Alright, let\'s just take the buses.')
else:
    print('Fine, let\'s stay home then.')
```
```
We should take the cars.
Maybe we could take the buses.
Alright, let's just take the buses.
```

### Exercise 31: Making Decisions
```python
print('You enter a dark room with two doors. Do you go through door #1 or door #2?')

door = input('> ')

if door == '1':
    print('There is a giant bear here eating a cheese cake. What do you do?')
    print('1. Take the cake.')
    print('2. Scream at the bear.')

    bear = input('> ')

    if bear == '1':
        print('The bear eats your face off. Good job!')
    elif bear == '2':
        print('The bear eats your leg off. Good job!')
    else:
        print('Well, doing %s is probably better. Bear runs away.' % bear)

elif door == '2':
    print('You stare into the endless abyss at Cthulhu\'s retina.')
    print('1. Blueberries.')
    print('2. Yellow jacket clothespins.')
    print('3. Understanding revolvers yellow melodies.')

    insanity = input('> ')

    if insanity == '1' or insanity == '2':
        print('Your body survives powered by a mind of jello. Good job!')
    else:
        print('The insanity rots your eyes into a pool of muck. Good job!')

else:
    print('You stumble around and fall on a knife and die. Good job!')
```
```
You enter a dark room with two doors. Do you go through door #1 or door #2?
> 1
There is a giant bear here eating a cheese cake. What do you do?
1. Take the cake.
2. Scream at the bear.
> 2
The bear eats your leg off. Good job!
```

### Exercise 32: Loops and Lists
```python
hairs = ['brown', 'blond', 'red']
eyes = ['brown', 'blue', 'green']
weights = [1, 2, 3, 4]

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print('This is count %d' % number)

# same as above
for fruit in fruits:
    print('A fruit of type: %s' % fruit)

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
    print('I got %r' % i)

# we can also build list, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print('Adding %d to the list.' % i)
    # append is a function that lists understand
    elements.append(i)

for i in elements:
    print('Element was: %d' % i)
```
```
This is count 1
This is count 2
This is count 3
This is count 4
This is count 5
A fruit of type: apples
A fruit of type: oranges
A fruit of type: pears
A fruit of type: apricots
I got 1
I got 'pennies'
I got 2
I got 'dimes'
I got 3
I got 'quarters'
Adding 0 to the list.
Adding 1 to the list.
Adding 2 to the list.
Adding 3 to the list.
Adding 4 to the list.
Adding 5 to the list.
Element was: 0
Element was: 1
Element was: 2
Element was: 3
Element was: 4
Element was: 5
```

### Exercise 33: While Loops
```python
i = 0
numbers = []

while i < 6:
    print('At the top i is %d' % i)
    numbers.append(i)

    i = i + 1
    print('Numbers now: ', numbers)
    print('At the bottom i is %d' % i)

print('The numbers: ')

for num in numbers:
    print(num)
```
```
At the top i is 0
Numbers now:  [0]
At the bottom i is 1
At the top i is 1
Numbers now:  [0, 1]
At the bottom i is 2
At the top i is 2
Numbers now:  [0, 1, 2]
At the bottom i is 3
At the top i is 3
Numbers now:  [0, 1, 2, 3]
At the bottom i is 4
At the top i is 4
Numbers now:  [0, 1, 2, 3, 4]
At the bottom i is 5
At the top i is 5
Numbers now:  [0, 1, 2, 3, 4, 5]
At the bottom i is 6
The numbers: 
0
1
2
3
4
5
```

### Exercise 35: Branches and Functions
```python
from sys import exit

def gold_room():
    print('This room is full of gold. How much do you take?')

    next = input('> ')
    if '0' in next or '1' in next:
        how_much = int(next)
    else:
        dead('Man, learn to type a number.')

    if how_much < 50:
        print('Nice, you\'re not greedy, you win!')
        exit(0)
    else:
        dead('You greedy bastard!')

def bear_room():
    print('There is a bear here.')
    print('The bear has a bunch of honey.')
    print('The fat bear is in front of another door.')
    print('How are you going to move the bear?')
    bear_moved = False

    while True:
        next = input('> ')

        if next == 'take honey':
            dead('The bear looks at you then slaps your face off.')
        elif next == 'taunt bear' and not bear_moved:
            print('The bear has moved from the door. You can go through it now.')
            bear_moved = True
        elif next == 'taunt bear' and bear_moved:
            dead('The bear gets pissed off and chews your leg off.')
        elif next == 'open door' and bear_moved:
            gold_room()
        else:
            print('I got no idea what that means.')

def cthulhu_room():
    print('Here you see the great evil Cthulhu.')
    print('He, it, whatever stares at you and you go insane.')
    print('Do you flee for your life or eat your head?')

    next = input('> ')

    if 'flee' in next:
        start()
    elif 'head' in next:
        dead('Well that was tasty!')
    else:
        cthulhu_room()

def dead(why):
    print(why, 'Good job!')
    exit(0)

def start():
    print('You are in a dark room.')
    print('There is a door to your right and left.')
    print('Which one do you take?')

    next = input('> ')

    if next == 'left':
        bear_room()
    elif next == 'right':
        cthulhu_room()
    else:
        dead('You stumble around the room until you starve.')

start()
```
```
You are in a dark room.
There is a door to your right and left.
Which one do you take?
> left
There is a bear here.
The bear has a bunch of honey.
The fat bear is in front of another door.
How are you going to move the bear?
> taunt bear
The bear has moved from the door. You can go through it now.
> open door
This room is full of gold. How much do you take?
> 1000
You greedy bastard! Good job!
```

### Exercise 38: Doing Things to Lists
```python
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
```
```
Wait there's is not 10 things in that list, let's fix that.
Adding:  Boy
There is 7 items now.
Adding:  Girl
There is 8 items now.
Adding:  Banana
There is 9 items now.
Adding:  Corn
There is 10 items now.
There we go:  ['Apples', 'Oranges', 'Crows', 'Telephone', 'Light', 'Sugar', 'Boy', 'Girl', 'Banana', 'Corn']
Let's do something with stuff.
Oranges
Corn
Corn
Apples Oranges Crows Telephone Light Sugar Boy Girl Banana
Telephone#Light
```

### Exercise 39: Dictionaries, Oh Lovely Dictionaries
```python
# create a mapping of state to abbreviation
states = {
        'Oregon': 'OR',
        'Florida': 'FL',
        'California': 'CA',
        'New York': 'NY',
        'Michigan': 'MI'
        }

# create a basic set of states and some cities in them
cities = {
        'CA': 'San Francisco',
        'MI': 'Destroit',
        'FL': 'Jacksonville'
        }

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-' * 10)
print('NY State has: ', cities['NY'])
print('OR State has: ', cities['OR'])

# print some states
print('-' * 10)
print('Michigan\'s abbreviation is: ', states['Michigan'])
print('Florida\'s abbreviation is: ', states['Florida'])

# do it by using the state then cities dict
print('-' * 10)
print('Michigan has ', cities[states['Michigan']])
print('Florida has ', cities[states['Florida']])

# print every state abbreviation
print('-' * 10)
for state, abbrev in states.items():
    print('%s is abbreviated %s' % (state, abbrev))

# print every city in state
print('-' * 10)
for abbrev, city in cities.items():
    print('%s has the city %s' % (abbrev, city))

# now do both at the same time
print('-' * 10)
for state, abbrev in states.items():
    print('%s state is abbreviated %s and has city %s' % (state, abbrev, cities[abbrev]))

print('-' * 10)
# safely get a abbreviation by state that might not be there
state = states.get('Texas', None)

if not state:
    print('Sorry, no Texas.')

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print('The city for the state "TX" is: %s' % city)
```
```
----------
NY State has:  New York
OR State has:  Portland
----------
Michigan's abbreviation is:  MI
Florida's abbreviation is:  FL
----------
Michigan has  Destroit
Florida has  Jacksonville
----------
Oregon is abbreviated OR
Florida is abbreviated FL
California is abbreviated CA
New York is abbreviated NY
Michigan is abbreviated MI
----------
CA has the city San Francisco
MI has the city Destroit
FL has the city Jacksonville
NY has the city New York
OR has the city Portland
----------
Oregon state is abbreviated OR and has city Portland
Florida state is abbreviated FL and has city Jacksonville
California state is abbreviated CA and has city San Francisco
New York state is abbreviated NY and has city New York
Michigan state is abbreviated MI and has city Destroit
----------
Sorry, no Texas.
The city for the state "TX" is: Does Not Exist
```

### Exercise 40: Modules, Classes, and Objects
```python
# # dict style
# mystuff['apples']

# # module style
# mystuff.apples()
# print mystuff.tangerine

# # class style
# thing = MyStuff()
# thing.apples()
# print thing.tangerine

class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print(line)

happy_bday = Song(["Happy birthday to you",
	"I don\'t want to get sued",
	"So I\'ll stop right there"])

bulls_on_parade = Song(["They rally around the family",
	"With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
```
```
Happy birthday to you
I don't want to get sued
So I'll stop right there
They rally around the family
With pockets full of shells
```

### Exercise 41: Learning to Speak Object Oriented
```python
import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
		"class ###(###):":
		"Make a class named ### that is-a ###.",
		"class ###(object):\n\tdef __init__(self, ***)" :
		"class ### has-a __init__ that takes self and *** parameters.",
		"class ###(object):\n\tdef ***(self, @@@)":
		"class ### has-a function named *** that takes self and @@@ parameters.",
		"*** = ###()":
		"Set *** to an instance of class ###.",
		"***.***(@@@)":
		"From *** get the *** function, and call it with parameters self, @@@.",
		"***.*** = '***'":
		"From *** get the *** attribute and set it to '***'."
		}

# do they want to drill phrases first
PHRASE_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] == "english":
	PHRASE_FIRST = True

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
	WORDS.append(word.strip().decode("utf-8"))

def convert(snippet, phrase):
	class_names = [w.capitalize() for w in
			random.sample(WORDS, snippet.count("###"))]
	other_names = random.sample(WORDS, snippet.count("***"))
	results = []
	param_names = []

	for i in range(0, snippet.count("@@@")):
		param_count = random.randint(1,3)
		param_names.append(', '.join(random.sample(WORDS, param_count)))

	for sentence in snippet, phrase:
		result = sentence[:]

		# fake class names
		for word in class_names:
			result = result.replace("###", word, 1)

		# fake other names
		for word in other_names:
			result = result.replace("***", word, 1)

		# fake parameter lists
		for word in param_names:
			result = result.replace("@@@", word, 1)

		results.append(result)

	return results
# keep going until they hit CTRL-D

try:
	while True:
		snippets = list(PHRASES.keys())
		random.shuffle(snippets)

		for snippet in snippets:
			phrase = PHRASES[snippet]
			question, answer = convert(snippet, phrase)
			if PHRASE_FIRST:
				question, answer = answer, question

			print(question)
			input("> ")
			print("ANSWER:  %s\n\n" % answer)
except EOFError:
	print("\nBye")
```
```
class Cherry(object):
	def canvas(self, coast, carriage, amount)
> 
ANSWER:  class Cherry has-a function named canvas that takes self and coast, carriage, amount parameters.


committee.ant = 'art'
> 
ANSWER:  From committee get the ant attribute and set it to 'art'.


class Aunt(Beginner):
> 
ANSWER:  Make a class named Aunt that is-a Beginner.


class Cushion(object):
	def __init__(self, dinosaurs)
> 
ANSWER:  class Cushion has-a __init__ that takes self and dinosaurs parameters.


drop.bag(copper, destruction)
> 
ANSWER:  From drop get the bag function, and call it with parameters self, copper, destruction.


clock = Basket()
> 
ANSWER:  Set clock to an instance of class Basket.


crime.cactus(appliance, desire)
> 
```

### Exercise 42: Is-A, Has-A, Objects and Classes
```python
## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a Animal
class Dog(Animal):
    def __init__(self, name):
        ## Dog has-a name
        self.name = name

## Cat is-a Animal
class Cat(Animal):
    def __init__(self, name):
        ## Cat has-a name
        self.name = name

## Person is-a object
class Person(object):
    def __init__(self, name):
        ## Person has-a name
        self.name = name
        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a Person
class Employee(Person):
    def __init__(self, name, salary):
        ## Employee has-a name
        super().__init__(name)
        ## Employee has-a salary
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog and has-a name Rover
rover = Dog("Rover")

## satan is-a Cat and has-a name Satan
satan = Cat("Satan")

## mary is-a Person and has-a name Mary
mary = Person("Mary")

## mary has-a pet cat named satan
mary.pet = satan

## frank is-a Employee and has-a salary of 120000
frank = Employee("Frank", 120000)

## frank has-a pet dog named rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()
```

### Exercise 43: Basic Object Oriented Analysis and Design
```
1. Write or draw about the problem.
2. Extract key concepts from #1 and research them.
3. Create a class hierarchy and object map for the concepts.
4. Code the classes and a test to run them.
5. Repeat and refine.
```

#### 1. Write or draw about the problem.
---
* Aliens have invaded a space ship and our hero has to go through a maze of rooms defeating them so he can escape into an escape pod to the planet below.
* The game will be more like a Zork or Adventure type game with text outputs and funny ways to die.
* The game will involve an engine that runs a map full of rooms or scenes.
* Each room will print its own description when the player enters it and then tell the engine what room to run next out of the map.

**Death**
> This is when the player dies and should be something funny.

**Central Corridor**
> This is the starting point and has a Gothon already standing there they have to defeat with a joke before continuing.

**Laser Weapon Armory**
> This is where they hero gets a neutron bomb to blow up the ship before getting to the escape pod. It has a keypad he has to guess the number for.

**The Bridge**
> Another battle scene with a Gothon where the hero places the bomb.

**Escape Pod**
> Where the hero escapes but only after guessing the right escape pod.

#### 2. Extract key concepts from #1 and research them.
---
* Alien
* Player
* Ship
* Maze
* Room
* Scene
* Gothon
* Escape Pod
* Planet
* Map
* Engine
* Death
* Central Corridor
* Laser Weapon Armory
* The Bridge

#### 3. Create a class hierarchy and object map for the concepts.
---
* Map
  * **next_scene**
  * **opening_scene**
* Engine
  * **play**
* Scene
  * **enter**
  * Death
  * Central Corridor
  * Laser Weapon Armory
  * The Bridge
  * Escape Pod

#### 4. Code the classes and a test to run them.
---

```python
class Scene(object):

    def enter(self):
        pass

class Engine(object):

    def __init__(self, scene_map):
        pass

    def play(self):
        pass

class Death(Scene):

    def enter(self):
        pass

class CentralCorridor(Scene):

    def enter(self):
        pass

class LaserWeaponArmory(Scene):

    def enter(self):
        pass

class TheBridge(Scene):

    def enter(self):
        pass

class EscapePod(Scene):

    def enter(self):
        pass

class Map(object):

    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
```

#### 5. Repeat and refine.
---
```python
from sys import exit
from random import randint

class Scene(object):

	def enter(self):
		print("This scene is not yet configured. Subclass it and implement enter().")
		exit(1)

class Engine(object):

	def __init__(self, scene_map):
		self.scene_map = scene_map

	def play(self):
		current_scene = self.scene_map.opening_scene()

		while True:
			print("\n--------")
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)

class Death(Scene):

	quips = [
			"You died.  You kinda suck at this.",
			"Your mom would be proud...if she were smarter.",
			"Such a luser.",
			"I have a small puppy that's better at this."
			]

	def enter(self):
		print(Death.quips[randint(0, len(self.quips)-1)])
		exit(1)

class CentralCorridor(Scene):

	def enter(self):
		print("The Gothons of Planet Percal #25 have invaded your ship and destroyed")
		print("your entire crew.  You are the last surviving member and your last")
		print("mission is to get the neutron destruct bomb from the Weapons Armory,")
		print("put it in the bridge, and blow the ship up after getting into an ")
		print("escape pod.")
		print("\n")
		print("You're running down the central corridor to the Weapons Armory when")
		print("a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume")
		print("flowing around his hate filled body.  He's blocking the door to the")
		print("Armory and about to pull a weapon to blast you.")

		action = input("> ")

		if action == "shoot!":
			print("Quick on the draw you yank out your blaster and fire it at the Gothon.")
			print("His clown costume is flowing and moving around his body, which throws")
			print("off your aim.  Your laser hits his costume but misses him entirely. This")
			print("completely ruins his brand new costume his mother bought him, which")
			print("makes him fly into an insane rage and blast you repeatedly in the face until")
			print("you are dead.  Then he eats you.")
			return 'death'

		elif action == "dodge!":
			print("Like a world class boxer you dodge, weave, slip and slide right")
			print("as the Gothon's blaster cranks a laser past your head.")
			print("In the middle of your artful dodge your foot slips and you")
			print("bang your head on the metal wall and pass out.")
			print("You wake up shortly after only to die as the Gothon stomps on")
			print("your head and eats you.")
			return 'death'

		elif action == "tell a joke":
			print("Lucky for you they made you learn Gothon insults in the academy.")
			print("You tell the one Gothon joke you know:")
			print("Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr.")
			print("The Gothon stops, tries not to laugh, then busts out laughing and can't move.")
			print("While he's laughing you run up and shoot him square in the head")
			print("putting him down, then jump through the Weapon Armory door.")
			return 'laser_weapon_armory'

		else:
			print("DOES NOT COMPUTE!")
			return 'central_corridor'

class LaserWeaponArmory(Scene):

	def enter(self):
		print("You do a dive roll into the Weapon Armory, crouch and scan the room")
		print("for more Gothons that might be hiding.  It's dead quiet, too quiet.")
		print("You stand up and run to the far side of the room and find the")
		print("neutron bomb in its container.  There's a keypad lock on the box")
		print("and you need the code to get the bomb out.  If you get the code")
		print("wrong 10 times then the lock closes forever and you can't")
		print("get the bomb.  The code is 3 digits.")
		code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
		guess = input("[keypad]> ")
		guesses = 0

		while guess != code and guesses < 10:
			print("BZZZZEDDD!")
			guesses += 1
			guess = input("[keypad]> ")

		if guess == code:
			print("The container clicks open and the seal breaks, letting gas out.")
			print("You grab the neutron bomb and run as fast as you can to the")
			print("bridge where you must place it in the right spot.")
			return 'the_bridge'
		else:
			print("The lock buzzes one last time and then you hear a sickening")
			print("melting sound as the mechanism is fused together.")
			print("You decide to sit there, and finally the Gothons blow up the")
			print("ship from their ship and you die.")
			return 'death'

class TheBridge(Scene):

	def enter(self):
		print("You burst onto the Bridge with the netron destruct bomb")
		print("under your arm and surprise 5 Gothons who are trying to")
		print("take control of the ship.  Each of them has an even uglier")
		print("clown costume than the last.  They haven't pulled their")
		print("weapons out yet, as they see the active bomb under your")
		print("arm and don't want to set it off.")

		action = input("> ")

		if action == "throw the bomb":
			print("In a panic you throw the bomb at the group of Gothons")
			print("and make a leap for the door.  Right as you drop it a")
			print("Gothon shoots you right in the back killing you.")
			print("As you die you see another Gothon frantically try to disarm")
			print("the bomb. You die knowing they will probably blow up when")
			print("it goes off.")
			return 'death'

		elif action == "slowly place the bomb":
			print("You point your blaster at the bomb under your arm")
			print("and the Gothons put their hands up and start to sweat.")
			print("You inch backward to the door, open it, and then carefully")
			print("place the bomb on the floor, pointing your blaster at it.")
			print("You then jump back through the door, punch the close button")
			print("and blast the lock so the Gothons can't get out.")
			print("Now that the bomb is placed you run to the escape pod to")
			print("get off this tin can.")
			return 'escape_pod'
		else:
			print("DOES NOT COMPUTE!")
			return "the_bridge"

class EscapePod(Scene):

	def enter(self):
		print("You rush through the ship desperately trying to make it to")
		print("the escape pod before the whole ship explodes.  It seems like")
		print("hardly any Gothons are on the ship, so your run is clear of")
		print("interference.  You get to the chamber with the escape pods, and")
		print("now need to pick one to take.  Some of them could be damaged")
		print("but you don't have time to look.  There's 5 pods, which one")
		print("do you take?")

		good_pod = randint(1,5)
		guess = input("[pod #]> ")

		if int(guess) != good_pod:
			print("You jump into pod %s and hit the eject button." % guess)
			print("The pod escapes out into the void of space, then")
			print("implodes as the hull ruptures, crushing your body")
			print("into jam jelly.")
			return 'death'
		else:
			print("You jump into pod %s and hit the eject button." % guess)
			print("The pod easily slides out into space heading to")
			print("the planet below.  As it flies to the planet, you look")
			print("back and see your ship implode then explode like a")
			print("bright star, taking out the Gothon ship at the same")
			print("time.  You won!")

			return 'finished'

class Map(object):

	scenes = {
			'central_corridor': CentralCorridor(),
			'laser_weapon_armory': LaserWeaponArmory(),
			'the_bridge': TheBridge(),
			'escape_pod': EscapePod(),
			'death': Death()
			}

	def __init__(self, start_scene):
		self.start_scene = start_scene

	def next_scene(self, scene_name):
		return Map.scenes.get(scene_name)

	def opening_scene(self):
		return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
```
```

--------
The Gothons of Planet Percal #25 have invaded your ship and destroyed
your entire crew.  You are the last surviving member and your last
mission is to get the neutron destruct bomb from the Weapons Armory,
put it in the bridge, and blow the ship up after getting into an 
escape pod.


You're running down the central corridor to the Weapons Armory when
a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume
flowing around his hate filled body.  He's blocking the door to the
Armory and about to pull a weapon to blast you.
> dodge!
Like a world class boxer you dodge, weave, slip and slide right
as the Gothon's blaster cranks a laser past your head.
In the middle of your artful dodge your foot slips and you
bang your head on the metal wall and pass out.
You wake up shortly after only to die as the Gothon stomps on
your head and eats you.

--------
Your mom would be proud...if she were smarter.
```
