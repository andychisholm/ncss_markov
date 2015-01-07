import random

text = open(raw_input("What file do you want to learn from? "), 'rU').read()
# split the text up into tokens
words = text.split()
# set up a dictionary to store things in
d = {}
numwords = len(words)

# loop over words, adding each word and the next word
for i in range(numwords-1):
    # if we haven't seen the word before, add a list with the next word it to the dictionary.
    word = words[i]
    nextword = words[i+1]
    if word not in d:
        d[word] = [nextword]
    else:
    # if we have seen the word before, add the next word to the list that is in the dictionary.
        d[word].append(nextword)

# choose a word to start with, and print it out
wd = 'the'
print wd,

# print out 15 words!
for i in range(15):
    # set the nextword as a random choice from the list in the dictionary for that word
    nxtwd = random.choice(d[wd])
    # print that nextword
    print nxtwd,
    # set the current word to nextword
    wd = nxtwd