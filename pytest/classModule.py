import pytest
from ddt import data, unpack, ddt


@data((2,4), (4,2))
@unpack
@pytest.fixture()
def testloginFunc(a, b):
    print(a+b)


# def testloginFunc(a, b):
#         c = a+b
#         print(c)

# testloginFunc(4,2)

# @ddt
# class FooTestCase():

#     @data(1, -3, 2, 0)
#     def test_not_larger_than_two(self, value):
#         self.assertFalse(larger_than_two(value))

#     @data(annotated(2, 1), annotated(10, 5))
#     def test_greater(self, value):
#         a, b = value
#         self.assertGreater(a, b)