#1
int_list = [10,20,30,40] 
number = int(input("Enter a number to add to the list: "))  
def add_to_list(num):
    global int_list
    int_list.append(num)
add_to_list(number)
print(int_list)

#2
def sum_list(numbers):
    return sum(numbers)

numbers = input("Enter numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers]
result = sum_list(numbers)
print("Sum of the list:", result)

#3
gl_str = "Global"

def func():
    gl_str = "Local"
    return gl_str

print(func())

#4
def digit_sum(number):
    if number == 0:
        return 0
    else:
        return number % 10 + digit_sum(number // 10)

num = int(input("Enter a number: "))
print("Sum of digits:", digit_sum(num))


#5
def reverse_string(s):
    if len(s) == 0:
        return ""
    else:
        return reverse_string(s[1:]) + s[0]

input_str = input("Enter a string: ")
print("Reversed string:", reverse_string(input_str))