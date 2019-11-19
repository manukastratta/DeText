import getLists
import textprocessing
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
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
    all_paragraphs = soup.findAll('p')
    if len(all_paragraphs)  < 1:
        all_paragraphs = soup.findAll('div') # if html does not have 'p' tags, use div
    for i in range(0, len(all_paragraphs)):
        all_paragraphs[i] = all_paragraphs[i].get_text() # cleaning, removing inner tags
    return all_paragraphs


# Returns list of explicit words present in paragraph
def contains_explicit(paragraph):
    found = []
    for explicit in EXPLICIT_LIST: # search the explicit list directly (more efficient, small size)
        if paragraph.find(explicit) != -1:
            for i in range(paragraph.count(explicit)):
                found.append(explicit) # add occurrences of word
    return found


# Returns list of implicit words present in paragraph
def contains_implicit(paragraph):
    tokenized_words = word_tokenize(paragraph)
    stop_words = set(stopwords.words("english"))
    filtered_words = []
    for w in tokenized_words:
        if w not in stop_words:
            filtered_words.append(w)
    filtered_words = [word.lower() for word in filtered_words if word.isalpha()]
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
def should_display_warning(p_content_data, nTotalP):
    total_explicit = 0
    total_implicit = 0
    negative_sentiment = False
    relevant_paragraphs = len(p_content_data)

    for data in p_content_data:
        total_explicit += data[0] # Adds count of explicit words
        total_implicit += data[1] # Adds count of implicit words
        if data[2] < 0.5 and data[2] != 0: # Checks for sentiment value
            negative_sentiment = True
    # print("total_explicit: ", total_explicit)
    # print("total_implicit: ", total_implicit)
    # print("negative_sentiment: ", negative_sentiment)
    # print("relevant paragaphs: ", relevant_paragraphs)
    # print("relevant_paragraphs/totalP: ", relevant_paragraphs/nTotalP)

    #if total_explicit >= 2 and total_implicit >=2 and relevant_paragraphs/nTotalP >= 0.2 and negative_sentiment:
    if total_explicit >= 2 and total_implicit >= 2 and relevant_paragraphs >= 2 and negative_sentiment:
        return True
    else:
        return False


def parse_website_content(html):
    clean_paragraphs = get_clean_paragraphs(html)
    p_content_data = [] # will store num of EXplicit, IMplicit, and sentiment for each relevant paragraph
    for p in clean_paragraphs:
        explicit_present, implicit_present = contains_keywords(p)
        if len(explicit_present) >= 1 and len(implicit_present) >= 1:  # TODO: tweak if necessary
            sentiment = analyze_sentiment(p)
            p_data = [len(explicit_present), len(implicit_present), sentiment]
            p_content_data.append(p_data)
            # print("p_data: ", p_data)
            # print("explicit_present: ", explicit_present)
            # print("implicit_present: ", implicit_present)

    return should_display_warning(p_content_data, len(clean_paragraphs))



''' BELOW: for testing purposes '''


''' code to test on training sets'''

# TRAINING_SET_SIZE = 12
# NO_WARNINGS = 1
#
# def getRawTextFromTrainingSet():
#     training_set = []
#     names = []
#     prefix = "../trainingSets/training-set"
#     for i in range(1,TRAINING_SET_SIZE+1):
#         file_name = prefix + str(i) + ".txt"
#         names.append(file_name)
#         training_set.append(readFile(file_name))
#     training_set.append(readFile("../trainingSets/wood-wiki.txt")) # adding example with no content warning
#     names.append("../trainingSets/wood-wiki.txt")
#     return training_set, names
#
# def testTrainingSets():
#     training_set, names = getRawTextFromTrainingSet()
#     for i in range(0, TRAINING_SET_SIZE+NO_WARNINGS):
#         print("{}:".format(names[i]), end=" ")
#         if parse_website_content(training_set[i]):
#             print("Should display content warning!")
#         else:
#             print("Should NOT display content warning.")
#
# testTrainingSets()



''' old code to test on training sets '''
# def getCleanText(page_text):
#     clean_txt = textprocessing.text_from_html(page_text)
#     clean_list = list(clean_txt.split(" "))
#     clean_list = list(set(clean_list)) # remove duplicates
#     clean_list = [x.lower() for x in clean_list] # lower case everything
#     return clean_list
#
# def containsImplicitExplicitWords(page_text, chosen_list, num = 2):
#     present = []
#     for word in page_text:
#         if word in chosen_list:
#             present.append(word)
#     return present
#
# def shouldDisplayContentWarning(page_text):
#     # Get words present in webpage that are also in explicit and implicit lists
#     explicit_present = containsImplicitExplicitWords(page_text, EXPLICIT_LIST)
#     implicit_present = containsImplicitExplicitWords(page_text, IMPLICIT_LIST)
#
#     if len(explicit_present) >= 2 and len(implicit_present) >= 2:
#         return True
#     else:
#         return False
#
# def test_function():
#     # Parse text files and extract clean html without tags
#     raw_training_set, names = getRawTextFromTrainingSet()
#     clean_training_set = []
#     for raw_set in raw_training_set:
#         clean_training_set.append(getCleanText(raw_set))
#
#     for i in range(0, TRAINING_SET_SIZE+NO_WARNINGS):
#         print("{}:".format(names[i]), end=" ")
#         if shouldDisplayContentWarning(clean_training_set[i]):
#             print("Should display content warning!")
#         else:
#             print("Should NOT display content warning.")
