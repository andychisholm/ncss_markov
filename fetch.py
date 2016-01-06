import urllib

url = "https://raw.githubusercontent.com/andychisholm/ncss_markov/master/data/"

filename = 'bieber.txt'

text = urllib.urlopen(url+filename).read()

print text[:100]

words = text.split()

print words[:20]
