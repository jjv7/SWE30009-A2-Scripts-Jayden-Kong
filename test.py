import pytest
from assignment2 import split_alphabets

# split_alphabets() should output tuple[list, list]
# represented as (lowercase, uppercase)

def test_lowercase_no_duplicates():
    inputs: list[str] = ['b', 'a', 'd', 'c']
    expected: tuple[list, list] = (['a', 'b', 'c', 'd'], [])
    output: tuple[list, list] = split_alphabets(inputs)

    assert output == expected, f"Expected {expected}, but got {output}"

def test_uppercase_no_duplicates():
    inputs: list[str] = ['D', 'B', 'A', 'C']
    expected: tuple[list, list] = ([], ['A', 'B', 'C', 'D'])
    output: tuple[list, list] = split_alphabets(inputs)

    assert output == expected, f"Expected {expected}, but got {output}"

def test_mixed_case_no_duplicates():
    inputs: list[str] = ['c', 'A', 'd', 'B']
    expected: tuple[list, list] = (['c', 'd'], ['A', 'B'])
    output: tuple[list, list] = split_alphabets(inputs)

    assert output == expected, f"Expected {expected}, but got {output}"

def test_case_sensitivity():
    inputs: list[str] = ['b', 'A', 'a', 'B']
    expected: tuple[list, list] = (['a', 'b'], ['A', 'B'])
    output: tuple[list, list] = split_alphabets(inputs)

    assert output == expected, f"Expected {expected}, but got {output}"

def test_lowercase_duplicate():
    inputs: list[str] = ['b', 'a', 'a', 'c', 'b']
    expected: tuple[list, list] = (['a', 'b', 'c'], [])
    output: tuple[list, list] = split_alphabets(inputs)

    assert output == expected, f"Expected {expected}, but got {output}"

def test_uppercase_duplicate():
    inputs: list[str] = ['A', 'C', 'B', 'A', 'C']
    expected: tuple[list, list] = ([], ['A', 'B', 'C'])
    output: tuple[list, list] = split_alphabets(inputs)

    assert output == expected, f"Expected {expected}, but got {output}"

def test_mixed_case_duplicate_case_sensitivity():
    inputs: list[str] = ['b', 'B', 'a', 'A', 'a', 'B']
    expected: tuple[list, list] = (['a', 'b'], ['A', 'B'])
    output: tuple[list, list] = split_alphabets(inputs)

    assert output == expected, f"Expected {expected}, but got {output}"
