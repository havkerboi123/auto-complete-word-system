# auto-complete-word-system-tries



This project was devolped as a aprt of my Data structure course semester project.It is a GUI-based auto-complete system built using Python's Tkinter library and a Trie data structure. It provides word suggestions as the user types, based on a dictionary of words scraped from the MIT website.

Features:

Insert and Search: Insert words into the Trie and search for the presence of words.
Autocomplete Suggestions: Provides suggestions for words that start with a given prefix.
Word Scraping: Scrapes a list of words from an online source to populate the Trie.
GUI Interface: User-friendly GUI to input text and get word suggestions.
Add and Check Words: Allows users to add new words to the Trie and check if a word exists in the Trie.
Components

Trie Data Structure
TrieNode

Represents a node in the Trie.
Contains a dictionary of child nodes and a boolean to indicate the end of a word.
Trie

Contains methods to insert words, search for words, and find words with a given prefix.
Methods:
insert(word): Inserts a word into the Trie.
search(word): Checks if a word exists in the Trie.
words_with_prefix(prefix): Returns a list of words starting with the given prefix.
search_words(current_node, auto_words, word): Helper method to find words recursively.
GUI Interface
WordSuggestionGUI

Inherits from Tkinter's Tk class.
Components:
Logo and heading labels.
Input field for typing words.
Listbox for displaying suggestions.
Input field and button for checking word existence.
Input field and button for adding new words.
Close button to exit the application.
Methods:

update_suggestions(event): Updates the suggestion list based on the input text.
handle_special_characters(text): Removes invalid characters from the text.
add_word(): Adds a new word to the Trie.
handle_spacebar(event): Handles spacebar events for updating suggestions.
check_word(): Checks if a word exists in the Trie.


