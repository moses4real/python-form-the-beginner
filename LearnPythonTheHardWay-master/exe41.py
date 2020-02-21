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


# --Output--
# class Cherry(object):
# 	def canvas(self, coast, carriage, amount)
# > 
# ANSWER:  class Cherry has-a function named canvas that takes self and coast, carriage, amount parameters.


# committee.ant = 'art'
# > 
# ANSWER:  From committee get the ant attribute and set it to 'art'.


# class Aunt(Beginner):
# > 
# ANSWER:  Make a class named Aunt that is-a Beginner.


# class Cushion(object):
# 	def __init__(self, dinosaurs)
# > 
# ANSWER:  class Cushion has-a __init__ that takes self and dinosaurs parameters.


# drop.bag(copper, destruction)
# > 
# ANSWER:  From drop get the bag function, and call it with parameters self, copper, destruction.


# clock = Basket()
# > 
# ANSWER:  Set clock to an instance of class Basket.


# crime.cactus(appliance, desire)
# > 
