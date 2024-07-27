import sys 
import pytest 

def test_python_version():
    assert sys.version_info[:2] == (3, 7), f"Python version is not 3.7: {sys.version}"
