import pytest
from pythonisms import PythonismCollection


def test_iter():
    collection = PythonismCollection([1, 2, 3, 4, 5])
    result = []
    for value in collection:
        result.append(value)
    assert result == [1, 2, 3, 4, 5]


def test_list_comprehension():
    collection = PythonismCollection([1, 2, 3, 4, 5])
    result = [value * 2 for value in collection]
    assert result == [2, 4, 6, 8, 10]


def test_convert_to_list():
    collection = PythonismCollection([1, 2, 3, 4, 5])
    result = list(collection)
    assert result == [1, 2, 3, 4, 5]


def test_generator():
    collection = PythonismCollection([1, 2, 3, 4, 5])
    gen = collection.generator()
    result = []
    for value in gen:
        result.append(value)
    assert result == [1, 2, 3, 4, 5]


def test_empty_collection_iter():
    collection = PythonismCollection([])
    result = []
    for value in collection:
        result.append(value)
    assert result == []


def test_empty_collection_list_comprehension():
    collection = PythonismCollection([])
    result = [value * 2 for value in collection]
    assert result == []


def test_empty_collection_convert_to_list():
    collection = PythonismCollection([])
    result = list(collection)
    assert result == []


def test_empty_collection_generator():
    collection = PythonismCollection([])
    gen = collection.generator()
    result = []
    for value in gen:
        result.append(value)
    assert result == []


def test_collection_with_one_value_iter():
    collection = PythonismCollection([5])
    result = []
    for value in collection:
        result.append(value)
    assert result == [5]


def test_collection_with_one_value_list_comprehension():
    collection = PythonismCollection([5])
    result = [value * 2 for value in collection]
    assert result == [10]


def test_collection_with_one_value_convert_to_list():
    collection = PythonismCollection([5])
    result = list(collection)
    assert result == [5]


def test_collection_with_one_value_generator():
    collection = PythonismCollection([5])
    gen = collection.generator()
    result = []
    for value in gen:
        result.append(value)
    assert result == [5]


def test_large_collection_iter():
    collection = PythonismCollection(list(range(10000)))
    result = []
    for value in collection:
        result.append(value)
    assert result == list(range(10000))


def test_large_collection_list_comprehension():
    collection = PythonismCollection(list(range(10000)))
    result = [value * 2 for value in collection]
    assert result == [value * 2 for value in range(10000)]


def test_large_collection_convert_to_list():
    collection = PythonismCollection(list(range(10000)))
    result = list(collection)
    assert result == list(range(10000))


def test_large_collection_generator():
    collection = PythonismCollection(list(range(10000)))
    gen = collection.generator()
    result = []
    for value in gen:
        result.append(value)
    assert result == list(range(10000))
