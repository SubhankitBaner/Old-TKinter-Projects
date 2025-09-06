import tkinter as tk

def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                print(e)
                value = "Error"
        scvalue.set(value)
        screen.update()
    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = tk.Tk()
root.geometry("300x450")
root.title("Calculator by Subhankit")
root.wm_iconbitmap("2.ico")

scvalue = tk.StringVar()
scvalue.set("")
screen = tk.Entry(root, textvariable=scvalue, font="lucida 30 bold", bd=5, relief=tk.SUNKEN)
screen.pack(fill=tk.X, padx=10, pady=10, ipadx=8)

button_frame = tk.Frame(root, bg="grey")
button_frame.pack(padx=10, pady=10, fill='both', expand=True)

button_font = "lucida 20 bold"
padx_val = 10
pady_val = 10

btn_c = tk.Button(button_frame, text="C", font=button_font, padx=padx_val, pady=pady_val, bg="orange")
btn_c.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
btn_c.bind("<Button-1>", click)

btn_div = tk.Button(button_frame, text="/", font=button_font, padx=padx_val, pady=pady_val)
btn_div.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
btn_div.bind("<Button-1>", click)

btn_mul = tk.Button(button_frame, text="*", font=button_font, padx=padx_val, pady=pady_val)
btn_mul.grid(row=0, column=2, padx=5, pady=5, sticky="nsew")
btn_mul.bind("<Button-1>", click)

btn_sub = tk.Button(button_frame, text="-", font=button_font, padx=padx_val, pady=pady_val)
btn_sub.grid(row=0, column=3, padx=5, pady=5, sticky="nsew")
btn_sub.bind("<Button-1>", click)

btn_7 = tk.Button(button_frame, text="7", font=button_font, padx=padx_val, pady=pady_val)
btn_7.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
btn_7.bind("<Button-1>", click)

btn_8 = tk.Button(button_frame, text="8", font=button_font, padx=padx_val, pady=pady_val)
btn_8.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
btn_8.bind("<Button-1>", click)

btn_9 = tk.Button(button_frame, text="9", font=button_font, padx=padx_val, pady=pady_val)
btn_9.grid(row=1, column=2, padx=5, pady=5, sticky="nsew")
btn_9.bind("<Button-1>", click)

btn_add = tk.Button(button_frame, text="+", font=button_font, padx=padx_val, pady=pady_val)
btn_add.grid(row=1, column=3, rowspan=2, padx=5, pady=5, sticky="nsew")
btn_add.bind("<Button-1>", click)

btn_4 = tk.Button(button_frame, text="4", font=button_font, padx=padx_val, pady=pady_val)
btn_4.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
btn_4.bind("<Button-1>", click)

btn_5 = tk.Button(button_frame, text="5", font=button_font, padx=padx_val, pady=pady_val)
btn_5.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")
btn_5.bind("<Button-1>", click)

btn_6 = tk.Button(button_frame, text="6", font=button_font, padx=padx_val, pady=pady_val)
btn_6.grid(row=2, column=2, padx=5, pady=5, sticky="nsew")
btn_6.bind("<Button-1>", click)

btn_1 = tk.Button(button_frame, text="1", font=button_font, padx=padx_val, pady=pady_val)
btn_1.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")
btn_1.bind("<Button-1>", click)

btn_2 = tk.Button(button_frame, text="2", font=button_font, padx=padx_val, pady=pady_val)
btn_2.grid(row=3, column=1, padx=5, pady=5, sticky="nsew")
btn_2.bind("<Button-1>", click)

btn_3 = tk.Button(button_frame, text="3", font=button_font, padx=padx_val, pady=pady_val)
btn_3.grid(row=3, column=2, padx=5, pady=5, sticky="nsew")
btn_3.bind("<Button-1>", click)

btn_eq = tk.Button(button_frame, text="=", font=button_font, padx=padx_val, pady=pady_val, bg="lightgreen")
btn_eq.grid(row=3, column=3, rowspan=2, padx=5, pady=5, sticky="nsew")
btn_eq.bind("<Button-1>", click)

btn_0 = tk.Button(button_frame, text="0", font=button_font, padx=padx_val, pady=pady_val)
btn_0.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
btn_0.bind("<Button-1>", click)

btn_dot = tk.Button(button_frame, text=".", font=button_font, padx=padx_val, pady=pady_val)
btn_dot.grid(row=4, column=2, padx=5, pady=5, sticky="nsew")
btn_dot.bind("<Button-1>", click)

for i in range(4):
    button_frame.grid_columnconfigure(i, weight=1)
for i in range(5):
    button_frame.grid_rowconfigure(i, weight=1)

root.mainloop()
