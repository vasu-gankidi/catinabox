import pytest

#global order
order=0


class Fruit:
    def __init__(self, name):
#        breakpoint()
        self.name = name

    def __eq__(self, other):
#        breakpoint()
        return self.name == other.name

# fixtures are designed to be executed only once by test function execution.
# and in fixture execution. The return value of the fixture are reused with in
# text function or other fixture execution, whenever the fixture is referenced.
# i.e. the 'my_fruit' fixture is executed only once. The Fruit object is reused
# in fruit_basket fixture and in test function. Hence we see the order value only
# 1.


@pytest.fixture
def my_fruit():
    global order
    order = order + 1
    print(f"printing order {order}")
    return Fruit("apple") # This statement calls fixture function (fixture.py) and returns the Fruit obj.


@pytest.fixture
def fruit_basket(my_fruit):
#    breakpoint()
    return [Fruit("banana"), my_fruit] # example of calling fixture with in fixtures. 


def test_my_fruit_in_basket(my_fruit, fruit_basket): # at this step of statement execution my_fruit function and fruit basket function is executed.
#    breakpoint()
    assert my_fruit in fruit_basket