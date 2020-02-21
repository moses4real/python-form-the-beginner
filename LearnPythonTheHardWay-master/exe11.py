print('How old are you?', end=' ')
age = input()
print('How tall are you?', end=' ')
height = input()
print('How much do you weigh?', end=' ')
weight = input()

print('So, you are %r old, %r tall and %r heavy.' % (age, height, weight))

# --Output--
# How old are you? 38
# How tall are you? 6'2"
# How much do you weigh? 180lb
# So, you are '38' old, '6\'2"' tall and '180lbs' heavy.
