from tkinter import *
from tkinter.ttk import *
import backend_functions


class App:
    def __init__(self):
        self.window = Tk()
        self.window.title("PMA")
        self.window.geometry("1200x600")
        self.btnframe = Frame(self.window)
        self.medframe = Frame(self.window)
        self.medtableframe = Frame(self.window)
        self.descframe = Frame(self.window)
        self.salesframe = Frame(self.window)
        self.medtable_results = backend_functions.get_medicine_table()
        Label(self.window, text="Pharmacist Medical Analyzer").pack()

        self.medicineBtn = Button(self.btnframe, text="Medicines", command=self.medicineClicked)
        self.salesBtn = Button(self.btnframe, text="Sales", command=self.salesClicked)
        self.insertBtn = Button(self.btnframe, text="Insert data")
        self.modifyBtn = Button(self.btnframe, text="Modify data")
        self.deleteBtn = Button(self.btnframe, text="Delete data")
        self.expBtn = Button(self.medframe, text="Expiring")
        self.predictBtn = Button(self.salesframe, text="Prediction", command=self.predictClicked)
        self.listBtn = Button(self.salesframe, text="List")

        self.medicineBtn.pack(side=LEFT)
        self.salesBtn.pack(side=LEFT)
        self.insertBtn.pack(side=LEFT)
        self.modifyBtn.pack(side=LEFT)
        self.deleteBtn.pack(side=LEFT)
        self.predictBtn.pack(side=TOP, fill=X)
        self.expBtn.pack(side=TOP, fill=X)
        self.btnframe.pack(side=TOP, anchor=W)
        
        self.cols1 = ('Stock ID', 'Expiration Date', 'Company name', 'Brand name', 'Description', 'Price', 'Quantity')
        self.cols2 = ('Receipt ID', 'Total', 'Patient ID', 'Receipt Date')
        
        self.listBox = Treeview(self.medtableframe, columns=self.cols1, show='headings')
        
        self.generate_medtable()
        self.window.mainloop()
        

    def medicineClicked(self):
        self.salesframe.pack_forget()
        self.medframe.pack(side=TOP, anchor=E)
        self.showtable()

    def salesClicked(self):
        self.medframe.pack_forget()
        self.listBtn.pack_forget()
        self.medtableframe.pack_forget()
        self.descframe.pack_forget()
        self.salesframe.pack(side=TOP, anchor=NE)

    def predictClicked(self):
        self.listBtn.pack(side=TOP, fill=X)

    def OnDoubleClick(self, event):
        row = self.listBox.focus()
        data = (self.listBox.item(row)['values'])
        self.destroywidgets(self.descframe)
        self.showdetails(data)

    def showdetails(self, item):
        for i in range(len(item)):
            Label(self.descframe, text=self.cols1[i] + ": " + str(item[i]), wraplength=1000).pack(side=TOP, anchor=W)
        self.descframe.pack(side=TOP)

    def destroywidgets(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

    def showtable(self):
        for row in self.medtable_results:
            self.listBox.insert("", "end", values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
        self.medtableframe.pack(side=TOP, anchor=W, fill=X)
        
    def generate_medtable(self):
        # Table for medicines

        self.listBox.bind("<Double-1>", self.OnDoubleClick)
        col_width = self.listBox.winfo_width()
        for col in self.cols1:
            self.listBox.heading(col, text=col)
            if col == 'Stock ID':
                self.listBox.column(col, anchor=W, width=col_width)
            else:
                self.listBox.column(col, anchor=E, width=col_width)
        self.listBox.pack(side=LEFT, expand=True, fill=BOTH)
        # Scroll bar
        scrollbar = Scrollbar(self.medtableframe, orient='vertical', command=self.listBox.yview)
        self.listBox.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=RIGHT, anchor=E, fill=Y)




if __name__ == '__main__':
    app = App()
