import getLists
import textprocessing


TRAINING_SET_SIZE = 12
NO_WARNINGS = 1


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


def getCleanText(raw_training_set):
    cleaned_training_set = []
    for page_text in raw_training_set:
        clean_txt = textprocessing.text_from_html(page_text)
        clean_list = list(clean_txt.split(" "))
        clean_list = list(set(clean_list)) # remove duplicates
        clean_list = [x.lower() for x in clean_list] # lower case everything
        # TODO: remove punctuation
        cleaned_training_set.append(clean_list)
    return cleaned_training_set


def containsImplicitExplicitWords(page_text, chosen_list, num = 2):
    present = []
    for word in page_text:
        if word in chosen_list:
            present.append(word)
    return present


# Basic first algorithm to detect presence of 2 or more words from explicit
# and implicit lists. TODO: complexify with more training data and sentiment!
def shouldDisplayContentWarning(page_text): 
    # Get explicit and implicit lists from Excel files
    explicit_list = getLists.getExplicitList()
    implicit_list = getLists.getImplicitList()

    # Get words present in webpage that are also in explicit and implicit lists
    explicit_present = containsImplicitExplicitWords(page_text, explicit_list)
    implicit_present = containsImplicitExplicitWords(page_text, implicit_list)
    # print("explicit present: ", explicit_present)
    # print("implicit present: ", implicit_present)

    if len(explicit_present) >= 2 and len(implicit_present) >= 2:
        return True  # TODO: define thresholds
    else:
        return False


def test_function():
    # Parse text files and extract clean html without tags
    raw_training_set, names = getRawTextFromTrainingSet()
    clean_training_set = getCleanText(raw_training_set)

    shouldDisplayContentWarning(clean_training_set[12])

    for i in range(0, TRAINING_SET_SIZE+NO_WARNINGS):
        print("{}:".format(names[i]), end=" ")
        if shouldDisplayContentWarning(clean_training_set[i]):
            print("Should display content warning!")
        else:
            print("Should NOT display content warning.")


test_function()
