"""
This module contains functions for text processing including cleaning text,
tokenizing text into words, and counting word frequencies.
"""

# import logging
import re
from collections import Counter

# Configuration logging
#logging.basicConfig(level=logging.DEBUG, format='%(levelname)s:%(message)s')

def clean_text(input_text):
    """
    Convert input text to lowercase and remove punctuation.
    
    Params
    ----------
    input_text : str
        The string to clean.
        
    Returns
    -------
    str
        The cleaned string.
    
    Raises
    ------
    AssertionError
        If the input is not a string or if the output is not a string.
    """
    assert isinstance(input_text, str), "Input must be a string"
    # logging.debug("Cleaning text: %s", input_text)
    cleaned_text = re.sub(r'[^\w\s]', '', input_text.lower())
    # logging.debug("Cleaned text: %s", cleaned_text)
    assert isinstance(cleaned_text, str), "Output must be a string"
    return cleaned_text

def tokenize(input_text):
    """
    Split cleaned input string into a list of words.
    
    Params
    ----------
    input_text : str
        The string to tokenize.
        
    Returns
    -------
    list
        A list of words from the input string.
    
    Raises
    ------
    AssertionError
        If the input is not a string or if the output is not a list.
    """
    assert isinstance(input_text, str), "Input must be a string"
    # logging.debug("Tokenizing text: %s", input_text)
    tokens = clean_text(input_text).split()
    # logging.debug("Tokens: %s", tokens)
    assert isinstance(tokens, list), "Output must be a list"
    return tokens

def count_words(input_text):
    """
    Count the frequency/occurance of each word in the input string..
    
    Params
    ----------
    input_text : str
        The string to count words of.
        
    Returns
    -------
    dict
        A dictionary with words as keys and their counts as values.
    
    Raises
    ------
    AssertionError
        If the input is not a string or if the output is not a dictionary.
    """
    assert isinstance(input_text, str), "Input must be a string"
    # logging.debug("Counting words in text: %s", input_text)
    words = tokenize(input_text)
    word_counts = Counter(words)
    # logging.debug("Word counts: %s", word_counts)
    assert isinstance(word_counts, dict), "Output must be a dictionary"
    return word_counts
