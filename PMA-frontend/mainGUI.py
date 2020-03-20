
from tkinter import *
from tkinter.ttk import *
from psql_functions import get_medicine_table

window = Tk()
window.title("PMA")
window.geometry("800x600")
btnframe = Frame(window)
medframe = Frame(window)
salesframe = Frame(window)


def medicineClicked():
    salesframe.pack_forget()
    medframe.pack(side=TOP, anchor=NE)
    tableframe.pack(anchor=W)


def salesClicked():
    medframe.pack_forget()
    listBtn.pack_forget()
    tableframe.pack_forget()
    salesframe.pack(side=TOP, anchor=NE)

def predictClicked():
    listBtn.pack(side=TOP, fill=X)


lbl = Label(window, text="Pharmacist Medical Analyzer")
lbl.pack()

medicineBtn = Button(btnframe, text="Medicines", command=medicineClicked)
salesBtn = Button(btnframe, text="Sales", command=salesClicked)
insertBtn = Button(btnframe, text="Insert data")
modifyBtn = Button(btnframe, text="Modify data")
deleteBtn = Button(btnframe, text="Delete data")
expBtn = Button(medframe, text="Expiring")
predictBtn = Button(salesframe, text="Prediction", command=predictClicked)
listBtn = Button(salesframe, text="List")

medicineBtn.pack(side=LEFT)
salesBtn.pack(side=LEFT)
insertBtn.pack(side=LEFT)
modifyBtn.pack(side=LEFT)
deleteBtn.pack(side=LEFT)
predictBtn.pack(side=TOP, fill=X)
expBtn.pack(side=TOP, fill=X)

btnframe.pack(side=TOP, anchor=W)

tableframe = Frame(window)

results = get_medicine_table()

cols = ('Stock ID', 'Expiration Date', 'Company name', 'Brand name', 'Description', 'Price', 'Quantity')
listBox = Treeview(tableframe, columns=cols, show='headings')
for col in cols:
    listBox.heading(col, text=col)
listBox.grid(row=1, column=0, columnspan=2)

for row in results:
    listBox.insert("", "end", values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

if __name__ == '__main__':
    window.mainloop()

