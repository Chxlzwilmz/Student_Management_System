import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root", 
    password="MySQL", 
    database="std_db"
)
cursor = conn.cursor()

# Function to add a student
def add_student(name, age, course):
    sql = "INSERT INTO students (name, age, course) VALUES ("Charles", 20,"BCA")"
    values = (name, age, course)
    cursor.execute(sql, values)
    conn.commit()
    print("Student added successfully!")

# Function to view students
def view_students():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    for student in students:
        print(student)

# Function to update a student
def update_student(student_id, name, age, course):
    sql = "UPDATE students SET name = "Karthik", age = 21, course = "IT" WHERE id = 7"
    values = (name, age, course, student_id)
    cursor.execute(sql, values)
    conn.commit()
    print("Student updated successfully!")

# Function to delete a student
def delete_student(student_id):
    sql = "DELETE FROM students WHERE id = %s"
    cursor.execute(sql, (student_id,))
    conn.commit()
    print("Student deleted successfully!")

# for menu program
while True:
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        course = input("Enter course: ")
        add_student(name, age, course)
    
    elif choice == "2":
        view_students()
    
    elif choice == "3":
        student_id = int(input("Enter student ID to update: "))
        name = input("Enter new name: ")
        age = int(input("Enter new age: "))
        course = input("Enter new course: ")
        update_student(student_id, name, age, course)
    
    elif choice == "4":
        student_id = int(input("Enter student ID to delete: "))
        delete_student(student_id)
    
    elif choice == "5":
        print("Exiting program...")
        break
    
    else:
        print("Invalid choice! Please try again.")

# Close the database connection
cursor.close()
conn.close()
