#import library
#impordin lisamooduleid
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import asksaveasfile 

#Tekitan uued värvid, millega saab vajadusel terve kasutajaliidese värviskeemi muuta
astanguLilla = ('#611759')
astanguRoheline = ('#bad405')
astanguHall = ('#f7f7f7')
valge = ('#ffffff')
must = ('#000000')

#Tekitan uued fondid, millega saab vajadusel kasutajaliidese fonte muuta
uusFont = ('Segoe UI', 14,)
uusFontRasvane = ('Segoe UI', 14, 'bold')

#initialize window
root = Tk()
#Lisan funktsiooni, mis tekitab Astangu logo programmi aknale
logo = PhotoImage(file='astangu.png')
root.iconphoto(False, logo)
#Muudan kasutajaliidese dimensioone
root.geometry('470x530')
#Muudan kasutajaliidese taustavärvi
root.config(bg=astanguHall)
#Muudan programmi pealkirja
root.title('Kontaktide märkmik - Marko Runtal ITS-20')
root.resizable(0,0)
#Lisan näidiseks Astangu KRK kontakti
contactlist = [
    ['Astangu KRK',  '6877231', 'Astangu 27', 'astangu@astangu.ee'],
    ]

Name = StringVar()
Number = StringVar()
#Lisan aadressi
Address = StringVar()
#Lisan e-maili
Email = StringVar()

#create frame
frame = Frame(root)
frame.pack(side=RIGHT)

scroll = Scrollbar(frame, orient=VERTICAL)
#Muudan kontaktide nimekirja akna dimensioonide väärtuseid
select = Listbox(frame, yscrollcommand=scroll.set, height=30, width=28)
scroll.config (command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT,  fill=BOTH, expand=1)


########### function to get select value
def Selected():
    return int(select.curselection()[0])
    
##fun to add new contact
#Lisan aadressi ja emaili kontaktile lisamiseks
def AddContact():
    contactlist.append([Name.get(), Number.get(), Address.get(), Email.get()])
    Select_set()

#fun to edit existing contact(first select the contact then click on view button then edit the contact and then click on edit button)
#Lisan aadressi ja emaili kontakti muutmiseks
def EDIT():
    contactlist[Selected()]=[Name.get(), Number.get(), Address.get(), Email.get()]
    Select_set()
    
#to delete selected contact
def DELETE():
    del contactlist[Selected()]
    Select_set()
   
#to view selected contact(first select then click on view button)
#Lisan aadressi ja emaili kontakti vaatamiseks
def VIEW():
    NAME, PHONE, ADDRESS, EMAIL = contactlist[Selected()]
    Name.set(NAME)
    Number.set(PHONE)
    Address.set(ADDRESS)
    Email.set(EMAIL)


###exit game window   
def EXIT():
    root.destroy()

#empty name and number field
#Lisan aadressi ja emaili väljadesse, mida saab lähtestada
def RESET():
    Name.set('')
    Number.set('')
    Address.set('')
    Email.set('')

#Lisan aadressi ja emaili, kui valida kontakt
def Select_set() :
    contactlist.sort()
    select.delete(0,END)
    for name,phone,address,email in contactlist :
        select.insert (END, name)
Select_set()

#Tekitan 'Ekspordi' nupu funktsiooni, mis salvestab kõik olemasolevad ja lisatud kontaktid tekstifaili
#Esimene pool funktsioonist tekitab backup tekstidokumendi kontaktide nimekirjaga kataloogi, kus asub programm
def ekspordiKontaktid():
    with open('Eksporditud Kontaktid.txt', 'w') as outfile:
        outfile.write('\n'.join(str(item) for item in contactlist))
        #Tahan valida kataloogi, kuhu vajadusel salvestada nimekirja koopia, seega arendan funktsiooni ja täiendan 'Ekspordi' nuppu
        files = [('All files', '*.*'),
                 ('Text Document', '*.txt')] 
        outfile = asksaveasfile(filetypes = files, defaultextension = files)
        outfile.write('\n'.join(str(item) for item in contactlist))
    outfile.close()
 

######define buttons #####labels and entry widget
#Kasutan eelnevalt tekitatud uut fonti ja selle väärtuseid
#Kasutan eelnevalt tekitatud uusi värve
#Muudan kasutajaliidese teksti eestikeelseks
#Muudan sisestusväljade paigutust ja dimensioone
Label(root, text='Nimi:', font=uusFont, fg=must, bg=astanguHall).place(x=30, y=18)
Entry(root, textvariable=Name, width=24).place(x=112, y=25)
Label(root, text='Telefon:', font=uusFont, fg=must, bg=astanguHall).place(x=30, y=48)
Entry(root, textvariable=Number, width=24).place(x=112, y=55)
#Lisan aadressi välja
Label(root, text='Aadress:', font=uusFont, fg=must, bg=astanguHall).place(x=30, y=78)
Entry(root, textvariable=Address, width = 24).place(x=112, y=85)
#Lisan emaili välja
Label(root, text='E-mail:', font=uusFont, fg=must, bg=astanguHall).place(x=30, y=108)
Entry(root, textvariable=Email, width=24).place(x=112, y=115)


#Muudan nuppude teksti, dimensioone, fonte, värve, paigutust
Button(root, text='LISA', width=20, font=uusFont, fg=valge, bg=astanguLilla, command=AddContact).place(x=30, y=150)
Button(root, text='VAATA', width=20, font=uusFont, fg=valge, bg=astanguLilla, command=VIEW).place(x=30, y=200)
Button(root, text='MUUDA',  width=20, font=uusFont, fg=valge, bg=astanguLilla,command=EDIT).place(x=30, y=250)
Button(root, text='LÄHTESTA', width=20, font=uusFont,  fg=valge, bg=astanguLilla, command=RESET).place(x=30, y=300)
Button(root, text='KUSTUTA', width=20, font=uusFont, fg=valge, bg=astanguLilla,command=DELETE).place(x=30, y=350)
Button(root, text='EKSPORDI', width=20, font=uusFont, fg=valge, bg=astanguLilla, command=ekspordiKontaktid).place(x=30, y=400)
Button(root, text='VÄLJU', width=20, font=uusFontRasvane, fg=must, bg=astanguRoheline, command = EXIT).place(x=30, y=462)



root.mainloop()
  
