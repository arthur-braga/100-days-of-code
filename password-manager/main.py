from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

FONT = ("Arial", 10, "normal")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    list_letters = [choice(letters) for _ in range(randint(8, 10))]
    list_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    list_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = list_letters + list_symbols + list_numbers

    shuffle(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, f"{''.join(password_list)}")
    pyperclip.copy(''.join(password_list))
    password_list.clear()


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_entry():
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()

    if website != "" and email != "" and password != "":
        is_ok = messagebox.askokcancel(title="Confirm",
                               message=f"These are the details entered: \nEmail: {email}\nPassword: {password}\n"
                                       f"Is it ok to save?")

        if is_ok:
            with open("data.txt", "a") as file:
                content = f"{website} | {email} | {password}\n"
                file.write(content)
            website_entry.delete(0, END)
            password_entry.delete(0, END)

            messagebox.showinfo(title="Success", message="Password saved!")

        else:
            messagebox.showinfo(title="Continue", message="Please try again.")
            password_entry.delete(0, END)
    else:
        messagebox.showinfo(title="Ooops", message="Please don't leave any fields empty!")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
mypass_lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=mypass_lock_img)
canvas.grid(row=0, column=1)

website_label = Label(window, text="Website:", fg="black", bg="white", font=FONT)
website_label.grid(row=1, column=0)

website_entry = Entry(width=42)
website_entry.grid(row=1, column=1, columnspan=2, sticky=W)
website_entry.focus()

email_username_label = Label(window, text="Email/Username:", fg="black", bg="white", font=FONT)
email_username_label.grid(row=2, column=0)

email_username_entry = Entry(width=42)
email_username_entry.grid(row=2, column=1, columnspan=2, sticky=W)
email_username_entry.insert(0, "arthur.m.braga@hotmail.com")

password_label = Label(window, text="Password:", fg="black", bg="white", font=FONT)
password_label.grid(row=3, column=0)

password_entry = Entry(width=25)
password_entry.grid(row=3, column=1, sticky=W)

add_button = Button()
add_button.config(text="Add", width=45, fg="black", bg="white", font=FONT, command=save_entry)
add_button.grid(row=4, column=1, columnspan=2, sticky=W)

generate_pass_button = Button()
generate_pass_button.config(text="Generate Password", fg="black", bg="white", font=FONT, command=generate_password)
generate_pass_button.grid(row=3, column=2, sticky=W)


window.mainloop()