class TrieNode:
    def __init__(self):
        
        self.children = {} #Diction that stores children nodes
        
        self.end_of_word = False

class Trie:
    def __init__(self):
    
        self.root = TrieNode()
    
    # i) Tranveres thorugh the entire tree , adds a new node for a char if it does not already exist
    # ii) Marks the last char node as the end of the word , by setting the 'end_of_word' variable equal to True
    
    def insert(self, word):
        current = self.root

        # Traverseing the Trie, creating nodes for each character in the word
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()  #the char is the key
            current = current.children[char]

        # Marking the last node as the end of a complete word
        current.end_of_word = True
        
        
        
        
    # i)Iterates over the characters in the word and checks if each character has a corresponding child node
    # ii) If any character doesn't have a corresponding child node, the word is not present in the Trie
    # iii) Otherwise,returns True if the last character's child node is marked as the end of a word.   

    def search(self, word):
        current = self.root

        # Traversing trie to check if the entire word exists
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]

        
        return current.end_of_word  # If True , means the word exists in the Trie
    
    
    
    
    
    # i) Returns all words in the Trie that start with a given prefix. 
    # ii) Iterates over the characters in the prefix and checks if each character has a corresponding child node. 
    # iii) If any character doesn't have a corresponding child node, the method returns an empty list. 
    # iv) Otherwise,the search_words function is called recursively find all words that start with the given prefix and have the current node as their ancestor.
    
    

    def words_with_prefix(self, prefix):
        auto_words = []
        current_node = self.root

        # Traversing Trie to the node corresponding to the last character of the prefix
        for char in prefix:
            if char not in current_node.children:
                return auto_words
            current_node = current_node.children[char]

        #  recursive search_words function to find all complete words with the given prefix
        self.search_words(current_node, auto_words, prefix)
        return auto_words
    
    
    
    
    # i) Helper method that recursively finds all words in the Trie that start with a given prefix and have a given node as their ancestor.
    # ii) Checks if the current node is the end of a word and, if so, adds the corresponding word to the auto_words list. 
    # iii) Then ,iterates over the current node's children and calls itself recursively for each child, passing the prefix plus the current character as the new prefix.
    

    def search_words(self, current_node, auto_words, word):
        if current_node is None:
            return

        
        if current_node.end_of_word:
            auto_words.append(word)

        # Recursively call search_words for each child node, expanding the word
        for char, node in current_node.children.items():
            self.search_words(node, auto_words, word + char)


if __name__ == "__main__":
    trie_ds = Trie()
    
