#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)

import re

#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True


def get_sentence():
    """Prompt until the user enters a valid sentence (uses is_sentence)."""
    while True:
        s = input("Enter a sentence (start with a capital, end with . ? !): ").strip()
        if is_sentence(s):
            return s
        print("Invalid sentence. Try again.")

def calculate_frequencies(sentence):
    """
    Return two parallel lists: word_list and freq_list.
    - case-insensitive
    - strips only . ? !
    - uses lists (not dict) to match the lab requirement
    """
    
    cleaned = re.sub(r"[.?!]", "", sentence.lower())
    tokens = cleaned.split()

    word_list = []
    freq_list = []

    for w in tokens:
        if w in word_list:
            idx = word_list.index(w)
            freq_list[idx] += 1
        else:
            word_list.append(w)
            freq_list.append(1)

    return word_list, freq_list

def print_frequencies(words, frequencies):
    """Print word frequencies in a readable format."""
    print("\nWord Frequencies")
    print("-" * 17)
    for i in range(len(words)):
        print(f"{words[i]}: {frequencies[i]}")

def main():
    sentence = get_sentence()
    words, freqs = calculate_frequencies(sentence)
    print_frequencies(words, freqs)

if __name__ == "__main__":
    main()



