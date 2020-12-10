#these are the required modules
#!pip install feedparser
#!pip install requests

import feedparser
import requests
import xml.etree.ElementTree as ET

# search the Sunnyvale Library for the book
# Since I don't work for a library, they won't give me access to the bibliocommons APIs.
# So I have to use a workaound to do the search with the public search URL and return an URL to the book if it exists. 
def search_book(booktitle, author):

    r =requests.get('https://gateway.bibliocommons.com/v2/libraries/sunnyvale/rss/search?custom_edit=false&query=%28title%3A%28'+ booktitle + '%29%20AND%20contributor%3A%28' + author + '%29%20%29&searchType=bl&suppress=true&view=grouped&initialSearch=true')

    root = ET.fromstring(r.content)
    for child in root.iter('*'):
        if child.tag == "guid":
           return(child.text)

#
# put your RSS feed URL here
#
NewsFeed = feedparser.parse("https://www.goodreads.com/review/list_rss/XXX")

for entry in NewsFeed.entries:
    print (entry.title," - ", entry.author_name)
# need to remove the '#' in the book title before passing to the call    
    print(search_book(entry.title.replace('#', ''), entry.author_name))
    print('-------')