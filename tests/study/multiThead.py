import pytest

@pytest.mark.release

class TestClass1(object):
    def test_one(self):
        x = "this"
    assert 'h' in x

    def test_two(self):
        x = "hello"
    assert hasattr(x, 'check')

@pytest.mark.regression
class TestClass2(object):
    def test_one(self):
    x = "this"
    assert 'h' in x
    
    def test_two(self):
    x = "hello"
    assert hasattr(x, 'check')
