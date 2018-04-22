import pytest
from fizzbuzz import fizzbuzz


# traditional test
def test_fizzbuzz():
    assert fizzbuzz(1) == 1
    assert fizzbuzz(2) == 2
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(4) == 4
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(30) == "FizzBuzz"


# parametrize decorator to pass in values
@pytest.mark.parametrize("arg, ret", [
    (1, 1),
    (2, 2),
    (3, "Fizz"),
    (4, 4),
    (5, "Buzz"),
    (6, "Fizz"),
    (7, 7),
    (8, 8),
    (15, "FizzBuzz"),
    (30, "FizzBuzz"),
])
def test_fizzbuzz_parametrize(arg, ret):
    assert fizzbuzz(arg) == ret
