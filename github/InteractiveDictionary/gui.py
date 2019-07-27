"""
This file will contain the GUI for the interactive dictionary
the user will be able to interact with the database through the GUI
created:24/07/19
"""

from tkinter import *
import backend


def view_command():
    bookList.delete(0,END)
    for row in backend.view():
        bookList.insert(END,row)

def search_command():
    bookList.delete(0,END)
    for row in backend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        bookList.insert(END,row)

def add_entry():
    row = backend.search(isbn=isbn_text.get())
    if not len(row)==0:
        return
    else:
        backend.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
        view_command()


def get_selected_row(event):
    global selected_tuple
    if bookList.size() > 0:
        index=bookList.curselection()[0]
        selected_tuple=bookList.get(index)


def delete_entry():
        backend.delete(selected_tuple[0])
        view_command()


def update_entry():
        backend.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
        view_command()

window=Tk()

window.wm_title('Bryans Book Store')

l1=Label(window,text='Title')
l1.grid(row=0,column=0)

l2=Label(window,text='Year')
l2.grid(row=1,column=0)

l3=Label(window,text='Author')
l3.grid(row=0,column=2)

l4=Label(window,text='ISBN')
l4.grid(row=1,column=2)

title_text=StringVar()
ent1=Entry(window,textvariable=title_text)
ent1.grid(row=0,column=1)

year_text=StringVar()
ent2=Entry(window,textvariable=year_text)
ent2.grid(row=1,column=1)

author_text=StringVar()
ent3=Entry(window,textvariable=author_text)
ent3.grid(row=0,column=3)

isbn_text=StringVar()
ent4=Entry(window,textvariable=isbn_text)
ent4.grid(row=1,column=3)

bookList=Listbox(window,height=6,width=35)
bookList.grid(row=2,column=0,rowspan=6,columnspan=2)

bookList.bind('<<ListboxSelect>>',get_selected_row)

scrollbar1=Scrollbar(window)
scrollbar1.grid(row=2,column=2,rowspan=6)

bookList.configure(yscrollcommand=scrollbar1.set)
scrollbar1.configure(command=bookList.yview)


b1=Button(window,text="View All",width=12,command=view_command)
b1.grid(row=2,column=3)

b2=Button(window,text="Search Entry",width=12,command=search_command)
b2.grid(row=3,column=3)

b3=Button(window,text="Add Entry",width=12,command=add_entry)
b3.grid(row=4,column=3)

b4=Button(window,text="Update",width=12,command=update_entry)
b4.grid(row=5,column=3)

b5=Button(window,text="Delete",width=12,command=delete_entry)
b5.grid(row=6,column=3)

b6=Button(window,text="Close",width=12,command=window.destroy)
b6.grid(row=7,column=3)

window.mainloop()
