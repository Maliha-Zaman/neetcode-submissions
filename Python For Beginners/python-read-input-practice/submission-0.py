def add_two_numbers() -> int:
    num_string = input()
    num_list = num_string.split(",")
    num_list = [int(x) for x in num_list]
    for x in range(len(num_list)-1):
        Add= num_list[x]+num_list[x+1]
    return Add



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
