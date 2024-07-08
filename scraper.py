import requests
from dsa import Trie  

#
def scrape_words(url, num_words, max_word_length): # scrapping function
    words = []
    response = requests.get(url)

    if response.status_code == 200:
        lines = response.text.split('\n') #reading line by line of the web page

        for line in lines:
            word = line.strip()
            if word and len(word) <= max_word_length: # only appending the words which fall in the check length check
                words.append(word)

    return words[:num_words]

# URL and parameters for scraping
url = 'https://www.mit.edu/~ecprice/wordlist.10000'
num_words_to_scrape = 10000
max_word_length = 15

# Scraping words from the URL using the defined function
scraped_words = scrape_words(url, num_words_to_scrape, max_word_length)

# Creating a Trie data structure and insert scraped words into it
trie_ds = Trie()
for word in scraped_words:
    trie_ds.insert(word)
