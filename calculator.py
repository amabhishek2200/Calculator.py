# def calculator():
#      print("== Calculator ==")
#      print("Type 'exit to quit")

#      while True:
#           expr =input("Enetr expression:")
#           if expr.lower()=="exit":
#                print("Exiting Caluclator.")
#                break
          
#           try:
#                result=eval(expr,{"__bulitins__":None},{})
#                print("Result:",result)
#           except Exception as e:
#                print("Invaild input:",e)

# if __name__=="__main__":
#      calculator()

import tkinter as tk
from tkinter import messagebox

def click(btn_text):
    if btn_text == "=":
        try:
            result = eval(entry.get(), {"__builtins__": None}, {})
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception:
            messagebox.showerror("Error", "Invalid Expression")
    elif btn_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, btn_text)

# Window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

entry = tk.Entry(root, font=("Arial", 18), justify="right")
entry.pack(fill=tk.BOTH, padx=10, pady=10)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

frame = tk.Frame(root)
frame.pack()

row, col = 0, 0
for btn in buttons:
    b = tk.Button(frame, text=btn, width=5, height=2, font=("Arial", 14),
                  command=lambda x=btn: click(x))
    b.grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col == 4:
        col = 0
        row += 1

clear_btn = tk.Button(root, text="C", width=10, height=2, font=("Arial", 14),
                      command=lambda: click("C"))
clear_btn.pack(pady=10)

root.mainloop()
