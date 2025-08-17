# Student Database Management System

This project is a **Student Database Management System** built using **Python** and **MySQL**. It allows users to manage student data with basic operations like inserting, updating, deleting, and displaying student records.

## 🔌 Technologies Used

- **Python 3.x**
- **MySQL**
- **MySQL Connector for Python**

## 📚 Functionalities

The project provides the following core features:

### 1. `insert_Data()`
- Allows the user to insert a new student record.
- Inputs: name, age, email, gender, student ID, class.

### 2. `update_Data()`
- Lets the user update existing student information (name, age, email, etc.) based on the student ID.

### 3. `delete_Data()`
- Deletes a student record by student ID.

### 4. `structure_table()`
- Displays the structure (columns and types) of the `Students` table.

### 5. `show_data()`
- Displays all the student records from the table.

### 6. `show_tables()`
- Lists all tables in the connected database.

### 7. `create_table()`
- Creates the `Students` table if it doesn't already exist.

## 📌 Notes

- All functions are menu-driven and user-friendly.
- User input is taken via terminal and executed with live MySQL connection.

## 🛡 Safety Tip

> It's recommended to use **parameterized queries** for real-world applications to avoid SQL injection.
