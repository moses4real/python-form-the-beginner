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

# --Output--
# $ Hi near, I'm the exe14.py script.
# $ I'd like to ask you a few questions.
# $ Do you like me near?
# $ > Yes
# $ Where do you live near?
# $ > LA
# $ What kind of computer do you have?
# $ > quantum

# Alright, so you said 'Yes' about liking me.
# You live in 'LA'.  Not sure where that is.
# And you have a 'quantum' computer.  Nice.
