def remove_fourth_character(word: str) -> str:
    first_half = word[:3]
    second_half = word[4:]
    new_word = first_half + second_half
    return new_word


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
