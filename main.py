
from disp_menu import display_menu
from add import add_student
from view import view_students
from search import search_student
from update import update_student
from delete import delete_student


while True:
    display_menu()

    choice = input("Enter your choice: ")
    if choice == '1':
        add_student(0, [])
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        update_student(0, [])
    elif choice == '5':
        delete_student()
    else:
        break
