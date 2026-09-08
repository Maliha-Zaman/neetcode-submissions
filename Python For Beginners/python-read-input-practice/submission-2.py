def add_two_numbers() -> int:
    num_string = input()
    num_list = num_string.split(",")
    num_list = [int(x) for x in num_list]
    return sum(num_list)



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
