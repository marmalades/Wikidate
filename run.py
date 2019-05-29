import requests
print("What date should we look up?: ")
userDate = input()

userDate = userDate.replace(" ", "_")
website_url = requests.get('https://en.wikipedia.org/wiki/Wikipedia:Selected_anniversaries/' + userDate).text

# TODO: find actual list items in Wikipedia
# currently feels like a workaround by getting list items that start with 4 digits
# probably improves speed too?

from bs4 import BeautifulSoup
soup = BeautifulSoup(website_url,'lxml')
for tag in soup.find_all("li"):
     info = "{0}: {0}".format(tag.text)
     if (info[:4].isdigit() == True):
         print("\n" + info)
