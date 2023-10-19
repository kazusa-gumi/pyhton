import tkinter as tk
from tkinter import messagebox

students = []
totalFees = 0

def printHeadings():
    heading = 'ID'.ljust(10) + 'NAME'.ljust(10) + 'COURSE'.ljust(10) + 'FEE'.ljust(10)
    return heading

def printStudentDetails(student):
    student_info = f"{student['id']:<10}{student['name']:<10}{student['course']:<10}{student['fee']:<10}"
    return student_info

def inputStudentDetails():
    global totalFees
    if len(students) >= 3:
        messagebox.showerror("Error", "You can't register more than 3 students.")
        return
    id = idEntry.get()
    name = nameEntry.get()
    course = courseEntry.get()
    fee = int(feeEntry.get())

    totalFees += fee
    students.append({'id': id, 'name': name, 'course': course, 'fee': fee})
    idEntry.delete(0, tk.END)
    nameEntry.delete(0, tk.END)
    courseEntry.delete(0, tk.END)
    feeEntry.delete(0, tk.END)

    if len(students) == 3:
        submitDetails()

def outputStudentDetails():
    all_students = ''
    for student in students:
        all_students += printStudentDetails(student) + '\n'
    return all_students

def outputTotalFee():
    return "\nTotal Fees for all students: $" + str(totalFees)

def submitDetails():
    detail = printHeadings() + '\n' + outputStudentDetails() + outputTotalFee()
    showDetailWindow(detail)

def showDetailWindow(details):
    detailWindow = tk.Toplevel(window)
    detailWindow.geometry("500x500")
    tk.Label(detailWindow, text=details, justify='left').pack()

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

tk.Button(window, text='Submit', command=inputStudentDetails).grid(row=4, column=1)

window.mainloop()