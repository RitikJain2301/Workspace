import pytest

@pytest.fixture(autouse=True, params=["a","b"])
def fix(request):
    print("this is the fixture function "+ request.param[0])

def test1():
    print("this is test 1 running through conf file")

def test2():
    print("this is test 2 running through conf file")

def test3():
    print("this is test 3 running through conf file")