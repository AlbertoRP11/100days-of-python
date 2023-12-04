import json
from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(6, 8)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def reset():
    website_entry.delete(0, END)
    password_entry.delete(0, END)
    website_entry.focus()


def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    new_data = {
        "Website": {
            "username": username,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open(file="data.json", mode="r") as file:
                # Reading old data
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as file:
                # Saving updated data
                json.dump(data, file, indent=4)
        finally:
            reset()

# ---------------------------- FIND PASSWORD ------------------------------- #


def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
    else:
        if website in data:
            username = data[website]["username"]
            password = data[website]["password"]
            msg = f"Username: {username}\nPassword: {password}"
            messagebox.showinfo(title=website, message=msg)
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:", bg="white", highlightthickness=0)
website_label.grid(row=1, column=0)
username_label = Label(text="Email/Username:", bg="white", highlightthickness=0)
username_label.grid(row=2, column=0)
password_label = Label(text="Password:", bg="white", highlightthickness=0)
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=20)
website_entry.grid(row=1, column=1)
website_entry.focus()

username_entry = Entry(width=39)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0, "alberto@email.com")

password_entry = Entry(width=20)
password_entry.grid(row=3, column=1)

# Buttons
search_button = Button(text="Search", width=15, bg="white", highlightthickness=0, command=find_password)
search_button.grid(row=1, column=2)

gen_password_button = Button(text="Generate Password", width=15, bg="white", highlightthickness=0, command=gen_password)
gen_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=25, bg="white", highlightthickness=0, command=save)
add_button.grid(row=4, column=1)

window.mainloop()
