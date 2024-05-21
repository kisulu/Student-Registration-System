from tkinter import *
from tkinter import messagebox
import mysql.connector

background = "#06283d"
frame_bg = "#EDEDED"
frame_fg = "#06283D"

global trial_no
trial_no = 0

def trial():
    global trial_no
    trial_no += 1
    print("trial number is ", trial_no)
    if trial_no == 3:
        messagebox.showwarning("Warning", "you have tried more than the limit!!")
        root.destroy()
    

def login_user():
    username = user.get()
    password = code.get()

    # print(username, password)
    if (username == "" or username == "UserID") or (password == "" or password == "Password"):
        messagebox.showerror("Entry Error", "Type username or password!!!")
    else:
        try:
            # pass
            db = mysql.connector.connect(host="localhost", user="root", password="BENEDICT@1234", database="student_registration")
            my_cursor = db.cursor()
            print("Connected to Database Successfully!!")

        except:
            # pass
            messagebox.showerror("Connection", "Database connection not established")
            return
        command = "use student_registration"
        my_cursor.execute(command)

        command = "select * from login where Username=%s and Password=%s"
        my_cursor.execute(command, (username, password))
        my_result = my_cursor.fetchone()
        print(my_result)

        if my_result == None:
            
            messagebox.showinfo("Invalid", "Invalid userid and password!!")

            # but user can try many times and crack password so lets make that user try up to 3 times only
            trial()

        else:
            messagebox.showinfo("Login", "login successfully!")
            root.destroy()
            import main


def register():
    root.destroy()
    import register


root = Tk()
root.title("Login System")
root.geometry("1000x560+210+100")
root.config(bg=background)
root.resizable(False, False)

# icon_image
image_icon = PhotoImage(file="Images/icon.png")
root.iconphoto(False, image_icon)


# background image
frame = Frame(root, bg="red")
frame.pack(fill=Y)
background_image = PhotoImage(file="Images/login.png")
Label(frame, image=background_image).pack()

# delete userid when you enter the text area


def user_enter(e):
    user.delete(0, 'end')


def user_leave(e):
    name = user.get()
    if name == "":
        user.insert(0, 'UserID')


user = Entry(frame, width=14, fg="white", border=0, bg="#375174", font=("arial bold", 24))
user.insert(0, "UserID")
user.bind("<FocusIn>", user_enter)
user.bind("<FocusOut>", user_leave)
user.place(x=395, y=245)


def password_enter(e):
    code.delete(0, 'end')


def password_leave(e):
    if code.get() == "":
        code.insert(0, 'Password')


code = Entry(frame, width=14, fg="white", border=0, bg="#375174", font=("arial bold", 24))
code.insert(0, "Password")
code.bind("<FocusIn>", password_enter)
code.bind("<FocusOut>", password_leave)
code.place(x=395, y=325)

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
eyeButton.place(x=615, y=325)
##############################

loginButton = Button(root, text="LOGIN", bg="#1f5675", fg="white", width=10, height=1, font=("arial bold", 16), command=login_user)
loginButton.place(x=430, y=480)

label = Label(root, text="Don't have an account?", bg="#00264d", fg="white", font=("Microsoft YaHei UI Light", 9))
label.place(x=370, y=400)

registerButton = Button(root, text="add new user", bg="#00264d", fg="#57a1f8", border=0, width=10, command=register)
registerButton.place(x=520, y=400)

root.mainloop()
