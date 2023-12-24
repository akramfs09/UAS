from cProfile import label
import string
from tkinter import *
import random
import time
from tkinter import messagebox
from tkinter import filedialog
from turtle import clear;



root = Tk()
root.config(bg='#c0c0c0') 

topFrame=Frame(root,bd=10,relief=RIDGE,bg='black') 
topFrame.pack(side=TOP)

labelTitle=Label(topFrame,text='====== FULL STORE ======',font=('Copperplate Gothic Bold',39),fg='#a9a9a9',bg='turquoise4', bd=15,width=39) # Output judul aplikasi
labelTitle.grid(row=0,column=10)


#------------------------------------------------------------------
#variabel list
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
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


#------------------------------------------------------------------
#var entri
#Sepatu Sneakers
e_niko = StringVar()
e_adidos = StringVar()
e_puntela = StringVar()
e_pumo = StringVar()
e_roobek = StringVar()
e_asik = StringVar()
e_vons = StringVar()

#Sepatu Running
e_compos = StringVar()
e_asain = StringVar()
e_spurx = StringVar()
e_latto = StringVar()
e_notbalance = StringVar()
e_pecaso = StringVar()
e_beko = StringVar()

#Sepatu Loafers
e_gocci = StringVar()
e_bolly = StringVar()
e_luivuitong = StringVar()
e_prodo = StringVar()
e_fondi = StringVar()
e_bagian = StringVar()
e_dogbit = StringVar()

# variabel Harga dalam struk
hargasneakersvar=StringVar()
hargarunningvar=StringVar()
hargaloafersvar=StringVar()
subtotalvar=StringVar()



e_niko.set('0')
e_adidos.set('0')
e_puntela.set('0')
e_pumo.set('0')
e_roobek.set('0')
e_asik.set('0')
e_vons.set('0')

e_compos.set('0')
e_asain.set('0')
e_spurx.set('0')
e_latto.set('0')
e_notbalance.set('0')
e_pecaso.set('0')
e_beko.set('0')

e_gocci.set('0')
e_bolly.set('0')
e_luivuitong.set('0')
e_prodo.set('0')
e_fondi.set('0')
e_bagian.set('0')
e_dogbit.set('0')

#PENHITUNGAN
def totalcost():
    # mengglobalkan beberapa variable terlebih dahulu
    global hargasneakers,hargarunning,hargaloafers,subtotalItems
    if var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0 or var5.get() != 0 or \
        var6.get() != 0 or var7.get() != 0 or var8.get() != 0 or var9.get() != 0 or var10.get() != 0 or\
        var11.get() != 0 or var12.get() != 0 or var13.get() != 0 or var14.get() != 0 or var15.get() != 0 or \
        var16.get() != 0 or var17.get() != 0 or var18.get() != 0 or var19.get() != 0 or var20.get() != 0 or \
        var21.get():

        item1=int(e_niko.get())
        item2=int(e_adidos.get())
        item3=int(e_puntela.get())
        item4=int(e_pumo.get())
        item5=int(e_roobek.get())
        item6=int(e_asik.get())
        item7=int(e_vons.get())

        item8=int(e_compos.get())
        item9=int(e_asain.get())
        item10=int(e_spurx.get())
        item11=int(e_latto.get())
        item12=int(e_notbalance.get())
        item13=int(e_pecaso.get())
        item14=int(e_beko.get())
   
        item15=int(e_gocci.get())
        item16=int(e_bolly.get())
        item17=int(e_luivuitong.get())
        item18=int(e_prodo.get())
        item19=int(e_fondi.get())
        item20=int(e_bagian.get())
        item21=int(e_dogbit.get())
       

        hargasneakers= (item1*1500000) + (item2*1200000) + (item3*500000) + (item4*1600000) + (item5*900000) + (item6*1600000) + (item7*1000000) 
        hargarunning= (item8*700000) + (item9*600000) + (item10*500000) + (item11*200000) + (item12*1700000) + (item13*2500000) + (item14*1000000)
        hargaloafers=  (item15*10000000) + (item16*5000000) + (item17*15000000) + (item18*4000000) + (item19*5000000) + (item20*3000000) + (item21*2000000)


        hargasneakersvar.set(str(hargasneakers))
        hargarunningvar.set(str(hargarunning))
        hargaloafersvar.set(str(hargaloafers))
        

        subtotalItems = hargasneakers + hargarunning + hargaloafers
        subtotalvar.set(str(subtotalItems))
    else:
        messagebox.showerror('Error','Tidak ada item yang dipilih')

#CETAK STRUK
def struk():
    global billnumber,date
    if hargasneakersvar.get() != '' or hargarunningvar.get() != '' or hargaloafersvar.get() != '':
        textStruk.delete(1.0,END)
        x=random.randint(100,10000)
        billnumber='BILL'+str(x)
        date=time.strftime('%d/%m/%Y')
        textStruk.insert(END,'Resep Ref:\t        '+billnumber+'\t         '+date+'\n')
        textStruk.insert(END,'******************\n')
        textStruk.insert(END,'Items:\t\t\t Jumlah\t          Harga Total (Rp)\n')
        textStruk.insert(END,'******************\n')
        if e_niko.get()!='0':
            textStruk.insert(END,f'Niko\t\t\t {e_niko.get()} \t\t Rp. {int(e_niko.get())* 1500000}\n\n')

        if e_adidos.get()!='0':
            textStruk.insert(END,f'Adidos\t\t\t {e_adidos.get()} \t\t Rp. {int(e_adidos.get())* 1200000}\n\n')

        if e_puntela.get()!='0':
            textStruk.insert(END,f'Puntela\t\t\t {e_puntela.get()} \t\t Rp. {int(e_puntela.get())* 500000}\n\n')

        if e_pumo.get() != '0':
            textStruk.insert(END, f'Pumo:\t\t\t {e_pumo.get()} \t\t Rp. {int(e_pumo.get()) * 1600000}\n\n')

        if e_roobek.get() != '0':
            textStruk.insert(END, f'Roobek:\t\t\t {e_roobek.get()} \t\t Rp. {int(e_roobek.get()) * 900000}\n\n')

        if e_asik.get() != '0':
            textStruk.insert(END, f'Asik:\t\t\t {e_asik.get()} \t\t Rp. {int(e_asik.get()) * 1600000}\n\n')

        if e_vons.get() != '0':
            textStruk.insert(END, f'Vons:\t\t\t {e_vons.get()} \t\t Rp. {int(e_vons.get()) * 1000000}\n\n')


        if e_compos.get() != '0':
            textStruk.insert(END, f'Compos toast:\t\t\t {e_compos.get()} \t\t Rp. {int(e_compos.get()) * 700000}\n\n')

        if e_asain.get() != '0':
            textStruk.insert(END, f'Asain:\t\t\t {e_asain.get()} \t\t Rp. {int(e_asain.get()) * 600000}\n\n')

        if e_spurx.get() != '0':
            textStruk.insert(END, f'Spurx:\t\t\t {e_spurx.get()} \t\t Rp. {int(e_spurx.get()) * 500000}\n\n')

        if e_latto.get() != '0':
            textStruk.insert(END, f'Latto:\t\t\t {e_latto.get()} \t\t Rp. {int(e_latto.get()) * 200000}\n\n')

        if e_notbalance.get() != '0':
            textStruk.insert(END, f'Not Balance:\t\t\t {e_notbalance.get()} \t\t Rp. {int(e_notbalance.get()) * 1700000}\n\n')

        if e_pecaso.get() != '0':
            textStruk.insert(END, f'Pecaso:\t\t\t {e_pecaso.get()} \t\t Rp. {int(e_pecaso.get()) * 2500000}\n\n')

        if e_beko.get() != '0':
            textStruk.insert(END, f'Beko:\t\t\t {e_beko.get()} \t\t Rp. {int(e_beko.get()) * 1000000}\n\n')


        if e_gocci.get() != '0':
            textStruk.insert(END, f'Gocci:\t\t\t {e_gocci.get()} \t\t Rp. {int(e_gocci.get()) * 10000000}\n\n')

        if e_bolly.get() != '0':
            textStruk.insert(END, f'Bolly:\t\t\t {e_bolly.get()} \t\t Rp. {int(e_bolly.get()) * 5000000}\n\n')

        if e_luivuitong.get() != '0':
            textStruk.insert(END, f'Luivuitong:\t\t\t {e_luivuitong.get()} \t\t Rp. {int(e_luivuitong.get()) * 15000000}\n\n')

        if e_prodo.get() != '0':
            textStruk.insert(END, f'Prodo:\t\t\t {e_prodo.get()} \t\t Rp. {int(e_prodo.get()) * 4000000}\n\n')

        if e_fondi.get() != '0':
            textStruk.insert(END, f'Fondi:\t\t\t {e_fondi.get()} \t\t Rp. {int(e_fondi.get()) * 5000000}\n\n')

        if e_bagian.get() != '0':
            textStruk.insert(END, f'Bagian:\t\t\t {e_bagian.get()} \t\t Rp. {int(e_bagian.get()) * 3000000}\n\n')

        if e_dogbit.get() != '0':
            textStruk.insert(END, f'Dogbit:\t\t\t {e_dogbit.get()} \t\t Rp. {int(e_dogbit.get()) * 2000000}\n\n')

        textStruk.insert(END,'******************\n')
        if hargasneakersvar.get()!='Rp 0':
            textStruk.insert(END,f'Harga dari seneakers\t\t\tRp. {hargasneakers}\n\n')
        if hargarunningvar.get() != 'Rp 0':
            textStruk.insert(END,f'Harga dari runningshoes\t\t\tRp. {hargarunning}\n\n')
        if hargaloafersvar.get() != 'Rp 0':
            textStruk.insert(END,f'Harga dari loavers\t\t\tRp. {hargaloafers}\n\n')


        textStruk.insert(END, f'Harga Total \t\t\tRp. {subtotalItems}\n\n')
        textStruk.insert(END, f'\n\nTerima kasih telah berbelanja disini\nsilahakan kembali lagi lain kali!')
    else:
        messagebox.showerror('Error','Tidak ada item yang dipilih')


#SIMPAN PERANGKAT
def save():
    if textStruk.get(1.0,END)=='\n':
        pass
    else:
        # HANYA DALAM EXTENSION FILE .txt
        url=filedialog.asksaveasfile(mode='w',defaultextension='.txt') 
        if url==None:
            pass
        else:

            bill_data=textStruk.get(1.0,END)
            url.write(bill_data)
            url.close()
            messagebox.showinfo('Informasi','Struk Anda berhasil disimpan')

#RESET
def reset():
    textStruk.delete(1.0,END)
    e_niko.set('0')
    e_adidos.set('0')
    e_puntela.set('0')
    e_pumo.set('0')
    e_roobek.set('0')
    e_asik.set('0')
    e_vons.set('0')

    e_compos.set('0')
    e_asain.set('0')
    e_spurx.set('0')
    e_latto.set('0')
    e_notbalance.set('0')
    e_pecaso.set('0')
    e_beko.set('0')

    e_gocci.set('0')
    e_bolly.set('0')
    e_luivuitong.set('0')
    e_prodo.set('0')
    e_fondi.set('0')
    e_bagian.set('0')
    e_dogbit.set('0')
    
    #BATAS VARIABLE
    textniko.config(state=DISABLED)
    textadidos.config(state=DISABLED)
    textpuntela.config(state=DISABLED)
    textpumo.config(state=DISABLED)
    textroobek.config(state=DISABLED)
    textasik.config(state=DISABLED)
    textvons.config(state=DISABLED)

    textcompos.config(state=DISABLED)
    textasain.config(state=DISABLED)
    textspurx.config(state=DISABLED)
    textlatto.config(state=DISABLED)
    textnotbalance.config(state=DISABLED)
    textpecaso.config(state=DISABLED)
    textbeko.config(state=DISABLED)

    textgocci.config(state=DISABLED)
    textbolly.config(state=DISABLED)
    textluivuitong.config(state=DISABLED)
    textprodo.config(state=DISABLED)
    textfondi.config(state=DISABLED)
    textbagian.config(state=DISABLED)
    textdogbit.config(state=DISABLED)

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

    hargasneakersvar.set('')
    hargarunningvar.set('')
    hargaloafersvar.set('')
    subtotalvar.set('')


#------------------------------------------------------------------
# mengaktifkan fungsi entry
#SNEAKERS
def niko():
    if var1.get()==1:
        textniko.config(state=NORMAL)
        textniko.delete(0,END)
        textniko.focus()
    else:
        textniko.config(state=DISABLED)
        e_niko.set('0')

def adidos():
    if var2.get()==1:
        textadidos.config(state=NORMAL)
        textadidos.delete(0,END)
        textadidos.focus()
    else:
        textadidos.config(state=DISABLED)
        e_adidos.set('0')

def puntela():
    if var3.get()==1:
        textpuntela.config(state=NORMAL)
        textpuntela.delete(0,END)
        textpuntela.focus()
    else:
        textpuntela.config(state=DISABLED)
        e_puntela.set('0')

def pumo():
    if var4.get()==1:
        textpumo.config(state=NORMAL)
        textpumo.delete(0,END)
        textpumo.focus()

    else:
        textpumo.config(state=DISABLED)
        e_pumo.set('0')

def roobek ():
    if var5.get()==1:
        textroobek.config(state=NORMAL)
        textroobek.delete(0,END)
        textroobek.focus()
    else:
        textroobek.config(state=DISABLED)
        e_roobek.set('0')

def asik():
    if var6.get()==1:
        textasik.config(state=NORMAL)
        textasik.delete(0,END)
        textasik.focus()
    else:
        textasik.config(state=DISABLED)
        e_asik.set('0')

def vons():
    if var7.get()==1:
        textvons.config(state=NORMAL)
        textvons.delete(0,END)
        textvons.focus()
    else:
        textvons.config(state=DISABLED)
        e_vons.set('0')

#RUNNING
def compos():
    if var8.get()==1:
        textcompos.config(state=NORMAL)
        textcompos.delete(0,END)
        textcompos.focus()
    else:
        textcompos.config(state=DISABLED)
        e_compos.set('0')

def asain():
    if var9.get()==1:
        textasain.config(state=NORMAL)
        textasain.delete(0,END)
        textasain.focus()
    else:
        textasain.config(state=DISABLED)
        e_asain.set('0')

def spurx():
    if var10.get()==1:
        textspurx.config(state=NORMAL)
        textspurx.delete(0,END)
        textspurx.focus()
    else:
        textspurx.config(state=DISABLED)
        e_spurx.set('0')

def latto():
    if var11.get()==1:
        textlatto.config(state=NORMAL)
        textlatto.delete(0,END)
        textlatto.focus()

    else:
        textlatto.config(state=DISABLED)
        e_latto.set('0')

def notbalance():
    if var12.get()==1:
        textnotbalance.config(state=NORMAL)
        textnotbalance.delete(0,END)
        textnotbalance.focus()
    else:
        textnotbalance.config(state=DISABLED)
        e_notbalance.set('0')

def pecaso():
    if var13.get()==1:
        textpecaso.config(state=NORMAL)
        textpecaso.delete(0,END)
        textpecaso.focus()
    else:
        textpecaso.config(state=DISABLED)
        e_pecaso.set('0')

def beko():
    if var14.get()==1:
        textbeko.config(state=NORMAL)
        textbeko.delete(0,END)
        textbeko.focus()
    else:
        textbeko.config(state=DISABLED)
        e_beko.set('0')

#LOAFERS 
def gocci():
    if var15.get()==1:
        textgocci.config(state=NORMAL)
        textgocci.delete(0,END)
        textgocci.focus()
    else:
        textgocci.config(state=DISABLED)
        e_gocci.set('0')

def bolly():
    if var16.get()==1:
        textbolly.config(state=NORMAL)
        textbolly.delete(0,END)
        textbolly.focus()
    else:
        textbolly.config(state=DISABLED)
        e_bolly.set('0')

def luivuitong():
    if var17.get()==1:
        textluivuitong.config(state=NORMAL)
        textluivuitong.delete(0,END)
        textluivuitong.focus()
    else:
        textluivuitong.config(state=DISABLED)
        e_luivuitong.set('0')

def prodo():
    if var18.get()==1:
        textprodo.config(state=NORMAL)
        textprodo.delete(0,END)
        textprodo.focus()
    else:
        textprodo.config(state=DISABLED)
        e_prodo.set('0')

def fondi():
    if var19.get()==1:
        textfondi.config(state=NORMAL)
        textfondi.delete(0,END)
        textfondi.focus()
    else:
        textfondi.config(state=DISABLED)
        e_fondi.set('0')

def bagian():
    if var20.get()==1:
        textbagian.config(state=NORMAL)
        textbagian.delete(0,END)
        textbagian.focus()
    else:
        textbagian.config(state=DISABLED)
        e_bagian.set('0')

def dogbit():
    if var21.get()==1:
        textdogbit.config(state=NORMAL)
        textdogbit.delete(0,END)
        textdogbit.focus()
    else:
        textdogbit.config(state=DISABLED)
        e_dogbit.set('0')

#frame
List=Frame(root,bd=10,relief=RIDGE,bg='dark slate grey')
List.pack(side=LEFT)

harga=Frame(List,bd=9,relief=RIDGE,bg='lightslategrey',pady=12)
harga.pack(padx=25,pady=40,side=BOTTOM)

sneakers=LabelFrame(List,text='   Sneakers   ',font=('Bernard MT Condensed',19,'bold'),bd=20,relief=RIDGE,fg='#2f2f2f', bg='cadet blue')
sneakers.pack(pady=40,side=LEFT)

running=LabelFrame(List,text='   Running Shoes   ',font=('Bernard MT Condensed',19,'bold'),bd=20,relief=RIDGE,fg='#2f2f2f', bg='cadet blue')
running.pack(pady=40,side=LEFT)

loafers=LabelFrame(List,text='   Loafers   ',font=('Bernard MT Condensed',19,'bold'),bd=20,relief=RIDGE,fg='#2f2f2f', bg='cadet blue')
loafers.pack(pady=40,side=LEFT)

#Membuat Tampilan Pada Frame 
#sneakers
niko=Checkbutton(sneakers,text='Niko      [Rp. 1.500.000]',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var1,
                         command=niko,bg='cadet blue')
niko.grid(row=0,column=0,sticky=W)

adidos=Checkbutton(sneakers,text='Adidos  [Rp. 1.200.000] ',font=('Calibri',16,'bold'),variable=var2,
                         command=adidos, bg='cadet blue')
adidos.grid(row=1,column=0,sticky=W)

puntela=Checkbutton(sneakers,text='Puntela    [Rp. 500.000]',font=('Calibri',16,'bold'),variable=var3,
                        command=puntela, bg='cadet blue')
puntela.grid(row=2,column=0,sticky=W)

pumo=Checkbutton(sneakers,text='Pumo    [Rp. 1.600.000]',font=('Calibri',16,'bold'),variable=var4,
                         command=pumo, bg='cadet blue')
pumo.grid(row=3,column=0,sticky=W)

roobek=Checkbutton(sneakers,text='Roobek    [Rp. 900.000]',font=('Calibri',16,'bold'),variable=var5,
                         command=roobek, bg='cadet blue')
roobek.grid(row=4,column=0,sticky=W)

asik=Checkbutton(sneakers,text='Asik       [Rp. 1.600.000]',font=('Calibri',16,'bold'),variable=var6,
                         command=asik, bg='cadet blue')
asik.grid(row=5,column=0,sticky=W)

vons=Checkbutton(sneakers,text='Vons      [Rp. 1.000.000]',font=('Calibri',16,'bold'),variable=var7,
                         command=vons, bg='cadet blue')
vons.grid(row=6,column=0,sticky=W)

#running
compos=Checkbutton(running,text='Compos           [Rp. 700.000]',font=('Calibri',16,'bold'),variable=var8,
                         command=compos, bg='cadet blue')
compos.grid(row=0,column=0,sticky=W)

asain=Checkbutton(running,text='Asain               [Rp. 600.000]',font=('Calibri',16,'bold'),variable=var9,
                         command=asain ,bg='cadet blue')
asain.grid(row=1,column=0,sticky=W)

spurx=Checkbutton(running,text='Spurx               [Rp. 500.000]',font=('Calibri',16,'bold'),variable=var10,
                         command=spurx ,bg='cadet blue')
spurx.grid(row=2,column=0,sticky=W)

latto=Checkbutton(running,text='Latto                [Rp. 200.000]',font=('Calibri',16,'bold'),variable=var11,
                         command=latto ,bg='cadet blue')
latto.grid(row=3,column=0,sticky=W)

notbalance=Checkbutton(running,text='Not balance [Rp. 1.700.000]',font=('Calibri',16,'bold'),variable=var12,
                         command=notbalance ,bg='cadet blue')
notbalance.grid(row=4,column=0,sticky=W)

pecaso=Checkbutton(running,text='Pecaso          [Rp. 2.500.000]',font=('Calibri',16,'bold'),variable=var13,
                         command=pecaso, bg='cadet blue')
pecaso.grid(row=5,column=0,sticky=W)

beko=Checkbutton(running,text='Beko             [Rp. 1.000.000]',font=('Calibri',16,'bold'),variable=var14,
                         command=beko ,bg='cadet blue')
beko.grid(row=6,column=0,sticky=W)

#Loafers
gocci=Checkbutton(loafers,text='Gocci            [Rp. 10.000.000]',font=('Calibri',16,'bold'),variable=var15,
                         command=gocci ,bg='cadet blue')
gocci.grid(row=0,column=0,sticky=W)

bolly=Checkbutton(loafers,text='Bolly                [Rp.5.000.000]',font=('Calibri',16,'bold'),variable=var16,
                         command=bolly ,bg='cadet blue')
bolly.grid(row=1,column=0,sticky=W)

luivuitong=Checkbutton(loafers,text='Lui vitong      [Rp.15.000.000]',font=('Calibri',16,'bold'),variable=var17,
                         command=luivuitong ,bg='cadet blue')
luivuitong.grid(row=2,column=0,sticky=W)

prodo=Checkbutton(loafers,text='Prodo              [Rp.4.000.000]',font=('Calibri',16,'bold'),variable=var18,
                         command=prodo ,bg='cadet blue')
prodo.grid(row=3,column=0,sticky=W)

fondi=Checkbutton(loafers,text='Fondi               [Rp.5.000.000]',font=('Calibri',16,'bold'),variable=var19,
                         command=fondi ,bg='cadet blue')
fondi.grid(row=4,column=0,sticky=W)

bagian=Checkbutton(loafers,text='Bagian             [Rp.3.000.000]',font=('Calibri',16,'bold'),variable=var20,
                         command=bagian ,bg='cadet blue')
bagian.grid(row=5,column=0,sticky=W)

dogbit=Checkbutton(loafers,text='Dogbit             [Rp.2.000.000]',font=('Calibri',16,'bold'),variable=var21,
                         command=dogbit ,bg='cadet blue')
dogbit.grid(row=6,column=0,sticky=W)

#------------------------------------------------------------------
#entri
#sneakers
textniko=Entry(sneakers,font=('Calibri','16','bold'),bd=7,width=3,state=DISABLED,textvar=e_niko)
textniko.grid(row=0,column=1)

textadidos=Entry(sneakers,font=('Calibri','16','bold'),bd=7,width=3,state=DISABLED,textvar=e_adidos)
textadidos.grid(row=1,column=1)

textpuntela=Entry(sneakers,font=('Calibri','16','bold'),bd=7,width=3,state=DISABLED,textvar=e_puntela)
textpuntela.grid(row=2,column=1)

textpumo=Entry(sneakers,font=('Calibri','16','bold'),bd=7,width=3,state=DISABLED,textvar=e_pumo)
textpumo.grid(row=3,column=1)

textroobek=Entry(sneakers,font=('Calibri','16','bold'),bd=7,width=3,state=DISABLED,textvar=e_roobek)
textroobek.grid(row=4,column=1)

textasik=Entry(sneakers,font=('Calibri','16','bold'),bd=7, width=3,state=DISABLED,textvar=e_asik)
textasik.grid(row=5,column=1)

textvons=Entry(sneakers,font=('Calibri','16','bold'),bd=7,width=3,state=DISABLED,textvar=e_vons)
textvons.grid(row=6,column=1)

#running
textcompos=Entry(running,font=('Calibri','16','bold'),bd=7,width=3,state=DISABLED,textvar=e_compos)
textcompos.grid(row=0,column=1)

textasain=Entry(running,font=('Calibri','16','bold'),bd=7,width=3,state=DISABLED,textvar=e_asain)
textasain.grid(row=1,column=1)

textspurx=Entry(running,font=('Calibri','16','bold'),bd=7,width=3,state=DISABLED,textvar=e_spurx)
textspurx.grid(row=2,column=1)

textlatto=Entry(running,font=('Calibri','16','bold'),bd=7,width=3,state=DISABLED,textvar=e_latto)
textlatto.grid(row=3,column=1)

textnotbalance=Entry(running,font=('Calibri','16','bold'),bd=7,width=3,state=DISABLED,textvar=e_notbalance)
textnotbalance.grid(row=4,column=1)

textpecaso=Entry(running,font=('Calibri','16','bold'),bd=7,width=3,state=DISABLED,textvar=e_pecaso)
textpecaso.grid(row=5,column=1)

textbeko=Entry(running,font=('Calibri','16','bold'),bd=7,width=3,state=DISABLED,textvar=e_beko)
textbeko.grid(row=6,column=1)

#LOAFERS
textgocci=Entry(loafers,font=('Calibri','16','bold'),bd=7,width=3,state=DISABLED,textvar=e_gocci)
textgocci.grid(row=0,column=1)

textbolly=Entry(loafers,font=('Calibri','16','bold'),bd=7,width=3,state=DISABLED,textvar=e_bolly)
textbolly.grid(row=1,column=1)

textluivuitong=Entry(loafers,font=('Calibri','16','bold'),bd=7,width=3,state=DISABLED,textvar=e_luivuitong)
textluivuitong.grid(row=2,column=1)

textprodo=Entry(loafers,font=('Calibri','16','bold'),bd=7,width=3,state=DISABLED,textvar=e_prodo)
textprodo.grid(row=3,column=1)

textfondi=Entry(loafers,font=('Calibri','16','bold'),bd=7,width=3,state=DISABLED,textvar=e_fondi)
textfondi.grid(row=4,column=1)

textbagian=Entry(loafers,font=('Calibri','16','bold'),bd=7,width=3,state=DISABLED,textvar=e_bagian)
textbagian.grid(row=5,column=1)

textdogbit=Entry(loafers,font=('Calibri','16','bold'),bd=7,width=3,state=DISABLED,textvar=e_dogbit)
textdogbit.grid(row=6,column=1)

# Membuat frame kanan untuk (Struk)
rightFrame=Frame(root,bd=15,relief=RIDGE, bg='lightslategrey')
rightFrame.pack(side=RIGHT)

strukFrame=Frame(rightFrame,bd=1,relief=RIDGE)
strukFrame.pack()

buttonFrame=Frame(rightFrame,bd=3,relief=RIDGE)
buttonFrame.pack()

# membuat label harga dan kolom entrinya
labelhargasneakers=Label(harga,text=' HARGA SNEAKERS ', font=('Constantia',15,'bold'),bg='lightslategrey',fg='#fde4c3')
labelhargasneakers.grid(row=0,column=0)

texthargasneakers=Entry(harga,font=('Calibri',16,'bold'),bd=6,width=18,state='readonly',textvariable=hargasneakersvar)
texthargasneakers.grid(row=0,column=1,padx=41)

labelhargarunning=Label(harga,text=' HARGA RUNNING ', font=('Constantia',15,'bold'),bg='lightslategrey',fg='#fde4c3')
labelhargarunning.grid(row=1,column=0)

texthargarunning=Entry(harga,font=('Calibri',16,'bold'),bd=6,width=18,state='readonly',textvariable=hargarunningvar)
texthargarunning.grid(row=1,column=1,padx=41)

labelhargarunning=Label(harga,text=' HARGA LOAFERS ', font=('Constantia',15,'bold'),bg='lightslategrey',fg='#fde4c3')
labelhargarunning.grid(row=2,column=0)

texthargaloafers=Entry(harga,font=('Calibri',16,'bold'),bd=6,width=18,state='readonly',textvariable=hargaloafersvar)
texthargaloafers.grid(row=2,column=1,padx=41)

labeltotal=Label(harga,text='HARGA TOTAL', font=('Constantia',18,'bold'),bg='lightslategrey',fg='#fde4c3')
labeltotal.grid(row=0,column=2)

texttotal=Entry(harga,font=('Calibri',18,'bold'),bd=6,width=20,state='readonly',textvariable=subtotalvar)
texttotal.grid(row=0,column=3,padx=41)

# Membuat tampilan Buttons struk (Tombol-tombol pada frame kanan)
buttonTotal= Button(buttonFrame,text='Total',font=('arial',12,'bold'),fg='#fefefe',bg='darkorchid3',bd=3,padx=12,
                    command=totalcost)
buttonTotal.grid(row=0,column=0)

buttonStruk= Button(buttonFrame,text='Struk',font=('arial',12,'bold'),fg='#fefefe',bg='darkorchid3',bd=3,padx=12,
                    command=struk)
buttonStruk.grid(row=0,column=1)

buttonSimpan= Button(buttonFrame,text='Simpan',font=('arial',12,'bold'),fg='#fefefe',bg='darkorchid3',bd=3,padx=12,
                    command=save)
buttonSimpan.grid(row=0,column=2)

buttonReset= Button(buttonFrame,text='Reset',font=('arial',12,'bold'),fg='#fefefe',bg='red',bd=3,padx=12,
            command=reset)
buttonReset.grid(row=0,column=4)

# menentukan teks pada frame struk
textStruk=Text(strukFrame,font=('arial',10,'bold'),bg='slategrey',bd=8,width=55,height=36,fg='#fde4c3')
textStruk.pack()
#------------------------------------------------------------------
root.mainloop()