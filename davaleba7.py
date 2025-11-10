# 1
seq = input("შეიყვანეთ მონაცემების მიმდევრობა (გამოყავით მძიმით): ")
items = seq.split(",")
unique_set = set(items)
print("უნიკალური მონაცემებიანი set:", unique_set)

# 2
seq2 = input("შეიყვანეთ მონაცემების მიმდევრობა (გამოყავით მძიმით): ")
items2 = seq2.split(",")
unique_frozenset = frozenset(items2)
print("უნიკალური მონაცემებიანი frozenset:", unique_frozenset)

# 3
set1 = {"a", "b", "c"}
set2 = {"d", "e", "f"}
union_tuple = tuple(set1.union(set2))
print("გაერთიანებული მონაცემები tuple:", union_tuple)

# 4
nums = input("შეიყვანეთ რიცხვები მძიმით გამოყოფილი: ")
num_tuple = tuple(nums.split(","))
unique_list = list(set(num_tuple))
print("უნიკალური ელემენტები სიის სახით:", unique_list)

# 5
people = [("Gega", 24), ("Gaga", 21), ("Goga", 19), ("Giga", 27), ("Gagi", 11)]
for name, age in people:
    print(f"Name: {name}, Age: {age}")

# 6
users1 = ["Irakli", "Giorgi", "Nona", "Oto"]
users2 = ["Kato", "Levani", "Nino", "Dato", "Irakli", "Nemo"]
intersection = set(users1) & set(users2)
print("თანხვედრა:", list(intersection))