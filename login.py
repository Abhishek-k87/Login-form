from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector


def main():
    win = Tk()
    app = login_window(win)
    win.mainloop()


class login_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Page")
        self.root.geometry("1550x800+0+0")
        self.bg = ImageTk.PhotoImage(
            file="wallpaperflare.com_wallpaper (4).jpg")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, width=1300, height=700)
        frame = Frame(self.root, bg="white")
        frame.place(x=510, y=170, width=240, height=350)
        img1 = Image.open(
            "pngtree.jpg")
        img1 = img1.resize((150, 150), Image.Resampling.HAMMING)
        self.Photoimage1 = ImageTk.PhotoImage(img1)
        lblimage1 = Label(image=self.Photoimage1, bg="white", borderwidth=0)
        lblimage1.place(x=580, y=170, width=100, height=100)
        get_str = Label(frame, text="Get Started", font=(
            "times new roman", 18, "bold"), fg="black", bg="White")
        get_str.place(x=59, y=95)
        user_name = lbl = Label(frame, text="Username", font=(
            "times new roman", 10, "bold"), fg="black", bg="white")
        user_name.place(x=30, y=140)
        self.txtuser = ttk.Entry(frame, font=("times new roman", 10, "bold"))
        self.txtuser.place(x=30, y=160, width=200)
        password = lbl = Label(frame, text="Password", font=(
            "times new roman", 10, "bold"), fg="black", bg="white")
        password.place(x=30, y=190)
        self.txtpass = ttk.Entry(frame, font=("times new roman", 10, "bold"))
        self.txtpass.place(x=30, y=210, width=200)
        loginbtn = Button(frame, command=self.login, text="Login", font=(
            "times new roman", 15, "bold"), bd=3, relief=RIDGE, fg="white", bg="red", activeforeground="white", activebackground="red")
        loginbtn.place(x=70, y=250, width=100, height=30)
        regbtn = Button(frame, text="New user Register", command=self.register_window, font=("times new roman", 10, "bold"),
                        borderwidth=0, fg="black", bg="white", activeforeground="black", activebackground="white")
        regbtn.place(x=15, y=282, width=110, height=20)
        forgetpass = Button(frame, text="Forget Password", command=self.forget_password_window, font=("times new roman", 10, "bold"),
                            borderwidth=0, fg="black", bg="white", activeforeground="black", activebackground="white")
        forgetpass.place(x=10, y=300, width=110, height=20)

    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = register(self.new_window)

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror(
                "Error", "Please fill all the fields", parent=self.root)
        elif self.txtuser.get() == "Abhi" and self.txtpass.get() == "Abhi@":
            messagebox.showinfo("Success", "Welcome Abhi", parent=self.root)
        else:
            conn = mysql.connector.connect(
                host="localhost", user="root", password="Abhi@8797", database="db")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s", (
                self.txtuser.get(),
                self.txtpass.get()
            ))
            row = my_cursor.fetchone()

            if row == None:
                messagebox.showerror("Error", "Invalid user name and password")
            else:
                open_main = messagebox.askyesno("yesno", "Access only admin")
                if open_main > 0:
                    # self.new_window = Toplevel(self.new_window)
                    import snake
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()
# ==================reset password=================

    def reset_pass(self):
        if self.combo_securty.get() == "select":
            messagebox.showerror(
                "Error", "select the security question", parent=self.root2)
        elif self.Securty_ans.get() == "":

            messagebox.showerror(
                "Error", "please entre your answer", parent=self.root2)
        elif self.txt_newpass.get() == "":

            messagebox.showerror(
                "Error", "please entre your new password", parent=self.root2)
        else:
            conn = mysql.connector.connect(
                host="localhost", user="root", password="Abhi@8797", database="db")
            my_cursor = conn.cursor()
            query = (
                "select *from register where email=%s and securityQuestion=%s and SecurityAnswer=%s")
            value = (self.txtuser.get(),
                     self.combo_securty.get(), self.Securty_ans.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror(
                    "Error", "Please enter the correct answer", parent=self.root2)
            else:
                query = ("update register set password=%s where email=%s")
                value = (self.txt_newpass.get(), self.txtuser.get())
                my_cursor.execute(query, value)
                conn.commit()
                conn.close()
                messagebox.showinfo(
                    "Info", "Your password has been reset,please login new password", parent=self.root2)
                self.root2.destroy()

    def forget_password_window(self):
        if self.txtuser.get() == "":
            messagebox.showerror("Error", "Please enter the email address")
        else:
            conn = mysql.connector.connect(
                host="localhost", user="root", password="Abhi@8797", database="db")
            my_cursor = conn.cursor()
            query = ("select *from register where email=%s")
            value = (self.txtuser.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            # print(row)
            if row == None:
                messagebox.showerror(
                    "my Error", "please enter the valid username")
            else:
                conn.close()
                self.root2 = Toplevel()
                self.root2.title("forget password")
                self.root2.geometry("340x450+610+170")

                l = Label(self.root2, text="Forget password", font=(
                    "times new roman", 15, "bold"), fg="black", bg="white")
                l.place(x=100, y=10, width=150)

                securty = Label(self.root2, text="What's Your Security Question", font=(
                    "times new roman", 10, "bold"), fg="black", bg="white")
                securty.place(x=60, y=50)
                self.combo_securty = ttk.Combobox(self.root2, font=(
                    "times new roman", 10, "bold"), state="readonly")
                self.combo_securty["values"] = (
                    "select", "Your birth place", "Your girlfriend name", "Your nick name")
                self.combo_securty.place(x=60, y=75, width=200, height=25)
                self.combo_securty.current(0)

                Securty_ans = Label(self.root2, text="your Security Answer", font=(
                    "times new roman", 10, "bold"), fg="black", bg="white")
                Securty_ans.place(x=60, y=120)
                self.Securty_ans = ttk.Entry(
                    self.root2, font=("times new roman", 10, "bold"))
                self.Securty_ans.place(x=60, y=140, width=200, height=25)

                new_password = Label(self.root2, text="New Password", font=(
                    "times new roman", 10, "bold"), fg="black", bg="white")
                new_password.place(x=60, y=180)
                self.txt_newpass = ttk.Entry(self.root2, font=(
                    "times new roman", 10, "bold"))
                self.txt_newpass.place(x=60, y=200, width=200, height=25)
                btn = Button(self.root2, text="RESET PASSWORD", font=("times new roman", 10, "bold"), bd=3,
                             relief=RIDGE, command=self.reset_pass, fg="white", bg="red", activeforeground="white", activebackground="blue")
                btn.place(x=60, y=250, width=200, height=30)


class register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register Form")
        self.root.geometry("1500x800+0+0")

        # ===========Text variable=========
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_email = StringVar()
        self.var_password = StringVar()
        self.var_confirm_password = StringVar()
        self.var_phone_number = StringVar()
        self.var_securty = StringVar()
        self.var_securty_ans = StringVar()
        self.var_check = IntVar()

        self.bg = ImageTk.PhotoImage(
            file="super-saiyan-goku-5120x2880-13279.jpg")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

# =========== LEFT IMAGE ===========
        self.bg1 = ImageTk.PhotoImage(file="pexels-tim-mossholder-1115680.jpg")
        lbl_bg1 = Label(self.root, image=self.bg1)
        lbl_bg1.place(x=40, y=100, width=500, height=450)
# ============= main frame ============
        frame = Frame(self.root, bg="white")
        frame.place(x=500, y=100, width=700, height=450)

        register_lbl = Label(frame, text="REGISTER HERE", font=(
            "times new roman", 20, "bold"), fg="green")
        register_lbl.place(x=250, y=20)

        user_name = Label(frame, text="Enter FirstName",
                          font=("times new roman", 10, "bold"), fg="black", bg="white")
        user_name.place(x=30, y=60)
        self.txtuser = ttk.Entry(
            frame, textvariable=self.var_fname, font=("times new roman", 10, "bold"))
        self.txtuser.place(x=30, y=80, width=200, height=25)

        last_name = Label(frame, text="Enter LastName", font=(
            "times new roman", 10, "bold"), fg="black", bg="white")
        last_name.place(x=400, y=60)
        self.last_name = ttk.Entry(
            frame, textvariable=self.var_lname, font=("times new roman", 10, "bold"))
        self.last_name.place(x=400, y=80, width=200, height=25)

        new_password = Label(frame, text="New Password", font=(
            "times new roman", 10, "bold"), fg="black", bg="white")
        new_password.place(x=30, y=120)
        self.txtnewpass = ttk.Entry(
            frame, textvariable=self.var_password, font=("times new roman", 10, "bold"))
        self.txtnewpass.place(x=30, y=140, width=200, height=25)

        confirm_pass = Label(frame, text="Confirm Password", font=(
            "times new roman", 10, "bold"), fg="black", bg="white")
        confirm_pass.place(x=30, y=175)
        self.txtconf_pass = ttk.Entry(
            frame, textvariable=self.var_confirm_password, font=("times new roman", 10, "bold"))
        self.txtconf_pass.place(x=30, y=195, width=200, height=25)

        mobileno = Label(frame, text="Mobile number", font=(
            "times new roman", 10, "bold"), fg="black", bg="white")
        mobileno.place(x=30, y=230)
        self_mobileno = ttk.Entry(frame, textvariable=self.var_phone_number, font=(
            "times new roman", 10, "bold"))
        self_mobileno.place(x=30, y=250, width=200, height=25)

        email = Label(frame, text="Email Id", font=(
            "times new roman", 10, "bold"), fg="black", bg="white")
        email.place(x=400, y=120)
        self.email = ttk.Entry(frame, textvariable=self.var_email, font=(
            "times new roman", 10, "bold"))
        self.email.place(x=400, y=140, width=200, height=25)

        securty = Label(frame, text="What's Your Security Question", font=(
            "times new roman", 10, "bold"), fg="black", bg="white")
        securty.place(x=400, y=177)
        self.combo_securty = ttk.Combobox(frame, textvariable=self.var_securty, font=(
            "times new roman", 10, "bold"), state="readonly")
        self.combo_securty["values"] = (
            "select", "Your birth place", "Your girlfriend name", "Your nick name")
        self.combo_securty.place(x=400, y=195, width=200, height=25)
        self.combo_securty.current(0)

        Securty_ans = Label(frame, text="your Security Answer", font=(
            "times new roman", 10, "bold"), fg="black", bg="white")
        Securty_ans.place(x=400, y=235)
        self.Securty_ans = ttk.Entry(
            frame, textvariable=self.var_securty_ans, font=("times new roman", 10, "bold"))
        self.Securty_ans.place(x=400, y=255, width=200, height=25)
        self.check_btn = Checkbutton(frame, variable=self.var_check, text="I agree with the T&C",
                                     font=("times new roman", 10, "bold"), onvalue=1, offvalue=0)
        self.check_btn.place(x=30, y=280)

# ================= BUTTON ===============
        image = Image.open("images.png")
        image = image.resize((70, 40), Image.Resampling.HAMMING)
        self.photoimg = ImageTk.PhotoImage(image)
        b1 = Button(frame, image=self.photoimg, command=self.register_data, borderwidth=0,
                    cursor="hand2", font=("times new line", 10, "bold"))
        b1.place(x=60, y=330, width=80)

        img1 = Image.open("images.jpeg")
        img1 = img1.resize((50, 20), Image.Resampling.HAMMING)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        b2 = Button(frame, image=self.photoimg1, command=self.return_login, borderwidth=0,
                    cursor="hand2", font=("times new roman", 10, "bold"))
        b2.place(x=400, y=340, width=50)

        # ========= fill updata========

    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securty.get() == "select":
            messagebox.showerror("Error", "All field are required")
        elif self.var_password.get() != self.var_confirm_password.get():
            messagebox.showerror(
                "Error", "Password and confirm password should be same")
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please agree with T&C")
        else:
            conn = mysql.connector.connect(
                host="localhost", user="root", password="Abhi@8797", database="db")
            my_cursor = conn.cursor()
            query = ("select *from register where email = %s")
            value = (self.var_email.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row != None:
                messagebox.showerror(
                    ("Error", "User allready exist, please try another email"))
            else:
                values = (self.var_fname.get(),
                          self.var_lname.get(),
                          self.var_email.get(),
                          self.var_phone_number.get(),
                          self.var_password.get(),
                          self.var_confirm_password.get(),
                          self.var_securty.get(),
                          self.var_securty_ans.get()
                          )
                print(values)
                my_cursor.execute(
                    "insert into register values(%s, %s, %s, %s, %s, %s, %s, %s)", values)
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Register Successfull")
            # conn = mysql.connector.connect(host="localhost", user="root", password="root", database="

    def return_login(self):
        self.root.destroy()


if __name__ == "__main__":
    main()
