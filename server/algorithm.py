import getLists
import textprocessing


TRAINING_SET_SIZE = 12
NO_WARNINGS = 1

EXPLICIT_LIST = getLists.getExplicitList()
IMPLICIT_LIST = getLists.getImplicitList()


def readFile(fileName):
    f = open(fileName)
    data = ""
    for x in f:
        data += x
    return data


def getRawTextFromTrainingSet():
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


def getCleanText(page_text):
    clean_txt = textprocessing.text_from_html(page_text)
    clean_list = list(clean_txt.split(" "))
    clean_list = list(set(clean_list)) # remove duplicates
    clean_list = [x.lower() for x in clean_list] # lower case everything
    # TODO: remove punctuation
    return clean_list


def containsImplicitExplicitWords(page_text, chosen_list, num = 2):
    present = []
    for word in page_text:
        if word in chosen_list:
            present.append(word)
    return present


# Basic first algorithm to detect presence of 2 or more words from explicit
# and implicit lists. TODO: complexify with more training data and sentiment!
def shouldDisplayContentWarning(page_text):
    # Get words present in webpage that are also in explicit and implicit lists
    explicit_present = containsImplicitExplicitWords(page_text, EXPLICIT_LIST)
    implicit_present = containsImplicitExplicitWords(page_text, IMPLICIT_LIST)
    # print("explicit present: ", explicit_present)
    # print("implicit present: ", implicit_present)

    if len(explicit_present) >= 2 and len(implicit_present) >= 2:
        return True  # TODO: define thresholds
    else:
        return False


def parse_website_content(html):
    clean_html = getCleanText(html)
    return shouldDisplayContentWarning(clean_html)


def test_function():
    # Parse text files and extract clean html without tags
    raw_training_set, names = getRawTextFromTrainingSet()
    clean_training_set = []
    for raw_set in raw_training_set:
        clean_training_set.append(getCleanText(raw_set))

    for i in range(0, TRAINING_SET_SIZE+NO_WARNINGS):
        print("{}:".format(names[i]), end=" ")
        if shouldDisplayContentWarning(clean_training_set[i]):
            print("Should display content warning!")
        else:
            print("Should NOT display content warning.")


test_function()
