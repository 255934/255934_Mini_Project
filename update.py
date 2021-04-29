import csv
student_fields = ['roll', 'name', 'age', 'email', 'phone']
student_database = 'students.csv'


def update_student(read_mode, var):
    print("--- Update Student ---")
    roll = input("Enter roll no. to update: ")
    index_student = None
    updated_data = []
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if roll == row[0]:
                    index_student = counter
                    print("Student Found: at index ", index_student)
                    student_data = []
                    for field in range(0, len(student_fields)):
                        if read_mode == 0:
                            value = input("Enter")
                        else:
                            value = var[field]
                        student_data.append(value)
                    updated_data.append(student_data)
                else:
                    updated_data.append(row)
                counter += 1

    if index_student is not None:
        with open(student_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
    else:
        print("Roll No. not found in our database")
        return 0
    if read_mode == 0:
        return student_data[0]
    return var[0]
