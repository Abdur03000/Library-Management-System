from views.student import StudentOperations
from views.book import BookOperations
from views.order import OrderOperations
from Database.Config import db
from models.student import Student
from models.book import Book
from models.order import Order

class LibrarySystem:
    def __init__(self):
        self.initialize()
        self.student_ops = StudentOperations()
        self.book_ops = BookOperations()
        self.order_ops = OrderOperations()

    def initialize(self):
        db.connect()
        db.create_tables([Student, Book, Order], safe=True)
        db.close()

    def display_menu(self):
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

    def process_choice(self, choice):
        if choice == "1":
            self.student_ops.registered_student()
        elif choice == "2":
            self.order_ops.create_order()
        elif choice == "3":
            self.book_ops.add_book()
        elif choice == "4":
            self.order_ops.return_book()
        elif choice == "5":
            self.student_ops.display_students()
        elif choice == "6":
            self.book_ops.display_books()
        elif choice == "7":
            self.order_ops.display_orders()
        elif choice == "8":
            self.student_ops.edit_student()
        elif choice == "9":
            self.book_ops.edit_book()
        elif choice == "10":
            self.book_ops.delete_book()
        elif choice == "11":
            self.student_ops.delete_student()
        elif choice == "12":
            print("Closing the Library System! Goodbye")
            return True
        else:
            print("Invalid choice. Please try again.")
        return True

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if not self.process_choice(choice):
                break


library_system = LibrarySystem()
library_system.run()
