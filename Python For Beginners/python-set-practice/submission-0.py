from typing import List

def contains_duplicate(words: List[str]) -> bool:
    len_my_list = len(words)
    my_set = set(words)
    len_my_set = len(my_set)
    if(len_my_list == len_my_set):
        return False
    else:
        return True

# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))
