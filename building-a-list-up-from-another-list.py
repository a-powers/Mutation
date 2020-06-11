powerball_numbers = [4, 8, 15, 16, 23, 42]

def squares(numbers):
    squares = []
    for number in numbers:
        squares.append(number ** 2)
    return squares
print(squares(powerball_numbers))


def convert_to_floats(numbers):
    floats = []
    for number in numbers:
        floats.append(float(number))
    return floats
print(convert_to_floats(powerball_numbers))


def even_or_odd(numbers):
    maths = []
    for number in numbers:
        if number % 2 == 0:
            maths.append(True)
        else:
            maths.append(False)
    return maths
print(even_or_odd(powerball_numbers))



# Coding Exercise 23

def only_evens(numbers):
    even_list = []
    for number in numbers:
        if number % 2 == 0:
            even_list.append(number)
    return even_list
print(only_evens([4, 8, 15, 16, 23, 42]))



def long_strings(string_list):
    new_list = []
    for string in string_list:
        if len(string) >= 5:
            new_list.append(string)
    return new_list
print(long_strings(["Hello", "Goodbye", "Sam"]))