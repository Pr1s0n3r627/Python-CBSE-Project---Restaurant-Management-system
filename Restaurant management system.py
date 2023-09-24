from tkinter import *
from tkinter import filedialog, messagebox
import random
import time


# Functions

def reset():
    textReceipt.delete(1.0, END)
    e_Naan.set('0')
    e_roti.set('0')
    e_sabji.set('0')
    e_Butter_Naan.set('0')
    e_kebab.set('0')
    e_chawal.set('0')
    e_mutton.set('0')
    e_paneer.set('0')
    e_chicken.set('0')

    e_lassi.set('0')
    e_coffee.set('0')
    e_faluda.set('0')
    e_roohafza.set('0')
    e_shikanji.set('0')
    e_jaljeera.set('0')
    e_masalatea.set('0')
    e_badammilk.set('0')
    e_coldrinks.set('0')

    e_Paneer_Bhurji.set('0')
    e_Daal_Makhani.set('0')
    e_Daal_Tadka.set('0')
    e_Shahi_Paneer.set('0')
    e_Butter_Chicken.set('0')
    e_Rogan_josh.set('0')
    e_Chicken_Biryani.set('0')
    e_Mutton_Biryani.set('0')
    e_Veg_Biryani.set('0')

    textroti.config(state=DISABLED)
    textNaan.config(state=DISABLED)
    textsabji.config(state=DISABLED)
    textButter_Naan.config(state=DISABLED)
    textkebab.config(state=DISABLED)
    textpaneer.config(state=DISABLED)
    textchicken.config(state=DISABLED)
    textmutton.config(state=DISABLED)
    textchawal.config(state=DISABLED)

    textlassi.config(state=DISABLED)
    textcoffee.config(state=DISABLED)
    textjaljeera.config(state=DISABLED)
    textroohafza.config(state=DISABLED)
    textshikanji.config(state=DISABLED)
    textbadammilk.config(state=DISABLED)
    textmasalatea.config(state=DISABLED)
    textfaluda.config(state=DISABLED)
    textcolddrinks.config(state=DISABLED)

    textDaal_Makhani.config(state=DISABLED)
    textDaal_Tadka.config(state=DISABLED)
    textPaneer_Bhurji.config(state=DISABLED)
    textShahi_Paneer.config(state=DISABLED)
    textButter_Chicken.config(state=DISABLED)
    textRogan_josh.config(state=DISABLED)
    textChicken_Biryani.config(state=DISABLED)
    textMutton_Biryani.config(state=DISABLED)
    textVeg_Biryani.config(state=DISABLED)

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)
    var25.set(0)
    var26.set(0)
    var27.set(0)

    costofdrinksvar.set('')
    costofBreadvar.set('')
    costofMain_Coursevar.set('')
    subtotalvar.set('')
    servicetaxvar.set('')
    totalcostvar.set('')


def save():
    if textReceipt.get(1.0, END) == '\n':
        pass
    else:
        url = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
        if url == None:
            pass
        else:

            bill_data = textReceipt.get(1.0, END)
            url.write(bill_data)
            url.close()
            messagebox.showinfo('Information', 'Your Bill Is Succesfully Saved')


def receipt():
    global billnumber, date
    if costofBreadvar.get() != '' or costofMain_Coursevar.get() != '' or costofdrinksvar.get() != '':
        textReceipt.delete(1.0, END)
        x = random.randint(69, 420)
        billnumber = 'BILL' + str(x)
        date = time.strftime('%d/%m/%Y')

        textReceipt.insert(END, 'Receipt Ref:\t\t' + billnumber + '\t\t' + date + '\n')
        textReceipt.insert(END, '***************************************************************\n')
        textReceipt.insert(END, 'Items:\t\t Cost Of Items(Rs)\n')
        textReceipt.insert(END, '***************************************************************\n')

        if e_roti.get() != '0':
            textReceipt.insert(END, f'Roti\t\t\t{int(e_roti.get()) * 10}\n\n')

        if e_Naan.get() != '0':
            textReceipt.insert(END, f'Naan\t\t\t{int(e_Naan.get()) * 60}\n\n')

        if e_Butter_Naan.get() != '0':
            textReceipt.insert(END, f'Butter_Naan\t\t\t{int(e_Butter_Naan.get()) * 100}\n\n')

        if e_chawal.get() != '0':
            textReceipt.insert(END, f'Chawal:\t\t\t{int(e_chawal.get()) * 30}\n\n')

        if e_sabji.get() != '0':
            textReceipt.insert(END, f'Sabji:\t\t\t{int(e_sabji.get()) * 50}\n\n')

        if e_paneer.get() != '0':
            textReceipt.insert(END, f'Paneer:\t\t\t{int(e_paneer.get()) * 100}\n\n')

        if e_kebab.get() != '0':
            textReceipt.insert(END, f'Kebab:\t\t\t{int(e_kebab.get()) * 40}\n\n')

        if e_chicken.get() != '0':
            textReceipt.insert(END, f'Chicken:\t\t\t{int(e_chicken.get()) * 120}\n\n')

        if e_mutton.get() != '0':
            textReceipt.insert(END, f'Mutton:\t\t\t{int(e_mutton.get()) * 120}\n\n')

        if e_lassi.get() != '0':
            textReceipt.insert(END, f'Lassi:\t\t\t{int(e_lassi.get()) * 50}\n\n')

        if e_coffee.get() != '0':
            textReceipt.insert(END, f'Coffee:\t\t\t{int(e_coffee.get()) * 40}\n\n')

        if e_faluda.get() != '0':
            textReceipt.insert(END, f'Faluda:\t\t\t{int(e_faluda.get()) * 80}\n\n')

        if e_shikanji.get() != '0':
            textReceipt.insert(END, f'Shikanji:\t\t\t{int(e_shikanji.get()) * 30}\n\n')

        if e_jaljeera.get() != '0':
            textReceipt.insert(END, f'Jaljeera:\t\t\t{int(e_jaljeera.get()) * 40}\n\n')

        if e_roohafza.get() != '0':
            textReceipt.insert(END, f'Roohafza:\t\t\t{int(e_roohafza.get()) * 60}\n\n')

        if e_masalatea.get() != '0':
            textReceipt.insert(END, f'Masala Chai:\t\t\t{int(e_masalatea.get()) * 20}\n\n')

        if e_badammilk.get() != '0':
            textReceipt.insert(END, f'Badam Milk:\t\t\t{int(e_badammilk.get()) * 50}\n\n')

        if e_coldrinks.get() != '0':
            textReceipt.insert(END, f'Cold Drinks:\t\t\t{int(e_coldrinks.get()) * 80}\n\n')

        if e_Daal_Makhani.get() != '0':
            textReceipt.insert(END, f'Daal_Makhani:\t\t\t{int(e_Daal_Makhani.get()) * 400}\n\n')

        if e_Daal_Tadka.get() != '0':
            textReceipt.insert(END, f'Daal_Tadka:\t\t\t{int(e_Daal_Tadka.get()) * 300}\n\n')

        if e_Paneer_Bhurji.get() != '0':
            textReceipt.insert(END, f'Paneer_Bhurji:\t\t\t{int(e_Paneer_Bhurji.get()) * 500}\n\n')

        if e_Butter_Chicken.get() != '0':
            textReceipt.insert(END, f'Butter_Chicken:\t\t\t{int(e_Butter_Chicken.get()) * 450}\n\n')

        if e_Rogan_josh.get() != '0':
            textReceipt.insert(END, f'Rogan_josh:\t\t\t{int(e_Rogan_josh.get()) * 800}\n\n')

        if e_Chicken_Biryani.get() != '0':
            textReceipt.insert(END, f'Chicken_Biryani:\t\t\t{int(e_Chicken_Biryani.get()) * 620}\n\n')

        if e_Mutton_Biryani.get() != '0':
            textReceipt.insert(END, f'Mutton_Biryani:\t\t\t{int(e_Mutton_Biryani.get()) * 700}\n\n')

        if e_Veg_Biryani.get() != '0':
            textReceipt.insert(END, f'Veg_Biryani:\t\t\t{int(e_Veg_Biryani.get()) * 550}\n\n')

        if e_Shahi_Paneer.get() != '0':
            textReceipt.insert(END, f'Shahi_Paneer:\t\t\t{int(e_Shahi_Paneer.get()) * 550}\n\n')

        textReceipt.insert(END, '***************************************************************\n')
        if costofBreadvar.get() != '0 Rs':
            textReceipt.insert(END, f'Cost Of Bread\t\t\t{priceofBread}Rs\n\n')
        if costofdrinksvar.get() != '0 Rs':
            textReceipt.insert(END, f'Cost Of Drinks\t\t\t{priceofDrinks}Rs\n\n')
        if costofMain_Coursevar.get() != '0 Rs':
            textReceipt.insert(END, f'Cost Of Main Course\t\t\t{priceofMain_Course}Rs\n\n')

        textReceipt.insert(END, f'Sub Total\t\t\t{subtotalofItems}Rs\n\n')
        textReceipt.insert(END, f'Service Tax\t\t\t{50}Rs\n\n')
        textReceipt.insert(END, f'Total Cost\t\t\t{subtotalofItems + 50}Rs\n\n')
        textReceipt.insert(END, '***************************************************************\n')

    else:
        messagebox.showerror('Error', 'No Item Is selected')


def totalcost():
    global priceofBread, priceofDrinks, priceofMain_Course, subtotalofItems
    if var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0 or var5.get() != 0 or \
            var6.get() != 0 or var7.get() != 0 or var8.get() != 0 or var9.get() != 0 or var10.get() != 0 or \
            var11.get() != 0 or var12.get() != 0 or var13.get() != 0 or var14.get() != 0 or var15.get() != 0 or \
            var16.get() != 0 or var17.get() != 0 or var18.get() != 0 or var19.get() != 0 or var20.get() != 0 or \
            var21.get() != 0 or var22.get() != 0 or var23.get() != 0 or var24.get() != 0 or var25.get() != 0 or \
            var26.get() != 0 or var27.get() != 0:

        item1 = int(e_roti.get())
        item2 = int(e_Naan.get())
        item3 = int(e_Butter_Naan.get())
        item4 = int(e_sabji.get())
        item5 = int(e_kebab.get())
        item6 = int(e_chawal.get())
        item7 = int(e_mutton.get())
        item8 = int(e_paneer.get())
        item9 = int(e_chicken.get())

        item10 = int(e_lassi.get())
        item11 = int(e_coffee.get())
        item12 = int(e_faluda.get())
        item13 = int(e_shikanji.get())
        item14 = int(e_jaljeera.get())
        item15 = int(e_roohafza.get())
        item16 = int(e_masalatea.get())
        item17 = int(e_badammilk.get())
        item18 = int(e_coldrinks.get())

        item19 = int(e_Daal_Makhani.get())
        item20 = int(e_Daal_Tadka.get())
        item21 = int(e_Paneer_Bhurji.get())
        item22 = int(e_Shahi_Paneer.get())
        item23 = int(e_Butter_Chicken.get())
        item24 = int(e_Rogan_josh.get())
        item25 = int(e_Chicken_Biryani.get())
        item26 = int(e_Mutton_Biryani.get())
        item27 = int(e_Veg_Biryani.get())

        priceofBread = (item1 * 10) \
                       + (item2 * 60) \
                       + (item3 * 80) \
                       + (item4 * 20) \
                       + (item5 * 40) \
                       + (item6 * 30) \
                       + (item7 * 120) \
                       + (item8 * 100) \
                       + (item9 * 120)

        priceofDrinks = (item10 * 50) \
                        + (item11 * 40) \
                        + (item12 * 80) \
                        + (item13 * 30) \
                        + (item14 * 40) \
                        + (item15 * 60) \
                        + (item16 * 20) \
                        + (item17 * 50) \
                        + (item18 * 80)

        priceofMain_Course = (item19 * 400) \
                             + (item20 * 300) \
                             + (item21 * 500) \
                             + (item22 * 550) \
                             + (item23 * 450) \
                             + (item24 * 800) \
                             + (item25 * 620) \
                             + (item26 * 700) \
                             + (item27 * 550)

        costofBreadvar.set(str(priceofBread) + ' Rs')
        costofdrinksvar.set(str(priceofDrinks) + ' Rs')
        costofMain_Coursevar.set(str(priceofMain_Course) + ' Rs')

        subtotalofItems = priceofBread + priceofDrinks + priceofMain_Course
        subtotalvar.set(str(subtotalofItems) + ' Rs')

        servicetaxvar.set('50 Rs')

        tottalcost = subtotalofItems + 50
        totalcostvar.set(str(tottalcost) + ' Rs')

    else:
        messagebox.showerror('Error', 'No Item Is selected')


def roti():
    if var1.get() == 1:
        textroti.config(state=NORMAL)
        textroti.delete(0, END)
        textroti.focus()
    else:
        textroti.config(state=DISABLED)
        e_roti.set('0')


def Naan():
    if var2.get() == 1:
        textNaan.config(state=NORMAL)
        textNaan.delete(0, END)
        textNaan.focus()

    else:
        textNaan.config(state=DISABLED)
        e_Naan.set('0')


def Butter_Naan():
    if var3.get() == 1:
        textButter_Naan.config(state=NORMAL)
        textButter_Naan.delete(0, END)
        textButter_Naan.focus()

    else:
        textButter_Naan.config(state=DISABLED)
        e_Butter_Naan.set('0')


def sabji():
    if var4.get() == 1:
        textsabji.config(state=NORMAL)
        textsabji.focus()
        textsabji.delete(0, END)
    elif var4.get() == 0:
        textsabji.config(state=DISABLED)
        e_sabji.set('0')


def kebab():
    if var5.get() == 1:
        textkebab.config(state=NORMAL)
        textkebab.focus()
        textkebab.delete(0, END)
    elif var5.get() == 0:
        textkebab.config(state=DISABLED)
        e_kebab.set('0')


def chawal():
    if var6.get() == 1:
        textchawal.config(state=NORMAL)
        textchawal.focus()
        textchawal.delete(0, END)
    elif var6.get() == 0:
        textchawal.config(state=DISABLED)
        e_chawal.set('0')


def mutton():
    if var7.get() == 1:
        textmutton.config(state=NORMAL)
        textmutton.focus()
        textmutton.delete(0, END)
    elif var7.get() == 0:
        textmutton.config(state=DISABLED)
        e_mutton.set('0')


def paneer():
    if var8.get() == 1:
        textpaneer.config(state=NORMAL)
        textpaneer.focus()
        textpaneer.delete(0, END)
    elif var8.get() == 0:
        textpaneer.config(state=DISABLED)
        e_paneer.set('0')


def chicken():
    if var9.get() == 1:
        textchicken.config(state=NORMAL)
        textchicken.focus()
        textchicken.delete(0, END)
    elif var9.get() == 0:
        textchicken.config(state=DISABLED)
        e_chicken.set('0')


def lassi():
    if var10.get() == 1:
        textlassi.config(state=NORMAL)
        textlassi.focus()
        textlassi.delete(0, END)
    elif var10.get() == 0:
        textlassi.config(state=DISABLED)
        e_lassi.set('0')


def coffee():
    if var11.get() == 1:
        textcoffee.config(state=NORMAL)
        textcoffee.focus()
        textcoffee.delete(0, END)
    elif var11.get() == 0:
        textcoffee.config(state=DISABLED)
        e_coffee.set('0')


def faluda():
    if var12.get() == 1:
        textfaluda.config(state=NORMAL)
        textfaluda.focus()
        textfaluda.delete(0, END)
    elif var12.get() == 0:
        textfaluda.config(state=DISABLED)
        e_faluda.set('0')


def shikanji():
    if var13.get() == 1:
        textshikanji.config(state=NORMAL)
        textshikanji.focus()
        textshikanji.delete(0, END)
    elif var13.get() == 0:
        textshikanji.config(state=DISABLED)
        e_shikanji.set('0')


def jaljeera():
    if var14.get() == 1:
        textjaljeera.config(state=NORMAL)
        textjaljeera.focus()
        textjaljeera.delete(0, END)
    elif var14.get() == 0:
        textjaljeera.config(state=DISABLED)
        e_jaljeera.set('0')


def roohafza():
    if var15.get() == 1:
        textroohafza.config(state=NORMAL)
        textroohafza.focus()
        textroohafza.delete(0, END)
    elif var15.get() == 0:
        textroohafza.config(state=DISABLED)
        e_roohafza.set('0')


def masalatea():
    if var16.get() == 1:
        textmasalatea.config(state=NORMAL)
        textmasalatea.focus()
        textmasalatea.delete(0, END)
    elif var16.get() == 0:
        textmasalatea.config(state=DISABLED)
        e_masalatea.set('0')


def badammilk():
    if var17.get() == 1:
        textbadammilk.config(state=NORMAL)
        textbadammilk.focus()
        textbadammilk.delete(0, END)
    elif var17.get() == 0:
        textbadammilk.config(state=DISABLED)
        e_badammilk.set('0')


def colddrinks():
    if var18.get() == 1:
        textcolddrinks.config(state=NORMAL)
        textcolddrinks.focus()
        textcolddrinks.delete(0, END)
    elif var18.get() == 0:
        textcolddrinks.config(state=DISABLED)
        e_coldrinks.set('0')


def Daal_Makhani():
    if var19.get() == 1:
        textDaal_Makhani.config(state=NORMAL)
        textDaal_Makhani.focus()
        textDaal_Makhani.delete(0, END)
    elif var19.get() == 0:
        textDaal_Makhani.config(state=DISABLED)
        e_Daal_Makhani.set('0')


def Daal_Tadka():
    if var20.get() == 1:
        textDaal_Tadka.config(state=NORMAL)
        textDaal_Tadka.focus()
        textDaal_Tadka.delete(0, END)
    elif var20.get() == 0:
        textDaal_Tadka.config(state=DISABLED)
        e_Daal_Tadka.set('0')


def Paneer_Bhurji():
    if var21.get() == 1:
        textPaneer_Bhurji.config(state=NORMAL)
        textPaneer_Bhurji.focus()
        textPaneer_Bhurji.delete(0, END)
    elif var21.get() == 0:
        textPaneer_Bhurji.config(state=DISABLED)
        e_Paneer_Bhurji.set('0')


def Shahi_Paneer():
    if var22.get() == 1:
        textShahi_Paneer.config(state=NORMAL)
        textShahi_Paneer.focus()
        textShahi_Paneer.delete(0, END)
    elif var22.get() == 0:
        textShahi_Paneer.config(state=DISABLED)
        e_Shahi_Paneer.set('0')


def Butter_Chicken():
    if var23.get() == 1:
        textButter_Chicken.config(state=NORMAL)
        textButter_Chicken.focus()
        textButter_Chicken.delete(0, END)
    elif var23.get() == 0:
        textButter_Chicken.config(state=DISABLED)
        e_Butter_Chicken.set('0')


def Rogan_josh():
    if var24.get() == 1:
        textRogan_josh.config(state=NORMAL)
        textRogan_josh.focus()
        textRogan_josh.delete(0, END)
    elif var24.get() == 0:
        textRogan_josh.config(state=DISABLED)
        e_Rogan_josh.set('0')


def Chicken_Biryani():
    if var25.get() == 1:
        textChicken_Biryani.config(state=NORMAL)
        textChicken_Biryani.focus()
        textChicken_Biryani.delete(0, END)
    elif var25.get() == 0:
        textChicken_Biryani.config(state=DISABLED)
        e_Chicken_Biryani.set('0')


def Mutton_Biryani():
    if var26.get() == 1:
        textMutton_Biryani.config(state=NORMAL)
        textMutton_Biryani.focus()
        textMutton_Biryani.delete(0, END)
    elif var26.get() == 0:
        textMutton_Biryani.config(state=DISABLED)
        e_Mutton_Biryani.set('0')


def Veg_Biryani():
    if var27.get() == 1:
        textVeg_Biryani.config(state=NORMAL)
        textVeg_Biryani.focus()
        textVeg_Biryani.delete(0, END)
    elif var27.get() == 0:
        textVeg_Biryani.config(state=DISABLED)
        e_Veg_Biryani.set('0')


root = Tk()

root.resizable(0, 0)

root.title('Restraunt Billing')

root.config(bg='black')

topFrame = Frame(root, bd=10, relief=RIDGE, bg='black')
topFrame.pack(side=TOP)

labelTitle = Label(topFrame,
                   text='Restraunt Billing',
                   font=('arial', 30, 'bold'),
                   fg='white', bd=9,
                   bg='black', width=51)
labelTitle.grid(row=0, column=0)

# frames

menuFrame = Frame(root, bd=10, relief=RIDGE, bg='black')
menuFrame.pack(side=LEFT)

costFrame = Frame(menuFrame, bd=4, relief=RIDGE, bg='black', pady=10)
costFrame.pack(side=BOTTOM)

BreadFrame = LabelFrame(menuFrame,
                        text='Bread',
                        font=('arial', 19, 'bold'),
                        bd=10, relief=RIDGE, fg='black', )
BreadFrame.pack(side=LEFT)

drinksFrame = LabelFrame(menuFrame,
                         text='Drinks',
                         font=('arial', 19, 'bold'),
                         bd=10, relief=RIDGE, fg='black')
drinksFrame.pack(side=LEFT)

Main_CourseFrame = LabelFrame(menuFrame,
                              text='Main Course',
                              font=('arial', 19, 'bold'),
                              bd=10, relief=RIDGE, fg='black')
Main_CourseFrame.pack(side=LEFT)

rightFrame = Frame(root,
                   bd=15,
                   relief=RIDGE,
                   bg='black')
rightFrame.pack(side=RIGHT)

calculatorFrame = Frame(rightFrame,
                        bd=1,
                        relief=RIDGE,
                        bg='black')
calculatorFrame.pack()

receiptFrame = Frame(rightFrame,
                     bd=4,
                     relief=RIDGE,
                     bg='black')
receiptFrame.pack()

buttonFrame = Frame(rightFrame,
                    bd=3,
                    relief=RIDGE,
                    bg='black')
buttonFrame.pack()

# Variables

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()
var19 = IntVar()
var20 = IntVar()
var21 = IntVar()
var22 = IntVar()
var23 = IntVar()
var24 = IntVar()
var25 = IntVar()
var26 = IntVar()
var27 = IntVar()

e_roti = StringVar()
e_Naan = StringVar()
e_sabji = StringVar()
e_chawal = StringVar()
e_Butter_Naan = StringVar()
e_mutton = StringVar()
e_kebab = StringVar()
e_chicken = StringVar()
e_paneer = StringVar()

e_lassi = StringVar()
e_coffee = StringVar()
e_faluda = StringVar()
e_shikanji = StringVar()
e_roohafza = StringVar()
e_jaljeera = StringVar()
e_masalatea = StringVar()
e_badammilk = StringVar()
e_coldrinks = StringVar()

e_Daal_Makhani = StringVar()
e_Paneer_Bhurji = StringVar()
e_Shahi_Paneer = StringVar()
e_Daal_Tadka = StringVar()
e_Veg_Biryani = StringVar()
e_Butter_Chicken = StringVar()
e_Rogan_josh = StringVar()
e_Chicken_Biryani = StringVar()
e_Mutton_Biryani = StringVar()

costofBreadvar = StringVar()
costofdrinksvar = StringVar()
costofMain_Coursevar = StringVar()
subtotalvar = StringVar()
servicetaxvar = StringVar()
totalcostvar = StringVar()

e_roti.set('0')
e_Naan.set('0')
e_sabji.set('0')
e_Butter_Naan.set('0')
e_kebab.set('0')
e_chawal.set('0')
e_mutton.set('0')
e_chicken.set('0')
e_paneer.set('0')

e_lassi.set('0')
e_coffee.set('0')
e_faluda.set('0')
e_roohafza.set('0')
e_shikanji.set('0')
e_jaljeera.set('0')
e_masalatea.set('0')
e_badammilk.set('0')
e_coldrinks.set('0')

e_Paneer_Bhurji.set('0')
e_Butter_Chicken.set('0')
e_Chicken_Biryani.set('0')
e_Daal_Tadka.set('0')
e_Mutton_Biryani.set('0')
e_Daal_Makhani.set('0')
e_Veg_Biryani.set('0')
e_Rogan_josh.set('0')
e_Shahi_Paneer.set('0')

# Bread

roti = Checkbutton(BreadFrame,
                   text='Roti',
                   font=('arial', 18, 'bold'),
                   onvalue=1, offvalue=0, variable=var1
                   , command=roti)
roti.grid(row=0, column=0, sticky=W)

Naan = Checkbutton(BreadFrame,
                   text='Naan',
                   font=('arial', 18, 'bold'),
                   onvalue=1, offvalue=0, variable=var2
                   , command=Naan)
Naan.grid(row=1, column=0, sticky=W)

Butter_Naan = Checkbutton(BreadFrame,
                          text='Butter Naan',
                          font=('arial', 18, 'bold'),
                          onvalue=1, offvalue=0, variable=var3
                          , command=Butter_Naan)
Butter_Naan.grid(row=2, column=0, sticky=W)

sabji = Checkbutton(BreadFrame,
                    text='Tandoori Roti',
                    font=('arial', 18, 'bold'),
                    onvalue=1, offvalue=0, variable=var4
                    , command=sabji)
sabji.grid(row=3, column=0, sticky=W)

kebab = Checkbutton(BreadFrame,
                    text='Rumali Roti',
                    font=('arial', 18, 'bold'),
                    onvalue=1, offvalue=0, variable=var5
                    , command=kebab)
kebab.grid(row=4, column=0, sticky=W)

chawal = Checkbutton(BreadFrame,
                     text='Butter Roti',
                     font=('arial', 18, 'bold'),
                     onvalue=1, offvalue=0, variable=var6
                     , command=chawal)
chawal.grid(row=5, column=0, sticky=W)

mutton = Checkbutton(BreadFrame,
                     text='Keema Parantha',
                     font=('arial', 18, 'bold'),
                     onvalue=1, offvalue=0, variable=var7,
                     command=mutton)
mutton.grid(row=6, column=0, sticky=W)

paneer = Checkbutton(BreadFrame,
                     text='Stuffed Naan',
                     font=('arial', 18, 'bold'),
                     onvalue=1, offvalue=0, variable=var8
                     , command=paneer)
paneer.grid(row=7, column=0, sticky=W)

chicken = Checkbutton(BreadFrame,
                      text='Lachha Parantha',
                      font=('arial', 18, 'bold'),
                      onvalue=1, offvalue=0, variable=var9
                      , command=chicken)
chicken.grid(row=8, column=0, sticky=W)

# Entry Fields for Bread Items

textroti = Entry(BreadFrame,
                 font=('arial', 18, 'bold'),
                 bd=7, width=6,
                 state=DISABLED,
                 textvariable=e_roti)
textroti.grid(row=0, column=1)

textNaan = Entry(BreadFrame,
                 font=('arial', 18, 'bold'),
                 bd=7, width=6,
                 state=DISABLED,
                 textvariable=e_Naan)
textNaan.grid(row=1, column=1)

textButter_Naan = Entry(BreadFrame,
                        font=('arial', 18, 'bold'),
                        bd=7, width=6,
                        state=DISABLED,
                        textvariable=e_Butter_Naan)
textButter_Naan.grid(row=2, column=1)

textsabji = Entry(BreadFrame,
                  font=('arial', 18, 'bold'),
                  bd=7, width=6,
                  state=DISABLED,
                  textvariable=e_sabji)
textsabji.grid(row=3, column=1)

textkebab = Entry(BreadFrame,
                  font=('arial', 18, 'bold'),
                  bd=7, width=6,
                  state=DISABLED,
                  textvariable=e_kebab)
textkebab.grid(row=4, column=1)

textchawal = Entry(BreadFrame,
                   font=('arial', 18, 'bold'),
                   bd=7, width=6,
                   state=DISABLED,
                   textvariable=e_chawal)
textchawal.grid(row=5, column=1)

textmutton = Entry(BreadFrame,
                   font=('arial', 18, 'bold'),
                   bd=7, width=6,
                   state=DISABLED,
                   textvariable=e_mutton)
textmutton.grid(row=6, column=1)

textpaneer = Entry(BreadFrame,
                   font=('arial', 18, 'bold'),
                   bd=7, width=6,
                   state=DISABLED,
                   textvariable=e_paneer)
textpaneer.grid(row=7, column=1)

textchicken = Entry(BreadFrame,
                    font=('arial', 18, 'bold'),
                    bd=7, width=6,
                    state=DISABLED,
                    textvariable=e_chicken)
textchicken.grid(row=8, column=1)

# Drinks

lassi = Checkbutton(drinksFrame,
                    text='Lassi',
                    font=('arial', 18, 'bold'),
                    onvalue=1, offvalue=0, variable=var10
                    , command=lassi)
lassi.grid(row=0, column=0, sticky=W)

coffee = Checkbutton(drinksFrame,
                     text='Coffee',
                     font=('arial', 18, 'bold'),
                     onvalue=1, offvalue=0, variable=var11
                     , command=coffee)
coffee.grid(row=1, column=0, sticky=W)

faluda = Checkbutton(drinksFrame,
                     text='Faluda',
                     font=('arial', 18, 'bold'),
                     onvalue=1, offvalue=0, variable=var12
                     , command=faluda)
faluda.grid(row=2, column=0, sticky=W)

shikanji = Checkbutton(drinksFrame,
                       text='Shikanji',
                       font=('arial', 18, 'bold'),
                       onvalue=1, offvalue=0, variable=var13
                       , command=shikanji)
shikanji.grid(row=3, column=0, sticky=W)

jaljeera = Checkbutton(drinksFrame,
                       text='Jaljeera',
                       font=('arial', 18, 'bold'),
                       onvalue=1, offvalue=0, variable=var14
                       , command=jaljeera)
jaljeera.grid(row=4, column=0, sticky=W)

roohafza = Checkbutton(drinksFrame,
                       text='Roohafza',
                       font=('arial', 18, 'bold'),
                       onvalue=1, offvalue=0, variable=var15
                       , command=roohafza)
roohafza.grid(row=5, column=0, sticky=W)

masalatea = Checkbutton(drinksFrame,
                        text='Masala Tea',
                        font=('arial', 18, 'bold'),
                        onvalue=1, offvalue=0,
                        variable=var16
                        , command=masalatea)
masalatea.grid(row=6, column=0, sticky=W)

badammilk = Checkbutton(drinksFrame,
                        text='Badam Milk',
                        font=('arial', 18, 'bold'),
                        onvalue=1, offvalue=0,
                        variable=var17
                        , command=badammilk)
badammilk.grid(row=7, column=0, sticky=W)

colddrinks = Checkbutton(drinksFrame,
                         text='Cold Drinks',
                         font=('arial', 18, 'bold'),
                         onvalue=1, offvalue=0,
                         variable=var18
                         , command=colddrinks)
colddrinks.grid(row=8, column=0, sticky=W)

# entry fields for drink items

textlassi = Entry(drinksFrame, font=('arial', 18, 'bold'),
                  bd=7, width=6,
                  state=DISABLED, textvariable=e_lassi)
textlassi.grid(row=0, column=1)

textcoffee = Entry(drinksFrame,
                   font=('arial', 18, 'bold'),
                   bd=7, width=6,
                   state=DISABLED, textvariable=e_coffee)
textcoffee.grid(row=1, column=1)

textfaluda = Entry(drinksFrame,
                   font=('arial', 18, 'bold'),
                   bd=7, width=6, state=DISABLED,
                   textvariable=e_faluda)
textfaluda.grid(row=2, column=1)

textshikanji = Entry(drinksFrame,
                     font=('arial', 18, 'bold'),
                     bd=7, width=6, state=DISABLED,
                     textvariable=e_shikanji)
textshikanji.grid(row=3, column=1)

textjaljeera = Entry(drinksFrame,
                     font=('arial', 18, 'bold'),
                     bd=7, width=6, state=DISABLED,
                     textvariable=e_jaljeera)
textjaljeera.grid(row=4, column=1)

textroohafza = Entry(drinksFrame,
                     font=('arial', 18, 'bold'),
                     bd=7, width=6, state=DISABLED,
                     textvariable=e_roohafza)
textroohafza.grid(row=5, column=1)

textmasalatea = Entry(drinksFrame,
                      font=('arial', 18, 'bold'),
                      bd=7, width=6, state=DISABLED,
                      textvariable=e_masalatea)
textmasalatea.grid(row=6, column=1)

textbadammilk = Entry(drinksFrame,
                      font=('arial', 18, 'bold'),
                      bd=7, width=6, state=DISABLED,
                      textvariable=e_badammilk)
textbadammilk.grid(row=7, column=1)

textcolddrinks = Entry(drinksFrame,
                       font=('arial', 18, 'bold'),
                       bd=7, width=6, state=DISABLED,
                       textvariable=e_coldrinks)
textcolddrinks.grid(row=8, column=1)

# Main_Course

Daal_Makhanicake = Checkbutton(Main_CourseFrame, text='Daal Makhani',
                               font=('arial', 18, 'bold'),
                               onvalue=1, offvalue=0, variable=var19
                               , command=Daal_Makhani)
Daal_Makhanicake.grid(row=0, column=0, sticky=W)

Daal_Tadkacake = Checkbutton(Main_CourseFrame, text='Daal Tadka',
                             font=('arial', 18, 'bold'),
                             onvalue=1, offvalue=0, variable=var20
                             , command=Daal_Tadka)
Daal_Tadkacake.grid(row=1, column=0, sticky=W)

Paneer_Bhurjicake = Checkbutton(Main_CourseFrame, text='Paneer Bhurji',
                                font=('arial', 18, 'bold'),
                                onvalue=1, offvalue=0, variable=var21
                                , command=Paneer_Bhurji)
Paneer_Bhurjicake.grid(row=2, column=0, sticky=W)

Shahi_Paneercake = Checkbutton(Main_CourseFrame, text='Shahi Paneer',
                               font=('arial', 18, 'bold'),
                               onvalue=1, offvalue=0, variable=var22
                               , command=Shahi_Paneer)
Shahi_Paneercake.grid(row=3, column=0, sticky=W)

Butter_Chickencake = Checkbutton(Main_CourseFrame, text='Butter Chicken',
                                 font=('arial', 18, 'bold'),
                                 onvalue=1, offvalue=0, variable=var23
                                 , command=Butter_Chicken)
Butter_Chickencake.grid(row=4, column=0, sticky=W)

Rogan_joshcake = Checkbutton(Main_CourseFrame, text='Rogan Josh',
                             font=('arial', 18, 'bold'),
                             onvalue=1, offvalue=0, variable=var24
                             , command=Rogan_josh)
Rogan_joshcake.grid(row=5, column=0, sticky=W)

Chicken_Biryanicake = Checkbutton(Main_CourseFrame, text='Chicken Biryani',
                                  font=('arial', 18, 'bold'),
                                  onvalue=1, offvalue=0,
                                  variable=var25
                                  , command=Chicken_Biryani)
Chicken_Biryanicake.grid(row=6, column=0, sticky=W)

Mutton_Biryanicake = Checkbutton(Main_CourseFrame, text='Mutton Biryani',
                                 font=('arial', 18, 'bold'),
                                 onvalue=1, offvalue=0,
                                 variable=var26
                                 , command=Mutton_Biryani)
Mutton_Biryanicake.grid(row=7, column=0, sticky=W)

Veg_Biryanicake = Checkbutton(Main_CourseFrame, text='Veg Biryani',
                              font=('arial', 18, 'bold'),
                              onvalue=1, offvalue=0,
                              variable=var27
                              , command=Veg_Biryani)
Veg_Biryanicake.grid(row=8, column=0, sticky=W)

# entry fields for Main_Course

textDaal_Makhani = Entry(Main_CourseFrame,
                         font=('arial', 18, 'bold'),
                         bd=7, width=6,
                         state=DISABLED,
                         textvariable=e_Daal_Makhani)
textDaal_Makhani.grid(row=0, column=1)

textDaal_Tadka = Entry(Main_CourseFrame,
                       font=('arial', 18, 'bold'),
                       bd=7, width=6,
                       state=DISABLED,
                       textvariable=e_Daal_Tadka)
textDaal_Tadka.grid(row=1, column=1)

textPaneer_Bhurji = Entry(Main_CourseFrame,
                          font=('arial', 18, 'bold'),
                          bd=7, width=6,
                          state=DISABLED,
                          textvariable=e_Paneer_Bhurji)
textPaneer_Bhurji.grid(row=2, column=1)

textShahi_Paneer = Entry(Main_CourseFrame,
                         font=('arial', 18, 'bold'),
                         bd=7, width=6,
                         state=DISABLED,
                         textvariable=e_Shahi_Paneer)
textShahi_Paneer.grid(row=3, column=1)

textButter_Chicken = Entry(Main_CourseFrame, font=('arial', 18, 'bold'), bd=7, width=6,
                           state=DISABLED,
                           textvariable=e_Butter_Chicken)
textButter_Chicken.grid(row=4, column=1)

textRogan_josh = Entry(Main_CourseFrame,
                       font=('arial', 18, 'bold'),
                       bd=7, width=6,
                       state=DISABLED,
                       textvariable=e_Rogan_josh)
textRogan_josh.grid(row=5, column=1)

textChicken_Biryani = Entry(Main_CourseFrame,
                            font=('arial', 18, 'bold'),
                            bd=7, width=6,
                            state=DISABLED,
                            textvariable=e_Chicken_Biryani)
textChicken_Biryani.grid(row=6, column=1)

textMutton_Biryani = Entry(Main_CourseFrame,
                           font=('arial', 18, 'bold'),
                           bd=7, width=6,
                           state=DISABLED,
                           textvariable=e_Mutton_Biryani)
textMutton_Biryani.grid(row=7, column=1)

textVeg_Biryani = Entry(Main_CourseFrame,
                        font=('arial', 18, 'bold'),
                        bd=7, width=6,
                        state=DISABLED,
                        textvariable=e_Veg_Biryani)
textVeg_Biryani.grid(row=8, column=1)

# costlabels & entry fields

labelCostofBread = Label(costFrame,
                         text='Cost of Bread',
                         font=('arial', 16, 'bold'),
                         bg='black', fg='white')
labelCostofBread.grid(row=0, column=0)

textCostofBread = Entry(costFrame,
                        font=('arial', 16, 'bold'),
                        bd=6, width=14,
                        state='readonly',
                        textvariable=costofBreadvar)
textCostofBread.grid(row=0, column=1, padx=41)

labelCostofDrinks = Label(costFrame,
                          text='Cost of Drinks',
                          font=('arial', 16, 'bold'),
                          bg='black', fg='white')
labelCostofDrinks.grid(row=1, column=0)

textCostofDrinks = Entry(costFrame,
                         font=('arial', 16, 'bold'),
                         bd=6, width=14,
                         state='readonly',
                         textvariable=costofdrinksvar)
textCostofDrinks.grid(row=1, column=1, padx=41)

labelCostofMain_Course = Label(costFrame,
                               text='Cost Of Main Course',
                               font=('arial', 16, 'bold'),
                               bg='black', fg='white')
labelCostofMain_Course.grid(row=2, column=0)

textCostofMain_Course = Entry(costFrame,
                              font=('arial', 16, 'bold'),
                              bd=6, width=14,
                              state='readonly',
                              textvariable=costofMain_Coursevar)
textCostofMain_Course.grid(row=2, column=1, padx=41)

labelSubTotal = Label(costFrame,
                      text='Sub Total',
                      font=('arial', 16, 'bold'),
                      bg='black', fg='white')
labelSubTotal.grid(row=0, column=2)

textSubTotal = Entry(costFrame,
                     font=('arial', 16, 'bold'),
                     bd=6, width=14,
                     state='readonly',
                     textvariable=subtotalvar)
textSubTotal.grid(row=0, column=3, padx=41)

labelServiceTax = Label(costFrame,
                        text='Service Tax',
                        font=('arial', 16, 'bold'),
                        bg='black', fg='white')
labelServiceTax.grid(row=1, column=2)

textServiceTax = Entry(costFrame,
                       font=('arial', 16, 'bold'),
                       bd=6, width=14,
                       state='readonly',
                       textvariable=servicetaxvar)
textServiceTax.grid(row=1, column=3, padx=41)

labelTotalCost = Label(costFrame,
                       text='Total Cost',
                       font=('arial', 16, 'bold'),
                       bg='black', fg='white')
labelTotalCost.grid(row=2, column=2)

textTotalCost = Entry(costFrame,
                      font=('arial', 16, 'bold'),
                      bd=6, width=14, state='readonly',
                      textvariable=totalcostvar)
textTotalCost.grid(row=2, column=3, padx=41)

# Buttons

buttonTotal = Button(buttonFrame,
                     text='Total',
                     font=('arial', 14, 'bold'),
                     fg='white', bg='black',
                     bd=3, padx=5,
                     command=totalcost)
buttonTotal.grid(row=0, column=0)

buttonReceipt = Button(buttonFrame,
                       text='Receipt',
                       font=('arial', 14, 'bold'),
                       fg='white', bg='black',
                       bd=3, padx=5
                       , command=receipt)
buttonReceipt.grid(row=0, column=1)

buttonSave = Button(buttonFrame,
                    text='Save',
                    font=('arial', 14, 'bold'),
                    fg='white', bg='black',
                    bd=3, padx=5
                    , command=save)
buttonSave.grid(row=0, column=2)

buttonReset = Button(buttonFrame,
                     text='Reset',
                     font=('arial', 14, 'bold'),
                     fg='white', bg='black',
                     bd=3, padx=5,
                     command=reset)
buttonReset.grid(row=0, column=4)

# textarea for receipt

textReceipt = Text(receiptFrame,
                   font=('arial', 12, 'bold'),
                   bd=3, width=42, height=27)
textReceipt.grid(row=0, column=0)

root.mainloop()
