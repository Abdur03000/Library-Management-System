from views.student import StudentOperations
from views.book import BookOperations
from views.order import OrderOperations
from Database.Config import db
from models.student import Student
from models.book import Book
from models.order import Order

def initialize():
    db.connect()
    db.create_tables([Student, Book, Order], safe=True)
    db.close()

def main():
    initialize()

    student_ops = StudentOperations()
    book_ops = BookOperations()
    order_ops = OrderOperations()

    while True:
        print("= Library Management System =")
        print("1. Create Student")
        print("2. Create Order")
        print("3. Create Book")
        print("4. Return Book")
        print("5. Display Students")
        print("6. Display Books")
        print("7. Display Orders")
        print("8. Edit Student")
        print("9. Edit Book")
        print("10. Delete Book")
        print("11. Delete Student")
        print("12. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            student_ops.registered_student()
        elif choice == "2":
            order_ops.create_order()
        elif choice == "3":
            book_ops.add_book()
        elif choice == "4":
            order_ops.return_book()
        elif choice == "5":
            student_ops.display_students()
        elif choice == "6":
            book_ops.display_books()
        elif choice == "7":
            order_ops.display_orders()
        elif choice == "8":
            student_ops.edit_student()
        elif choice == "9":
            book_ops.edit_book()
        elif choice == "10":
            book_ops.delete_book()
        elif choice == "11":
            student_ops.delete_student()
        elif choice == "12":
            print("Closing the Library System! Goodbye")
            break
        else:
            print("Invalid choice. Please try again.")


main()
