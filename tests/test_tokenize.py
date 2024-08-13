import logging
import re
import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tokenizer_functions import clean_text, tokenize

# Defining file paths for all English test
test_files = [
    "pg17192.txt",  # The Raven
    "pg932.txt",    # Fall of the House of Usher
    "pg1063.txt",   # Cask of Amontillado
    "pg10031.txt",  # The Poems
]

# True test assessing tokenize
def test_tokenize():
    """
    GIVEN a text input string
    WHEN the text is passed to the `tokenize` function
    THEN the function should return a list of words
    """
    text = "But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."
    expected_output = ["but", "the", "raven", "sitting", "lonely", "on", "the", "placid", "bust", "spoke", "only", "that", "one", "word", "as", "if", "his", "soul", "in", "that", "one", "word", "he", "did", "outpour"]
    tokens = tokenize(text)
    assert tokens == expected_output, f"Expected '{expected_output}', but got '{tokens}'"
    assert isinstance(tokens, list), f"Tokenizer failed on sample text: {text}"

# Fail test of tokenize
@pytest.mark.xfail(reason="This test is supposed to fail", strict=True)
def test_fail_tokenize():
    """
    GIVEN a text input string
    WHEN the text is passed to the `tokenize` function
    THEN the test should purposefully fail
    """
    text = "But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."
    incorrect_output = ["but", "the", "raven", "sitting"]
    tokens = tokenize(text)
    assert tokens == incorrect_output, "This test is expected to fail"
    assert isinstance(tokens, list), f"Tokenizer failed on sample text: {text}"

# Attempt to show pytest skipping
@pytest.mark.skip(reason="This test is skipped intentionally")
def test_tokenize_skipper():
    """
    GIVEN any input
    WHEN the input is passed to the `tokenize` function
    THEN this test is skipped intentionally
    """
    text = "Any text here"
    assert tokenize(text) == []

# True test assessing tokenize on The Raven
def test_tokenize_raven():
    """
    GIVEN the full text of 'The Raven'
    WHEN the text is passed to the `tokenize` function
    THEN the function should return the tokenized text correctly
    """
    with open('pg17192.txt', 'r', encoding='utf-8') as file:
        text = file.read()
    tokens = tokenize(text)
    assert isinstance(tokens, list), "Output must be a list"
    assert len(tokens) > 0, "The tokenized text should not be empty"

# True test of tokenize on all English texts
@pytest.mark.parametrize("file_path", test_files)
def test_tokenize_all(file_path):
    """
    GIVEN a list of file paths
    WHEN each file's text is passed to the `tokenize` function
    THEN the function should return the tokenized text correctly for each file
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    tokens = tokenize(text)
    assert isinstance(tokens, list), "Output must be a list"
    assert len(tokens) > 0, f"Output for {file_path} should not be empty"

# True test of tokenize on a snippet of French Le Corbeau
def test_tokenize_french():
    """
    GIVEN a snippet of French text from Le Corbeau
    WHEN the text is passed to the `tokenize` function
    THEN the function should return the tokenized text correctly
    """
    french_text = '''_Mais le Corbeau, perché solitairement sur ce buste placide, parla
    ce seul mot comme si, son âme, en ce seul mot, il la répandait. Je ne
    proférai donc rien de plus: il n'agita donc pas de plume--jusqu'à ce
    que je fis à peine davantage que marmotter «D'autres amis déjà ont
    pris leur vol--demain il me laissera comme mes Espérances déjà ont
    pris leur vol.» Alors l'oiseau dit: «Jamais plus.»_'''
    cleaned_text = clean_text(french_text)  # making sure the text is cleaned first before tokenizing
    tokens = tokenize(cleaned_text)
    assert isinstance(tokens, list), f"Tokenizer failed on French text: {french_text}"
    assert len(tokens) > 0, "The tokenized output should not be empty"
