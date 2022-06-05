# This is a sample Python script.
# import nltk - if u have error to run this
# nltk.downloader.download('vader_lexicon')

import urllib.request, urllib.error, urllib.parse, base
import ssl
from KMP_Algorithm import KMP
from RabinKarp_Algorithm import rabinkarp
import matplotlib.pyplot as plt
import numpy as np

ssl._create_default_https_context = ssl._create_unverified_context

from nltk.sentiment.vader import SentimentIntensityAnalyzer

def sentiment_ranking():
    country =[]
    japan = []
    japan.append('https://english.kyodonews.net/news/2022/05/3645980f7e25-focus-japan-economy-may-rebound-but-faces-headwind-amid-price-surge.html')
    japan.append('https://www.hurriyetdailynews.com/japans-economy-shrinks-in-173873')
    japan.append('https://www.nippon.com/en/in-depth/d00778/')
    japan.append('https://japantoday.com/category/business/update2-japan-economic-report-drops-mention-of-coronavirus')
    japan.append('https://www.brinknews.com/the-japanese-economy-has-reinvented-itself/')
    country.append(japan)

    china = []
    china.append('https://www.worldbank.org/en/country/china/overview#1')
    china.append('https://www.frontiersin.org/articles/10.3389/fpubh.2021.787190/full')
    china.append('https://observer.com/2022/05/china-economy-slowdown-zero-covid-lockdown/')
    china.append('https://www.straitstimes.com/asia/east-asia/how-covid-19-restrictions-are-choking-chinas-economy-asian-insider')
    china.append('https://www.aljazeera.com/economy/2022/5/11/china-resorts-to-old-economic-tools-as-lockdowns-bite')
    country.append(china)

    UAE = []
    UAE.append('https://www.arabnews.com/node/2092066/business-economy')
    UAE.append('https://www.khaleejtimes.com/property/dubai-apartment-rents-increase-by-up-to-25-in-some-areas')
    UAE.append('https://www.arabnews.com/node/2092251/business-economy')
    UAE.append('https://gulfnews.com/uae/government/shorter-uae-work-week-highlights-high-adaptability-of-government-world-economic-forum-hears-1.88177737')
    UAE.append('https://www.khaleejtimes.com/business/uae-highlights-national-vision-at-world-economic-forum')
    country.append(UAE)

    # rabinkarpAlgorithm(japan[0])
    # kmpAlgorithm(japan[0])
    countryAverageSentiment = []
    netSentiment = 0
    for i in range(len(country)):
        for j in range(len(country[i])):
            result = kmpAlgorithm(country[i][j])
            # plotPie(result[0],result[1]) - plot pie chart for each article
            netSentiment += np.round((float(result[0]) - float(result[1])),2)
        countryAverageSentiment.append(np.round(netSentiment/5,2))

    countrySentimentDict = {"Japan":countryAverageSentiment[0], "China":countryAverageSentiment[1], "UAE":countryAverageSentiment[2]}
    countryRanking(countrySentimentDict)

# our group alternative algorithm
def sentiment_analysis(url):
    pos_word_list = []
    count_pos_word = []
    neg_word_list = []
    count_neg_word = []
    neu_word_list = []
    count_neu_word = []

    sid = SentimentIntensityAnalyzer()

    response = urllib.request.urlopen(url)
    html = response.read().decode('UTF-8')
    text = base.stripTags(html).lower()
    fullwordlist = base.stripNonAlphaNum(text)
    wordlist = base.removeStopwords(fullwordlist, base.getStopWords())
    dictionary = base.wordListToFreqDict(wordlist)

    # alternative algo method
    for s in dictionary:
        if (sid.polarity_scores(str(s))['compound']) >= 0.5:
            pos_word_list.append(str(s))
            count_pos_word.append(dictionary[s])
        elif (sid.polarity_scores(str(s))['compound']) <= -0.5:
            neg_word_list.append(str(s))
            count_neg_word.append(dictionary[s])
        else:
            neu_word_list.append(str(s))
            count_neu_word.append(dictionary[s])

    totalPositiveWords = 0
    for i in count_pos_word:
        totalPositiveWords += i

    totalNegativeWords = 0
    for i in count_neg_word:
        totalNegativeWords += i

    totalNeutralWords = 0
    for i in count_neu_word:
        totalNeutralWords += i

    total = totalPositiveWords + totalNegativeWords + totalNeutralWords
    res1 = "{:.2f}".format(totalPositiveWords / total * 100)
    res2 = "{:.2f}".format(totalNegativeWords / total * 100)

    result = [res1, res2]
    return result

def wordsDifference(first, second):
    return [item for item in first if item not in second]

def kmpAlgorithm(url):
    response = urllib.request.urlopen(url)
    html = response.read().decode('UTF-8')
    text = base.stripTags(html).lower()
    fullwordlist = base.stripNonAlphaNum(text)
    wordlist = base.removeStopwords(fullwordlist, base.getStopWords())
    dictionary = base.wordListToFreqDict(wordlist)
    sorteddict = base.sortFreqDict(dictionary)

    pos_word_list = []
    count_pos_word = []
    neg_word_list = []
    count_neg_word = []

    postive_words = base.get_positiveWords();
    for i in postive_words:
        kmp = KMP()
        count = kmp.KMPSearch(i, text)
        if count > 0:
            pos_word_list.append(i)
            count_pos_word.append(count)
    #
    negative_words = base.get_negativeWords();
    for i in negative_words:
        kmp = KMP()
        count = kmp.KMPSearch(i, text)
        if count > 0:
            neg_word_list.append(i)
            count_neg_word.append(count)

    neu_word_list = wordsDifference(wordlist, pos_word_list)
    neu_word_list = wordsDifference(neu_word_list, neg_word_list)

    totalPositiveWords = 0
    for i in count_pos_word:
        totalPositiveWords += i

    totalNegativeWords = 0
    for i in count_neg_word:
        totalNegativeWords += i

    count_neu_word = len(neu_word_list)

    total = totalPositiveWords + totalNegativeWords + count_neu_word
    res1 = "{:.2f}".format(totalPositiveWords / total * 100)
    res2 = "{:.2f}".format(totalNegativeWords / total * 100)

    result = [res1, res2]
    return result

def rabinkarpAlgorithm(url):
    response = urllib.request.urlopen(url)
    html = response.read().decode('UTF-8')
    text = base.stripTags(html).lower()
    fullwordlist = base.stripNonAlphaNum(text)
    wordlist = base.removeStopwords(fullwordlist, base.getStopWords())
    dictionary = base.wordListToFreqDict(wordlist)
    sorteddict = base.sortFreqDict(dictionary)

    pos_word_list = []
    count_pos_word = []
    neg_word_list = []
    count_neg_word = []

    postive_words = base.get_positiveWords();
    for i in postive_words:
        rk = rabinkarp()
        count = rk.rabinkarp(text, i, 256, 101)
        if count > 0:
            pos_word_list.append(i)
            count_pos_word.append(count)
    #
    negative_words = base.get_negativeWords();
    for i in negative_words:
        rk = rabinkarp()
        count = rk.rabinkarp(text, i, 256, 101)
        if count > 0:
            neg_word_list.append(i)
            count_neg_word.append(count)

    neu_word_list = wordsDifference(wordlist, pos_word_list)
    neu_word_list = wordsDifference(neu_word_list, neg_word_list)

    totalPositiveWords = 0
    for i in count_pos_word:
        totalPositiveWords += i

    totalNegativeWords = 0
    for i in count_neg_word:
        totalNegativeWords += i

    count_neu_word = len(neu_word_list)

    total = totalPositiveWords + totalNegativeWords + count_neu_word
    res1 = "{:.2f}".format(totalPositiveWords / total * 100)
    res2 = "{:.2f}".format(totalNegativeWords / total * 100)

    result = [res1, res2]
    return result

def plotGraph(dictionaryWords):
    words = list(dictionaryWords.keys())
    frequency = list(dictionaryWords.values())
    plt.xlabel('Words')
    plt.xticks(rotation=90)
    plt.ylabel('Frequency')
    plt.title('Words Frequency')
    plt.bar(words, frequency, label='Word Count')
    plt.legend()
    plt.show()

def plotPie(percentagePositive, percentageNegative):
    percentageNeutral = (100.00 - float(percentagePositive)) - float(percentageNegative)
    mylabels = ["Positive Words(%)","Negative Words(%)","Neutral Words(%)"]
    y = [percentagePositive,percentageNegative,percentageNeutral]
    plt.pie(y, labels=mylabels, shadow=True, autopct=lambda p: '{:.0f}%'.format(p))
    plt.title("Analysis of Article")
    plt.show()

def countryRanking(countryDict):
    print("Based on the analysis of net sentiment, the ranking of countries from worst to best is as below:- \n")
    sortedCountry = base.sortFreqDict(countryDict)
    sortedKey = list(sortedCountry.keys())
    sortedValues = list(sortedCountry.values())

    for i in range(len(sortedCountry)):
        print(str(i+1) + "th Position : " + sortedKey[i] + " with average net sentiment of " + str(sortedValues[i]) + "\n")

    plt.bar(sortedKey, sortedValues, fc="lightgray", ec="black")
    plt.xlabel("Country")
    plt.ylabel("Average Net Sentiment")
    plt.title("Analysis of Article")

    for i in range(len(sortedKey)):
        plt.text(i,sortedValues[i],sortedValues[i],ha="center",va="bottom")

    plt.show()

sentiment_ranking()






