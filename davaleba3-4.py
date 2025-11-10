import string

#დავალება 3
# 1
n = int(input("შეიყვანეთ რიცხვი n: "))
total = 0
for i in range(1, n + 1):
    total += i
print("ჯამი:", total)

# 2
num = int(input("შეიყვანეთ რიცხვი: "))
while num > 0:
    print(num)
    num -= 1

# 3
secret_number = 15
while True:
    guess = int(input("გამოიცანით რიცხვი: "))
    if guess == secret_number:
        print("სწორია! თამაში დასრულდა.")
        break

# 4
total_sum = 0
while True:
    value = input("შეიყვანეთ რიცხვი ან 'sum': ")
    if value == 'sum':
        break
    try:
        num = int(value)
        if num > 0:
            total_sum += num
    except ValueError:
        continue
print("დადებითი რიცხვების ჯამი:", total_sum)

#დავალება 5
# 1
def utf8_encode(s):
    return s.encode('utf-8')

# 2
def process_string(s):
    s = s.strip().lower()
    if "python" in s:
        s = s.replace("python", "Python")
    return s + "Python"

# 3
def first_half(s):
    mid = len(s) // 2
    return s[:mid]

# 4
def is_valid(s):
    has_letter = any(c in string.ascii_letters for c in s)
    has_digit = any(c.isdigit() for c in s)
    allowed = set(string.ascii_letters + string.digits)
    no_extra = all(c in allowed for c in s)
    return has_letter and has_digit and no_extra

# 5
def bytes_conversion(s):
    b = s.encode()
    print(b)
    s2 = b.decode()
    print(s2)