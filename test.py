def Add(numbers: str) -> int:
    if numbers == "":
        return 0

    if numbers.endswith(",") or numbers.endswith("\n"):
        raise ValueError("Invalid input: trailing separator")

    numbers = numbers.replace("\n", ",")
    num_list = numbers.split(",")
    
    return sum(int(num) for num in num_list if num.isdigit())

# Tests
assert Add("") == 0
assert Add("1") == 1
assert Add("2") == 2
assert Add("1,2") == 3
assert Add("10,20") == 30
assert Add("1,2,3,4,5") == 15
assert Add("100,200,300") == 600
assert Add("1\n2,3") == 6
assert Add("1,2\n3") == 6

# Testing for invalid inputs
try:
    Add("1,2,")
except ValueError as e:
    assert str(e) == "Invalid input: trailing separator"

try:
    Add("1,2\n")
except ValueError as e:
    assert str(e) == "Invalid input: trailing separator"

assert Add("1,2\n") == 6
