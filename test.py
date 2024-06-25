def Add(numbers: str) -> int:
    if numbers == "":
        return 0
    return int(numbers)

# Tests
assert Add("") == 0
assert Add("1") == 1
assert Add("2") == 2