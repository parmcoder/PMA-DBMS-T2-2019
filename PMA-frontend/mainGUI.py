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
        self.insertselectionframe = Frame(self.window)
        self.medframe = Frame(self.window)
        self.medtableframe = Frame(self.window)
        self.exptableframe = Frame(self.window)
        self.salesframe = Frame(self.window)
        self.salestableframe = Frame(self.window)
        self.patienttableframe = Frame(self.window)
        self.descframe = Frame(self.window)
        self.predictframe = Frame(self.window)
        self.buylistframe = Frame(self.window)
        self.entryframe1 = Frame(self.window)
        self.entryframe2 = Frame(self.window)
        self.submitframe = Frame(self.window)
        
        self.medtable_results = backend_functions.get_medicine_table()
        self.expire_results = backend_functions.nearest_expire_date()
        self.receipt_results = backend_functions.get_receipt_table()
        self.patient_results = backend_functions.get_patient_table()
        self.buylist_results = backend_functions.predict_restock()[0]
        Label(self.window, text="Pharmacist Medical Analyzer").pack()

        self.medicineBtn = Button(self.btnframe, text="Medicines", command=self.medicineClicked)
        self.salesBtn = Button(self.btnframe, text="Sales", command=self.salesClicked)
        self.patientBtn = Button(self.btnframe, text="Patients", command=self.patientclicked)
        self.insertBtn = Button(self.btnframe, text="Insert data", command=self.insertclicked)
        self.modifyBtn = Button(self.btnframe, text="Modify data")
        self.deleteBtn = Button(self.btnframe, text="Delete data")
        self.expBtn = Button(self.medframe, text="Expiring", command=self.expiredclicked)
        self.predictBtn = Button(self.salesframe, text="Prediction", command=self.predictClicked)
        self.listBtn = Button(self.salesframe, text="List", command=self.listclicked)
        self.insertmedbtn = Button(self.insertselectionframe, text="Insert data into medicine table", command=self.insert_medicine_entry)
        self.insertsalesbtn = Button(self.insertselectionframe, text="Insert data into sales table", command=self.insert_patient_entry)
        self.insertpatientbtn = Button(self.insertselectionframe, text="Insert data into patient table")
        self.submitbtn = Button(self.submitframe, text='Submit', command=self.submit_insert_request_1)
        
        
        self.insert_entry_data1 = StringVar()
        self.insert_entry_data2 = StringVar()
        self.insert_entry_data3 = StringVar()
        self.insert_entry_data4 = StringVar()
        self.insert_entry_data5 = StringVar()
        self.insert_entry_data6 = StringVar()
        self.insert_entry_data7 = StringVar()
        self.insert_entry1 = Entry(self.entryframe1, textvariable=self.insert_entry_data1)
        self.insert_entry2 = Entry(self.entryframe1, textvariable=self.insert_entry_data2)
        self.insert_entry3 = Entry(self.entryframe1, textvariable=self.insert_entry_data3)
        self.insert_entry4 = Entry(self.entryframe1, textvariable=self.insert_entry_data4)
        self.insert_entry5 = Entry(self.entryframe1, textvariable=self.insert_entry_data5)
        self.insert_entry6 = Entry(self.entryframe1, textvariable=self.insert_entry_data6)
        self.insert_entry7 = Entry(self.entryframe1, textvariable=self.insert_entry_data7)
        
        self.insert_entry1.pack(side=TOP)
        self.insert_entry2.pack(side=TOP)
        self.insert_entry3.pack(side=TOP)
        self.insert_entry4.pack(side=TOP)
        self.insert_entry5.pack(side=TOP)
        self.insert_entry6.pack(side=TOP)
        self.insert_entry7.pack(side=TOP)
        
        self.insert_patient_entry1 = Entry(self.entryframe2, textvariable=self.insert_entry_data1)
        self.insert_patient_entry2 = Entry(self.entryframe2, textvariable=self.insert_entry_data2)
        self.insert_patient_entry3 = Entry(self.entryframe2, textvariable=self.insert_entry_data3)
        
        self.insert_patient_entry1.pack(side=TOP)
        self.insert_patient_entry2.pack(side=TOP)
        self.insert_patient_entry3.pack(side=TOP)
        
        

        self.medicineBtn.pack(side=LEFT)
        self.salesBtn.pack(side=LEFT)
        self.patientBtn.pack(side=LEFT)
        self.insertBtn.pack(side=LEFT)
        self.modifyBtn.pack(side=LEFT)
        self.deleteBtn.pack(side=LEFT)
        self.predictBtn.pack(side=TOP, fill=X)
        self.expBtn.pack(side=TOP, fill=X)
        self.insertmedbtn.pack(side=LEFT)
        self.insertsalesbtn.pack(side=LEFT)
        self.insertpatientbtn.pack(side=LEFT)
        self.btnframe.pack(side=TOP, anchor=W)
        self.insert_entry1.pack(side=TOP, anchor=S)
        self.submitbtn.pack()
       
        
        self.cols1 = ('Stock ID', 'Expiration Date', 'Company name', 'Brand name', 'Description', 'Price', 'Quantity')
        self.cols2 = ('Expired', 'Stock ID', 'Expiration Date', 'Company name', 'Brand name', 'Description', 'Price', 'Quantity') 
        self.cols3 = ('Receipt ID', 'Total', 'Patient ID', 'Receipt Date')
        self.cols4 = ('Patient ID', 'Name', 'Allergy')
        self.cols5 = ('Restocking amount', 'Sold amount', 'Amount left', 'Stock ID')
        
        self.medicinetable = Treeview(self.medtableframe, columns=self.cols1, show='headings')
        self.medicinetable.bind("<Double-1>", lambda event: self.OnDoubleClick(self.medicinetable, self.cols1))
        self.exptable = Treeview(self.exptableframe, columns=self.cols2, show='headings')
        self.exptable.bind("<Double-1>", lambda event: self.OnDoubleClick(self.exptable, self.cols2))
        self.receipttable = Treeview(self.salestableframe, columns=self.cols3, show='headings')
        self.receipttable.bind("<Double-1>", lambda event: self.OnDoubleClick(self.receipttable, self.cols3))
        self.patienttable = Treeview(self.patienttableframe, columns=self.cols4, show='headings')
        self.patienttable.bind("<Double-1>", lambda event: self.OnDoubleClick(self.patienttable, self.cols4))
        self.buylisttable = Treeview(self.buylistframe, columns=self.cols5, show='headings')
        
        
        self.generate_medtable()
        self.generate_exptable()
        self.generate_receipttable()
        self.generate_patienttable()
        self.generate_buylisttable()
        self.medicinetable.pack(side=LEFT, expand=True, fill=BOTH)
        self.exptable.pack(side=LEFT, expand=True, fill=BOTH)
        self.receipttable.pack(side=LEFT, expand=True, fill=BOTH)
        self.patienttable.pack(side=LEFT, expand=True, fill=BOTH)
        self.buylisttable.pack(side=LEFT, expand=True, fill=BOTH)
        
        self.image = Image.open("processed.png")
        self.image = self.image.resize((900, 500), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.image)
        
        Label(self.predictframe, image=self.img).pack()
        
        self.window.mainloop()

    def submit_insert_request_1(self):
        getvar1 = self.insert_entry_data1.get()
        getvar2 = self.insert_entry_data2.get()
        getvar3 = self.insert_entry_data3.get()
        getvar4 = self.insert_entry_data4.get()
        getvar5 = self.insert_entry_data5.get()
        getvar6 = self.insert_entry_data6.get()
        getvar7 = self.insert_entry_data7.get()
        
        values = [getvar1, getvar2, getvar3, getvar4, getvar5, getvar6, getvar7]
        print(values)
        
        
    def submit_insert_request_2(self):
        getvar1 = self.insert_patient_entry1
        getvar2 = self.insert_patient_entry2
        getvar3 = self.insert_patient_entry3
        
        values = [getvar1, getvar2, getvar3]
        print(values)

    def medicineClicked(self):
        self.buylistframe.pack_forget()
        self.predictframe.pack_forget()
        self.salesframe.pack_forget()
        self.exptableframe.pack_forget()
        self.descframe.pack_forget()
        self.salestableframe.pack_forget()
        self.patienttableframe.pack_forget()
        self.insertselectionframe.pack_forget()
        self.medframe.pack(side=TOP, anchor=E)
        self.showtable(self.medtableframe)
        
    def expiredclicked(self):
        self.medtableframe.pack_forget()
        self.descframe.pack_forget()
        self.showtable(self.exptableframe)

    def salesClicked(self):
        self.buylistframe.pack_forget()
        self.predictframe.pack_forget()
        self.medframe.pack_forget()
        self.listBtn.pack_forget()
        self.medtableframe.pack_forget()
        self.descframe.pack_forget()
        self.exptableframe.pack_forget()
        self.patienttableframe.pack_forget()
        self.insertselectionframe.pack_forget()
        self.salesframe.pack(side=TOP, anchor=NE)
        self.showtable(self.salestableframe)

    def predictClicked(self):
        self.buylistframe.pack_forget()
        self.salestableframe.pack_forget()
        self.descframe.pack_forget()
        self.showtable(self.predictframe)
        self.listBtn.pack(side=TOP, fill=X)
        
    def patientclicked(self):
        self.buylistframe.pack_forget()
        self.predictframe.pack_forget()
        self.medframe.pack_forget()
        self.salesframe.pack_forget()
        self.descframe.pack_forget()
        self.exptableframe.pack_forget()
        self.salestableframe.pack_forget()
        self.medtableframe.pack_forget()
        self.insertselectionframe.pack_forget()
        self.showtable(self.patienttableframe)
        
    def listclicked(self):
        self.predictframe.pack_forget()
        self.showtable(self.buylistframe)
        
        
    def insertclicked(self):
        self.buylistframe.pack_forget()
        self.predictframe.pack_forget()
        self.medframe.pack_forget()
        self.salesframe.pack_forget()
        self.descframe.pack_forget()
        self.exptableframe.pack_forget()
        self.salestableframe.pack_forget()
        self.medtableframe.pack_forget()
        self.patienttableframe.pack_forget()
        self.insertselectionframe.pack(side=TOP, anchor=W, pady=20)
        
    def insert_medicine_entry(self):
        self.entryframe2.pack_forget()
        self.submitframe.pack_forget()
        self.entryframe1.pack(side=TOP, anchor=W, padx=20)
        self.submitframe.pack(side=TOP, anchor=W, padx=20)
        
    def insert_patient_entry(self):
        self.entryframe1.pack_forget()
        self.submitframe.pack_forget()
        self.entryframe2.pack(side=TOP, anchor=W, padx=20)
        self.submitframe.pack(side=TOP, anchor=W, padx=20)

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

        frame.pack(side=TOP, anchor=W, fill=BOTH)
        
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
            
    
    def generate_buylisttable(self):
        col_width = self.buylisttable.winfo_width()
        for col in self.cols5:
            self.buylisttable.heading(col, text=col)
            self.buylisttable.column(col, anchor=W, width=col_width)
        scrollbar = Scrollbar(self.buylistframe, orient='vertical', command=self.buylisttable.yview)
        self.buylisttable.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=RIGHT, anchor=E, fill=Y)

        for row in self.buylist_results:
            self.buylisttable.insert("", "end", values=(row[0], row[1][0], row[1][1], row[1][2]))
        


if __name__ == '__main__':
    app = App()
