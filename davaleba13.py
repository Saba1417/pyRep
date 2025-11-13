import csv
import os

CSV_FILE = "students.csv"
FIELDNAMES = ["id", "name", "age", "grade", "subject_name", "mark"]

def ensure_csv_exists(path=CSV_FILE):
    if not os.path.exists(path):
        with open(path, "w", newline='', encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()
            writer.writerow({
                "id": "1", "name": "string", "age": "0", "grade": "string",
                "subject_name": "string", "mark": "0"
            })
            writer.writerow({
                "id": "2", "name": "string", "age": "0", "grade": "string",
                "subject_name": "string", "mark": "0"
            })


def read_all_rows(path=CSV_FILE):
    ensure_csv_exists(path)
    with open(path, newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def write_all_rows(rows, path=CSV_FILE):
    with open(path, "w", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)


def add_student(id_, name, age, grade, subject_name, mark, path=CSV_FILE):
    ensure_csv_exists(path)
    rows = read_all_rows(path)
    new_row = {
        "id": str(id_),
        "name": str(name),
        "age": str(age),
        "grade": str(grade),
        "subject_name": str(subject_name),
        "mark": str(mark)
    }
    rows.append(new_row)
    try:
        rows.sort(key=lambda r: int(r["id"]))
    except ValueError:
        rows.sort(key=lambda r: r["id"])
    write_all_rows(rows, path)
    print(f"ჩანაწერი id={id_} დამატებულია.")


def read_students(student_id=None, path=CSV_FILE):

    rows = read_all_rows(path)
    if student_id is None:
        print("ყველა ჩანაწერი:")
        for r in rows:
            print(r)
        return rows
    else:
        sid = str(student_id)
        filtered = [r for r in rows if r["id"] == sid]
        if not filtered:
            print(f"ჩანაწერი id={student_id} ვერ მოიძებნა.")
        else:
            print(f"ჩანაწერები id={student_id}:")
            for r in filtered:
                print(r)
        return filtered


def average_marks_by_subject(path=CSV_FILE):

    rows = read_all_rows(path)
    sums = {}
    counts = {}
    for r in rows:
        subj = r["subject_name"]
        try:
            m = float(r["mark"])
        except (ValueError, TypeError):
            continue
        sums[subj] = sums.get(subj, 0.0) + m
        counts[subj] = counts.get(subj, 0) + 1
    averages = {}
    for subj in sums:
        averages[subj] = sums[subj] / counts[subj]
    print("საშუალო ქულა საგნების მიხედვით:")
    for subj, avg in averages.items():
        print(f"{subj}: {avg:.2f}")
    return averages


def update_mark(student_id, subject_name, new_mark, path=CSV_FILE):
    rows = read_all_rows(path)
    sid = str(student_id)
    updated = False
    for r in rows:
        if r["id"] == sid and r["subject_name"] == subject_name:
            r["mark"] = str(new_mark)
            updated = True
    if updated:
        write_all_rows(rows, path)
        print(f"id={student_id}, subject={subject_name} - ქულა განახლდა: {new_mark}")
    else:
        print(f"შედეგი: id={student_id} და subject={subject_name} არ მოიძებნა.")


def _input_prompt():
    ensure_csv_exists(CSV_FILE)
    while True:
        print("\nაირჩიეთ ოპცია:")
        print("1 - დამატება")
        print("2 - წაკითხვა (ყველა)")
        print("3 - წაკითხვა (პირადი id)")
        print("4 - საშუალო ქულა საგნების მიხედვით")
        print("5 - ქულის განახლება")
        print("0 - გამოსვლა")
        choice = input("ოპცია: ").strip()
        if choice == "1":
            id_ = input("id: ").strip()
            name = input("name: ").strip()
            age = input("age: ").strip()
            grade = input("grade: ").strip()
            subject = input("subject_name: ").strip()
            mark = input("mark: ").strip()
            add_student(id_, name, age, grade, subject, mark)
        elif choice == "2":
            read_students()
        elif choice == "3":
            sid = input("id: ").strip()
            read_students(sid)
        elif choice == "4":
            average_marks_by_subject()
        elif choice == "5":
            sid = input("id: ").strip()
            subject = input("subject_name: ").strip()
            new_mark = input("new mark: ").strip()
            update_mark(sid, subject, new_mark)
        elif choice == "0":
            print("გამოსვლა.")
            break
        else:
            print("არაასწორი ოფცია.")


if __name__ == "__main__":
    _input_prompt()