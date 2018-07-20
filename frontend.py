from tkinter import *
import backend

def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)   

def search_command():
    list1.delete(0,END)
    for row in backend.search(text_var.get(),author_var.get(),year_var.get(),isbn_var.get()):
        list1.insert(END,row)

def insert_command():
    backend.insert(text_var.get(),author_var.get(),year_var.get(),isbn_var.get())
    list1.delete(0,END)
    list1.insert(END,(text_var.get(),author_var.get(),year_var.get(),isbn_var.get()))

def get_selected_row(event):
    global selected_tuple
    if(len(list1.curselection())!=0):
        index = list1.curselection()[0]
        selected_tuple = list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    

def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    backend.update(selected_tuple[0],text_var.get(),author_var.get(),year_var.get(),isbn_var.get())

window = Tk()
window.wm_title("BookStore")
window.resizable(False, False)                  #the maximize button does not appear anymore

l1 = Label(window, text="Title", font = ('MS Sans Serif', 12))
l1.grid(row = 0, column =0, pady = 15)

l2 = Label(window, text="Author", font = ('MS Sans Serif', 12))
l2.grid(row = 0, column =2, pady = 15)

l3 = Label(window, text="Completed Reading on", font = ('MS Sans Serif', 12))
l3.grid(row = 1, column =0, pady = 15)

l4 = Label(window, text="Goodreads Rating", font = ('MS Sans Serif', 12))
l4.grid(row = 1, column =2, pady = 15)

text_var = StringVar()
e1 =Entry(window,textvariable = text_var)
e1.grid(row = 0, column = 1)

author_var = StringVar()
e2 =Entry(window,textvariable = author_var)
e2.grid(row = 0, column = 3,padx = (0,20))

year_var = StringVar()
e3 =Entry(window,textvariable = year_var)
e3.grid(row = 1, column = 1)

isbn_var = StringVar()
e4 =Entry(window,textvariable = isbn_var)
e4.grid(row = 1, column = 3,padx = (0,20))

frame = Frame(window)
frame.grid(row = 2 ,column = 0, columnspan = 2, rowspan = 6, padx = (20,20), pady = (0,20))
list1 = Listbox(frame, height = 12, width = 50)
list1.pack(side = LEFT)

sb = Scrollbar(frame, orient = "vertical")
sb.pack(side = RIGHT, fill = Y)

list1.configure(yscrollcommand = sb.set)
sb.configure(command = list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

b1 = Button(window, text = "View All",command = view_command, width = 15)
b1.grid(row = 2, column = 3)

b2 = Button(window, text = "Search Entry",command = search_command, width = 15)
b2.grid(row = 3, column = 3)

b3 = Button(window, text = "Add Entry",command = insert_command, width = 15)
b3.grid(row = 4, column = 3)

b4 = Button(window, text = "Update",command = update_command, width = 15)
b4.grid(row = 5, column = 3)

b5 = Button(window, text = "Delete",command = delete_command, width = 15)
b5.grid(row = 6, column = 3)

b6 = Button(window, text = "Close", command = window.destroy, width = 15)
b6.grid(row = 7, column = 3)

window.mainloop()