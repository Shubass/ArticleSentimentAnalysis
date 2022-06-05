# obo.py

def getStopWords():
    f = open("C:\\Users\\User\\PycharmProjects\\Algo\\Files\\stop_words.txt", 'r')
    stop_words = []
    for word in f:
        stop_words.append(word[:-1])
    return stop_words

def stripTags(pageContents):
    pageContents = str(pageContents)
    startLoc = pageContents.find("<p>")
    endLoc = pageContents.rfind("<br/>")

    pageContents = pageContents[startLoc:endLoc]

    inside = 0
    text = ''

    for char in pageContents:
        if char == '<':
            inside = 1
        elif (inside == 1 and char == '>'):
            inside = 0
        elif inside == 1:
            continue
        else:
            text += char

    return text

# Given a text string, remove all non-alphanumeric
# characters (using Unicode definition of alphanumeric).

def stripNonAlphaNum(text):
    import re
    return re.compile(r'\W+', re.UNICODE).split(text)

# Given a list of words, return a dictionary of
# word-frequency pairs.

def wordListToFreqDict(wordlist):
    wordfreq = [wordlist.count(p) for p in wordlist]
    return dict(list(zip(wordlist,wordfreq)))

# Sort a dictionary of word-frequency pairs in
# order of descending frequency.

def sortFreqDict(freqdict):
    return {k: v for k, v in sorted(freqdict.items(), key=lambda item: item[1], reverse=True)}

# Given a list of words, remove any that are
# in a list of stop words.

def removeStopwords(wordlist, stopwords):
    return [w for w in wordlist if w not in stopwords]

def get_positiveWords():
    f = open("C:\\Users\\User\\PycharmProjects\\Algo\\Files\\positive_words.txt", 'r')
    content_list = f.read().split(",")

    positive_words = []
    for word in content_list:
        positive_words.append(word.strip())
    return positive_words

def get_negativeWords():
    f = open("C:\\Users\\User\\PycharmProjects\\Algo\\Files\\negative_words.txt", 'r')
    content_list = f.read().split(",")
    negative_words = []
    for word in content_list:
        negative_words.append(word.strip())
    return negative_words