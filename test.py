def Add(numbers: str) -> int:
    if numbers == "":
        return 0
    elif "," in numbers:
        num1, num2 = numbers.split(",")
        return int(num1) + int(num2)
    else:
        return int(numbers)

# Tests
assert Add("") == 0
assert Add("1") == 1
assert Add("2") == 2
assert Add("1,2") == 3
assert Add("10,20") == 30