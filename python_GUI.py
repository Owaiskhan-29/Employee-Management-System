
import tkinter as tk
from tkinter import messagebox
from python_emoloyee import Management, Employee  


manager = Management()

def add_employee_gui():
    emp_id = entry_id.get()
    name = entry_name.get()
    age = entry_age.get()
    salary = entry_salary.get()

    if emp_id and name and age and salary:
        emp_id = int(emp_id)
        age = int(age)
        salary = float(salary)
        emp = Employee(emp_id, name, age, salary)
        manager.add_employee(emp)
        messagebox.showinfo("Success", f"Employee {name} added successfully.")
        display_employees_gui()
    else:
        messagebox.showwarning("Input Error", "Please fill all fields.")


def remove_employee_gui():
    emp_id = entry_id.get()
    if emp_id:
        emp_id = int(emp_id)
        manager.remove_employee(emp_id)
        messagebox.showinfo("Success", f"Employee with ID {emp_id} removed successfully.")
        display_employees_gui()
    else:
        messagebox.showwarning("Input Error", "Please provide the employee ID.")


def promote_employee_gui():
    emp_id = entry_id.get()
    new_position = entry_position.get()

    if emp_id and new_position:
        emp_id = int(emp_id)
        manager.promote_employee(emp_id, new_position)
        messagebox.showinfo("Success", f"Employee with ID {emp_id} promoted to {new_position}.")
        display_employees_gui()
    else:
        messagebox.showwarning("Input Error", "Please provide the employee ID and new position.")

def display_employees_gui():
    employee_list = manager.display_employees()
    listbox_employees.delete(0, tk.END)  
    listbox_employees.insert(tk.END, employee_list)


root = tk.Tk()
root.title("Employee Management System")

label_id = tk.Label(root, text="Employee ID:")
label_id.pack()
entry_id = tk.Entry(root)
entry_id.pack()

label_name = tk.Label(root, text="Name:")
label_name.pack()
entry_name = tk.Entry(root)
entry_name.pack()

label_age = tk.Label(root, text="Age:")
label_age.pack()
entry_age = tk.Entry(root)
entry_age.pack()

label_salary = tk.Label(root, text="Salary:")
label_salary.pack()
entry_salary = tk.Entry(root)
entry_salary.pack()

label_position = tk.Label(root, text="New Position (for Promotion):")
label_position.pack()
entry_position = tk.Entry(root)
entry_position.pack()

button_add = tk.Button(root, text="Add Employee", command=add_employee_gui)
button_add.pack()

button_remove = tk.Button(root, text="Remove Employee", command=remove_employee_gui)
button_remove.pack()

button_promote = tk.Button(root, text="Promote Employee", command=promote_employee_gui)
button_promote.pack()

button_display = tk.Button(root, text="Display Employees", command=display_employees_gui)
button_display.pack()

listbox_employees = tk.Listbox(root, width=50, height=10)
listbox_employees.pack()

root.mainloop()
