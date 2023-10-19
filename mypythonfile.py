# StudentRegistration.py
# This program processes student details to register them into courses and then
# displays this information onto the screen.
# Author: Your Name Here
# Date: Today's Date

import tkinter as tk
from tkinter import messagebox

students = [] # Initialize students list
totalFees = 0 # Initialize totalFees variable

def printHeadings():
    messagebox.showinfo("Headings", 'ID' + '\t' + 'NAME' + '\t' + 'COURSE' + '\t' + 'FEE')

def printStudentDetails(student): # Function to print student details
    student_info = f"ID: {student['id']}\nName: {student['name']}\nCourse: {student['course']}\nFee: ${student['fee']}"
    messagebox.showinfo("Student Details", student_info)

def inputStudentDetails():
    global totalFees
    id = idEntry.get()
    name = nameEntry.get()
    course = courseEntry.get()
    fee = int(feeEntry.get())

    totalFees += fee # Add the fee to the total fees
    students.append({'id': id, 'name': name, 'course': course, 'fee': fee})

def outputStudentDetails():
    if students:
        for student in students:
            printStudentDetails(student)
            
def outputTotalFee(): # Function to output total Fees
    messagebox.showinfo("Total Fees", "\nTotal Fees for all students: $" + str(totalFees))

def submitDetails():
    inputStudentDetails()
    outputStudentDetails()
    outputTotalFee()

# Create a Tkinter window
window = tk.Tk()

tk.Label(window, text="ID").grid(row=0)
tk.Label(window, text="Name").grid(row=1)
tk.Label(window, text="Course").grid(row=2)
tk.Label(window, text="Fee").grid(row=3)

idEntry = tk.Entry(window)
idEntry.grid(row=0, column=1)

nameEntry = tk.Entry(window)
nameEntry.grid(row=1, column=1)

courseEntry = tk.Entry(window)
courseEntry.grid(row=2, column=1)

feeEntry = tk.Entry(window)
feeEntry.grid(row=3, column=1)

tk.Button(window, text='Submit', command=submitDetails).grid(row=4, column=1)

window.mainloop()