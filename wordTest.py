import requests
from lxml import html

def wordChecker(word):
    url = ("http://www.dictionary.reference.com/browse/%s?db=dictionary" % word)
    page = requests.get(url)
    tree = html.fromstring(page.text)
    #This will create a list of buyers:
    text = tree.xpath('//span[@class="me"]/text()')
    ##print 'Header: ', text
    return text

def is_word(word):
    """checks dictionary.com to see if the input word is an actual
    word"""
    word = word.lower()
    wordList = wordChecker(word)
    if word in wordList:
        return True
    else:
        return False