#დავალება 1
# 1
a = float(input("პირველი რიცხვი: "))
b = float(input("მეორე რიცხვი: "))

print("მიმატება:", a + b)
print("გამოკლება:", a - b)
print("გამრავლება:", a * b)
print("ჩვეულებრივი გაყოფა:", a / b)
print("მთელზე გაყოფა:", a // b)
print("ნაშთის აღება:", a % b)
print("ახარისხება:", a ** b)

# 2
d1 = float(input("პირველი დიაგონალის სიგრძე: "))
d2 = float(input("მეორე დიაგონალის სიგრძე: "))
area_rhombus = (d1 * d2) / 2
print("ფართობი:", area_rhombus)

# 3
meters = float(input())
print("სანტიმეტრები:", meters * 100)
print("დეციმეტრები:", meters * 10)
print("მილიმეტრები:", meters * 1000)
print("მილები:", meters / 1609.344)

# 4
base = float(input("სამკუთხედის ფუძის სიგრძე: "))
height = float(input("სამკუთხედის სიმაღლე: "))
area_triangle = (base * height) / 2
print("ფართობი:", area_triangle)

# 5
num = int(input())
digit_sum = (num // 10) + (num % 10)
print(digit_sum)

#დავალება 2
# 1
num_list = [44, 23, 11, 8, 20, 56, 33, 55]
number = int(input())
if number in num_list:
    print("The number in list")
else:
    print("The number not in list")

# 2
num = int(input())
if num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

# 3
st1 = input("first string: ")
st2 = input("second string: ")
if st1 is st2:
    print("Same object")
else:
    print("Different object")

# 4
num_list = [44, 23, 11, 8, 20, 56, 33, 55]
number = int(input("number: "))
if number > num_list[2] and number < num_list[-1]:
    print("More than list elements")
elif number == num_list[5]:
    print("Equal")
else:
    print("None of the conditions were met")