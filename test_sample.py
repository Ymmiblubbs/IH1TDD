from sample import FizzBuzz

def test_divisible_by_5_and_3():
    assert FizzBuzz(15) == "FizzBuzz"
    assert FizzBuzz(30) == "FizzBuzz"

def test_divisble_by_5():
    assert FizzBuzz(5) == "Buzz"
    assert FizzBuzz(10) == "Buzz"
    
