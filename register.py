from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
from turtle import width
from PIL import Image, ImageTk
import mysql.connector


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
        b2 = Button(frame, image=self.photoimg1, borderwidth=0,
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


if __name__ == "__main__":
    root = Tk()
    app = register(root)
    root.mainloop()
