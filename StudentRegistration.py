# StudentRegistration.py
# This program processes student details to register them into courses.
# Displays this information onto the screen.
# Author: Kazusa Naoi
# Date: 24/10/2023

# Importing tkinter and its submodules simpledialog and messagebox
import tkinter as tk
from tkinter import simpledialog, messagebox

# Creating a new window
window = tk.Tk()
# Hiding the window
window.withdraw()

# Creating an empty list for storing student data
students = []
# Variable to store the total fees
totalFees = 0

# Function to print the headers
def printHeadings():
  # All headings as a string, ljust adds spaces at the end to align all headings
  heading = "---HOLMESGLEN INSTITUTE---\n" + \
        'ID'.ljust(10) + 'NAME'.ljust(10) + 'COURSE'.ljust(10) + 'FEE'.ljust(10)
  return heading

# Function to output total fees
def outputTotalFee():
  return "Total Fees for all students: $" + str(totalFees)

# Function to input details of a student
def inputStudentDetails():
  global totalFees
  # Asking for ID and storing the result in id, passing parent=window so that dialog pops over the app window
  id = simpledialog.askstring("Input", "Input ID:", parent=window)
  if id is None:
    return None
  # Same with other details like name, course, and fee
  name = simpledialog.askstring("Input", "Input Name:", parent=window)
  if name is None:
    return None
  course = simpledialog.askstring("Input", "Input Course:", parent=window)
  if course is None:
    return None
  fee = simpledialog.askinteger(
      "Input", "Input Fee:", parent=window, minvalue=0, maxvalue=100000)
  if fee is None:
    return None
  # Adding the fee to total fees
  totalFees += fee

  # Appending the student info to the student list
  students.append({'id': id, 'name': name, 'course': course, 'fee': fee})

  # If we have details of 3 students
  if len(students) >= 3:
    # Formatting the data for each student
    student_details = "\n".join(f"{student['id']:<10}{student['name']:<10}{student['course']:<10}{student['fee']:<10}" for student in students)
    
    # Creating a new window to display details
    detailWindow = tk.Toplevel(window)
    detailWindow.geometry("500x500")
    # Formatting all the details into a single string and displaying it in a Label widget
    details = printHeadings() + "\n" + student_details + "\n" + outputTotalFee()
    tk.Label(detailWindow, text=details, justify='left', anchor='w').pack()
  else:
    # If we don't have details of 3 students, we call inputStudentDetails again
    return inputStudentDetails()
  
# Call the function to display the dialog
inputStudentDetails()

# Start the TK main event loop to keep the application opening
tk.mainloop()