import requests
from bs4 import BeautifulSoup
from bs4.element import Comment


# Filtering function — returns True if HTML segment is visible on screen
def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


# Processes HTML input into text-only output
def text_from_html(body):  # TODO:Split by Paragraphs
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)  # Filters out non-visible segments
    # print("visible_texts: {}".format(visible_texts))
    # for text in visible_texts:
    #     print(text)
    return " ".join(text.strip() for text in visible_texts)


# Receives HTML from url and passes to text_from_html (for TESTING purposes only)
def get_response(web_url):
    # Makes GET request to web_url
    response = requests.get(web_url)

    # Check if received valid response
        # Invalid response, crash server...
    if response.status_code > 300 or response.status_code < 200:
        print("Possible Error, response code:", response.status_code)
        exit()
    else:
        print("Received Valid Response from website")
        print("Processing...")
    return text_from_html(response.content)

