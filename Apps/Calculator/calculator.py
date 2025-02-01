import tkinter as tk

def on_click(button_text):
    if button_text == "C":
        entry_var.set("")
    elif button_text == "←":
        entry_var.set(entry_var.get()[:-1])
    elif button_text == "=":
        try:
            result = eval(entry_var.get())
            entry_var.set(result)
        except Exception:
            entry_var.set("Error")
    else:
        entry_var.set(entry_var.get() + button_text)

def create_button(root, text, row, column):
    return tk.Button(root, text=text, font=("Arial", 20), command=lambda: on_click(text))\
        .grid(row=row, column=column, sticky="nsew", padx=5, pady=5)

root = tk.Tk()
root.title("Calculator")
root.geometry("400x500")

tk.Grid.columnconfigure(root, 0, weight=1)
tk.Grid.rowconfigure(root, 0, weight=1)

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 24), justify='right', bd=10, relief=tk.RIDGE)
entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

buttons = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("C", "0", "=", "+"),
    ("←",)
]

for r, row in enumerate(buttons, start=1):
    for c, text in enumerate(row):
        create_button(root, text, r, c)
        tk.Grid.columnconfigure(root, c, weight=1)
    tk.Grid.rowconfigure(root, r, weight=1)

root.mainloop()
