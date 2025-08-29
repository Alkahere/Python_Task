import json
students = {}


def insert_data():
    name = input("Enter name (unique): ")
    if name in students:
        print("Name already exists!")
        return

    address = input("Enter address: ")
    city = input("Enter city: ")
    country = input("Enter country: ")
    pincode = input("Enter pincode: ")
    sat_score = int(input("Enter SAT score: "))

    status = "Pass" if sat_score > 30 else "Fail"

    students[name] = {
        "address": address,
        "city": city,
        "country": country,
        "pincode": pincode,
        "sat_score": sat_score,
        "passed": status
    }
    print(f" Record inserted for {name}.")


def view_all():
    "Display all records in JSON format"
    if not students:
        print(" No records found.")
        return
    print(json.dumps(students, indent=4))


def get_rank():
    """Get rank of a student by SAT score"""
    name = input("Enter student name: ")
    if name not in students:
        print("⚠️ Record not found.")
        return

    sorted_students = sorted(students.items(), key=lambda x: x[1]["sat_score"], reverse=True)
    for rank, (student_name, _) in enumerate(sorted_students, start=1):
        if student_name == name:
            print(f" {name} is ranked #{rank}")
            return


def update_score():
    "Update SAT score of a student"
    name = input("Enter name: ")
    if name not in students:
        print(" Record not found.")
        return

    new_score = int(input("Enter new SAT score: "))
    students[name]["sat_score"] = new_score
    students[name]["passed"] = "Pass" if new_score > 30 else "Fail"
    print(f" Score updated for {name}.")


def delete_record():
    "Delete a student record"
    name = input("Enter name to delete: ")
    if name in students:
        del students[name]
        print(f" {name}'s record deleted.")
    else:
        print(" Record not found.")


def calculate_average():
    if not students:
        print("No records available.")
        return
    total = sum(s["sat_score"] for s in students.values())
    avg = total / len(students)
    print(f"Average SAT Score: {avg:.2f}")


def filter_records():
    status = input("Enter Pass or Fail: ").capitalize()
    filtered = {k: v for k, v in students.items() if v["passed"] == status}
    if not filtered:
        print(f"No {status} records found.")
    else:
        print(json.dumps(filtered, indent=4))


def save_to_json():
    """Save all data to JSON file"""
    with open("sat_results.json", "w") as f:
        json.dump(students, f, indent=4)
    print(" Data saved to sat_results.json")



def menu():
    while True:
        print("\n=== SAT Results Menu ===")
        print("1. Insert data")
        print("2. View all data")
        print("3. Get rank")
        print("4. Update score")
        print("5. Delete one record")
        print("6. Calculate Average SAT Score")
        print("7. Filter records by Pass/Fail Status")
        print("8. Save data to JSON file")
        print("9. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            insert_data()
        elif choice == "2":
            view_all()
        elif choice == "3":
            get_rank()
        elif choice == "4":
            update_score()
        elif choice == "5":
            delete_record()
        elif choice == "6":
            calculate_average()
        elif choice == "7":
            filter_records()
        elif choice == "8":
            save_to_json()
        elif choice == "9":
            print("👋 Exiting program.")
            break
        else:
            print("⚠️ Invalid choice. Try again.")


if __name__ == "__main__":
 
    menu()
