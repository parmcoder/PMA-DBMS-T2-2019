from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image
import backend_functions

class App:
    def __init__(self):
        self.window = Tk()
        self.window.title("PMA")
        self.window.geometry("1200x600")
        self.btnframe = Frame(self.window)
        self.medframe = Frame(self.window)
        self.medtableframe = Frame(self.window)
        self.exptableframe = Frame(self.window)
        self.salesframe = Frame(self.window)
        self.salestableframe = Frame(self.window)
        self.patientframe = Frame(self.window)
        self.patienttableframe = Frame(self.window)
        self.descframe = Frame(self.window)
        self.predictframe = Frame(self.window)
        
        self.medtable_results = backend_functions.get_medicine_table()
        self.expire_results = backend_functions.nearest_expire_date()
        self.receipt_results = backend_functions.get_receipt_table()
        self.patient_results = backend_functions.get_patient_table()
        self.buylist_results = backend_functions.predict_restock()[0]
        print(self.buylist_results)
        Label(self.window, text="Pharmacist Medical Analyzer").pack()

        self.medicineBtn = Button(self.btnframe, text="Medicines", command=self.medicineClicked)
        self.salesBtn = Button(self.btnframe, text="Sales", command=self.salesClicked)
        self.patientBtn = Button(self.btnframe, text="Patients", command=self.patientclicked)
        self.insertBtn = Button(self.btnframe, text="Insert data")
        self.modifyBtn = Button(self.btnframe, text="Modify data")
        self.deleteBtn = Button(self.btnframe, text="Delete data")
        self.expBtn = Button(self.medframe, text="Expiring", command=self.expiredclicked)
        self.predictBtn = Button(self.salesframe, text="Prediction", command=self.predictClicked)
        self.listBtn = Button(self.salesframe, text="List")

        self.medicineBtn.pack(side=LEFT)
        self.salesBtn.pack(side=LEFT)
        self.patientBtn.pack(side=LEFT)
        self.insertBtn.pack(side=LEFT)
        self.modifyBtn.pack(side=LEFT)
        self.deleteBtn.pack(side=LEFT)
        self.predictBtn.pack(side=TOP, fill=X)
        self.expBtn.pack(side=TOP, fill=X)
        self.btnframe.pack(side=TOP, anchor=W)
        
        self.cols1 = ('Stock ID', 'Expiration Date', 'Company name', 'Brand name', 'Description', 'Price', 'Quantity')
        self.cols2 = ('Expired', 'Stock ID', 'Expiration Date', 'Company name', 'Brand name', 'Description', 'Price', 'Quantity') 
        self.cols3 = ('Receipt ID', 'Total', 'Patient ID', 'Receipt Date')
        self.cols4 = ('Patient ID', 'Name', 'Allergy')
        
        self.medicinetable = Treeview(self.medtableframe, columns=self.cols1, show='headings')
        self.medicinetable.bind("<Double-1>", lambda event: self.OnDoubleClick(self.medicinetable, self.cols1))
        self.exptable = Treeview(self.exptableframe, columns=self.cols2, show='headings')
        self.exptable.bind("<Double-1>", lambda event: self.OnDoubleClick(self.exptable, self.cols2))
        self.receipttable = Treeview(self.salestableframe, columns=self.cols3, show='headings')
        self.receipttable.bind("<Double-1>", lambda event: self.OnDoubleClick(self.receipttable, self.cols3))
        self.patienttable = Treeview(self.patienttableframe, columns=self.cols4, show='headings')
        self.patienttable.bind("<Double-1>", lambda event: self.OnDoubleClick(self.patienttable, self.cols4))
        
        self.generate_medtable()
        self.generate_exptable()
        self.generate_receipttable()
        self.generate_patienttable()
        self.medicinetable.pack(side=LEFT, expand=True, fill=BOTH)
        self.exptable.pack(side=LEFT, expand=True, fill=BOTH)
        self.receipttable.pack(side=LEFT, expand=True, fill=BOTH)
        self.patienttable.pack(side=LEFT, expand=True, fill=BOTH)
        
        self.image = Image.open("processed.png")
        self.image = self.image.resize((900,500), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.image)
        
        Label(self.predictframe, image=self.img).pack()
        
        self.window.mainloop()
        

    def medicineClicked(self):
        self.predictframe.pack_forget()
        self.salesframe.pack_forget()
        self.exptableframe.pack_forget()
        self.descframe.pack_forget()
        self.salestableframe.pack_forget()
        self.patienttableframe.pack_forget()
        self.medframe.pack(side=TOP, anchor=E)
        self.showtable(self.medtableframe)
        
    def expiredclicked(self):
        self.medtableframe.pack_forget()
        self.descframe.pack_forget()
        self.showtable(self.exptableframe)

    def salesClicked(self):
        self.predictframe.pack_forget()
        self.medframe.pack_forget()
        self.listBtn.pack_forget()
        self.medtableframe.pack_forget()
        self.descframe.pack_forget()
        self.exptableframe.pack_forget()
        self.patienttableframe.pack_forget()
        self.salesframe.pack(side=TOP, anchor=NE)
        self.showtable(self.salestableframe)

    def predictClicked(self):
        self.salestableframe.pack_forget()
        self.descframe.pack_forget()
        self.predictframe.pack(side=TOP, fill=BOTH, expand=True)
        self.listBtn.pack(side=TOP, fill=X)
        
    def patientclicked(self):
        self.predictframe.pack_forget()
        self.medframe.pack_forget()
        self.salesframe.pack_forget()
        self.descframe.pack_forget()
        self.exptableframe.pack_forget()
        self.salestableframe.pack_forget()
        self.medtableframe.pack_forget()
        self.showtable(self.patienttableframe)

    def OnDoubleClick(self, table, cols):
        row = table.focus()
        data = (table.item(row)['values'])
        self.destroywidgets(self.descframe)
        self.showdetails(data, cols)

    def showdetails(self, item, cols):
        for i in range(len(item)):
            Label(self.descframe, text=cols[i] + ": " + str(item[i]), wraplength=1000).pack(side=TOP, anchor=W)
        self.descframe.pack(side=TOP)

    def destroywidgets(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

    def showtable(self, frame):

        frame.pack(side=TOP, anchor=W, fill=X)
        
    def generate_medtable(self):
        # Table for medicines
        col_width = self.medicinetable.winfo_width()
        for col in self.cols1:
            self.medicinetable.heading(col, text=col)
            if col == 'Stock ID':
                self.medicinetable.column(col, anchor=W, width=col_width)
            else:
                self.medicinetable.column(col, anchor=E, width=col_width)

        # Scroll bar
        scrollbar = Scrollbar(self.medtableframe, orient='vertical', command=self.medicinetable.yview)
        self.medicinetable.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=RIGHT, anchor=E, fill=Y)
        for row in self.medtable_results:
            self.medicinetable.insert("", "end", values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
        
    def generate_exptable(self):
        col_width = self.exptable.winfo_width()
        for col in self.cols2:
            self.exptable.heading(col, text=col)
            if col == 'Expired':
                self.exptable.column(col, anchor=E, width=col_width)
            else:
                self.exptable.column(col, anchor=E, width=col_width)
        # Scroll bar
        scrollbar = Scrollbar(self.exptableframe, orient='vertical', command=self.exptable.yview)
        self.exptable.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=RIGHT, anchor=E, fill=Y)
        
        for row in self.expire_results:
            if row[0]:
                self.exptable.insert("", "end", values=(
                row[0], row[1][0], row[1][1], row[1][2], row[1][3], row[1][4], row[1][5], row[1][6]), tags = ('expired',))
            else:
                self.exptable.insert("", "end", values=(row[0], row[1][0], row[1][1], row[1][2], row[1][3], row[1][4], row[1][5], row[1][6]))
        self.exptable.tag_configure('expired', background='red')


    def generate_receipttable(self):
        col_width = self.receipttable.winfo_width()
        for col in self.cols3:
            self.receipttable.heading(col, text=col)
            self.receipttable.column(col, anchor=E, width=col_width)
        # Scroll bar
        scrollbar = Scrollbar(self.salestableframe, orient='vertical', command=self.receipttable.yview)
        self.receipttable.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=RIGHT, anchor=E, fill=Y)
        
        for row in self.receipt_results:
            self.receipttable.insert("", "end", values=(row[0], row[1], row[2], row[3]))
            
            
    def generate_patienttable(self):
        col_width = self.patienttable.winfo_width()
        for col in self.cols4:
            self.patienttable.heading(col, text=col)
            self.patienttable.column(col, anchor=W, width=col_width)
        scrollbar = Scrollbar(self.patienttableframe, orient='vertical', command=self.patienttable.yview)
        self.patienttable.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=RIGHT, anchor=E, fill=Y)
        
        for row in self.patient_results:
            self.patienttable.insert("", "end", values=(row[0], row[1], row[2]))
        
        


if __name__ == '__main__':
    app = App()
