import tkinter as tk
from dsa import Trie
import re
import requests

def scrape_words(url, num_words, max_word_length):
    words = []
    response = requests.get(url)

    if response.status_code == 200:
        lines = response.text.split('\n')

        for line in lines:
            word = line.strip()
            if word and len(word) <= max_word_length:
                words.append(word)

    return words[:num_words] # we need 10,000 words.

class WordSuggestionGUI(tk.Tk):
    def __init__(self, trie_ds):
        super().__init__()
        self.title("Auto Complete System using Trie")
        self.geometry("600x400")  

        
        self.logo = tk.PhotoImage(file="logo.png")  
        self.logo_label = tk.Label(self, image=self.logo)
        self.logo_label.pack()
        self.logo_label.pack(pady=20)

        
        self.heading_label = tk.Label(self, text="Auto Complete System using Trie", font=("Helvetica", 60), bg="white", fg="black")
        self.heading_label.pack()
        self.heading_label.pack(pady=40)

        #Scraping words 
        url = 'https://www.mit.edu/~ecprice/wordlist.10000'
        num_words_to_scrape = 10000
        max_word_length = 15

        scraped_words = scrape_words(url, num_words_to_scrape, max_word_length)

        # creating a Trie and inserting the scraped words
        self.trie = Trie()
        for word in scraped_words:
            self.trie.insert(word)

        # suggestions
        self.input_field = tk.Entry(self, width=50, font=("Helvetica", 14))
        
        self.input_field.pack(pady=20)  
        self.input_field.bind("<KeyRelease>", self.update_suggestions) #whenever the user releases a key while typing in the field, the self.update_suggestions() method will be called.
                                                                       #Does the generating and displaying word suggestions based on the user's input

        self.input_field.bind("<space>", self.handle_spacebar) #binds the spacebar key press to the self.handle_spacebar() method , indicating a new word.

        # creates a container frame within the GUI window to house the list of suggestions.
        self.suggestions_frame = tk.Frame(self)
        self.suggestions_frame.pack()

        self.suggestions_list = tk.Listbox(self.suggestions_frame, width=40, height=5, font=("Helvetica", 20))
        self.suggestions_list.pack(pady=20)

        # Input field for checking if a word exists
        self.check_word_label = tk.Label(self, text="Check Word:", font=("Helvetica", 14))
        self.check_word_label.pack(pady=10)

        self.check_word_field = tk.Entry(self, width=20, font=("Helvetica", 14))
        self.check_word_field.pack(pady=10)

        # Check button and result label
        self.check_button = tk.Button(self, text="Check", command=self.check_word, font=("Helvetica", 14))
        self.check_button.pack(pady=10) 

        self.result_label = tk.Label(self, text="", font=("Helvetica", 14))
        self.result_label.pack(pady=10)

        ## Buttons
        
        
        
        #Close button
        self.close_button = tk.Button(self, text="Close", command=self.destroy, font=("Helvetica", 14)) 
        self.close_button.pack(side=tk.RIGHT, padx=10)
        
        #Add-word button
        self.add_word_label = tk.Label(self, text="Add Word:", font=("Helvetica", 14), bg="black", fg="white")
        self.add_word_label.pack(pady=10)
        self.add_word_field = tk.Entry(self, width=20, font=("Helvetica", 14))
        self.add_word_field.pack(pady=10)

        
        self.add_word_button = tk.Button(self, text="Add Word", command=self.add_word, font=("Helvetica", 14))
        self.add_word_button.pack(pady=10)

        self.update_suggestions("") # When empty , the sugesstion list should also be empty.

        

    def update_suggestions(self, event):
        
        text = self.input_field.get().strip() #strip() removes any leading or trailing white-sapces
        
        # check to avoid suggestions when the text field is empty
        if not text:
            self.suggestions_list.delete(0, tk.END)
            return
        words = text.split()
        if words:
            last_word = words[-1]
            prefix = last_word.strip()
        else:
             prefix = ""
        suggestions = [suggestion for suggestion in self.trie.words_with_prefix(prefix) if not suggestion.startswith(".")] #list comprehension : no need to make a seprate loop with 'append'
        self.suggestions_list.delete(0, tk.END) #clears the existing suggestions in the list, preparing for the updated list.
        
        for suggestion in suggestions:
            self.suggestions_list.insert(tk.END, suggestion)
            
            

    def handle_special_characters(self, text):
        valid_chars = r'[a-zA-Z ]'  # Only letters and spaces allowed
        return re.sub(r'[^{}]'.format(valid_chars), '', text)

    
    
    
    def add_word(self):
        new_word = self.add_word_field.get().strip()

       #checking if the length is within the limit and the word is non-alphabetic
        if len(new_word) > 15 or not new_word.isalpha():
            self.result_label.config(text="Invalid word. Please enter a non-alphabetic word with a maximum length of 15 characters.")
            return

        if new_word:
            self.trie.insert(new_word)
            self.update_suggestions("")  # Updating suggestions after adding the new word
            self.add_word_field.delete(0, tk.END)  # Clearing the input field
            self.result_label.config(text=f"The word '{new_word}' has been added!")



    def handle_spacebar(self, event):
        self.update_suggestions(event)
        
        

    def check_word(self):
        word_to_check = self.check_word_field.get()
        if self.trie.search(word_to_check):
            result_text = f"The word '{word_to_check}' exists in the Trie."
        else:
            result_text = f"The word '{word_to_check}' does not exist in the Trie."
        self.result_label.config(text=result_text)

    
# Example usage:

trie_ds = Trie()

app = WordSuggestionGUI(trie_ds)
app.configure(bg="white")  
app.mainloop()
