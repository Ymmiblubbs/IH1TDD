def Fizzbuzz(int):
    if int % 5 == 0 and int % 3 == 0:
        return "Fizzbuzz"

    if int % 5 == 0:
        return "Buzz"

    if int % 3 == 0:
        return "Fizz"
