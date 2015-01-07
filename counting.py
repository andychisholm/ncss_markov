import sys
from fancypants.sampling import choice

if len(sys.argv) != 2:
    print "Please run me like:\n\tpython %s file_to_learn_from.txt" % sys.argv[0]

text = open(sys.argv[1], 'rU').read()
# split the text up into tokens
words = text.lower().split()
# set up a dictionary to store things in
d = {}
numwords = len(words)

# loop over words, adding each word and the next word
for i in range(1, numwords-1):
    # if we haven't seen the word before, add a list with the next word it to the dictionary.
    lastword = words[i-1]
    word = words[i]
    nextword = words[i+1]

    context = (lastword, word)

    # if we haven't see these words before, we need to add an item to the dictionary
    if context not in d:
        # instead of storing a list, we now store a dictionary of words and counts
        d[context] = {}

    # we need to check if this word is in the dictionary
    if nextword not in d[context]:
        # it's a new word for this context, so we set the count to one
        d[context][nextword] = 1
    else:
        # add one to it's count
        d[context][nextword] += 1
      # if we have seen these words before, add the next word to the list that is in the dictionary

# input our starting words
prompt_words = raw_input("Two word prompt? ").strip().split()

if len(prompt_words) < 2:
    print "Need atleast two words :(!"
    exit()

# print out our prompt words
print ' '.join(prompt_words),

# use that two words of the input as out context
context = tuple(prompt_words[-2:])

# print out 15 words!
for i in range(30):
    # set the nextword as a random choice from the list in the dictionary for that word
    nxtwd = choice(d[context].keys(), d[context].values())

    # print that nextword
    print nxtwd,

    # set the context based on the nextword
    context = context[1], nxtwd