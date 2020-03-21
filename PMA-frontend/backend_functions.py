import psycopg2
import numpy as np
from matplotlib import pyplot as plt
import math
from scipy.optimize import minimize
import time
import datetime
"""
@Parm db_executer - execute on db4parm
Instruction: db_executer(query,mode,rows)
mode 0 is getting a single tuple of query.
*RETURN* -> tuple
mode 1 is getting whole list of tuples of query. That means you have to do result_set[tuple][attribute].
*RETURN* -> list of tuple with corresponding attributes
mode 2 is getting rows from whole list of result_set.
*RETURN* -> list of tuple with corresponding attributes
mode 3 is used for updating the tables. It just commit the changes, remember the transaction class?
*RETURN* -> None

When insertion finished, it will automatically commit for you :D
"""
def db_executer(query_i, mode=1, rows=1):

    conn = None
    pointer = query_i
    result_set = None
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(database="defaultdb", user="doadmin", password="de53jzgsny7bamuk",
                                host="db4parm-do-user-7150737-0.db.ondigitalocean.com", port="25060")
        # create a cursor
        cur = conn.cursor()

        # execute a statement
        print('PostgreSQL executing query: '+ pointer)

        cur.execute(pointer)

        # display the PostgreSQL database server version
        if mode == 0:
            result_set = cur.fetchone()
        elif mode == 1:
            result_set = cur.fetchall()
        elif mode == 2:
            result_set = cur.fetchmany(rows)
        elif mode == 3:
            conn.commit()
            print("COMMITTED")
        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
            return result_set

#Recall meeting discussion
"""
@Parm get_medicine_table - return sorted medicine table
Instruction: get_medicine_table()
*RETURN* -> list of tuple with corresponding attributes
"""
def get_medicine_table():
    med_query = "SELECT * FROM medicine order by stock_id"
    resultset = db_executer(med_query, 1, )
    # for i in resultset:
    #     print(i)
    return resultset

"""
@Parm get_medicine_rows - return sorted medicine rows with stock_id asked for
Instruction: get_medicine_rows(stock_id)
*RETURN* -> list of tuple with corresponding attributes
"""
def get_medicine_rows(ids):
    med_id_query = "SELECT * FROM medicine where stock_id = "
    ids_n = len(ids)
    for i, ele in enumerate(ids):
        med_id_query = med_id_query + str(ele)
        if i < ids_n-1 :
            med_id_query=med_id_query + " or stock_id = "
    med_id_query = med_id_query+" order by stock_id"
    resultset = db_executer(med_id_query, 1, )
    for i in resultset:
        print(i)
    return resultset

"""
@Parm get_patient_table - return sorted patient table
Instruction: get_patient_table()
*RETURN* -> list of tuple with corresponding attributes
"""
def get_patient_table():
    p_query = "SELECT * FROM patient order by pid"
    resultset = db_executer(p_query, 1, )
    # for i in resultset:
    #     print(i)
    return resultset

"""
@Parm get_receipt_table - return sorted receipt table
Instruction: get_receipt_table()
*RETURN* -> list of tuple with corresponding attributes
"""
def get_receipt_table():
    r_query = "SELECT * FROM receipt order by rid"
    resultset = db_executer(r_query, 1, )
    # for i in resultset:
    #     print(i)
    return resultset

"""
@Parm get_prescription_table - return sorted prescription table
Instruction: get_prescription_table()
*RETURN* -> list of tuple with corresponding attributes
"""
def get_prescription_table():
    pre_query = "SELECT * FROM prescription order by rid"
    resultset = db_executer(pre_query, 1, )
    return resultset

"""
@Parm update_medicine_table(update) - make changes to medicine table
Instruction: update_medicine_table(update) where update list must be put in this form
[stock_id*, exp_date, company_name, brand_name, description, price, quantity]
We assumed that there must be a change given in one of each value and stock_id must not be None
"""
def update_medicine_table(update):
    if update[0] is None:
        return
    iter_list_name = ["exp_date", "company_name", "brand_name", "description", "price", "quantity"]
    um_query = "UPDATE medicine SET "
    for i, attr in enumerate(iter_list_name):
        if update[i+1] is not None and (4 <= i <= 5):
            um_query = um_query + attr + " = " + str(update[i+1]) + ", "
        if update[i+1] is not None and (0 <= i <= 3):
            um_query = um_query + attr + " = \'" + str(update[i+1]) + "\', "
    um_query = um_query[:len(um_query)-2] + " WHERE stock_id = "+ str(update[0]) + ";"
    db_executer(um_query, 3, )

"""
@Parm update_receipt_prescription_table(values, prescription_dict) - make changes to receipt and prescription tables
Instruction: update_receipt_prescription_table(values, prescription_dict) where update list must be put in this form
[rid*, total, pid, r_date] , {stock_id: quantity}
We assumed that there must be a change given in one of each value and stock_id must not be None

EXAMPLE : 
    pre_dict = {234:43, 231:32, 646:32}
    update_receipt_prescription_table([123,None,34,"2020-01-10"], pre_dict)
"""
def update_receipt_prescription_table(values, prescription_dict):
    if values[0] is None:
        return
    iter_list_name = ["total", "pid", "r_date"]
    ur_query = "UPDATE receipt(rid, total, pid, r_date) SET "
    for i, attr in enumerate(iter_list_name):
        if values[i + 1] is not None and i<2:
            ur_query = ur_query + attr + " = " + str(values[i + 1]) + ", "
        if values[i + 1] is not None and i==2:
            ur_query = ur_query + attr + " = \'" + str(values[i + 1]) + "\', "
    ur_query = ur_query[:len(ur_query) - 2] + " WHERE rid = " + str(values[0]) + ";"
    db_executer(ur_query, 3, )

    for key_stock in prescription_dict.keys():
        upre_query = "UPDATE prescription(rid, stock_id, quantity) " + \
                             "SET quantity = "+ str(prescription_dict[key_stock]) + \
                             " WHERE rid = " + str(values[0]) + \
                             " and stock_id = "+ str(key_stock)
        db_executer(upre_query, 3, )


"""
@Parm update_patient_table(update) - make changes to patient table
Instruction: update_patient_table(update) where update list must be put in this form
[pid*, p_name, allergy]
We assumed that there must be a change given in one of each value and pid must not be None
"""
def update_patient_table(update):
    if update[0] is None:
        return
    iter_list_name = ["p_name", "allergy"]
    up_query = "UPDATE patient SET "
    for i, attr in enumerate(iter_list_name):
        if update[i + 1] is not None:
            up_query = up_query + attr + " = \'" + str(update[i + 1]) + "\', "
    up_query = up_query[:len(up_query) - 2] + " WHERE pid = " + str(update[0]) + ";"
    db_executer(up_query, 3, )

"""
@Parm insert_patient_table(values) - delete tuple with receipt_id from data, accept list only
Instruction: insert_patient_table(values) values follow attributes in the schemas
[pid, p_name, allergy]
*RETURN* -> None
"""
def insert_patient_table(values):
    pid, p_name, allergy = values
    ip_query = "INSERT INTO patient(pid, p_name, allergy) VALUES ("+str(pid)+",\'"+str(p_name)+"\',\'"+str(allergy)+"\')"
    db_executer(ip_query, 3, )

"""
@Parm insert_medicine_table(values) -  insert tuple with pid from data, accept list only
Instruction: insert_medicine_table(values) values follow attributes in the schemas
[stock_id, exp_date, company_name, brand_name, description, price, quantity]
*RETURN* -> None
"""
def insert_medicine_table(values):
    stock_id, exp_date, company_name, brand_name, description, price, quantity = values
    ip_query = "INSERT INTO patient(stock_id, exp_date, company_name, brand_name, description, price, quantity" \
               ") VALUES (" + str(stock_id) + ",\'" + str(exp_date) + "\',\'" + str(company_name) + "\',\'" + str(brand_name) + "\'," \
               "\'" + str(description) + "\'," + str(price) + "," + str(quantity) + ")"
    db_executer(ip_query, 3, )

"""
@Parm insert_receipt_prescription_table - insert tuple with receipt_id from data, accept list only
Instruction: delete_receipt_prescription_table(patient_id_list)
*RETURN* -> None
This function affect receipt and prescription
EXAMPLE : 
    pre_dict = {234:43, 231:32, 646:32}
    insert_receipt_prescription_table([123,345,34,"2020-01-10"], pre_dict)
"""
def insert_receipt_prescription_table(values, prescription_dict):
    rid, total, pid, r_date = values
    receipt_query = "INSERT INTO receipt(rid, total, pid, r_date) VALUES ("+str(rid)+",\'"+str(total)+"\'," \
                    "\'"+str(pid)+"\',\'"+str(r_date)+"\')"
    db_executer(receipt_query, 3, )
    for key_stock in prescription_dict.keys():
        prescription_query = "INSERT INTO prescription(rid, stock_id, quantity) " \
                             "VALUES (" + str(rid) + "," + str(key_stock) + "," + str(prescription_dict[key_stock]) + ")"
        db_executer(prescription_query, 3, )


"""
@Parm delete_medicine_table - delete tuple with stock_id from data, accept list only
Instruction: get_receipt_table(stock_id_list)
*RETURN* -> None
"""
def delete_medicine_table(sids):
    for stock_id in sids:
        m_query = "DELETE FROM medicine WHERE stock_id = "+str(stock_id)
        db_executer(m_query, 3, )

"""
@Parm delete_patient_table - delete tuple with patient_id from data, accept list only
Instruction: get_patient_table(patient_id_list)
*RETURN* -> None
"""
def delete_patient_table(pids):
    for pid in pids:
        p_query = "DELETE FROM patient WHERE pid = "+str(pid)
        db_executer(p_query, 3, )

"""
@Parm delete_receipt_prescription_table - delete tuple with receipt_id from data, accept list only
Instruction: delete_receipt_prescription_table(patient_id_list)
*RETURN* -> None
This function affect receipt and prescription
"""
def delete_receipt_prescription_table(rids):
    for rid in rids:
        r1_query = "DELETE FROM receipt WHERE rid = "+str(rid)
        r2_query = "DELETE FROM prescription WHERE rid = "+str(rid)
        db_executer(r2_query, 3, )
        db_executer(r1_query, 3, )

"""
@Parm expire_compare_bool - compare time if time_first is before time_another
Instruction: expire_compare_bool(time_first, time_another)
*RETURN* -> Boolean
"""
def expire_compare_bool(t1, t2):
    t1s = t1.split("-")
    t2s = t2.split("-")
    if int(t1s[0]) > int(t2s[0]):
        return True
    if int(t1s[1]) > int(t2s[1]):
        return True
    if int(t1s[2]) >= int(t2s[2]):
        return True
    return False

"""
@Parm nearest_expire_date - search through the medicine table and show the list of expiring stocks
Instruction: nearest_expire_date(next_days)
*RETURN* -> list of [Boolean, tuple] where Boolean stands for expired status

This is advance function, but it is not hard to implement
"""
def nearest_expire_date(days=7):
    named_tuple = time.localtime()  # get struct_time
    date = datetime.datetime(named_tuple[0], named_tuple[1], named_tuple[2])
    exp_check = date + datetime.timedelta(days)
    time_string = exp_check.strftime('%Y-%m-%d')
    present_string = date.strftime('%Y-%m-%d')
    expire_query = "SELECT * FROM medicine where exp_date < \'"+time_string+"\' order by exp_date desc"
    resultset = db_executer(expire_query, 1, )

    expires = []
    for i in resultset:
        if expire_compare_bool(present_string, str(i[1])):
            expires.append([True,i])
        else:
            expires.append([False,i])
    return expires

"""
@Parm predict_restock - search through the receipt table and prescription 
then show the list of stocks that needed to be restock according to the trend.

About the product popularity trend, we find the first top 10 most purchased drug on the 
last month and let them be popular drugs.
About the sales trend, we plot the graph by using total earning from each month to predict 
how much do we need to pre-purchase the drugs.

With 2 data, we assume that the more we earn in the previous month, the more we will purchase the drugs.
Also, the basic formula is as follow :
    amount_to_buy  = base_stock - amount_left + amount_sold + amount_sold/(2.5*ranking)   if on the top 3
                   = base_stock - amount_left + int((amount_sold)*trend_slope/100)        if on the top 10, but not top 3 and the trend is positive
                                                                                          or not on the top 10 and the trend is negative
                   = base_stock - amount_left                                             otherwise           
trend_slope is predicted using linear regression on the trend with straight line.
base_stock is around 100, depends on the shop size.

Instruction: predict_restock(base_stock)
*RETURN* ->  to_buy_list, trend_slope_x, trend_slope_y, trend_slope, c, date
    *to_buy_list* is a list of [integer, stock_info] where integer stands for amount of drugs needed to be bought
    Example : [[47, (16, 75, 145)],...,]
                    1.amount_purchase  2.amount_left_in_stock 3.stock_id
    trend_slope_x, trend_slope_y, trend_slope, and c are used for plotting
    date is list of pivots for the graph you may use it for explanation, just show in a table
    present_string is the day you run this query
 
ีused plotter(...) to plot the graph and you will find a processed.jpeg

This is advance function calculate the shortage of stocks and maximize profit
"""
def predict_restock(base_stock=100):
    named_tuple = time.localtime()  # get struct_time
    date = datetime.datetime(named_tuple[0], named_tuple[1], named_tuple[2])
    popularity_check = date - datetime.timedelta(30)
    time_string = popularity_check.strftime('%Y-%m-%d')
    present_string = date.strftime('%Y-%m-%d')
    top_drug_1_month = db_executer("select amount_purchase, quantity, chosen.stock_id sid from "
                                   "(select sum(quantity) amount_purchase, stock_id "
                                   " from prescription INNER JOIN receipt r on prescription.rid = r.rid"
                                   " where r_date > \'" + time_string +"\' group by stock_id "
                                   ") chosen INNER JOIN medicine on medicine.stock_id = chosen.stock_id "
                                   "order by amount_purchase desc;", 1, )

    trends_my_earning = db_executer("select extract(month from r_date) as mm,"
                                    "extract(year from r_date) as yyyy,"
                                    "sum(total) as earning from receipt "
                                    "group by 1,2 order by 2,1;", 1, )

    trend_slope_x = np.array([i for i, ele in enumerate(trends_my_earning)]) #?
    trend_slope_y = np.array([ele[2] for i, ele in enumerate(trends_my_earning)]) #?

    date = [[i, [ele[0],ele[1]]] for i, ele in enumerate(trends_my_earning)]

    def cost(v):
        m, c = v
        return np.sum((m * trend_slope_x + c - trend_slope_y) ** 2)
    res = minimize(cost, np.array([10, 15]))
    trend_slope, c = res.x
    plotter(trend_slope_x, trend_slope_y, trend_slope, c, date, present_string)
    to_buy_list = []
    for i, ele in enumerate(top_drug_1_month):
        amount_left = ele[1]
        amount_sold = ele[0]
        ranking = i+1
        if i < 3:
            amount_to_buy = base_stock - amount_left + amount_sold + amount_sold / (2.5 * ranking)
        elif 3 <= i <= 9:
            amount_to_buy = base_stock - amount_left
            if(trend_slope>0):
                amount_to_buy = amount_to_buy + int((amount_sold) * trend_slope / 100)
        else:
            amount_to_buy = base_stock - amount_left
            if(trend_slope<0):
                amount_to_buy = amount_to_buy + int((amount_sold) * trend_slope / 100)
        if amount_to_buy < 0:
            amount_to_buy = 0
        to_buy_list.append([int(amount_to_buy), ele])
    print(to_buy_list)
    print(date)
    return to_buy_list, date, trend_slope_x, trend_slope_y, trend_slope, c, date, present_string

def plotter(trend_slope_x, trend_slope_y, trend_slope, c, date, present_string):
    plt.figure(figsize=(20, 10))
    plt.plot(trend_slope_x, [trend_slope*i + c for i in trend_slope_x], label='overall trend')
    plt.plot(trend_slope_x, trend_slope_y, 'o', label='earning per month')
    plt.plot(trend_slope_x, trend_slope_y, label='actual earning trend')
    plt.xlabel("Months after " + str(round(date[0][1][0])) + "/" + str(round(date[0][1][1])))
    plt.ylabel("Total earning each month")
    plt.title("Graph of total earnings before "+str(present_string))
    plt.legend()
    plt.savefig("processed.png")
    print("done")











