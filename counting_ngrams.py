from fancypants.sampling import choice
import sys

if len(sys.argv) != 2:
    print "Please run me like:\n\tpython %s file_to_learn_from.txt" % sys.argv[0]

context_size = 2

text = open(sys.argv[1], 'rU').read()
# split the text up into tokens
words = text.lower().split()
# set up a dictionary to store things in
d = {}
numwords = len(words)

# loop over words, adding each word and the next word
for i in range(context_size-1, numwords-1):
    nextword = words[i+1]

    # construct a tuple of context words based on the selected context_sizez
    context = tuple(words[x] for x in xrange(i-context_size+1, i+1))

    print (context, nextword)

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
prompt_words = raw_input("Please supply atleast %i words as a prompt: " % context_size).strip().split()

if len(prompt_words) < context_size:
    print "Need atleast %i words :(!" % context_size
    exit()

# print out our prompt words
print ' '.join(prompt_words),

# use that two words of the input as out context
context = tuple(prompt_words[-context_size:])

# print out 15 words!
for i in range(30):
    # set the nextword as a random choice from the list in the dictionary for that word
    nxtwd = choice(d[context].keys(), d[context].values())

    # print that nextword
    print nxtwd,

    # set the context based on the nextword
    context = tuple(list(context)[1:] + [nxtwd])