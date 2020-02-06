import pytest
from pythonisms import HashTable

def test_dunder_iter():
    ht = HashTable()
    ht.add('apple', 10)
    ht.add('banana', 101)

    actual = [item for item in ht if item]
    assert actual == [[['banana', 101]], [['apple', 10]]]

def test_dunder_iter_many():
    ht = HashTable()
    ht.add('apple', 10)
    ht.add('banana', 101)
    ht.add('cantelope', 40)
    ht.add('dates', 11)
    ht.add('eggplant', 5)
    ht.add('figs', 23)
    ht.add('grapes', 55)
    ht.add('hops', 67)
    ht.add('iodine', 88)

    actual = [key for key in ht if key]
    assert actual == [[['banana', 101]], [['iodine', 88]], [['figs', 23]], [['dates', 11]], [['apple', 10]], [['hops', 67]], [['grapes', 55]], [['eggplant', 5]], [['cantelope', 40]]]

def test_dunder_iter_length():
    ht = HashTable(1024)
    ht.add('apple', 10)
    ht.add('banana', 101)
    ht.add('cantelope', 40)
    ht.add('dates', 11)
    ht.add('eggplant', 5)
    ht.add('figs', 23)
    ht.add('grapes', 55)
    ht.add('hops', 67)
    ht.add('iodine', 88)

    actual = [key for key in ht]
    assert len(actual) == 1024