import sys 
import pytest 

def test_python_version():
    valid_versions = [(3, 8), (3, 9), (3, 12)]
    assert sys.version_info[:2] in valid_versions, f"Python version is not one of the supported versions (3.7, 3.8, 3.9): {sys.version}"
