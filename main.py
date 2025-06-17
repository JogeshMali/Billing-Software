import random, os
import tempfile
from datetime import datetime
from time import strftime
from tkinter import *
from tkinter import ttk, messagebox

import mysql.connector
import self
from PIL import Image, ImageTk  # pip install pillow


class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x800+0+0")
        self.root.title("Billing Software")

        # ===========Variables==========
        self.c_name = StringVar()
        self.c_phon = StringVar()
        self.bill_no = StringVar()
        z = random.randint(1000, 9999)
        self.bill_no.set(z)
        self.c_email = StringVar()
        self.search_bill = StringVar()
        self.product = StringVar()
        self.prices = IntVar()
        self.qty = IntVar()
        self.sub_total = StringVar()
        self.tax_input = StringVar()
        self.total = StringVar()
        self.payment=['cash','UPI','credit card']
        self.pay=StringVar()
        # Product Categories
        self.Category = ["Select Option", "Clothing", "LifeStyle", "Mobiles"]

        # SubCatClothing
        self.SubCatClothing = ["Pant", "T-Shirt", "Shirt"]

        self.pant = ["Levis", "Mufti", "Spykar"]
        self.price_levis = 5080
        self.price_mufti = 7000
        self.price_spaykar = 8000

        self.T_shirt = ['Polo', 'Roadster', 'Jack&Jones']
        self.price_polo = 1500
        self.price_Roadster = 1800
        self.price_JackJones = 1700

        self.Shirt = ['Peter England', 'Louis Phillipe', 'Park Avenue']
        self.price_Peter = 2100
        self.price_Louis = 2700
        self.price_Park = 1740

        # SubCatLifStyle
        self.SubCatLifStyle = ['Bath Soap', 'Face Creame', 'Hair Oil']

        self.Bath_soap = ['LifeBuy', 'Lux', 'Santoor', 'Pearl']
        self.price_life = float(20)
        self.price_lux = 20
        self.price_santoor = 20
        self.price_pearl = 30

        self.Face_creame = ['Fair & Lovely', 'Ponds', 'Olay', 'Garnier']
        self.price_fair = 20
        self.price_ponds = 20
        self.price_olay = 20
        self.price_garnier = 30

        self.Hair_oil = ['Parachute', 'Jashmin', 'Bajaj']
        self.price_para = 25
        self.price_jashmin = 22
        self.price_bajaj = 30

        # SubCatMobiles
        self.SubCatMobiles = ['Iphone', 'Sumsung', 'Xiome', 'RealMe', "One+"]

        self.Iphone = ['Iphone_X', 'Iphone_11', 'Iphone_12']
        self.price_ix = 40000
        self.price_i11 = 60000
        self.price_i12 = 85000

        self.Samsung = ['Samsung M16', 'Sumsung M12', 'Sumsung M21']
        self.price_sm16 = 16000
        self.price_sm12 = 12000
        self.price_sm21 = 18000

        self.Xiome = ['Red11', 'Redme-12', 'RedmePro']
        self.price_r11 = 11000
        self.price12 = 12000
        self.price_rpro = 9000

        self.RealMe = ['RealMe 12', 'RealMe 13', 'RealMe Pro']
        self.price_rel12 = 25800
        self.price_rel13 = 22000
        self.price_relpro = 30000

        self.OnePlus = ['OnePlus1', 'OnePlus2', 'OnePlus3']
        self.price_one1 = 45000
        self.price_one12 = 60000
        self.price_one3 = 45800

        # image1



        # image2
        img_2 = Image.open("image/gmart3.png")
        img_2 = img_2.resize((1500, 150))
        self.photoimg_2 = ImageTk.PhotoImage(img_2)

        lbl_img_2 = Label(self.root, image=self.photoimg_2)
        lbl_img_2.place(x=0, y=0, width=1500, height=170)

        # image3


        lbl_title = Label(self.root, text="BILLING SOFTWARE", font=("times new roman", 35, "bold"), bg="white",
                          fg="red")
        lbl_title.place(x=0, y=130, width=1530, height=45)

        def time():
            string = strftime("%H:%M:%S %p")


            lbl.config(text=string)
            lbl.after(1000, time)

        lbl = Label(lbl_title, font=('times new roman', 16, 'bold'), background='white', foreground='blue')
        lbl.place(x=0, y=0, width=120, height=45)
        time()

        Main_Frame = Frame(self.root, bd=5, relief=GROOVE, bg="white")
        Main_Frame.place(x=0, y=175, width=1530, height=620)

        # Customer LabelFrame
        Cust_Frame = LabelFrame(Main_Frame, text="Customer", font=("times new roman", 12, "bold"), bg="white", fg="red")
        Cust_Frame.place(x=10, y=5, width=350, height=140)

        self.lbl_mob = Label(Cust_Frame, text="Mobile No.", font=("times new roman", 12, "bold"), bg="white", bd=4)
        self.lbl_mob.grid(row=0, column=0, stick=W, padx=5, pady=2)

        self.entry_mob = ttk.Entry(Cust_Frame, textvariable=self.c_phon, font=("times new roman", 10, "bold"), width=24)
        self.entry_mob.grid(row=0, column=1)

        self.lblCustName = Label(Cust_Frame, font=('arial', 12, 'bold'), bg="white", text="Customer Name", bd=4)
        self.lblCustName.grid(row=1, column=0, sticky=W, padx=5, pady=2)

        self.txtCustName = ttk.Entry(Cust_Frame, textvariable=self.c_name, font=('arial', 10, 'bold'), width=24)
        self.txtCustName.grid(row=1, column=1, sticky=W, padx=5, pady=2)

        self.lblEmail = Label(Cust_Frame, font=('arial', 12, 'bold'), bg="white", text="Email", bd=4)
        self.lblEmail.grid(row=2, column=0, sticky=W, padx=5, pady=2)

        self.txtEmail = ttk.Entry(Cust_Frame, textvariable=self.c_email, font=('arial', 10, 'bold'), width=24)
        self.txtEmail.grid(row=2, column=1, sticky=W, padx=5, pady=2)

        # Product LabelFrame
        Product_Frame = LabelFrame(Main_Frame, text="Product", font=("times new roman", 12, "bold"), bg="white",
                                   fg="red")
        Product_Frame.place(x=378, y=5, width=628, height=140)

        # Category
        self.lblCategory = Label(Product_Frame, font=('arial', 12, 'bold'), bg="white", text="Select Categories", bd=4)
        self.lblCategory.grid(row=0, column=0, sticky=W, padx=5, pady=2)

        self.Combo_Category = ttk.Combobox(Product_Frame, value=self.Category, font=('arial', 10, 'bold'), width=24,
                                           state="readonly")
        self.Combo_Category.current(0)
        self.Combo_Category.bind("<<ComboboxSelected>>", self.Categories)
        self.Combo_Category.grid(row=0, column=1, sticky=W, padx=5, pady=2)

        # SubCategory
        self.lblSubCategory = Label(Product_Frame, font=('arial', 12, 'bold'), bg="white", text="Subcategory", bd=4)
        self.lblSubCategory.grid(row=1, column=0, sticky=W, padx=5, pady=2)

        self.ComboSubCategory = ttk.Combobox(Product_Frame, value=[""], state="readonly", font=('arial', 10, 'bold'),
                                             width=24)
        self.ComboSubCategory.grid(row=1, column=1, sticky=W, padx=5, pady=2)
        self.ComboSubCategory.bind("<<ComboboxSelected>>", self.Product_add)

        # Product Name
        self.lblproduct = Label(Product_Frame, font=('arial', 12, 'bold'), bg="white", text="Product Name", bd=4)
        self.lblproduct.grid(row=2, column=0, sticky=W, padx=5, pady=2)

        self.ComboProduct = ttk.Combobox(Product_Frame, textvariable=self.product, state="readonly",
                                         font=('arial', 10, 'bold'), width=24)
        self.ComboProduct.grid(row=2, column=1, sticky=W, padx=5, pady=2)
        self.ComboProduct.bind("<<ComboboxSelected>>", self.price)

        # Price
        self.lblPrice = Label(Product_Frame, font=('arial', 12, 'bold'), bg="white", text="Price", bd=4)
        self.lblPrice.grid(row=0, column=2, sticky=W, padx=5, pady=2)

        self.ComboPrice = ttk.Combobox(Product_Frame, state="readonly", textvariable=self.prices,
                                       font=('arial', 10, 'bold'), width=15)
        self.ComboPrice.grid(row=0, column=3, sticky=W, padx=5, pady=2)

        # Qty
        self.lblQty = Label(Product_Frame, font=('arial', 12, 'bold'), bg="white", text="Qty", bd=4)
        self.lblQty.grid(row=1, column=2, sticky=W, padx=5, pady=2)

        self.ComboQty = ttk.Entry(Product_Frame, textvariable=self.qty, font=('arial', 10, 'bold'), width=17)
        self.ComboQty.grid(row=1, column=3, sticky=W, padx=5, pady=2)
        #pay
        self.lbl = Label(Product_Frame, font=('arial', 12, 'bold'), bg="white", text="Payment Mode", bd=4)
        self.lbl.grid(row=2, column=2, sticky=W, padx=5, pady=2)

        self.Combopay = ttk.Combobox(Product_Frame, values=self.payment,textvariable=self.pay, state="readonly",
                                         font=('arial', 10, 'bold'), width=15)
        self.Combopay.grid(row=2, column=3, sticky=W, padx=5, pady=2)

        # Middle Frame
        MiddleFrame = Frame(Main_Frame, bd=10)
        MiddleFrame.place(x=10, y=150, width=995, height=340)

        # Image3
        img12 = Image.open("image/good.jpg")
        img12 = img12.resize((490, 340))
        self.photoimg12 = ImageTk.PhotoImage(img12)

        lbl_img12 = Label(MiddleFrame, image=self.photoimg12)
        lbl_img12.place(x=0, y=0, width=490, height=340)

        # Image 4
        img_13 = Image.open("image/cart1.jpg")
        img_13 = img_13.resize((490, 340))
        self.photoimg13 = ImageTk.PhotoImage(img_13)

        lbl_img_13 = Label(MiddleFrame, image=self.photoimg13)
        lbl_img_13.place(x=490, y=0, width=500, height=340)

        # Search
        Search_Frame = Frame(Main_Frame, bd=2, bg="white")
        Search_Frame.place(x=1020, y=15, width=500, height=40)

        self.lblBill = Label(Search_Frame, font=('arial', 12, 'bold'), fg="white", bg="red", text="Bill Number")
        self.lblBill.grid(row=0, column=0, sticky=W, padx=1)

        self.txt_Entry_Search = ttk.Entry(Search_Frame, textvariable=self.search_bill, font=('arial', 10, 'bold'),
                                          width=24)
        self.txt_Entry_Search.grid(row=0, column=1, sticky=W, padx=2)

        self.BtnSearch = Button(Search_Frame, text="Search", command=self.find_bill, font=('arial', 10, 'bold'),
                                bg="orangered", fg="white", width=15, cursor="hand2")
        self.BtnSearch.grid(row=0, column=2)

        # RightFrame Bill Area
        RightLabelFrame = LabelFrame(Main_Frame, text="Bill Area", font=("times new roman", 12, "bold"), bg="white",
                                     fg="red")
        RightLabelFrame.place(x=1025, y=45, width=480, height=438)

        scroll_y = Scrollbar(RightLabelFrame, orient=VERTICAL)
        self.textarea = Text(RightLabelFrame, yscrollcommand=scroll_y.set, bg="white", fg="blue",
                             font=("times new roman", 12, "bold"))
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)

        # Bill Counter LabelFrame
        Bottom_Frame = LabelFrame(Main_Frame, text="Bill Counter", font=("times new roman", 12, "bold"), bg="white",
                                  fg="red")
        Bottom_Frame.place(x=0, y=485, width=1520, height=125)

        self.lblSubTotal = Label(Bottom_Frame, font=('arial', 12, 'bold'), bg="white", text="Sub Total", bd=4)
        self.lblSubTotal.grid(row=0, column=0, sticky=W, padx=5, pady=2)

        self.EntySubTotal = ttk.Entry(Bottom_Frame, textvariable=self.sub_total, font=('arial', 10, 'bold'), width=24)
        self.EntySubTotal.grid(row=0, column=1, sticky=W, padx=5, pady=2)

        self.lbl_tax = Label(Bottom_Frame, font=('arial', 12, 'bold'), bg="white", text="Gov Tax", bd=4)
        self.lbl_tax.grid(row=1, column=0, sticky=W, padx=5, pady=2)

        self.txt_tax = ttk.Entry(Bottom_Frame, textvariable=self.tax_input, font=('arial', 10, 'bold'), width=24)
        self.txt_tax.grid(row=1, column=1, sticky=W, padx=5, pady=2)

        self.lblAmountTotal = Label(Bottom_Frame, font=(' arial', 12, 'bold'), bg="white", text="Total", bd=4)
        self.lblAmountTotal.grid(row=2, column=0, sticky=W, padx=5, pady=2)

        self.txtAmountTotal = ttk.Entry(Bottom_Frame, textvariable=self.total, font=('arial', 10, 'bold'), width=24)
        self.txtAmountTotal.grid(row=2, column=1, sticky=W, padx=5, pady=2)

        # Button
        Btn_Frame = Frame(Bottom_Frame, bd=2, bg="white")
        Btn_Frame.place(x=320, y=0)

        self.BtnAddToCart = Button(Btn_Frame, command=self.AddItem, height=2, text="Add To Cart",
                                   font=('arial', 15, 'bold'), bg="orangered", fg="white", width=15, cursor="hand2")
        self.BtnAddToCart.grid(row=0, column=0)

        self.Btngenerate_bill = Button(Btn_Frame, command=self.removeitem, height=2, text="Remove From Cart",
                                       font=('arial', 15, 'bold'), bg="orangered", fg="white", width=15, cursor="hand2")
        self.Btngenerate_bill.grid(row=0, column=1)

        self.BtnSave = Button(Btn_Frame, command=self.gen_bill, height=2, text="Generate Bill", font=('arial', 15, 'bold'),
                              bg="orangered", fg="white", width=15, cursor="hand2")
        self.BtnSave.grid(row=0, column=2)

        self.BtnPrint = Button(Btn_Frame, command=self.save_bill, height=2, text="Save Bill", font=('arial', 15, 'bold'),
                               bg="orangered", fg="white", width=15, cursor="hand2")
        self.BtnPrint.grid(row=0, column=3)

        self.BtnClear = Button(Btn_Frame, command=self.clear, height=2, text="Clear", font=('arial', 15, 'bold'),
                               bg="orangered", fg="white", width=15, cursor="hand2")
        self.BtnClear.grid(row=0, column=4)

        self.BtnExit = Button(Btn_Frame, command=self.root.destroy, height=2, text="Exit", font=('arial', 15, 'bold'),
                              bg="orangered", fg="white", width=15, cursor="hand2")
        self.BtnExit.grid(row=0, column=5)
        self.welcome()

        self.l = []

    # ===============Function Declaration==============

    # add to cart
    def AddItem(self):
        Tax = 1

        self.n = self.prices.get()
        self.m = self.qty.get() * self.n
        self.l.append(self.m)
        if self.product.get() == "":
            messagebox.showerror("Error", "Plaease Select the Product Name")
        else:
            self.textarea.insert(END, f"\n  {self.product.get()}\t\t\t{self.qty.get()}\t\t{self.m}")
            self.sub_total.set(str('Rs.%.2f' % (sum(self.l))))
            self.tax_input.set(str('Rs.%.2f' % ((((sum(self.l)) - (self.prices.get())) * Tax) / 100)))
            self.total.set(str('Rs.%.2f' % (((sum(self.l)) + ((((sum(self.l)) - (self.prices.get())) * Tax) / 100)))))
            self.t=(((sum(self.l)) + ((((sum(self.l)) - (self.prices.get())) * Tax) / 100)))
    # generate bill
    def gen_bill(self):
        if self.product.get() == "":
            messagebox.showerror("Error", "Please Add To Cart Product")
        else:
            text = self.textarea.get(11.0, (11.0 + float(len(self.l))))
            self.welcome()
            self.textarea.insert(END, text)
            self.textarea.insert(END, "\n==================================================")
            self.textarea.insert(END, f"\n Sub Amount:\t\t\t{self.sub_total.get()}")
            self.textarea.insert(END, f"\n Tax Amount: \t\t\t{self.tax_input.get()}")
            self.textarea.insert(END, f"\n Total Amount:\t\t\t{self.total.get()}")
            self.textarea.insert(END, "\n==================================================")

    # save bill
    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do you want to save the Bill")

        if op > 0:
            self.mydb = mysql.connector.connect(host='localhost', user='root', password='Your-password',
                                                database='G_Mart')
            self.mycursor = self.mydb.cursor()
            self.billno = self.bill_no.get()
            self.cname = self.c_name.get()
            self.phno = self.c_phon.get()
            self.email = self.c_email.get()
            self.p=self.pay.get()
            self.totalamount=self.t
            self.save = "insert into Bills values({},'{}','{}','{}','{}','{}')".format(self.billno, self.cname, self.phno,
                                                                          self.email,self.totalamount,self.p)

            self.mycursor.execute(self.save)

            self.mydb.commit()
            self.mycursor.close()
            self.mydb.close()
            self.bill_data = self.textarea.get(1.0, END)
            f1 = open('bills/' + str(self.bill_no.get()) + ".txt", 'w')
            f1.write(self.bill_data)
            op = messagebox.showinfo("Saved", f"Bill No: {self.bill_no.get()} saved successfully")
            f1.close()
    # print bil
    def removeitem(self):
       Tax=1
       self.n = self.prices.get()
       self.m = self.qty.get() * self.n
       self.l.remove(self.m)

       self.textarea.delete("end-1l","end")
       self.sub_total.set(str('Rs.%.2f' % (sum(self.l))))
       self.tax_input.set(str('Rs.%.2f' % ((((sum(self.l)) - (self.prices.get())) * Tax) / 100)))
       self.total.set(str('Rs.%.2f' % (((sum(self.l)) +((((sum(self.l)) - (self.prices.get())) * Tax) / 100)))))
       self.t = (((sum(self.l))+((((sum(self.l)) - (self.prices.get())) * Tax) / 100)))

    # seach bill
    def find_bill(self):
        found = "no"
        self.mydb = mysql.connector.connect(host='localhost', user='root', password='Your-password',
                                            database='G_Mart')
        self.mycursor = self.mydb.cursor()
        self.searchb=int(self.search_bill.get())
        self.search="select Billno from Bills where Billno={}".format(self.searchb)
        self.mycursor.execute(self.search)
        self.row=self.mycursor.fetchone()
        if self.row is not None:
            self.i=self.row[0]
            f1 = open(f'bills/{self.i}.txt', 'r')
            self.textarea.delete(1.0, END)
            for d in f1:
                self.textarea.insert(END, d)
            f1.close()
            found = "yes"
            self.mydb.commit()

        if found == 'no':
            messagebox.showerror("Error", "Invalid Bill No.")
        else:
            op = messagebox.askyesno("Delete Bill", "Do you want to delete the Bill")
            if op > 0:
                self.mycursor.execute("delete from Bills where Billno={}".format(self.searchb))
                self.mydb.commit()
                self.path = f'bills/{self.search_bill.get()}.txt'
                os.remove(self.path)
                self.welcome()
                op = messagebox.showinfo("Delete", f"Bill No: {self.search_bill.get()} Deleted successfully")
        self.mycursor.close()
        self.mydb.close()


    # default welcome page
    def welcome(self):
        self.textarea.delete(1.0, END)
        self.textarea.insert(END, "\t \t  Welcome To G-MART")
        self.textarea.insert(END, f" \n Bill Number: {self.bill_no.get()}")
        self.textarea.insert(END, f"\n Customer Name: {self.c_name.get()}")
        self.textarea.insert(END, f"\n Phone Number: {self.c_phon.get()}")
        self.textarea.insert(END, f"\n Customer Email: {self.c_email.get()}")
        self.textarea.insert(END, f"\n Payment Mode: {self.pay.get()}")
        self.textarea.insert(END, "\n==================================================")
        self.textarea.insert(END, f"\n Products\t\t\tQTY\t\tPrice")
        self.textarea.insert(END, "\n==================================================\n")

    # clear function
    def clear(self):
        self.textarea.delete(1.0, END)

        self.c_name.set("")
        self.c_phon.set("")
        self.c_email.set("")
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill.set("")
        self.product.set("")
        self.prices.set(0)
        self.qty.set(0)
        self.l = [0]
        self.total.set("")
        self.sub_total.set("")
        self.tax_input.set('')
        self.welcome()

    # category (customer label frame)
    def Categories(self, event=""):
        if self.Combo_Category.get() == "Clothing":
            self.ComboSubCategory.config(value=self.SubCatClothing)
            self.ComboSubCategory.current(0)
        if self.Combo_Category.get() == "LifeStyle":
            self.ComboSubCategory.config(value=self.SubCatLifStyle)
            self.ComboSubCategory.current(0)
        if self.Combo_Category.get() == "Mobiles":
            self.ComboSubCategory.config(value=self.SubCatMobiles)
            self.ComboSubCategory.current(0)

    # adding products to bill
    def Product_add(self, event=""):
        if self.ComboSubCategory.get() == "Pant":
            self.ComboProduct.config(value=self.pant)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get() == "T-Shirt":
            self.ComboProduct.config(value=self.T_shirt)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get() == "Shirt":
            self.ComboProduct.config(value=self.Shirt)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get() == "Bath Soap":
            self.ComboProduct.config(value=self.Bath_soap)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get() == "Face Creame":
            self.ComboProduct.config(value=self.Face_creame)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get() == "Hair Oil":
            self.ComboProduct.config(value=self.Hair_oil)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get() == "Iphone":
            self.ComboProduct.config(value=self.Iphone)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get() == "Sumsung":
            self.ComboProduct.config(value=self.Samsung)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get() == "Xiome":
            self.ComboProduct.config(value=self.Xiome)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get() == "RealMe":
            self.ComboProduct.config(value=self.RealMe)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get() == "One+":
            self.ComboProduct.config(value=self.OnePlus)
            self.ComboProduct.current(0)

    # price label
    def price(self, event=""):
        # pant
        if self.ComboProduct.get() == "Levis":
            self.ComboPrice.config(value=self.price_levis)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Mufti":
            self.ComboPrice.config(value=self.price_mufti)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Spaykar":
            self.ComboPrice.config(value=self.price_spaykar)
            self.ComboPrice.current(0)
            self.qty.set(1)

        # T-Shirt
        if self.ComboProduct.get() == "Polo":
            self.ComboPrice.config(value=self.price_polo)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Roadster":
            self.ComboPrice.config(value=self.price_Roadster)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Jack&Jones":
            self.ComboPrice.config(value=self.price_JackJones)
            self.ComboPrice.current(0)
            self.qty.set(1)

        # Shirt
        if self.ComboProduct.get() == "Peter England":
            self.ComboPrice.config(value=self.price_Peter)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Louis Phillipe":
            self.ComboPrice.config(value=self.price_Louis)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Park Avenue":
            self.ComboPrice.config(value=self.price_Park)
            self.ComboPrice.current(0)
            self.qty.set(1)

        # Bath_soap
        if self.ComboProduct.get() == "LifeBuy":
            self.ComboPrice.config(value=self.price_life)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Lux":
            self.ComboPrice.config(value=self.price_lux)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Santoor":
            self.ComboPrice.config(value=self.price_santoor)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Pearl":
            self.ComboPrice.config(value=self.price_pearl)
            self.ComboPrice.current(0)
            self.qty.set(1)

        # face creames
        if self.ComboProduct.get() == "Fair & Lovely":
            self.ComboPrice.config(value=self.price_fair)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Ponds":
            self.ComboPrice.config(value=self.price_ponds)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Olay":
            self.ComboPrice.config(value=self.price_olay)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Garnier":
            self.ComboPrice.config(value=self.price_garnier)
            self.ComboPrice.current(0)
            self.qty.set(1)

        # Hair_oil
        if self.ComboProduct.get() == "Parachute":
            self.ComboPrice.config(value=self.price_para)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Jashmin":
            self.ComboPrice.config(value=self.price_jashmin)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Bajaj":
            self.ComboPrice.config(value=self.price_bajaj)
            self.ComboPrice.current(0)
            self.qty.set(1)

        # Iphone
        if self.ComboProduct.get() == "Iphone_X":
            self.ComboPrice.config(value=self.price_ix)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Iphone_11":
            self.ComboPrice.config(value=self.price_i11)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Iphone_12":
            self.ComboPrice.config(value=self.price_i12)
            self.ComboPrice.current(0)
            self.qty.set(1)

        # Samsung
        if self.ComboProduct.get() == "Samsung M16":
            self.ComboPrice.config(value=self.price_sm16)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Sumsung M12":
            self.ComboPrice.config(value=self.price_sm12)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Sumsung M21":
            self.ComboPrice.config(value=self.price_sm21)
            self.ComboPrice.current(0)
            self.qty.set(1)

        # xiomi
        if self.ComboProduct.get() == "Red11":
            self.ComboPrice.config(value=self.price_r11)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Redme-12":
            self.ComboPrice.config(value=self.price12)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "RedmePro":
            self.ComboPrice.config(value=self.price_rpro)
            self.ComboPrice.current(0)
            self.qty.set(1)

        # RealMe
        if self.ComboProduct.get() == "RealMe 12":
            self.ComboPrice.config(value=self.price_rel12)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "RealMe 13":
            self.ComboPrice.config(value=self.price_rel13)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "RealMe Pro":
            self.ComboPrice.config(value=self.price_relpro)
            self.ComboPrice.current(0)
            self.qty.set(1)

        # OnePlus
        if self.ComboProduct.get() == "OnePlus1":
            self.ComboPrice.config(value=self.price_one1)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "OnePlus2":
            self.ComboPrice.config(value=self.price_one12)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "OnePlus3":
            self.ComboPrice.config(value=self.price_one3)
            self.ComboPrice.current(0)
            self.qty.set(1)


if __name__ == '__main__':
    root = Tk()
    obj = Bill_App(root)

    root.mainloop()