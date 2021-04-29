import csv
student_fields = ['roll', 'name', 'age', 'email', 'phone']
student_database = 'students.csv'


def add_student(read_mode, var):
    print("-------------------------")
    print("Add Student Information")
    print("-------------------------")
    global student_fields
    global student_database

    student_data = []
    for field in range(0,len(student_fields)):
        if read_mode == 0:
            value = input("Enter "+ ": ")
        else:
            value = var[field]
        student_data.append(value)

    with open(student_database, "a", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([student_data])

    print("Data saved successfully")
    input("Press any key to continue")
    if read_mode == 0:
        return student_data[0]
    return var[0]
