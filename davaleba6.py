my_dict = {
    "students": [
        {"id": 20, "name": "Giorgi", "age": 25},
        {"id": 25, "name": "Giorgi", "age": 23},
        {"id": 56, "name": "Nika", "age": 25},
        {"id": 100, "name": "Nika", "age": 22},
        {"id": 1232, "name": "Dato", "age": 22},
        {"id": 846723, "name": "Archili", "age": 32}
    ],
    "subjects": [
        {"id": 1, "name": "Math", "grades": {"20": "B", "25": "A", "56": "B", "100": "A", "1232": "C", "846723": "A"}},
        {"id": 2, "name": "Physics", "grades": {"20": "A", "25": "B", "56": "B", "100": "A", "1232": "C", "846723": "B"}},
        {"id": 3, "name": "English", "grades": {"20": "A", "25": "A", "56": "A", "100": "A", "1232": "B", "846723": "A"}},
        {"id": 4, "name": "Chemistry", "grades": {"20": "B", "25": "B", "56": "B", "100": "A", "1232": "A", "846723": "A"}},
        {"id": 5, "name": "History", "grades": {"20": "C", "25": "B", "56": "B", "100": "A", "1232": "A", "846723": "A"}},
    ]
}

student_ids = [str(student["id"]) for student in my_dict["students"]]
print("სტუდენტების ID:", ", ".join(student_ids))

selected_id = input("აირჩიეთ სტუდებტის ID: ").strip()

student = next((s for s in my_dict["students"] if str(s["id"]) == selected_id), None)

if student:
    print("\nstudent infomration:")
    print(f"ID: {student['id']}, Name: {student['name']}, Age: {student['age']}")
    for subject in my_dict["subjects"]:
        grade = subject["grades"].get(selected_id)
        print(f"subject: {subject['name']}, grade: {grade}")
else:
    print(" სტუდენტის ID არ არსებობს.")