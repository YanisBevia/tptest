import re

def Add(numbers: str) -> int:
    if numbers == "":
        return 0
    
    delimiter = ","
    numbers_list = numbers

    if numbers.startswith("//"):
        parts = numbers.split("\n", 1)
        delimiter = parts[0][2:]  
        numbers_list = parts[1]   

    numbers_list = numbers_list.replace("\n", delimiter)
    
    if delimiter != ",":
        expected_pattern = f"[^0-9{delimiter}]"
        match = re.search(expected_pattern, numbers_list)
        if match:
            pos = match.start()
            found_char = match.group(0)
            raise ValueError(f"'{delimiter}' expected but '{found_char}' found at position {pos}.")
    
    num_list = numbers_list.split(delimiter)

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

# Custom delimiter tests
assert Add("//;\n1;3") == 4
assert Add("//|\n1|2|3") == 6
assert Add("//sep\n2sep5") == 7

# Invalid delimiter usage
try:
    Add("//|\n1|2,3")
except ValueError as e:
    assert str(e) == "'|' expected but ',' found at position 3."

try:
    Add("1,2,")
except ValueError as e:
    assert str(e) == "Invalid input: trailing separator"

try:
    Add("1,2\n")
except ValueError as e:
    assert str(e) == "Invalid input: trailing separator"

assert Add("//|\n1|2,3") == 7