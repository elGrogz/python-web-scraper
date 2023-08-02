import requests
from bs4 import BeautifulSoup as bs  # Library to work with HTML/XML data

github_user = input("Input Github user: ")  # Get console input

url = f"https://github.com/{github_user}"  # standard HTTP request
request = requests.get(url)  # do a get request

soup = bs(
    request.content, "html.parser"
)  # using beautiful soup, get the content of the request and parse it with the html parser
profile_image = soup.find("img", {"alt": "Avatar"})[
    "src",
]  # find an image tag and narrow it down with the alt = 'avatar' attribute, and get its src attribute

print(profile_image)
print(soup)
