from bs4 import BeautifulSoup
from bs4.element import Comment
import requests


def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)
    return " ".join(text.strip() for text in visible_texts)


response = requests.get("https://www.crummy.com/software/BeautifulSoup/")

# Check for valid response
if response.status_code > 300 or response.status_code < 200:
    print("Possible Error, response code:", response.status_code)
    exit()
else:
    print("Received Valid Response from website")
    print("Processing...")

print(text_from_html(response.content))
