from functools import reduce

#1
def group_lists(*lists):
    try:
        if not all(len(list_) == len(lists[0]) for list_ in lists):
            raise ValueError("All lists must be of equal length")
        return list(zip(*lists))
    except IndexError:
        return []

list1 = input("Enter elements of first list separated by spaces: ").split()
list2 = input("Enter elements of second list separated by spaces: ").split()
result = group_lists(list1, list2)
print(result)

#2
num_list = input("Enter elements of list separated by spaces: ").split()
num_list = [int(x) for x in num_list]
def calculate_multiplication(numbers):
    try:
        return reduce(lambda x, y: x * y, numbers, 1)
    except TypeError:
        raise TypeError("calculate_multiplication expects an iterable of numbers") from None
multiplication = calculate_multiplication(num_list)
print("multiplication of all elements:", multiplication)

#3
num_list = input("Enter elements of list separated by spaces: ").split()
num_list = [int(x) for x in num_list]
lambda_func = lambda numbers: list(filter(lambda x: x%2!= 0  , numbers))
odds = lambda_func(num_list)
print("Odd elements:", odds)

#4
def filter_by_ending(strings, ending):
    try:
        if not isinstance(ending, str):
            raise TypeError("ending must be a string")
        return list(filter(lambda s: isinstance(s, str) and s.endswith(ending), strings))
    except TypeError as e:
        print("TypeError:", e)
        return []
    except Exception as e:
        print("Error:", e)
        return []

strings = input("Enter list of strings separated by spaces: ").split()
ending = input("Enter ending string: ")
result = filter_by_ending(strings, ending)
print(result)