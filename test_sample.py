from sample import FizzBuzz

def test_divisible_by_5_and_3():
    assert FizzBuzz(15) == "FizzBuzz"
    assert FizzBuzz(30) == "FizzBuzz"

def test_divisble_by_5():
    assert FizzBuzz(5) == "Buzz"
    assert FizzBuzz(10) == "Buzz"
    
def test_divisible_by_3():
    assert FizzBuzz(3) == "Fizz"
    assert FizzBuzz(9) == "Fizz"

def test_neither_divisible_by_5_nor_3():
    assert Fizzbuzz(4) == 4
    assert Fizzbuzz(21) == 21
    
