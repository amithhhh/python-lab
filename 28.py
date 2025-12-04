from tkinter import *

def do_sum():
    n1 = float(entry1.get())
    n2 = float(entry2.get())
    result_entry.delete(0, END)
    result_entry.insert(0, n1 + n2)

def do_diff():
    n1 = float(entry1.get())
    n2 = float(entry2.get())
    result_entry.delete(0, END)
    result_entry.insert(0, n1 - n2)

def do_prod():
    n1 = float(entry1.get())
    n2 = float(entry2.get())
    result_entry.delete(0, END)
    result_entry.insert(0, n1 * n2)

def do_quot():
    n1 = float(entry1.get())
    n2 = float(entry2.get())
    result_entry.delete(0, END)
    if n2 != 0:
        result_entry.insert(0, n1 / n2)
    else:
        result_entry.insert(0, "Error: Divide by 0")

root = Tk()
root.title("Arithmetic Operations")

Label(root, text="Enter Number 1:").grid(row=0, column=0, padx=5, pady=5)
entry1 = Entry(root)
entry1.grid(row=0, column=1)

Label(root, text="Enter Number 2:").grid(row=1, column=0, padx=5, pady=5)
entry2 = Entry(root)
entry2.grid(row=1, column=1)

Button(root, text="Sum", command=do_sum).grid(row=2, column=0, padx=5, pady=5)
Button(root, text="Difference", command=do_diff).grid(row=2, column=1, padx=5, pady=5)
Button(root, text="Product", command=do_prod).grid(row=3, column=0, padx=5, pady=5)
Button(root, text="Quotient", command=do_quot).grid(row=3, column=1, padx=5, pady=5)

Label(root, text="Result:").grid(row=4, column=0, padx=5, pady=10)
result_entry = Entry(root, width=20)
result_entry.grid(row=4, column=1)

root.mainloop()
