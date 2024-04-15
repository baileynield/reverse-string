# Make a functino that takes in a string and returns a reversed copy

def reverse(s: str) -> str:
    new_string = ""
    for i in s:
        new_string = i + new_string
    return new_string

def test_reverse():
    s = "steve"
    assert reverse(s) == "evets"