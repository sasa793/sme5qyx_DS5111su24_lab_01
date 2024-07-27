import sys
import subprocess
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from collections import Counter
from tokenizer_functions import clean_text, tokenize, count_words

# Group testing to make sure all the functions work
@pytest.mark.integration
def test_integration_process():
    """
    GIVEN a sample text from 'The Raven'
    WHEN the text is processed through clean_text, tokenize, and count_words functions
    THEN the functions should return the expected results correctly for the text
    """
    text = "But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."
    cleaned_text = clean_text(text)
    expected_cle_output = "but the raven sitting lonely on the placid bust spoke only that one word as if his soul in that one word he did outpour"

    tokens = tokenize(cleaned_text)
    expected_tok_output = ["but", "the", "raven", "sitting", "lonely", "on", "the", "placid", "bust", "spoke", "only", "that", "one", "word", "as", "if", "his", "soul", "in", "that", "one", "word", "he", "did", "outpour"]

    word_counts = count_words(cleaned_text)
    expected_wor_output = Counter(["but", "the", "raven", "sitting", "lonely", "on", "the", "placid", "bust", "spoke", "only", "that", "one", "word", "as", "if", "his", "soul", "in", "that", "one", "word", "he", "did", "outpour"])

    assert cleaned_text == expected_cle_output, f"Expected '{expected_cle_output}', but got '{cleaned_text}'"
    assert tokens == expected_tok_output, f"Expected '{expected__tok_output}', but got '{tokens}'"
    assert word_counts == expected_wor_output, f"Expected '{expected_wor_output}', but got '{word_counts}'"
    assert len(word_counts) > 0, "Word counts should not be empty"

# Group testing to make sure everything is downloaded and ready to go
# Had Office Hours help for the below integration test
@pytest.mark.integration
def test_environment_setup_and_get_texts():
    """
    GIVEN the environment needs to be set up and books need to be downloaded
    WHEN the 'make get_texts' command is run
    THEN the books should be downloaded successfully and the environment should be ready
    """
    # environment setup
    result = subprocess.run(['make', 'setup_env'], capture_output=True, text=True)
    assert result.returncode == 0, "Failed to set up the environment"

    # run 'make get_texts' command
    result = subprocess.run(['make', 'get_texts'], capture_output=True, text=True)
    assert result.returncode == 0, "Failed to download the texts"

    # Check if the books exist
    test_files = [
        "pg17192.txt",  # The Raven
        "pg932.txt",    # Fall of the House of Usher
        "pg1063.txt",   # Cask of Amontillado
        "pg10031.txt",  # The Poems
    ]
    for book in test_files:
        assert os.path.isfile(book), f"{book} is not downloaded"
