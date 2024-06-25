def Add(numbers: str) -> int:
    if numbers == "":
        return 0
    else:
        num_list = numbers.split(",")
        return sum(int(num) for num in num_list)

# Tests
assert Add("") == 0
assert Add("10,20") == 30
assert Add("1,2,3,4,5") == 15
assert Add("100,200,300") == 400