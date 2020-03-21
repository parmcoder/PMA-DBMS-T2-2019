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
        self.entryframe3 = Frame(self.window)
        self.submitframe = Frame(self.window)
<<<<<<< HEAD

        
=======

>>>>>>> master
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
        self.insertmedbtn = Button(self.insertselectionframe, text="Insert data into medicine table",
                                   command=self.insert_medicine_entry)
        self.insertsalesbtn = Button(self.insertselectionframe, text="Insert data into patient table",
                                     command=self.insert_patient_entry)
        self.insertpatientbtn = Button(self.insertselectionframe, text="Insert data into sales table",
                                       command=self.insert_receipt_entry)
        self.submitbtn1 = Button(self.submitframe, text='Submit', command=self.submit_insert_request_1)
        self.submitbtn2 = Button(self.submitframe, text='Submit', command=self.submit_insert_request_2)
        self.submitbtn3 = Button(self.submitframe, text='Submit', command=self.submit_insert_request_3)
        self.confirm = Button(self.entryframe3, text='Confirm', command=self.confirm_prescription_number)

        self.insert_label_1 = Label(self.entryframe1,
                                    text="Insert Stock ID, Expiration Date, Company name, Brand name, Description, Price and Quantity")
        self.insert_label_1.pack(side=TOP)

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

        self.insert_label_2 = Label(self.entryframe2, text="Insert Patient ID, Patient name, and allergy")
        self.insert_label_2.pack(side=TOP)

        self.insert_patient_entry1 = Entry(self.entryframe2, textvariable=self.insert_entry_data1)
        self.insert_patient_entry2 = Entry(self.entryframe2, textvariable=self.insert_entry_data2)
        self.insert_patient_entry3 = Entry(self.entryframe2, textvariable=self.insert_entry_data3)

        self.insert_patient_entry1.pack(side=TOP)
        self.insert_patient_entry2.pack(side=TOP)
        self.insert_patient_entry3.pack(side=TOP)

        self.insert_label_3 = Label(self.entryframe3,
                                    text="Insert Receipt ID, Total, Patient ID, Date, and number of prescriptions")
        self.insert_label_3.pack(side=TOP)

        self.insert_receipt_entry1 = Entry(self.entryframe3, textvariable=self.insert_entry_data1)
        self.insert_receipt_entry2 = Entry(self.entryframe3, textvariable=self.insert_entry_data2)
        self.insert_receipt_entry3 = Entry(self.entryframe3, textvariable=self.insert_entry_data3)
        self.insert_receipt_entry4 = Entry(self.entryframe3, textvariable=self.insert_entry_data4)
        self.insert_receipt_entry5 = Entry(self.entryframe3, textvariable=self.insert_entry_data5)

        self.insert_receipt_entry1.pack(side=TOP)
        self.insert_receipt_entry2.pack(side=TOP)
        self.insert_receipt_entry3.pack(side=TOP)
        self.insert_receipt_entry4.pack(side=TOP)
        self.insert_receipt_entry5.pack(side=TOP)
<<<<<<< HEAD

        
        
=======
        self.insertBtn = Button(self.btnframe, text="Insert data")
        self.modifyBtn = Button(self.btnframe, text="Modify data", command=self.updateClicked)
        self.deleteBtn = Button(self.btnframe, text="Delete data")
        self.expBtn = Button(self.medframe, text="Expiring", command=self.expiredclicked)
        self.predictBtn = Button(self.salesframe, text="Prediction", command=self.predictClicked)
        self.listBtn = Button(self.salesframe, text="List")

        # Parm's updateGUI - start
        self.uchoose = Frame(self.window)
        self.um_update = Frame(self.window)
        self.up_update = Frame(self.window)
        self.ur_dictionaryframe = Frame(self.window)
        self.ur_modifyframe = Frame(self.window)

        self.updateValues = []  # update values
        self.updateDictionary = {}  # dictionary

        ##Choose table
        self.update_choose_label1 = Label(self.uchoose, text="Choose the table that you want to update")
        self.update_choose_label1.grid(column=1, row=2, padx=10, pady=10)

        self.choose_medicine = Button(self.uchoose, text='Medicines', command=self.update_chooseMedicineClicked)
        self.choose_medicine.grid(column=2, row=2, padx=10, pady=10)
        self.choose_rp = Button(self.uchoose, text='Sales', command=self.update_chooseRpClicked)
        self.choose_rp.grid(column=3, row=2, padx=10, pady=10)
        self.choose_patient = Button(self.uchoose, text='Patients', command=self.update_choosePatientClicked)
        self.choose_patient.grid(column=4, row=2, padx=10, pady=10)

        ##Medicine
        self.update_med_label1 = Label(self.um_update, text="Enter Your Stock_ID*")
        self.update_med_label1.grid(column=1, row=1)
        self.update_med_label2 = Label(self.um_update, text="Enter Your New Expire Date (YYYY-MM-DD)")
        self.update_med_label2.grid(column=1, row=2)
        self.update_med_label3 = Label(self.um_update, text="Enter The New Company Name")
        self.update_med_label3.grid(column=1, row=3)
        self.update_med_label4 = Label(self.um_update, text="Enter The New Brand Name")
        self.update_med_label4.grid(column=1, row=4)
        self.update_med_label5 = Label(self.um_update, text="Enter The Drug Description")
        self.update_med_label5.grid(column=1, row=5)
        self.update_med_label6 = Label(self.um_update, text="Enter The Price")
        self.update_med_label6.grid(column=1, row=6)
        self.update_med_label7 = Label(self.um_update, text="Enter The Quantity")
        self.update_med_label7.grid(column=1, row=7)

        self.um_stock_ID               = StringVar()
        self.um_exp_date_year_input    = StringVar()
        self.um_exp_date_month_input   = StringVar()
        self.um_exp_date_day_input     = StringVar()
        self.um_company_name           = StringVar()
        self.um_brand_name             = StringVar()
        self.um_description            = StringVar()
        self.um_price                  = StringVar()
        self.um_quantity               = StringVar()

        self.um_input_list1 = [self.um_stock_ID, self.um_exp_date_year_input,self.um_exp_date_month_input,
                               self.um_exp_date_day_input,self.um_company_name,self.um_brand_name,
                               self.um_description,self.um_price,self.um_quantity]

        self.um_stock_IDEntered             = Entry(self.um_update, width=20, textvariable=self.um_stock_ID)
        self.um_stock_IDEntered.grid(column=2, row=1, padx=5, pady=5)
        self.um_exp_date_year_inputEntered  = Entry(self.um_update, width=20, textvariable=self.um_exp_date_year_input)
        self.um_exp_date_year_inputEntered.grid(column=2, row=2, padx=5, pady=5)
        self.um_exp_date_month_inputEntered = Entry(self.um_update, width=20, textvariable=self.um_exp_date_month_input)
        self.um_exp_date_month_inputEntered.grid(column=3, row=2, padx=5, pady=5)
        self.um_exp_date_day_inputEntered   = Entry(self.um_update, width=20, textvariable=self.um_exp_date_day_input)
        self.um_exp_date_day_inputEntered.grid(column=4, row=2, padx=5, pady=5)
        self.um_company_nameEntered         = Entry(self.um_update, width=20, textvariable=self.um_company_name)
        self.um_company_nameEntered.grid(column=2, row=3, padx=5, pady=5)
        self.um_brand_nameEntered           = Entry(self.um_update, width=20, textvariable=self.um_brand_name)
        self.um_brand_nameEntered.grid(column=2, row=4, padx=5, pady=5)
        self.um_descriptionEntered          = Entry(self.um_update, width=20, textvariable=self.um_description)
        self.um_descriptionEntered.grid(column=2, row=5, padx=5, pady=5)
        self.um_priceEntered                = Entry(self.um_update, width=20, textvariable=self.um_price)
        self.um_priceEntered.grid(column=2, row=6, padx=5, pady=5)
        self.um_quantityEntered             = Entry(self.um_update, width=20, textvariable=self.um_quantity)
        self.um_quantityEntered.grid(column=2, row=7, padx=5, pady=5)

        self.um_updateButton1 = Button(self.um_update, text='Confirm',
                                            command=lambda: self.medUpdateConfirmedClicked(self.updateValues))
        self.um_updateButton1.grid(column=2, row=8, padx=5, pady=5)

        ##Patient
        self.update_patient_label1 = Label(self.up_update, text="Enter The Patient ID*")
        self.update_patient_label1.grid(column=1, row=1)
        self.update_patient_label2 = Label(self.up_update, text="Enter The Patient Name")
        self.update_patient_label2.grid(column=1, row=2)
        self.update_patient_label3 = Label(self.up_update, text="Enter The Patient Allergy")
        self.update_patient_label3.grid(column=1, row=3)

        self.up_patient_ID = StringVar()
        self.up_patient_name_input = StringVar()
        self.up_patient_allergy_input = StringVar()

        self.up_input_list1 = [self.up_patient_ID, self.up_patient_name_input, self.up_patient_allergy_input
                               ]

        self.um_patient_IDEntered = Entry(self.up_update, width=20, textvariable=self.up_patient_ID)
        self.um_patient_IDEntered.grid(column=2, row=1, padx=5, pady=5)
        self.um_patient_name_inputEntered = Entry(self.up_update, width=20, textvariable=self.up_patient_name_input)
        self.um_patient_name_inputEntered.grid(column=2, row=2, padx=5, pady=5)
        self.um_patient_allergy_inputEntered = Entry(self.up_update, width=20, textvariable=self.up_patient_allergy_input)
        self.um_patient_allergy_inputEntered.grid(column=2, row=3, padx=5, pady=5)

        self.um_updateButton1 = Button(self.up_update, text='Confirm',
                                       command=lambda: self.patientUpdateConfirmedClicked(self.updateValues))
        self.um_updateButton1.grid(column=2, row=8, padx=5, pady=5)
        ##RECEIPT
        self.r_label1 = Label(self.ur_modifyframe, text="Enter Your Receipt ID")
        self.r_label1.grid(column=1, row=1, padx=5, pady=5)
        self.r_label2 = Label(self.ur_modifyframe, text="Enter Your New Total Purchase")
        self.r_label2.grid(column=1, row=2, padx=5, pady=5)
        self.r_label3 = Label(self.ur_modifyframe, text="Enter The New Patient ID")
        self.r_label3.grid(column=1, row=3, padx=5, pady=5)
        self.r_label4 = Label(self.ur_modifyframe, text="Enter The New Receipt Date (YYYY-MM-DD)")
        self.r_label4.grid(column=1, row=4, padx=5, pady=5)
        self.r_label5 = Label(self.ur_modifyframe, text="How Many Drugs Info Needed To Be Changed? (Max: 5)")
        self.r_label5.grid(column=1, row=5, padx=5, pady=5)

        self.rid_input = StringVar()
        self.total_input = StringVar()
        self.pid_input = StringVar()
        self.r_year_input = StringVar()
        self.r_month_input = StringVar()
        self.r_day_input = StringVar()
        self.keys_count = StringVar()

        self.ur_input_list1 = [self.rid_input, self.total_input, self.pid_input,
                               self.r_year_input, self.r_month_input, self.r_day_input]

        self.rid_inputEntered = Entry(self.ur_modifyframe, width=20, textvariable=self.rid_input)
        self.rid_inputEntered.grid(column=2, row=1, padx=5, pady=5)
        self.total_inputEntered = Entry(self.ur_modifyframe, width=20, textvariable=self.total_input)
        self.total_inputEntered.grid(column=2, row=2, padx=5, pady=5)
        self.pid_inputEntered = Entry(self.ur_modifyframe, width=20, textvariable=self.pid_input)
        self.pid_inputEntered.grid(column=2, row=3, padx=5, pady=5)
        self.r_year_inputEntered = Entry(self.ur_modifyframe, width=20, textvariable=self.r_year_input)
        self.r_year_inputEntered.grid(column=2, row=4, padx=5, pady=5)
        self.r_month_inputEntered = Entry(self.ur_modifyframe, width=20, textvariable=self.r_month_input)
        self.r_month_inputEntered.grid(column=3, row=4, padx=5, pady=5)
        self.r_day_inputEntered = Entry(self.ur_modifyframe, width=20, textvariable=self.r_day_input)
        self.r_day_inputEntered.grid(column=4, row=4, padx=5, pady=5)
        self.keys_countEntered = Entry(self.ur_modifyframe, width=20, textvariable=self.keys_count)
        self.keys_countEntered.grid(column=2, row=5, padx=5, pady=5)

        self.ur_modifyFrameButton1 = Button(self.ur_modifyframe, text='Confirm',
                                            command=lambda: self.updateConfirmedClicked(self.updateValues,
                                                                                        self.keys_count.get()))

        ##Prescription
        self.pre_label1 = Label(self.ur_dictionaryframe, text="Enter The First Drug ID and Quantity Respectively")
        self.pre_label2 = Label(self.ur_dictionaryframe, text="Enter The Second Drug ID and Quantity Respectively")
        self.pre_label3 = Label(self.ur_dictionaryframe, text="Enter The Third Drug ID and Quantity Respectively")
        self.pre_label4 = Label(self.ur_dictionaryframe, text="Enter The Fourth Drug ID and Quantity Respectively")
        self.pre_label5 = Label(self.ur_dictionaryframe, text="Enter The Fifth Drug ID and Quantity Respectively")

        self.drug_ID_input1 = StringVar()
        self.drug_ID_input2 = StringVar()
        self.drug_ID_input3 = StringVar()
        self.drug_ID_input4 = StringVar()
        self.drug_ID_input5 = StringVar()

        self.quantity_input1 = StringVar()
        self.quantity_input2 = StringVar()
        self.quantity_input3 = StringVar()
        self.quantity_input4 = StringVar()
        self.quantity_input5 = StringVar()

        self.ur_input_dict = [self.drug_ID_input1, self.quantity_input1,
                              self.drug_ID_input2, self.quantity_input2,
                              self.drug_ID_input3, self.quantity_input3,
                              self.drug_ID_input4, self.quantity_input4,
                              self.drug_ID_input5, self.quantity_input5,
                              ]

        self.drug_ID_input1Entered = Entry(self.ur_dictionaryframe, width=20, textvariable= self.drug_ID_input1)
        self.quantity_input1Entered = Entry(self.ur_dictionaryframe, width=20, textvariable= self.quantity_input1)

        self.drug_ID_input2Entered = Entry(self.ur_dictionaryframe, width=20, textvariable=self.drug_ID_input2)
        self.quantity_input2Entered = Entry(self.ur_dictionaryframe, width=20, textvariable=self.quantity_input2)

        self.drug_ID_input3Entered = Entry(self.ur_dictionaryframe, width=20, textvariable=self.drug_ID_input3)
        self.quantity_input3Entered = Entry(self.ur_dictionaryframe, width=20, textvariable=self.quantity_input3)

        self.drug_ID_input4Entered = Entry(self.ur_dictionaryframe, width=20, textvariable=self.drug_ID_input4)
        self.quantity_input4Entered = Entry(self.ur_dictionaryframe, width=20, textvariable=self.quantity_input4)

        self.drug_ID_input5Entered = Entry(self.ur_dictionaryframe, width=20, textvariable=self.drug_ID_input5)
        self.quantity_input5Entered = Entry(self.ur_dictionaryframe, width=20, textvariable=self.quantity_input5)

        self.up_showEntries_list = [self.pre_label1, self.drug_ID_input1Entered, self.quantity_input1Entered,
                                    self.pre_label2, self.drug_ID_input2Entered, self.quantity_input2Entered,
                                    self.pre_label3, self.drug_ID_input3Entered, self.quantity_input3Entered,
                                    self.pre_label4, self.drug_ID_input4Entered, self.quantity_input4Entered,
                                    self.pre_label5, self.drug_ID_input5Entered, self.quantity_input5Entered,
                                    ]

        self.up_ConfirmButton = Button(self.ur_dictionaryframe, text='Confirm',
                                   command=lambda: self.updateConfirmedClicked2(self.updateValues, self.updateDictionary))

        # Parm's updateGUI - end

>>>>>>> master
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
self.submitframe.pack(side=LEFT, padx=20)
<<<<<<< HEAD

       
        
=======

>>>>>>> master
        self.cols1 = ('Stock ID', 'Expiration Date', 'Company name', 'Brand name', 'Description', 'Price', 'Quantity')
        self.cols2 = (
        'Expired', 'Stock ID', 'Expiration Date', 'Company name', 'Brand name', 'Description', 'Price', 'Quantity')
        self.cols3 = ('Receipt ID', 'Total', 'Patient ID', 'Receipt Date')
        self.cols4 = ('Patient ID', 'Name', 'Allergy')
        self.cols5 = ('Restocking amount', 'Sold amount', 'Amount left', 'Stock ID')
<<<<<<< HEAD

        
=======

>>>>>>> master
        self.medicinetable = Treeview(self.medtableframe, columns=self.cols1, show='headings')
        self.medicinetable.bind("<Double-1>", lambda event: self.OnDoubleClick(self.medicinetable, self.cols1))
        self.exptable = Treeview(self.exptableframe, columns=self.cols2, show='headings')
        self.exptable.bind("<Double-1>", lambda event: self.OnDoubleClick(self.exptable, self.cols2))
        self.receipttable = Treeview(self.salestableframe, columns=self.cols3, show='headings')
        self.receipttable.bind("<Double-1>", lambda event: self.OnDoubleClick(self.receipttable, self.cols3))
        self.patienttable = Treeview(self.patienttableframe, columns=self.cols4, show='headings')
        self.patienttable.bind("<Double-1>", lambda event: self.OnDoubleClick(self.patienttable, self.cols4))
        self.buylisttable = Treeview(self.buylistframe, columns=self.cols5, show='headings')
<<<<<<< HEAD

        
        
=======

>>>>>>> master
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
<<<<<<< HEAD

        
=======

>>>>>>> master
        self.image = Image.open("processed.png")
        self.image = self.image.resize((900, 500), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.image)

        Label(self.predictframe, image=self.img).pack()

        self.window.mainloop()    def confirm_prescription_number(self):
        getvar1 = self.insert_receipt_entry5.get()

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
        getvar1 = self.insert_patient_entry1.get()
        getvar2 = self.insert_patient_entry2.get()
        getvar3 = self.insert_patient_entry3.get()

        values = [getvar1, getvar2, getvar3]
        print(values)


    def submit_insert_request_3(self):
        getvar1 = self.insert_receipt_entry1.get()
        getvar2 = self.insert_receipt_entry2.get()
        getvar3 = self.insert_receipt_entry3.get()
        getvar4 = self.insert_receipt_entry4.get()

        values = [getvar1, getvar2, getvar3, getvar4]

    def medicineClicked(self):
        self.buylistframe.pack_forget()

<<<<<<< HEAD
        

=======

    def medicineClicked(self):
        self.hide_update()
>>>>>>> master
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
        self.hide_update()
        self.medtableframe.pack_forget()
        self.descframe.pack_forget()
        self.showtable(self.exptableframe)

    def salesClicked(self):
        self.buylistframe.pack_forget()
<<<<<<< HEAD

=======
        self.hide_update()
>>>>>>> master
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

<<<<<<< HEAD

=======
        self.hide_update()
>>>>>>> master
        self.salestableframe.pack_forget()
        self.descframe.pack_forget()
        self.showtable(self.predictframe)
        self.listBtn.pack(side=TOP, fill=X)

    def patientclicked(self):
        self.buylistframe.pack_forget()
<<<<<<< HEAD

=======
        self.hide_update()
>>>>>>> master
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
        self.submitbtn2.pack_forget()
        self.entryframe3.pack_forget()
        self.submitbtn3.pack_forget()

        self.entryframe1.pack(side=TOP, anchor=W, padx=20)
        self.submitbtn1.pack()

        
    def insert_patient_entry(self):
        self.entryframe1.pack_forget()
        self.submitbtn1.pack_forget()
        self.entryframe3.pack_forget()
        self.submitbtn3.pack_forget()

        self.entryframe2.pack(side=TOP, anchor=W, padx=20)
        self.submitbtn2.pack()
        
        
    def insert_receipt_entry(self):
        self.entryframe1.pack_forget()
        self.submitbtn1.pack_forget()
        self.entryframe2.pack_forget()
        self.submitbtn2.pack_forget()
        
        self.entryframe3.pack(side=TOP, anchor=W, padx=20)
        self.submitbtn3.pack()
        self.confirm.pack()
        

    # Parm's updateFunction - start

    def patientUpdateConfirmedClicked(self, storage):
        storage.clear()
        if len(self.up_input_list1[0].get()) == 0 :
            return

        for i in range(len(self.up_input_list1)):
            if len(self.up_input_list1[i].get()) == 0:
                storage.append(None)
            else:
                storage.append(self.up_input_list1[i].get())
        print(storage)
        backend_functions.update_patient_table(storage)
        self.hide_update()

    def medUpdateConfirmedClicked(self, storage):
        storage.clear()
        if len(self.um_input_list1[0].get()) == 0:
            return
        date = self.um_input_list1[1].get() + "-" + self.um_input_list1[2].get() + "-" + self.um_input_list1[3].get()
        for i in range(len(self.um_input_list1)):
            if len(self.um_input_list1[i].get()) == 0:
                storage.append(None)
            else:
                storage.append(self.um_input_list1[i].get())
            if i == 0:
                storage.append(date)
                i = i + 3
        print(storage)
        backend_functions.update_medicine_table(storage)
        self.hide_update()

    def updateConfirmedClicked(self, storage, count):
        storage.clear()
        if int(count)>5 or len(self.ur_input_list1[3].get()) != 4 or \
                len(self.ur_input_list1[4].get()) != 2 or len(self.ur_input_list1[5].get()) != 2:
            return
        for i in range(len(self.ur_input_list1)):
            if len(self.ur_input_list1[i].get()) == 0:
                storage.append(None)
            if i < 3 and len(self.ur_input_list1[i].get()) != 0:
                storage.append(self.ur_input_list1[i].get())
        date = self.ur_input_list1[3].get() + "-" + self.ur_input_list1[4].get() + "-" + self.ur_input_list1[5].get()
        storage.append(date)
        print(storage)

        for i in range(0, int(count)*3, 3):
            self.up_showEntries_list[i].grid(column=1, row=int(i/3), padx=5, pady=5)
            self.up_showEntries_list[i+1].grid(column=2, row=int(i/3), padx=5, pady=5)
            self.up_showEntries_list[i+2].grid(column=3, row=int(i/3), padx=5, pady=5)

        self.ur_dictionaryframe.pack(side=TOP, fill=X)
        self.ur_modifyFrameButton1.grid_forget()
        self.up_ConfirmButton.grid(column=3, row=5, padx=5, pady=5)

    def updateConfirmedClicked2(self, listPointer, dictPointer : dict):
        dictPointer.clear()
        for i in range(0, len(self.ur_input_dict), 2):
            if len(self.ur_input_dict[i].get()) > 0:
                dictPointer[self.ur_input_dict[i].get()] = self.ur_input_dict[i+1].get()
        print(dictPointer)
        self.up_ConfirmButton.grid_forget()
        self.hide_update()
        backend_functions.update_receipt_prescription_table(listPointer, dictPointer)

    def update_chooseRpClicked(self):
        self.hide_update()
        self.ur_modifyframe.pack(side=TOP, fill=X)
        self.ur_modifyFrameButton1.grid(column=3, row=5, padx=5, pady=5)

    def update_chooseMedicineClicked(self):
        self.hide_update()
        self.um_update.pack(side=TOP, fill=X)

    def update_choosePatientClicked(self):
        self.hide_update()
        self.up_update.pack(side=TOP, fill=X)

    def updateClicked(self):
        self.hide_update()
        self.medframe.pack_forget()
        self.salesframe.pack_forget()
        self.descframe.pack_forget()
        self.exptableframe.pack_forget()
        self.salestableframe.pack_forget()
        self.patientframe.pack_forget()
        self.patienttableframe.pack_forget()
        self.medtableframe.pack_forget()
        self.uchoose.pack(side=TOP, fill=X)

    def hide_update(self):
        self.uchoose.pack_forget()
        self.um_update.pack_forget()
        self.up_update.pack_forget()
        self.ur_dictionaryframe.pack_forget()
        self.ur_modifyframe.pack_forget()
    # Parm's updateFunction - end

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
<<<<<<< HEAD


        
=======

>>>>>>> master
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
                    row[0], row[1][0], row[1][1], row[1][2], row[1][3], row[1][4], row[1][5], row[1][6]),
                                     tags=('expired',))
            else:
                self.exptable.insert("", "end", values=(
                row[0], row[1][0], row[1][1], row[1][2], row[1][3], row[1][4], row[1][5], row[1][6]))
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
<<<<<<< HEAD
            
    

        
=======
>>>>>>> master


if __name__ == '__main__':
    app = App()
