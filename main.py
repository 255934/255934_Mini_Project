import csv
from disp_menu import display_menu
from add import add_student
from view import view_students
from search import search_student
from update import update_student
from delete import delete_student

student_fields = ['roll', 'name', 'age', 'email', 'phone']
student_database = 'students.csv'
while True:
    display_menu()

    choice = input("Enter your choice: ")
    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        update_student()
    elif choice == '5':
        delete_student()
    else:
        break
