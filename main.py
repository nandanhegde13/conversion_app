from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from symbols import dic
from temperature import temp


def comboclick(event):
    combo_home.get()


def comboclick1(event):
    combo_for.get()


def convert():
    key = combo_for.get()

    try:
        value = float(rate_entry.get())
        amount = float(amount_entry.get())
        result = float(value * amount)
        symbol = dic.get(key)
        if output.get() is None:
            output.insert(0, f'{symbol}{result}')
        else:
            output.delete(0, END)
            output.insert(0, f'{symbol}{result}')

    except ValueError:
        messagebox.showwarning("WARNING!", "Please enter valid number")


def temp1(event):
    combo_from.get()


def temp2(event):
    combo_to.get()


def converter():
    from_value = combo_from.get()
    to_value = combo_to.get()
    temp_value = int(amount.get())

    obj1 = temp(from_value, to_value, temp_value)
    final_result = obj1.get_unit()
    result_value = result.get()
    if result_value is None:
        result.insert(0,final_result)
    else:
        result.delete(0, END)
        result.insert(0,final_result)


# ---------------------------------- GUI SETUP---------------------------------------
root = Tk()
root.geometry("600x600")
root.title("CONVERSION APP")
root.geometry()
notebook = ttk.Notebook(root, width=580, height=580)
notebook.pack(pady=15)

window1 = Frame(notebook, width=500, height=500, borderwidth=5, highlightthickness=2, relief="raised", bg="lightgray")
window2 = Frame(notebook, width=500, height=500, borderwidth=5, highlightthickness=2, relief="raised", bg="lightgray")

window1.pack(pady=10, padx=10)
window2.pack(pady=10, padx=10)

notebook.add(window1, text="Currency")
notebook.add(window2, text="Temperature")

# -------------------currency window-------------------

heading1 = Label(window1, text="Currency Converter", font=("bold", 20), fg="blue", bg="lightgray")
heading1.pack(pady=10)

# drop down
selected = StringVar()
option_list = []

for key in dic:
    option_list.append(key)
    option_list.sort()
home_label = LabelFrame(window1, text="Select home currency", borderwidth=2, relief="raised", bg="lightgray")
home_label.pack()

# dropdown = OptionMenu(home_label, selected, *option_list)
# dropdown.pack()

# getting selected value inside combobox

combo_home = ttk.Combobox(home_label, value=option_list, width=40)
combo_home.current(37)
combo_home.bind("<<ComboboxSelected>>", comboclick)
combo_home.pack(pady=10, padx=10)

convert_label = LabelFrame(window1, text="Select foreign currency ", borderwidth=2, relief="raised", bg="lightgray")
convert_label.pack(pady=15)

combo_for = ttk.Combobox(convert_label, value=option_list, width=40)
combo_for.current(37)
combo_for.bind("<<ComboboxSelected>>", comboclick1)
combo_for.config()
combo_for.pack(padx=10, pady=10)

rate_label = LabelFrame(window1, text="Enter conversion rate", borderwidth=2, relief="raised", bg="lightgray")
rate_label.pack(pady=15)

rate_entry = Entry(rate_label, width=43)
rate_entry.pack(padx=10, pady=10)

amount_label = LabelFrame(window1, text="Enter amount to be converted", borderwidth=2, relief="raised", bg="lightgray")
amount_label.pack(pady=15)

amount_entry = Entry(amount_label, width=45)
amount_entry.pack(padx=10, pady=10)

button = Button(window1, text="convert", command=convert, bg="lightgray")
button.pack(pady=10)

output_label = LabelFrame(window1, text="Converted rate", borderwidth=2, relief="raised", bg="lightgray")
output_label.pack()

output = Entry(output_label, width=45)
output.pack(padx=10, pady=10)

# --------------------------temperature window--------------------------------------


heading = Label(window2, text="Temperature Converter", bg="lightgray", fg="blue", font=("bold", 20))
heading.pack()

temp_option = ["Celsius", "Kelvin", "Fahrenheit"]

from_label = LabelFrame(window2, text="temperature to be converted", borderwidth=2, relief="raised", bg="lightgray")
from_label.pack(pady=10)

combo_from = ttk.Combobox(from_label, value=temp_option, width=40)
combo_from.current(0)
combo_from.bind("<<ComboboxSelected>>", temp1)
combo_from.pack(padx=10, pady=10)

to_label = LabelFrame(window2, text="temperature to convert", borderwidth=2, relief="raised", bg="lightgray")
to_label.pack(pady=10)

combo_to = ttk.Combobox(to_label, value=temp_option, width=40)
combo_to.current(0)
combo_to.bind("<<ComboboxSelected>>", temp2)
combo_to.pack(padx=10, pady=10)

entry_label = LabelFrame(window2, text="Temperature", width=40, borderwidth=2, relief="raised", bg="lightgray")
entry_label.pack(padx=10, pady=10)

amount = Entry(entry_label, width=44)
amount.pack(padx=10, pady=10)

temp_convert = Button(window2, text="convert", bg="lightgray", command=converter)
temp_convert.pack()

result_label = LabelFrame(window2, text="result", width=40, borderwidth=2, relief="raised", bg="lightgray")
result_label.pack(padx=10, pady=10)

result = Entry(result_label, width=44)
result.pack(padx=10, pady=10)

root.mainloop()
