from tkinter import *
from tkinter import messagebox
import random
import os,tempfile,smtplib
import subprocess

#!function port

def clear():
    pass

def send_email():
    def send_gmail():
        ob=smtplib.SMTP('smtp.gmail.com',587)
        ob.starttls()
        ob.login(senderEntry.get(),passwordEntry.get())
        message = email_textarea.get(1.0,END)
        ob.sendmail(senderEntry.get(),recieverEntry.get(),message)
        ob.quit()
        messagebox.showinfo('success','successfully sent email')
    if textArea.get(1.0, 'end') == '\n':
        messagebox.showerror('Error', 'Bill is Empty')    
    else: 
        root1 =Toplevel()
        root1.title('send gmail')
        root1.config(bg='darkgreen')
        root1.resizable(0,0)

        senderFrame = LabelFrame(root1, text='Sender', font=('arial', 16, 'bold'))
        senderFrame.grid(row=0, column=0, padx=40, pady=20)


        senderLabel = Label(senderFrame, text='Senders Email', font=('arial', 16, 'bold'), bg='darkgreen', fg='whitesmoke')
        senderLabel.grid(row=0, column=0, padx=10, pady=10)
        senderEntry = Entry(senderFrame, font=('arial', 16, 'bold'), bd=2, relief=GROOVE, width=23)
        senderEntry.grid(row=0, column=1, padx=10, pady=10)

        passwordLabel = LabelFrame(senderFrame, text='Password', font=('arial', 16, 'bold'))
        passwordLabel.grid(row=1, column=0, padx=10, pady=8)
        passwordEntry = Entry(senderFrame, font=('arial', 16, 'bold'), bd=2, relief=RIDGE, width=23, show='*')
        passwordEntry.grid(row=1, column=1, padx=10, pady=8)

        recipientFrame = LabelFrame(root1, text='Recipient', font=('arial', 16, 'bold'))
        recipientFrame.grid(row=1, column=0, padx=40, pady=20)

        recieverLabel = Label(recipientFrame, text='Email Adress', font=('arial', 16, 'bold'))
        recieverLabel.grid(row=0, column=0, padx=40, pady=20)

        recieverEntry = Entry(recipientFrame, font=('arial', 16, 'bold'), bd=2, relief=GROOVE, width=23)
        recieverEntry.grid(row=0, column=1, padx=10, pady=10)

        messageLabel = Label(recipientFrame, text='Message', font=('arial', 16, 'bold'))
        messageLabel.grid(row=1, column=0, padx=40, pady=20)

        email_textarea = Text(recipientFrame,font=('arial', 16, 'bold'),bd=2,relief=SUNKEN,width=42,height=12)
        email_textarea.grid(row=2, column=0,columnspan=2)
        email_textarea.delete(1.0,END)
        email_textarea.insert(END,textArea.get(1.0,END).replace('=','').replace('-',''))


        sendButton = Button(root1,text='SEND',font=('arial', 16, 'bold'),width=15,command=send_gmail)
        sendButton.grid(row=2,column=0,pady=20)

        root1.mainloop()



#! YAZDIRMA FATURA YAZDIRMA
def print_bill():
    if textArea.get(1.0, 'end') == '\n':
        messagebox.showerror('Error', 'Bill is Empty')
    else:
        file_path = tempfile.NamedTemporaryFile(suffix='.txt', delete=False).name
        with open(file_path, 'w') as file:
            file.write(textArea.get(1.0, 'end'))
        subprocess.run(['open', '-a', 'Preview', file_path])


#?search bill
def search_bill():
    for i in os.listdir('bills/'):
        if i.split('.')[0] == billEntry.get():
            f=open(f'bills/{i}','r')
            textArea.delete(1.0,END)
            for data in f :
                textArea.insert(END,data)
            f.close()
            break
        else:
            messagebox.showerror('error','ınvalid bill number')

#! klasör oluşturma komutları
if not os.path.exists("bills"):
    os.mkdir("bills")

#! save bill
def save_bill():
    global billNumber
    result = messagebox.askyesno("Confirm", "Do you want to save the bill?")
    if result:
        bill_content = textArea.get(1.0, END)
        file = open(f"bills/{billNumber}.txt", "w")
        file.write(bill_content)
        file.close()
        messagebox.showinfo("Successfully", f"Bill Number : {billNumber} is saved successfully")
        billNumber = random.randint(500, 1000)


billNumber = random.randint(500, 1000)


def bill_area():
    if nameEntry.get() == "" and phoneEntry.get == "":
        messagebox.showerror("Error", "Customer Details not available!")
    elif (
        frontEndPriceEntry.get() == ""
        and backEndPriceEntry.get() == ""
        and fullStackPriceEntry == ""
    ):
        messagebox.showerror("Error", "Null Products !")
    else:
        textArea.insert(END, "\t\t**Welcome  Customer**\n")
        textArea.insert(END, f"\nBill Number : {billNumber}\n")
        textArea.insert(END, f"\nCustomer Name : {nameEntry.get()}\n")
        textArea.insert(END, f"\n Customer Phone : {phoneEntry.get()}\n")
        textArea.insert(END, "\n===========================================")
        textArea.insert(END, "\nProduct\t\tQuantity\t\tPrice")
        textArea.insert(END, "\n===========================================")
        #!FRONT PRİCE ETİKET YAZDIRMA
        if htmlEntry.get() != 0:
            textArea.insert(
                END, f"\nHtml Project:\t{htmlEntry.get()}\t\t\t{htmlPrice} TL"
            )
        if cssEntry.get() != 0:
            textArea.insert(END, f"\nCss Project:\t{cssEntry.get()}\t\t\t{cssPrice} TL")
        if bootstrapEntry.get() != 0:
            textArea.insert(
                END,
                f"\nBootstrapt Project:\t{bootstrapEntry.get()}\t\t\t{bootsraptPrice} TL",
            )
        if reactEntry.get() != 0:
            textArea.insert(
                END, f"\nReact Project:\t{reactEntry.get()}\t\t\t{reactPrice} TL"
            )
        if tailwindEntry.get() != 0:
            textArea.insert(
                END,
                f"\nTailwind Project:\t{tailwindEntry.get()}\t\t\t{tailwindPrice} TL",
            )
        if reactplustailwindEntry.get() != 0:
            textArea.insert(
                END,
                f"\nReact+Tailwind Project:\t{reactplustailwindEntry.get()}\t\t\t{reactplustailwindPrice} TL",
            )

        # TODO back pricce etiket yazdırma
        if flaskEntry.get() != 0:
            textArea.insert(
                END, f"\nFlask Project:\t{flaskEntry.get()}\t\t\t{flaskPrice} TL"
            )
        if djangoEntry.get() != 0:
            textArea.insert(
                END, f"\nDjango Project:\t{djangoEntry.get()}\t\t\t{djangoPrice} TL"
            )
        if nodejsEntry.get() != 0:
            textArea.insert(
                END, f"\nNode.js Project:\t{nodejsEntry.get()}\t\t\t{nodejsPrice} TL"
            )
        if sqlserverEntry.get() != 0:
            textArea.insert(
                END, f"\nSql Project:\t{sqlserverEntry.get()}\t\t\t{sqlServerPrice} TL"
            )
        if djangoplusEntry.get() != 0:
            textArea.insert(
                END,
                f"\nReact+Tailwind Project:\t{djangoplusEntry.get()}\t\t\t{djangoplusPrice} TL",
            )
        if nodeplusEntry.get() != 0:
            textArea.insert(
                END, f"\nTailwind Project:\t{nodejsEntry.get()}\t\t\t{nodeplusPrice} TL"
            )

        # ? fULL STACK PRİCE ETİKET
        if javascriptEntry.get() != 0:
            textArea.insert(
                END,
                f"\nJavaScript Project:\t{javascriptEntry.get()}\t\t\t{javascriptPrice} TL",
            )
        if pythonEntry.get() != 0:
            textArea.insert(
                END, f"\nPython Project:\t{pythonEntry.get()}\t\t\t{pythonPrice} TL"
            )
        if desktopEntry.get() != 0:
            textArea.insert(
                END, f"\nDesktop Project:\t{desktopEntry.get()}\t\t\t{desktopPrice} TL"
            )
        if reactPlusDjangoEntry.get() != 0:
            textArea.insert(
                END,
                f"\nReact + Django Project:\t{reactPlusDjangoEntry.get()}\t\t\t{reactplusDjangoPrice} TL",
            )
        if reactPlusFlaskEntry.get() != 0:
            textArea.insert(
                END,
                f"\nReact+Flask Project:\t{reactPlusFlaskEntry.get()}\t\t\t{reactplusflaskPrice} TL",
            )
        if mobileEntry.get() != 0:
            textArea.insert(
                END, f"\nMobile Project:\t{mobileEntry.get()}\t\t\t{mobilePrice} TL"
            )

        #! TAX FİYAT YAZDIRMA ETİKET
        textArea.insert(END, "\n------------------------------------------------")
        if frontEndTaxEntry.get() != 0:
            textArea.insert(END, f"\n FrontEnd Tax: \t{frontEndTaxEntry.get()}")
        if backEndTaxEntry.get() != 0:
            textArea.insert(END, f"\n Backend Tax: \t{backEndTaxEntry.get()}")
        if fullStackTaxEntry.get() != 0:
            textArea.insert(END, f"\n FullStack Tax: \t{fullStackTaxEntry.get()}")
        textArea.insert(END, f"\nTotal Bill : \t\t {totalBill} ")

        save_bill()


def total():
    global totalBill
    # ? front price
    global htmlPrice, bootsraptPrice, reactplustailwindPrice
    global cssPrice, reactPrice, tailwindPrice
    htmlPrice = int(htmlEntry.get()) * 20
    cssPrice = int(cssEntry.get()) * 50
    bootsraptPrice = int(bootstrapEntry.get()) * 70
    reactPrice = int(reactEntry.get()) * 110
    tailwindPrice = int(tailwindEntry.get()) * 90
    reactplustailwindPrice = int(reactplustailwindEntry.get()) * 200

    totalFrontPrice = (
        htmlPrice
        + cssPrice
        + bootsraptPrice
        + reactPrice
        + tailwindPrice
        + reactplustailwindPrice
    )
    frontEndPriceEntry.delete(0, END)
    frontEndPriceEntry.insert(0, f"{totalFrontPrice} TL")

    frontEndTax = totalFrontPrice * 0.15
    frontEndTaxEntry.delete(0, END)
    frontEndTaxEntry.insert(0, f"{frontEndTax} TL")

    #! back price
    global flaskPrice, djangoPrice, nodejsPrice
    global sqlServerPrice, djangoplusPrice, nodeplusPrice
    flaskPrice = int(flaskEntry.get()) * 120
    djangoPrice = int(djangoEntry.get()) * 150
    nodejsPrice = int(nodejsEntry.get()) * 170
    sqlServerPrice = int(sqlserverEntry.get()) * 100
    djangoplusPrice = int(djangoplusEntry.get()) * 190
    nodeplusPrice = int(nodeplusEntry.get()) * 200

    totalBackPrice = (
        flaskPrice
        + djangoPrice
        + nodejsPrice
        + sqlServerPrice
        + djangoplusPrice
        + nodeplusPrice
    )
    backEndPriceEntry.delete(0, END)
    backEndPriceEntry.insert(0, f"{totalBackPrice} TL")
    backendTax = totalBackPrice * 0.15
    backEndTaxEntry.delete(0, END)
    backEndTaxEntry.insert(0, f"{backendTax} TL")

    # TODO full stack price
    global javascriptPrice, pythonPrice, desktopPrice
    global reactplusDjangoPrice, reactplusflaskPrice, mobilePrice
    javascriptPrice = int(javascriptEntry.get()) * 110
    pythonPrice = int(pythonEntry.get()) * 100
    desktopPrice = int(desktopEntry.get()) * 170
    reactplusDjangoPrice = int(reactPlusDjangoEntry.get()) * 300
    reactplusflaskPrice = int(reactPlusFlaskEntry.get()) * 220
    mobilePrice = int(mobileEntry.get()) * 260

    totalFullStackPrice = (
        javascriptPrice
        + pythonPrice
        + desktopPrice
        + reactplusDjangoPrice
        + reactplusflaskPrice
        + mobilePrice
    )
    fullStackPriceEntry.delete(0, END)
    fullStackPriceEntry.insert(0, f"{totalFullStackPrice} TL")
    fullstackTax = totalFullStackPrice * 0.15
    fullStackTaxEntry.delete(0, END)
    fullStackTaxEntry.insert(0, f"{fullstackTax} TL")

    totalBill = (
        totalFrontPrice
        + totalFullStackPrice
        + totalBackPrice
        + frontEndTax
        + backendTax
        + fullstackTax
    )


#! proje çerçevesi oluşumu

root = Tk()
root.title("Software Billing System")
root.geometry("1270x685")
root.iconbitmap("bıllıng.ico")

#! header sistem designed
headingLabel = Label(
    root,
    text="Software Billing System",
    font=("times new roman", 30, "bold"),
    bg="darkgreen",
    fg="whitesmoke",
    bd=12,
    relief=GROOVE,
)
headingLabel.pack(fill=X)

# ? başlık detay
customer_detail_frame = LabelFrame(
    root,
    text="Customer Details",
    font=("times new roman", 20, "bold"),
    fg="whitesmoke",
    bg="darkgreen",
    bd=8,
    relief=GROOVE,
)
customer_detail_frame.pack(fill=X)
#!isim
nameLabel = Label(
    customer_detail_frame,
    text="Name :",
    font=("times new roman", 15, "bold"),
    bg="darkgreen",
    fg="black",
)
nameLabel.grid(row=0, column=0, padx=20)
nameEntry = Entry(customer_detail_frame, font=("arial", 15), bd=7, width=18)
nameEntry.grid(row=0, column=1, padx=8)

#! telefon
phoneLabel = Label(
    customer_detail_frame,
    text="Phone Number :",
    font=("times new roman", 15, "bold"),
    bg="darkgreen",
    fg="black",
)
phoneLabel.grid(
    row=0,
    column=2,
    padx=2,
)

phoneEntry = Entry(customer_detail_frame, font=("arial", 15), bd=7, width=18)
phoneEntry.grid(row=0, column=3, padx=8)

#! Fatura Numarası

billLabel = Label(
    customer_detail_frame,
    text="Bill Number :",
    font=("times new roman", 15, "bold"),
    bg="darkgreen",
    fg="black",
)
billLabel.grid(row=0, column=4, padx=20, pady=2)
billEntry = Entry(customer_detail_frame, font=("arial", 15), bd=7, width=18)
billEntry.grid(row=0, column=5, padx=8)

# TODO Search button
searchButton = Button(
    customer_detail_frame,
    text="SEARCH",
    font=("arial", 15, "bold"),
    bg="darkgreen",
    fg="black",
    bd=7,
    width=20,
    command=search_bill,
)
searchButton.grid(row=0, column=6, padx=20, pady=8)

#! ALAN 2 İÇERİK KISMI
productsFrame = Frame(root)
productsFrame.pack()
# ? front Alanı
frontendFrame = LabelFrame(
    productsFrame,
    text="FrontEnd",
    bg="darkgreen",
    fg="whitesmoke",
    relief=GROOVE,
    bd=8,
    font=("times new roman", 20, "bold"),
)
frontendFrame.grid(row=0, column=0)

#! html label
htmlLabel = Label(
    frontendFrame,
    text="Html Project : ",
    font=("times new roman", 15, "bold"),
    bg="darkgreen",
    fg="black",
)
htmlLabel.grid(row=0, column=0, pady=9)

htmlEntry = Entry(frontendFrame, font=("times new roman", 15, "bold"), width=10, bd=5)
htmlEntry.grid(row=0, column=1, pady=9)

#! CSS LABEL

cssLabel = Label(
    frontendFrame,
    text="Css Project : ",
    font=("times new roman", 15, "bold"),
    bg="darkgreen",
    fg="black",
)
cssLabel.grid(row=1, column=0, pady=9, padx=10)

cssEntry = Entry(frontendFrame, font=("times new roman", 15, "bold"), width=10, bd=5)
cssEntry.grid(row=1, column=1, pady=9, padx=10)

#!bootstrap label

bootstrapLabel = Label(
    frontendFrame,
    text="Bootstrap Project : ",
    font=("times new roman", 15, "bold"),
    bg="darkgreen",
    fg="black",
)
bootstrapLabel.grid(row=2, column=0, pady=9, padx=10)

bootstrapEntry = Entry(
    frontendFrame, font=("times new roman", 15, "bold"), width=10, bd=5
)
bootstrapEntry.grid(row=2, column=1, pady=9, padx=10)

#! react proje label

reactLabel = Label(
    frontendFrame,
    text="React Project : ",
    font=("times new roman", 15, "bold"),
    bg="darkgreen",
    fg="black",
)
reactLabel.grid(row=3, column=0, pady=9, padx=10)

reactEntry = Entry(frontendFrame, font=("times new roman", 15, "bold"), width=10, bd=5)
reactEntry.grid(row=3, column=1, pady=9, padx=10)

# TODO tailwind project

tailwindLabel = Label(
    frontendFrame,
    text="Tailwind Project : ",
    font=("times new roman", 15, "bold"),
    bg="darkgreen",
    fg="black",
)
tailwindLabel.grid(row=4, column=0, pady=9, padx=10)

tailwindEntry = Entry(
    frontendFrame, font=("times new roman", 15, "bold"), width=10, bd=5
)
tailwindEntry.grid(row=4, column=1, pady=9, padx=10)

# ? react + tailwind
reactplustailwindLabel = Label(
    frontendFrame,
    text="Tailwind+React Project : ",
    font=("times new roman", 15, "bold"),
    bg="darkgreen",
    fg="black",
)
reactplustailwindLabel.grid(row=5, column=0, pady=9, padx=10)

reactplustailwindEntry = Entry(
    frontendFrame, font=("times new roman", 15, "bold"), width=10, bd=5
)
reactplustailwindEntry.grid(row=5, column=1, pady=9, padx=10)


# TODO BACKEND FRAME BÖLÜMÜ
backendFrame = LabelFrame(
    productsFrame,
    text="BackEnd",
    bg="darkgreen",
    fg="whitesmoke",
    relief=GROOVE,
    bd=8,
    font=("times new roman", 20, "bold"),
)
backendFrame.grid(row=0, column=1)
#! FLASK LABEL
flaskLabel = Label(
    backendFrame,
    text="Flask Project : ",
    font=("times new roman", 15, "bold"),
    bg="darkgreen",
    fg="black",
)
flaskLabel.grid(row=0, column=0, pady=9, padx=10)

flaskEntry = Entry(backendFrame, font=("times new roman", 15, "bold"), width=10, bd=5)
flaskEntry.grid(row=0, column=1, pady=9, padx=10)
#!DJANGO LABEL
djangoLabel = Label(
    backendFrame,
    text="Django Project : ",
    font=("times new roman", 15, "bold"),
    bg="darkgreen",
    fg="black",
)
djangoLabel.grid(row=1, column=0, pady=9, padx=10)

djangoEntry = Entry(backendFrame, font=("times new roman", 15, "bold"), width=10, bd=5)
djangoEntry.grid(row=1, column=1, pady=9, padx=10)

#! nodejs
nodejsLabel = Label(
    backendFrame,
    text="NodeJS Project : ",
    font=("times new roman", 15, "bold"),
    bg="darkgreen",
    fg="black",
)
nodejsLabel.grid(row=2, column=0, pady=9, padx=10)

nodejsEntry = Entry(backendFrame, font=("times new roman", 15, "bold"), width=10, bd=5)
nodejsEntry.grid(row=2, column=1, pady=9, padx=10)

#! SQL Server PROJECT

sqlserverLabel = Label(
    backendFrame,
    text="MySQl Project : ",
    font=("times new roman", 15, "bold"),
    bg="darkgreen",
    fg="black",
)
sqlserverLabel.grid(row=3, column=0, pady=9, padx=10)

sqlserverEntry = Entry(
    backendFrame, font=("times new roman", 15, "bold"), width=10, bd=5
)
sqlserverEntry.grid(row=3, column=1, pady=9, padx=10)

#! node+ project
nodeplusLabel = Label(
    backendFrame,
    text="NodeJS+ Project : ",
    font=("times new roman", 15, "bold"),
    bg="darkgreen",
    fg="black",
)
nodeplusLabel.grid(row=4, column=0, pady=9, padx=10)

nodeplusEntry = Entry(
    backendFrame, font=("times new roman", 15, "bold"), width=10, bd=5
)
nodeplusEntry.grid(row=4, column=1, pady=9, padx=10)

#! django+ project

djangoplusLabel = Label(
    backendFrame,
    text="Django+ Project : ",
    font=("times new roman", 15, "bold"),
    bg="darkgreen",
    fg="black",
)
djangoplusLabel.grid(row=5, column=0, pady=9, padx=10)

djangoplusEntry = Entry(
    backendFrame, font=("times new roman", 15, "bold"), width=10, bd=5
)
djangoplusEntry.grid(row=5, column=1, pady=9, padx=10)

#! FULL STACK ALANI

fullstackFrame = LabelFrame(
    productsFrame,
    text="Full Stack",
    bg="darkgreen",
    fg="whitesmoke",
    relief=GROOVE,
    bd=8,
    font=("times new roman", 20, "bold"),
)
fullstackFrame.grid(row=0, column=2)

fullstackFrame = LabelFrame(
    productsFrame,
    text="Full Stack",
    bg="darkgreen",
    fg="whitesmoke",
    relief=GROOVE,
    bd=8,
    font=("times new roman", 20, "bold"),
)
fullstackFrame.grid(row=0, column=2)

# JavaScript label
javascriptLabel = Label(
    fullstackFrame,
    text="Javascript+ Project : ",
    font=("times new roman", 15, "bold"),
    bg="darkgreen",
    fg="black",
)
javascriptLabel.grid(row=0, column=0, pady=9, padx=10)

javascriptEntry = Entry(
    fullstackFrame, font=("times new roman", 15, "bold"), width=10, bd=5
)
javascriptEntry.grid(row=0, column=1, pady=9, padx=10)

# Python Alanı:
pythonLabel = Label(
    fullstackFrame,
    text="Python+ Project : ",
    font=("times new roman", 15, "bold"),
    bg="darkgreen",
    fg="black",
)
pythonLabel.grid(row=1, column=0, pady=9, padx=10)

pythonEntry = Entry(
    fullstackFrame, font=("times new roman", 15, "bold"), width=10, bd=5
)
pythonEntry.grid(row=1, column=1, pady=9, padx=10)

# Desktop GUI alanı
desktopLabel = Label(
    fullstackFrame,
    text="DesktopGUI+ Project : ",
    font=("times new roman", 15, "bold"),
    bg="darkgreen",
    fg="black",
)
desktopLabel.grid(row=2, column=0, pady=9, padx=10)

desktopEntry = Entry(
    fullstackFrame, font=("times new roman", 15, "bold"), width=10, bd=5
)
desktopEntry.grid(row=2, column=1, pady=9, padx=10)

# React + Django
reactPlusDjangoLabel = Label(
    fullstackFrame,
    text="React+Django Project : ",
    font=("times new roman", 15, "bold"),
    bg="darkgreen",
    fg="black",
)
reactPlusDjangoLabel.grid(row=3, column=0, pady=9, padx=10)

reactPlusDjangoEntry = Entry(
    fullstackFrame, font=("times new roman", 15, "bold"), width=10, bd=5
)
reactPlusDjangoEntry.grid(row=3, column=1, pady=9, padx=10)

# React + Flask
reactPlusFlaskLabel = Label(
    fullstackFrame,
    text="React+Flask Project : ",
    font=("times new roman", 15, "bold"),
    bg="darkgreen",
    fg="black",
)
reactPlusFlaskLabel.grid(row=4, column=0, pady=9, padx=10)

reactPlusFlaskEntry = Entry(
    fullstackFrame, font=("times new roman", 15, "bold"), width=10, bd=5
)
reactPlusFlaskEntry.grid(row=4, column=1, pady=9, padx=10)

# Mobile app
mobileLabel = Label(
    fullstackFrame,
    text="Mobile Project : ",
    font=("times new roman", 15, "bold"),
    bg="darkgreen",
    fg="black",
)
mobileLabel.grid(row=5, column=0, pady=9, padx=10)

mobileEntry = Entry(
    fullstackFrame, font=("times new roman", 15, "bold"), width=10, bd=5
)
mobileEntry.grid(row=5, column=1, pady=9, padx=10)
#! text alanı
billFrame = Frame(productsFrame, bd=8, relief=GROOVE)
billFrame.grid(row=0, column=3, padx=8)

billAreaLabel = Label(
    billFrame,
    text="Bill Area",
    font=("times new roman", 15, "bold"),
    bd=7,
    relief=GROOVE,
)
billAreaLabel.pack(fill=X)
#! scrollbarr
scrollBar = Scrollbar(billFrame, orient=VERTICAL)
scrollBar.pack(side=RIGHT, fill=Y)

textArea = Text(billFrame, height=18, width=50, yscrollcommand=scrollBar.set)
textArea.pack()
scrollBar.config(command=textArea.yview)


#! FATURA MENÜSÜ
billMenuFrame = LabelFrame(
    root,
    text="Bill Menu",
    font=("times new roman", 15, "bold"),
    fg="whitesmoke",
    bg="darkgreen",
    bd=8,
    relief=GROOVE,
)

billMenuFrame.pack()
#! front price
frontEndPriceLabel = Label(
    billMenuFrame,
    text="FrontEnd Price : ",
    font=("times new roman", 14, "bold"),
    bg="darkgreen",
    fg="black",
)
frontEndPriceLabel.grid(row=0, column=0, pady=9, padx=10)

frontEndPriceEntry = Entry(
    billMenuFrame, font=("times new roman", 13, "bold"), width=10, bd=5
)
frontEndPriceEntry.grid(row=0, column=1, padx=10)

# back price
backEndPriceLabel = Label(
    billMenuFrame,
    text="backEnd Price : ",
    font=("times new roman", 13, "bold"),
    bg="darkgreen",
    fg="black",
)
backEndPriceLabel.grid(row=1, column=0, pady=9, padx=10)

backEndPriceEntry = Entry(
    billMenuFrame, font=("times new roman", 13, "bold"), width=10, bd=5
)
backEndPriceEntry.grid(row=1, column=1, padx=10)

#! fullstack price
fullStackPriceLabel = Label(
    billMenuFrame,
    text="Full Stack Price : ",
    font=("times new roman", 15, "bold"),
    bg="darkgreen",
    fg="black",
)
fullStackPriceLabel.grid(row=2, column=0, pady=9, padx=10)

fullStackPriceEntry = Entry(
    billMenuFrame, font=("times new roman", 13, "bold"), width=10, bd=5
)
fullStackPriceEntry.grid(row=2, column=1, padx=10)

#! front vergi
frontEndTaxLabel = Label(
    billMenuFrame,
    text="FrontEnd Tax : ",
    font=("times new roman", 14, "bold"),
    bg="darkgreen",
    fg="black",
)
frontEndTaxLabel.grid(row=0, column=2, pady=9, padx=10)

frontEndTaxEntry = Entry(
    billMenuFrame, font=("times new roman", 13, "bold"), width=10, bd=5
)
frontEndTaxEntry.grid(row=0, column=3, padx=10)

# back vergi
backEndTaxLabel = Label(
    billMenuFrame,
    text="backEnd Tax : ",
    font=("times new roman", 13, "bold"),
    bg="darkgreen",
    fg="black",
)
backEndTaxLabel.grid(row=1, column=2, pady=9, padx=10)

backEndTaxEntry = Entry(
    billMenuFrame, font=("times new roman", 13, "bold"), width=10, bd=5
)
backEndTaxEntry.grid(row=1, column=3, padx=10)

#! fullstack vergi
fullStackTaxLabel = Label(
    billMenuFrame,
    text="Full Stack Tax : ",
    font=("times new roman", 15, "bold"),
    bg="darkgreen",
    fg="black",
)
fullStackTaxLabel.grid(row=2, column=2, pady=9, padx=10)

fullStackTaxEntry = Entry(
    billMenuFrame, font=("times new roman", 13, "bold"), width=10, bd=5
)
fullStackTaxEntry.grid(row=2, column=3, padx=10)

#! buton köşesi
buttonFrame = Frame(billMenuFrame, bd=0, relief=GROOVE)
buttonFrame.grid(row=0, column=4, rowspan=3)

#! TOTAL
totalButton = Button(
    buttonFrame,
    text="TOTAL",
    font=("arial", 16, "bold"),
    bg="brown1",
    fg="black",
    bd=6,
    width=8,
    pady=10,
    command=total,
)
totalButton.grid(row=0, column=0, pady=20, padx=5)
#! BİLL
billButton = Button(
    buttonFrame,
    text="BİLL",
    font=("arial", 16, "bold"),
    bg="brown1",
    fg="black",
    bd=6,
    width=8,
    pady=8,
    command=bill_area,
)
billButton.grid(row=0, column=1, pady=20, padx=5)
#!EMAİL
emailButton = Button(
    buttonFrame,
    text="EMAİL",
    font=("arial", 16, "bold"),
    bg="brown",
    fg="black",
    bd=6,
    width=8,
    pady=8,
    command=send_email,
)
emailButton.grid(row=0, column=2, pady=20, padx=5)
#!PRİNT
printButton = Button(
    buttonFrame,
    text="PRINT",
    font=("arial", 16, "bold"),
    bg="brown",
    fg="black",
    bd=6,
    width=8,
    pady=8,
    command=print_bill,
)
printButton.grid(row=0, column=3, pady=20, padx=5)
#!CLEAR
clearButton = Button(
    buttonFrame,
    text="CLEAR",
    font=("arial", 16, "bold"),
    bg="brown",
    fg="black",
    bd=6,
    width=8,
    pady=8,
    command=clear,
)
clearButton.grid(row=0, column=4, pady=20, padx=5)


# ? çerçeve boyutlandırması
root.mainloop()
