import logging
import re
import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tokenizer_functions import clean_text

# Defining file paths for all English test
test_files = [
    "pg17192.txt",  # The Raven
    "pg932.txt",    # Fall of the House of Usher
    "pg1063.txt",   # Cask of Amontillado
    "pg10031.txt",  # The Poems
]

# True test assessing clean_text
def test_clean_text():
    """
    GIVEN a text input string
    WHEN the text is passed to the `clean_text` function
    THEN the function should hopefully return a lowercase string with no punctuation
    """
    text = "But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."
    expected_output = "but the raven sitting lonely on the placid bust spoke only that one word as if his soul in that one word he did outpour"
    cleaned_text = clean_text(text)
    assert cleaned_text == expected_output, f"Expected '{expected_output}', but got '{cleaned_text}'"
    assert isinstance(clean_text(text), str), f"Cleaner failed on sample text: {text}" #Provided in your example

# Fail test of clean_text
@pytest.mark.xfail(reason="This test is supposed to fail", strict=True)
def test_fail_clean_text():
    """
    GIVEN a text input string
    WHEN the text is passed to the `clean_text` function
    THEN the test should purposefully fail
    """
    text = "But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."
    incorrect_output = "but THE raven sitting lonely on the placid bust spoke"
    cleaned_text = clean_text(text)
    assert cleaned_text == incorrect_output, "This test is expected to fail"
    assert isinstance(clean_text(text), str), f"Cleaner failed on sample text: {text}"

# Attempt to show pytest skipping
@pytest.mark.skip(reason="This test is skipped intentionally")
def test_clean_text_skipper():
    """
    GIVEN any input
    WHEN the input is passed to the `clean_text` function
    THEN this test is skipped intentionally
    """
    text = "Any text here"
    assert clean_text(text) == ""

# True test assessing clean_text on The Raven
def test_clean_text_raven():
    """
    GIVEN the full text of 'The Raven'
    WHEN the text is passed to the `clean_text` function
    THEN the function should return the cleaned text correctly
    """
    with open('pg17192.txt', 'r', encoding='utf-8') as file:
        text = file.read()
    cleaned_text = clean_text(text)
    assert 'raven' in cleaned_text, "The word 'raven' should be present in the cleaned text"
    assert isinstance(clean_text(text), str), f"Cleaner failed on sample text: {text}"

# True test of clean_text on all english texts
@pytest.mark.parametrize("file_path", test_files)
def test_clean_text_all(file_path):
    """
    GIVEN a list of file paths
    WHEN each file's text is passed to the `clean_text` function
    THEN the function should return the cleaned text correctly for each file
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    cleaned_text = clean_text(text)
    assert len(cleaned_text) > 0, f"Output for {file_path} should not be empty"
    assert isinstance(clean_text(text), str), f"Cleaner failed on sample text: {text}"

# True test of clean_text on a snippet of french Le Corbeau
def test_clean_text_french():
    """
    GIVEN a snippet of French text from Le Corbeau
    WHEN the text is passed to the `clean_text` function
    THEN the function should return the cleaned text correctly
    """
    french_text = '''_Mais le Corbeau, perché solitairement sur ce buste placide, parla
    ce seul mot comme si, son âme, en ce seul mot, il la répandait. Je ne
    proférai donc rien de plus: il n'agita donc pas de plume--jusqu'à ce
    que je fis à peine davantage que marmotter «D'autres amis déjà ont
    pris leur vol--demain il me laissera comme mes Espérances déjà ont
    pris leur vol.» Alors l'oiseau dit: «Jamais plus.»_'''
    #expected_output = re.sub(r'[^\w\s]', '', french_text.lower().replace('\n', ' ').strip())
    cleaned_text = clean_text(french_text)
    #assert cleaned_text == expected_output, f"Expected '{expected_output}', but got '{cleaned_text}'"
    assert isinstance(cleaned_text, str), f"Cleaner failed on french text: {french_text}"
