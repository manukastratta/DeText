import getLists, textprocessing
from bs4 import BeautifulSoup

import nltk
nltk.download('punkt')
nltk.download('stopwords')

from nltk.tokenize import word_tokenize, RegexpTokenizer
from nltk.corpus import stopwords
from textblob import TextBlob

# Explicit and implicit lists
EXPLICIT_LIST = getLists.getExplicitList()
IMPLICIT_LIST = getLists.getImplicitList()



def readFile(fileName):
    f = open(fileName)
    data = ""
    for x in f:
        data += x
    return data


# Breaks html down into paragraphs, stripped of all tags
def get_clean_paragraphs(html):
    soup = BeautifulSoup(html, 'html.parser')

    # Find all paragraphs in html
    all_paragraphs = soup.findAll('p')
    if len(all_paragraphs) < 1:
        all_paragraphs = soup.findAll('div')  # if html does not have 'p' tags, use div

    # Clean paragraphs, remove inner html tags
    for i in range(0, len(all_paragraphs)):
        all_paragraphs[i] = all_paragraphs[i].get_text()

    return all_paragraphs


# Returns list of explicit words present in paragraph
def contains_explicit(paragraph):
    found = []
    for explicit in EXPLICIT_LIST:
        if paragraph.find(explicit) != -1:
            for i in range(paragraph.count(explicit)):
                found.append(explicit) # add all occurrences of word
    return found


# Returns list of implicit words present in paragraph
def contains_implicit(paragraph):
    # Split paragraph into individual words, remove stop words
    tokenized_words = word_tokenize(paragraph)
    stop_words = set(stopwords.words("english"))

    filtered_words = []
    for w in tokenized_words:
        if w not in stop_words:
            filtered_words.append(w)
    filtered_words = [word.lower() for word in filtered_words if word.isalpha()]

    # Check for words present in implicit list
    found = []
    for word in filtered_words:
        if word in IMPLICIT_LIST:
            found.append(word)

    return found


# Returns list of present explicit and implicit words in paragraph
def contains_keywords(paragraph):
    explicit_present = contains_explicit(paragraph)
    implicit_present = contains_implicit(paragraph)
    return explicit_present, implicit_present


# Returns polarity of paragraph, where >0 means
# positive polarity, <0 means negative polarity,
# near 0 (+/- 0.05) means neutral
def analyze_sentiment(paragraph):
    analysis = TextBlob(paragraph)
    return analysis.sentiment.polarity
    # if analysis.sentiment.polarity > 0:
    #     return 1  # positive sentiment
    # elif -0.01 <= analysis.sentiment.polarity <= 0.01:
    #     return 0  # neutral sentiment
    # else:
    #     return -1  # negative sentiment



"""
    Conditions for flagging a website:
    - total explicit words >= 2
    - total implicit words >= 2
    - relevant paragraphs: >= 2 (size of data array)
    - negative sentiment analysis on >=1 paragraph
"""
def should_display_warning(p_content_data, nTotalP, total_explicit_article):
    total_explicit_in_p = 0
    total_implicit_in_p = 0
    polarized_sentiment = False
    relevant_paragraphs = len(p_content_data)

    for data in p_content_data:
        total_explicit_in_p += data[0] # Adds count of explicit words
        total_implicit_in_p += data[1] # Adds count of implicit words
        if not (-0.05 < data[2] < 0.05): # Checks for polarized sentiment value
            polarized_sentiment = True
    if total_explicit_in_p >= 2 and total_implicit_in_p >= 2 and relevant_paragraphs >= 2 \
            and polarized_sentiment or total_explicit_article >= 5:
        return True
    else:
        return False


def parse_website_content(html):
    clean_paragraphs = get_clean_paragraphs(html)

    p_content_data = [] # will store num of explicit, implicit, and sentiment for each relevant paragraph
    total_explicit_article = []
    for p in clean_paragraphs:
        # Get explicit and implicit phrases present in paragraph
        explicit_present, implicit_present = contains_keywords(p)
        for x in explicit_present: total_explicit_article.append(x)

        # If paragraph is relevant: at least one explicit and one implicit phrase
        if len(explicit_present) >= 1 and len(implicit_present) >= 1:
            # Store paragraph information in p_data data structure
            sentiment = analyze_sentiment(p)
            p_data = [len(explicit_present), len(implicit_present), sentiment]
            p_content_data.append(p_data)

    return should_display_warning(p_content_data, len(clean_paragraphs), len(total_explicit_article))




''' BELOW: for testing purposes '''
''' old code to test on training sets '''
TRAINING_SET_SIZE = 12
NO_WARNINGS = 1

def get_raw_text_from_training_set():
    training_set = []
    names = []
    prefix = "../trainingSets/training-set"
    for i in range(1,TRAINING_SET_SIZE+1):
        file_name = prefix + str(i) + ".txt"
        names.append(file_name)
        training_set.append(readFile(file_name))
    training_set.append(readFile("../trainingSets/wood-wiki.txt")) # adding example with no content warning
    names.append("../trainingSets/wood-wiki.txt")
    return training_set, names

def test_training_set():
    training_set, names = get_raw_text_from_training_set()
    for i in range(0, TRAINING_SET_SIZE+NO_WARNINGS):
        print("{}:".format(names[i]), end=" ")
        if parse_website_content(training_set[i]):
            print("Should display content warning!")
        else:
            print("Should NOT display content warning.")

# test_training_set()
