from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image
import backend_functions

class App:
    def __init__(self):
        # Initialize all frames, buttons, and data
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
        self.modifyBtn = Button(self.btnframe, text="Modify data", command=self.updateClicked)
        self.deleteBtn = Button(self.btnframe, text="Delete data")
        self.expBtn = Button(self.medframe, text="Expiring", command=self.expiredclicked)
        self.predictBtn = Button(self.salesframe, text="Prediction", command=self.predictClicked)
        self.listBtn = Button(self.salesframe, text="List", command=self.listclicked)




        # Insert
        self.ichoose = Frame(self.window)
        self.im_insert = Frame(self.window)
        self.ip_insert = Frame(self.window)
        self.ir_dictionaryframe = Frame(self.window)
        self.ir_modifyframe = Frame(self.window)

        self.insertValues = []  # update values
        self.insertDictionary = {}  # dictionary

        ##Choose table
        self.insert_choose_label1 = Label(self.ichoose, text="Choose the table that you want to insert")
        self.insert_choose_label1.grid(column=1, row=2, padx=10, pady=10)

        self.insert_choose_medicine = Button(self.ichoose, text='Medicines', command=self.insert_chooseMedicineClicked)
        self.insert_choose_medicine.grid(column=2, row=2, padx=10, pady=10)
        self.insert_choose_rp = Button(self.ichoose, text='Sales', command=self.insert_chooseRpClicked)
        self.insert_choose_rp.grid(column=3, row=2, padx=10, pady=10)
        self.insert_choose_patient = Button(self.ichoose, text='Patients', command=self.insert_choosePatientClicked)
        self.insert_choose_patient.grid(column=4, row=2, padx=10, pady=10)

        self.insert_med_label1 = Label(self.im_insert, text="Enter Your Stock_ID*")
        self.insert_med_label1.grid(column=1, row=1)
        self.insert_med_label2 = Label(self.im_insert, text="Enter Your Expire Date (YYYY-MM-DD)")
        self.insert_med_label2.grid(column=1, row=2)
        self.insert_med_label3 = Label(self.im_insert, text="Enter The Company Name")
        self.insert_med_label3.grid(column=1, row=3)
        self.insert_med_label4 = Label(self.im_insert, text="Enter The Brand Name")
        self.insert_med_label4.grid(column=1, row=4)
        self.insert_med_label5 = Label(self.im_insert, text="Enter The Drug Description")
        self.insert_med_label5.grid(column=1, row=5)
        self.insert_med_label6 = Label(self.im_insert, text="Enter The Price")
        self.insert_med_label6.grid(column=1, row=6)
        self.insert_med_label7 = Label(self.im_insert, text="Enter The Quantity")
        self.insert_med_label7.grid(column=1, row=7)

        self.im_stock_ID               = StringVar()
        self.im_exp_date_year_input    = StringVar()
        self.im_exp_date_month_input   = StringVar()
        self.im_exp_date_day_input     = StringVar()
        self.im_company_name           = StringVar()
        self.im_brand_name             = StringVar()
        self.im_description            = StringVar()
        self.im_price                  = StringVar()
        self.im_quantity               = StringVar()

        self.im_input_list1 = [self.im_stock_ID, self.im_exp_date_year_input,self.im_exp_date_month_input,
                               self.im_exp_date_day_input,self.im_company_name,self.im_brand_name,
                               self.im_description,self.im_price,self.im_quantity]

        self.im_stock_IDEntered             = Entry(self.im_insert, width=20, textvariable=self.im_stock_ID)
        self.im_stock_IDEntered.grid(column=2, row=1, padx=5, pady=5)
        self.im_exp_date_year_inputEntered  = Entry(self.im_insert, width=20, textvariable=self.im_exp_date_year_input)
        self.im_exp_date_year_inputEntered.grid(column=2, row=2, padx=5, pady=5)
        self.im_exp_date_month_inputEntered = Entry(self.im_insert, width=20, textvariable=self.im_exp_date_month_input)
        self.im_exp_date_month_inputEntered.grid(column=3, row=2, padx=5, pady=5)
        self.im_exp_date_day_inputEntered   = Entry(self.im_insert, width=20, textvariable=self.im_exp_date_day_input)
        self.im_exp_date_day_inputEntered.grid(column=4, row=2, padx=5, pady=5)
        self.im_company_nameEntered         = Entry(self.im_insert, width=20, textvariable=self.im_company_name)
        self.im_company_nameEntered.grid(column=2, row=3, padx=5, pady=5)
        self.im_brand_nameEntered           = Entry(self.im_insert, width=20, textvariable=self.im_brand_name)
        self.im_brand_nameEntered.grid(column=2, row=4, padx=5, pady=5)
        self.im_descriptionEntered          = Entry(self.im_insert, width=20, textvariable=self.im_description)
        self.im_descriptionEntered.grid(column=2, row=5, padx=5, pady=5)
        self.im_priceEntered                = Entry(self.im_insert, width=20, textvariable=self.im_price)
        self.im_priceEntered.grid(column=2, row=6, padx=5, pady=5)
        self.im_quantityEntered             = Entry(self.im_insert, width=20, textvariable=self.im_quantity)
        self.im_quantityEntered.grid(column=2, row=7, padx=5, pady=5)

        self.im_updateButton1 = Button(self.im_insert, text='Confirm',
                                            command=lambda: self.medInsertConfirmedClicked(self.insertValues))
        self.im_updateButton1.grid(column=2, row=8, padx=5, pady=5)

        ##Patient
        self.insert_patient_label1 = Label(self.ip_insert, text="Enter The Patient ID*")
        self.insert_patient_label1.grid(column=1, row=1)
        self.insert_patient_label2 = Label(self.ip_insert, text="Enter The Patient Name")
        self.insert_patient_label2.grid(column=1, row=2)
        self.insert_patient_label3 = Label(self.ip_insert, text="Enter The Patient Allergy")
        self.insert_patient_label3.grid(column=1, row=3)

        self.ip_patient_ID = StringVar()
        self.ip_patient_name_input = StringVar()
        self.ip_patient_allergy_input = StringVar()

        self.ip_input_list1 = [self.ip_patient_ID, self.ip_patient_name_input, self.ip_patient_allergy_input
                               ]

        self.ip_patient_IDEntered = Entry(self.ip_insert, width=20, textvariable=self.ip_patient_ID)
        self.ip_patient_IDEntered.grid(column=2, row=1, padx=5, pady=5)
        self.ip_patient_name_inputEntered = Entry(self.ip_insert, width=20, textvariable=self.ip_patient_name_input)
        self.ip_patient_name_inputEntered.grid(column=2, row=2, padx=5, pady=5)
        self.ip_patient_allergy_inputEntered = Entry(self.ip_insert, width=20, textvariable=self.ip_patient_allergy_input)
        self.ip_patient_allergy_inputEntered.grid(column=2, row=3, padx=5, pady=5)

        self.ip_updateButton1 = Button(self.ip_insert, text='Confirm',
                                       command=lambda: self.patientInsertConfirmedClicked(self.insertValues))
        self.ip_updateButton1.grid(column=2, row=8, padx=5, pady=5)
        ##RECEIPT
        self.insert_r_label1 = Label(self.ir_modifyframe, text="Enter Your Receipt ID")
        self.insert_r_label1.grid(column=1, row=1, padx=5, pady=5)
        self.insert_r_label2 = Label(self.ir_modifyframe, text="Enter Your Total Purchase")
        self.insert_r_label2.grid(column=1, row=2, padx=5, pady=5)
        self.insert_r_label3 = Label(self.ir_modifyframe, text="Enter The Patient ID")
        self.insert_r_label3.grid(column=1, row=3, padx=5, pady=5)
        self.insert_r_label4 = Label(self.ir_modifyframe, text="Enter The Receipt Date (YYYY-MM-DD)")
        self.insert_r_label4.grid(column=1, row=4, padx=5, pady=5)
        self.insert_r_label5 = Label(self.ir_modifyframe, text="How Many Drugs Info Needed To Be Inserted? (Max: 5)")
        self.insert_r_label5.grid(column=1, row=5, padx=5, pady=5)

        self.rid_input = StringVar()
        self.total_input = StringVar()
        self.pid_input = StringVar()
        self.r_year_input = StringVar()
        self.r_month_input = StringVar()
        self.r_day_input = StringVar()
        self.keys_count = StringVar()

        self.ir_input_list1 = [self.rid_input, self.total_input, self.pid_input,
                               self.r_year_input, self.r_month_input, self.r_day_input]

        self.insert_rid_inputEntered = Entry(self.ir_modifyframe, width=20, textvariable=self.rid_input)
        self.insert_rid_inputEntered.grid(column=2, row=1, padx=5, pady=5)
        self.insert_total_inputEntered = Entry(self.ir_modifyframe, width=20, textvariable=self.total_input)
        self.insert_total_inputEntered.grid(column=2, row=2, padx=5, pady=5)
        self.insert_pid_inputEntered = Entry(self.ir_modifyframe, width=20, textvariable=self.pid_input)
        self.insert_pid_inputEntered.grid(column=2, row=3, padx=5, pady=5)
        self.insert_r_year_inputEntered = Entry(self.ir_modifyframe, width=20, textvariable=self.r_year_input)
        self.insert_r_year_inputEntered.grid(column=2, row=4, padx=5, pady=5)
        self.insert_r_month_inputEntered = Entry(self.ir_modifyframe, width=20, textvariable=self.r_month_input)
        self.insert_r_month_inputEntered.grid(column=3, row=4, padx=5, pady=5)
        self.insert_r_day_inputEntered = Entry(self.ir_modifyframe, width=20, textvariable=self.r_day_input)
        self.insert_r_day_inputEntered.grid(column=4, row=4, padx=5, pady=5)
        self.insert_keys_countEntered = Entry(self.ir_modifyframe, width=20, textvariable=self.keys_count)
        self.insert_keys_countEntered.grid(column=2, row=5, padx=5, pady=5)

        self.ir_modifyFrameButton1 = Button(self.ir_modifyframe, text='Confirm',
                                            command=lambda: self.insertConfirmedClicked(self.insertValues,
                                                                                        self.keys_count.get()))

        ##Prescription
        self.insert_pre_label1 = Label(self.ir_dictionaryframe, text="Enter The First Drug ID and Quantity Respectively")
        self.insert_pre_label2 = Label(self.ir_dictionaryframe, text="Enter The Second Drug ID and Quantity Respectively")
        self.insert_pre_label3 = Label(self.ir_dictionaryframe, text="Enter The Third Drug ID and Quantity Respectively")
        self.insert_pre_label4 = Label(self.ir_dictionaryframe, text="Enter The Fourth Drug ID and Quantity Respectively")
        self.insert_pre_label5 = Label(self.ir_dictionaryframe, text="Enter The Fifth Drug ID and Quantity Respectively")

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

        self.ir_input_dict = [self.drug_ID_input1, self.quantity_input1,
                              self.drug_ID_input2, self.quantity_input2,
                              self.drug_ID_input3, self.quantity_input3,
                              self.drug_ID_input4, self.quantity_input4,
                              self.drug_ID_input5, self.quantity_input5,
                              ]

        self.insert_drug_ID_input1Entered = Entry(self.ir_dictionaryframe, width=20, textvariable= self.drug_ID_input1)
        self.insert_quantity_input1Entered = Entry(self.ir_dictionaryframe, width=20, textvariable= self.quantity_input1)

        self.insert_drug_ID_input2Entered = Entry(self.ir_dictionaryframe, width=20, textvariable=self.drug_ID_input2)
        self.insert_quantity_input2Entered = Entry(self.ir_dictionaryframe, width=20, textvariable=self.quantity_input2)

        self.insert_drug_ID_input3Entered = Entry(self.ir_dictionaryframe, width=20, textvariable=self.drug_ID_input3)
        self.insert_quantity_input3Entered = Entry(self.ir_dictionaryframe, width=20, textvariable=self.quantity_input3)

        self.insert_drug_ID_input4Entered = Entry(self.ir_dictionaryframe, width=20, textvariable=self.drug_ID_input4)
        self.insert_quantity_input4Entered = Entry(self.ir_dictionaryframe, width=20, textvariable=self.quantity_input4)

        self.insert_drug_ID_input5Entered = Entry(self.ir_dictionaryframe, width=20, textvariable=self.drug_ID_input5)
        self.insert_quantity_input5Entered = Entry(self.ir_dictionaryframe, width=20, textvariable=self.quantity_input5)

        self.ip_showEntries_list = [self.insert_pre_label1, self.insert_drug_ID_input1Entered, self.insert_quantity_input1Entered,
                                    self.insert_pre_label2, self.insert_drug_ID_input2Entered, self.insert_quantity_input2Entered,
                                    self.insert_pre_label3, self.insert_drug_ID_input3Entered, self.insert_quantity_input3Entered,
                                    self.insert_pre_label4, self.insert_drug_ID_input4Entered, self.insert_quantity_input4Entered,
                                    self.insert_pre_label5, self.insert_drug_ID_input5Entered, self.insert_quantity_input5Entered,
                                    ]

        self.ip_ConfirmButton = Button(self.ir_dictionaryframe, text='Confirm',
                                   command=lambda: self.insertConfirmedClicked2(self.insertValues, self.insertDictionary))


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

        # Pack all buttons and table.

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
        self.cols2 = (
        'Expired', 'Stock ID', 'Expiration Date', 'Company name', 'Brand name', 'Description', 'Price', 'Quantity')
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


    def medicineClicked(self):
        self.hide_update()
        self.hide_insert()
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
        self.hide_update()
        self.hide_insert()
        self.medtableframe.pack_forget()
        self.descframe.pack_forget()
        self.showtable(self.exptableframe)

    def salesClicked(self):
        self.buylistframe.pack_forget()
        self.hide_update()
        self.hide_insert()
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
        self.hide_update()
        self.hide_insert()
        self.salestableframe.pack_forget()
        self.descframe.pack_forget()
        self.showtable(self.predictframe)
        self.listBtn.pack(side=TOP, fill=X)

    def patientclicked(self):
        self.buylistframe.pack_forget()
        self.hide_update()
        self.hide_insert()
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
        self.hide_update()
        self.hide_insert()
        self.medframe.pack_forget()
        self.salesframe.pack_forget()
        self.descframe.pack_forget()
        self.exptableframe.pack_forget()
        self.salestableframe.pack_forget()
        self.patienttableframe.pack_forget()
        self.medtableframe.pack_forget()
        self.buylistframe.pack_forget()
        self.ichoose.pack(side=TOP, fill=X)

    def patientInsertConfirmedClicked(self, storage):
        storage.clear()
        if len(self.ip_input_list1[0].get()) == 0 :
            return

        for i in range(len(self.up_input_list1)):
            if len(self.ip_input_list1[i].get()) == 0:
                storage.append(None)
            else:
                storage.append(self.ip_input_list1[i].get())
        print(storage)
        backend_functions.insert_patient_table(storage)
        self.hide_insert()

    def medInsertConfirmedClicked(self, storage):
        storage.clear()
        if len(self.im_input_list1[0].get()) == 0:
            return
        date = self.im_input_list1[1].get() + "-" + self.im_input_list1[2].get() + "-" + self.im_input_list1[3].get()
        for i in range(len(self.im_input_list1)):
            if len(self.im_input_list1[i].get()) == 0:
                storage.append(None)
            else:
                storage.append(self.im_input_list1[i].get())
            if i == 0:
                storage.append(date)
                i = i + 3
        print(storage)
        backend_functions.insert_medicine_table(storage)
        self.hide_insert()

    def insertConfirmedClicked(self, storage, count):
        storage.clear()
        if int(count)>5 or len(self.ir_input_list1[3].get()) != 4 or \
                len(self.ir_input_list1[4].get()) != 2 or len(self.ir_input_list1[5].get()) != 2:
            return
        for i in range(len(self.ir_input_list1)):
            if len(self.ir_input_list1[i].get()) == 0:
                storage.append(None)
            if i < 3 and len(self.ir_input_list1[i].get()) != 0:
                storage.append(self.ir_input_list1[i].get())
        date = self.ir_input_list1[3].get() + "-" + self.ir_input_list1[4].get() + "-" + self.ir_input_list1[5].get()
        storage.append(date)
        print(storage)

        for i in range(0, int(count)*3, 3):
            self.ip_showEntries_list[i].grid(column=1, row=int(i/3), padx=5, pady=5)
            self.ip_showEntries_list[i+1].grid(column=2, row=int(i/3), padx=5, pady=5)
            self.ip_showEntries_list[i+2].grid(column=3, row=int(i/3), padx=5, pady=5)

        self.ir_dictionaryframe.pack(side=TOP, fill=X)
        self.ir_modifyFrameButton1.grid_forget()
        self.ip_ConfirmButton.grid(column=3, row=5, padx=5, pady=5)

    def insertConfirmedClicked2(self, listPointer, dictPointer : dict):
        dictPointer.clear()
        for i in range(0, len(self.ir_input_dict), 2):
            if len(self.ir_input_dict[i].get()) > 0:
                dictPointer[self.ir_input_dict[i].get()] = self.ir_input_dict[i+1].get()
        print(dictPointer)
        self.ip_ConfirmButton.grid_forget()
        self.hide_insert()
        backend_functions.insert_receipt_prescription_table(listPointer, dictPointer)

    def insert_chooseRpClicked(self):
        self.hide_insert()
        self.ir_modifyframe.pack(side=TOP, fill=X)
        self.ir_modifyFrameButton1.grid(column=3, row=5, padx=5, pady=5)

    def insert_chooseMedicineClicked(self):
        self.hide_insert()
        self.im_insert.pack(side=TOP, fill=X)

    def insert_choosePatientClicked(self):
        self.hide_insert()
        self.ip_insert.pack(side=TOP, fill=X)


    def hide_insert(self):
        self.ichoose.pack_forget()
        self.im_insert.pack_forget()
        self.ip_insert.pack_forget()
        self.ir_dictionaryframe.pack_forget()
        self.ir_modifyframe.pack_forget()
        

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
        self.hide_insert()
        self.medframe.pack_forget()
        self.salesframe.pack_forget()
        self.descframe.pack_forget()
        self.exptableframe.pack_forget()
        self.salestableframe.pack_forget()
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


if __name__ == '__main__':
    app = App()
