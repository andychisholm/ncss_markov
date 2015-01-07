import random
import sys

if len(sys.argv) != 2:
    print "Please run me like:\n\tpython %s file_to_learn_from.txt" % sys.argv[0]

text = open(sys.argv[1], 'rU').read()
# split the text up into tokens
words = text.split()
# set up a dictionary to store things in
d = {}
numwords = len(words)

# loop over words, adding each word and the next word
for i in range(1, numwords-1):
    # if we haven't seen the word before, add a list with the next word it to the dictionary.
    lastword = words[i-1]
    word = words[i]
    nextword = words[i+1]

    key = (lastword, word)
    if key not in d:
        d[key] = [nextword]
    else:
        # if we have seen these words before, add the next word to the list that is in the dictionary.
        d[key].append(nextword)

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
    nxtwd = random.choice(d[context])

    # print that nextword
    print nxtwd,

    # set the context based on the nextword
    context = context[1], nxtwd