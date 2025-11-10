import re

#დავალება 5
#1
numbers = []

while True:
    command = input("შეიყვანეთ ბრძანება (a-დამატება, r-წაშლა, e-გასვლა): ")
    if command == 'a':
        num = input("შეიყვანეთ რიცხვი დასამატებლად: ")
        if num.isdigit():
            numbers.append(int(num))
        else:
            print("გთხოვთ შეიყვანოთ მხოლოდ რიცხვი.")
        print("მიმდინარე სია:", numbers)
    elif command == 'r':
        if numbers:
            num = input("შეიყვანეთ რიცხვი წასაშლელად: ")
            if num.isdigit():
                num = int(num)
                if num in numbers:
                    numbers.remove(num)
                else:
                    print("ეს რიცხვი სიაში არ არის.")
            else:
                print("გთხოვთ შეიყვანოთ მხოლოდ რიცხვი.")
        else:
            print("სია ცარიელია.")
        print("მიმდინარე სია:", numbers)
    elif command == 'e':
        print("პროგრამა დასრულდა. საბოლოო სია:", numbers)
        break
    else:
        print("არასწორი ბრძანება.")



#2
my_list_1 = [43, '22', 12, 66, 210, ["hi"]]

# a
print(my_list_1.index(210))

# b
my_list_1[-1].append("hello")

# c
del my_list_1[2]
print(my_list_1)

# d
my_llist_2 = my_list_1.copy()
my_llist_2.clear()
print(my_list_1)
print(my_llist_2)


#3
phone = input("შეიყვანეთ ტელეფონის ნომერი: ")
pattern = r"\(\d{3}\) \d{3}-\d{3}"

if re.fullmatch(pattern, phone):
    print(phone)
else:
    print("Invalid format")