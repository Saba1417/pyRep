#დავალება 8 
#1
def fibo(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

if __name__ == "__main__":
    n = input("Enter the number of Fibonacci numbers to generate: ")
    n = int(n)
    for num in fibo(n): 
        print(num) 


#2
def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
if are_anagrams(s1, s2):
    print("The strings are anagrams")
else:
    print("The strings are not anagrams")


#3
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
num = int(input("Enter a number to compute its factorial: "))
result = factorial(num)
print(f"The factorial of {num} is {result}")


#4
def char_count(s):
    count = {}
    for char in s:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count
string = input("Enter a string: ")
result = char_count(string)
char = input("Enter a character to find its count: ")
if char in result:
    print(f"The character '{char}' appears {result[char]} times.")