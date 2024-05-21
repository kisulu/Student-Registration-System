from tkinter import *
from tkinter import messagebox
import mysql.connector

background = "#06283d"
frame_bg = "#EDEDED"
frame_fg = "#06283D"

root = Tk()
root.title("New User Registration")
root.geometry("720x410+210+100")
root.config(bg=background)
root.resizable(False, False)


def register():
    username = user.get()
    password = code.get()
    admin_code = admin_access.get()

#   print(username, password, admin_code) always check once to confirm its working
    if admin_code == "9995":
        if (username == "" or username == "UserID") or (password == "" or password == "Password"):
            messagebox.showerror("Entry Error", "Type username or password!!!")

        else:
            try:
                # pass
                db = mysql.connector.connect(host="localhost", user="root", password="BENEDICT@1234")
                my_cursor = db.cursor()
                print("Connected to Database Successfully!!")

            except:
                # pass
                messagebox.showerror("Connection", "Database connection not established")
                return

            try:
                command = "create database student_registration"
                my_cursor.execute(command)

                command = "use student_registration"
                my_cursor.execute(command)

                command = ("create table login (user int auto_increment key not null, username varchar(50)"
                           ", password varchar(100))")
                my_cursor.execute(command)

            except:
                command = "use student_registration"
                db = mysql.connector.connect(host="localhost", user="root", password="BENEDICT@1234", database="student_registration")
                my_cursor = db.cursor()
                my_cursor.execute(command)

                command = "insert into login(username, password) values(%s, %s)"
                my_cursor.execute(command, (username, password))
                db.commit()
                db.close()
                messagebox.showinfo("Register", "New user added successfully!!")


    else:
        messagebox.showerror("Admin code!!", "Input correct admin code to add new user!")


def login():
    root.destroy()
    import login


# icon_image
image_icon = PhotoImage(file="Images/icon.png")
root.iconphoto(False, image_icon)

# background image
frame = Frame(root, bg="red")
frame.pack(fill=Y)
background_image = PhotoImage(file="Images/register.png")
Label(frame, image=background_image).pack()

admin_access = Entry(frame, width=10, fg="#000", border=0, bg="#e8ecf7", font=("arial bold", 20))
admin_access.focus()
admin_access.config(show="*")
admin_access.place(x=310, y=160)


# delete userid when you enter the text area
def user_enter(e):
    user.delete(0, 'end')


def user_leave(e):
    name = user.get()
    if name == "":
        user.insert(0, 'UserID')


user = Entry(frame, width=12, fg="white", border=0, bg="#375174", font=("arial bold", 20))
user.insert(0, "UserID")
user.bind("<FocusIn>", user_enter)
user.bind("<FocusOut>", user_leave)
user.place(x=285, y=215)


def password_enter(e):
    code.delete(0, 'end')


def password_leave(e):
    if code.get() == "":
        code.insert(0, 'Password')


code = Entry(frame, width=12, fg="white", border=0, bg="#375174", font=("arial bold", 20))
code.insert(0, "Password")
code.bind("<FocusIn>", password_enter)
code.bind("<FocusOut>", password_leave)
code.place(x=285, y=268)


# ######### Hide and Show Button
button_mode = True


def hide():
    global button_mode
    if button_mode:
        eyeButton.config(image=close_eye, activebackground="white")
        code.config(show="*")
        button_mode = False
    else:
        eyeButton.config(image=open_eye, activebackground="white")
        code.config(show="")
        button_mode = True


open_eye = PhotoImage(file="Images/open_eye.png")
close_eye = PhotoImage(file="Images/close_eye.png")

eyeButton = Button(frame, image=open_eye, bg="#375174", bd=0, command=hide)
eyeButton.place(x=440, y=268)
##############################

regisButton = Button(root, text="ADD NEW USER", bg="#455C88", fg="white", width=12, height=1, font=("arial bold", 14),
                     command=register)
regisButton.place(x=285, y=345)

back_button = PhotoImage(file="Images/back_button.png")
back_Button = Button(root, image=back_button, fg="#deeefb", command=login)
back_Button.place(x=20, y=15)

root.mainloop()
