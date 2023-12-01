import tkinter

FONT = ("Arial", 14, "bold")

window = tkinter.Tk()
window.title("Pound(lb) to Kg Converter")
# window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Entry
lb_input = tkinter.Entry(width=7, font=FONT)
lb_input.grid(column=1, row=0)

# Pounds
lb_label = tkinter.Label(text="pounds", font=FONT)
lb_label.grid(column=2, row=0)

# Is equal to
equal_label = tkinter.Label(text="is equal to", font=FONT)
equal_label.grid(column=0, row=1)

# Weight in Kg
weight = tkinter.Label(font=FONT)
weight.grid(column=1, row=1)

# Kg
kg = tkinter.Label(text="Kg", font=FONT)
kg.grid(column=2, row=1)

# Button


def calculate():
    weight_kg = float(lb_input.get()) * 0.453592
    weight.config(text=f'{weight_kg:.2f}')


button = tkinter.Button(text="Calculate", command=calculate, width=8, font=("Arial", 12, "bold"))
button.grid(column=1, row=2)

window.mainloop()
