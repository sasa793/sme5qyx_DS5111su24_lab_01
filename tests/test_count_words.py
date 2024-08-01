import logging
import re
import sys
import os
import pytest
from collections import Counter
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tokenizer_functions import count_words

# Defining file paths for all English tests
test_files = [
    "pg17192.txt",  # The Raven
    "pg932.txt",    # Fall of the House of Usher
    "pg1063.txt",   # Cask of Amontillado
    "pg10031.txt",  # The Poems
]

# True test assessing count_words
def test_count_words():
    """
    GIVEN a text input string
    WHEN the text is passed to the `count_words` function
    THEN the function should return a dictionary of word counts
    """
    text = "But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."
    expected_output = Counter(["but", "the", "raven", "sitting", "lonely", "on", "the", "placid", "bust", "spoke", "only", "that", "one", "word", "as", "if", "his", "soul", "in", "that", "one", "word", "he", "did", "outpour"])
    word_counts = count_words(text)
    assert word_counts == expected_output, f"Expected '{expected_output}', but got '{word_counts}'"
    assert isinstance(word_counts, dict), f"Count words failed on sample text: {text}"

# Fail test of count_words
@pytest.mark.xfail(reason="This test is supposed to fail", strict=True)
def test_fail_count_words():
    """
    GIVEN a text input string
    WHEN the text is passed to the `count_words` function
    THEN the test should purposefully fail
    """
    text = "But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."
    incorrect_output = {"but": 1, "the": 2, "raven": 1, "sitting": 1}
    word_counts = count_words(text)
    assert word_counts == incorrect_output, "This test is expected to fail"
    assert isinstance(word_counts, dict), f"Count words failed on sample text: {text}"

# Attempt to show pytest skipping
@pytest.mark.skip(reason="This test is skipped intentionally")
def test_count_words_skipper():
    """
    GIVEN any input
    WHEN the input is passed to the `count_words` function
    THEN this test is skipped intentionally
    """
    text = "Any text here"
    assert count_words(text) == {}

# True test assessing count_words on The Raven
def test_count_words_raven():
    """
    GIVEN the full text of 'The Raven'
    WHEN the text is passed to the `count_words` function
    THEN the function should return the word counts correctly
    """
    with open('pg17192.txt', 'r', encoding='utf-8') as file:
        text = file.read()
    word_counts = count_words(text)
    assert isinstance(word_counts, dict), "Output must be a dictionary"
    assert 'raven' in word_counts, "The word 'raven' should be present in the word counts"

# True test of count_words on all English texts
@pytest.mark.parametrize("file_path", test_files)
def test_count_words_all(file_path):
    """
    GIVEN a list of file paths
    WHEN each file's text is passed to the `count_words` function
    THEN the function should return the word counts correctly for each file
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    word_counts = count_words(text)
    assert isinstance(word_counts, dict), "Output must be a dictionary"
    assert len(word_counts) > 0, f"Output for {file_path} should not be empty"

# True test of count_words on a snippet of French Le Corbeau
def test_count_words_french():
    """
    GIVEN a snippet of French text from Le Corbeau
    WHEN the text is passed to the `count_words` function
    THEN the function should return the word counts correctly
    """
    french_text = '''_Mais le Corbeau, perché solitairement sur ce buste placide, parla
    ce seul mot comme si, son âme, en ce seul mot, il la répandait. Je ne
    proférai donc rien de plus: il n'agita donc pas de plume--jusqu'à ce
    que je fis à peine davantage que marmotter «D'autres amis déjà ont
    pris leur vol--demain il me laissera comme mes Espérances déjà ont
    pris leur vol.» Alors l'oiseau dit: «Jamais plus.»_'''
    word_counts = count_words(french_text)
    assert isinstance(word_counts, dict), f"Count words failed on French text: {french_text}"
    assert len(word_counts) > 0, "The count words output should not be empty"
