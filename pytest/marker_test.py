import pytest

@pytest.mark.sanity
def testMark():
    print("this is sanity marker")

@pytest.mark.smoke
def testMark():
    print("this is smoke marker")

@pytest.mark.regression
def testMark():
    print("this is regression marker")
