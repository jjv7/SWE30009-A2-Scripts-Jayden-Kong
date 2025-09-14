import pytest
from assignment2 import split_alphabets

# split_alphabets() should output tuple[list, list]
# represented as (lowercase, uppercase)

def test_single_lowercase():
    inputs: list[str] = ['a']
    expected: tuple[list, list] = (['a'], [])
    output: tuple[list, list] = split_alphabets(inputs)

    assert output == expected, f"Expected {expected}, but got {output}"

def test_uppercase_no_duplicates():
    inputs: list[str] = ['A']
    expected: tuple[list, list] = ([], ['A'])
    output: tuple[list, list] = split_alphabets(inputs)

    assert output == expected, f"Expected {expected}, but got {output}"

def test_duplicate_lowercase():
    inputs: list[str] = ['d', 'b', 'a', 'c', 'a', 'b']
    expected: tuple[list, list] = (['a', 'b', 'c', 'd'], [])
    output: tuple[list, list] = split_alphabets(inputs)

    assert output == expected, f"Expected {expected}, but got {output}"

def test_duplicate_uppercase():
    inputs: list[str] = ['A', 'C', 'B', 'A', 'C']
    expected: tuple[list, list] = ([], ['A', 'B', 'C'])
    output: tuple[list, list] = split_alphabets(inputs)

    assert output == expected, f"Expected {expected}, but got {output}"

def test_mixed_case():
    inputs: list[str] = ['d', 'B', 'c', 'A']
    expected: tuple[list, list] = (['c', 'd'], ['A', 'B'])
    output: tuple[list, list] = split_alphabets(inputs)

    assert output == expected, f"Expected {expected}, but got {output}"

def test_case_sensitivity():
    inputs: list[str] = ['b', 'B', 'a', 'A', 'a', 'B']
    expected: tuple[list, list] = (['a', 'b'], ['A', 'B'])
    output: tuple[list, list] = split_alphabets(inputs)

    assert output == expected, f"Expected {expected}, but got {output}"

def test_maximum_input():
    inputs: list[str] = ['j', 'a', 'B', 'e', 'D', 'c', 'A', 'i', 'f', 'G', 'h', 'H', 'd', 'C', 'E', 'g', 'F', 'J', 'a', 'A']
    expected: tuple[list, list] = (['a', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'], ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J'])
    output: tuple[list, list] = split_alphabets(inputs)

    assert output == expected, f"Expected {expected}, but got {output}"
