def Add(numbers: str) -> int:
    if numbers == "":
        return 0
    else:
        numbers = numbers.replace("\n", ",")
        num_list = numbers.split(",")
        return sum(int(num) for num in num_list if num)

# Tests
assert Add("") == 0
assert Add("1") == 1
assert Add("2") == 2
assert Add("1,2") == 3
assert Add("10,20") == 30
assert Add("1,2,3,4,5") == 15
assert Add("100,200,300") == 600
assert Add("1\n2,3") == 5
assert Add("1,2\n3") == 6
