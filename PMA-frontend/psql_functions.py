import datetime
import time

import psycopg2

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
    med_query = "SELECT * FROM medicine order by stock_id desc"
    resultset = db_executer(med_query, 1, )
    return resultset

"""
@Parm get_patient_table - return sorted patient table
Instruction: get_patient_table()
*RETURN* -> list of tuple with corresponding attributes
"""
def get_patient_table():
    p_query = "SELECT * FROM patient order by pid desc"
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
    r_query = "SELECT * FROM receipt order by rid desc"
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
    pre_query = "SELECT * FROM prescription order by rid desc"
    resultset = db_executer(pre_query, 1, )
    # for i in resultset:
    #     print(i)
    return resultset

"""
@Parm NOT DONE
"""
def update_medicine_table(updates):
    return 1

"""
@Parm NOT DONE
These 2 tables go together
"""
def update_receipt_prescription_table(updates):
    return 1

"""
@Parm NOT DONE
"""
def update_patient_table(updates):
    return 1

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
        r1_query = "DELETE FROM patient WHERE rid = "+str(rid)
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
    # for i in expires:
    #     print(i)
    return expires

"""
@Parm predict_restock - search through the receipt table and prescription 
then show the list of stocks that needed to be restock according to the trend.

About the product popularity trend, we find the top 10 most purchased drug on the last 3 month and let them be popular drugs.
About the sales trend, we plot the graph by using total earning in each month to predict how much do we need to pre-purchase the drugs.

With 2 data, we assume that the more we earn in the previous month, the more we will purchase the drugs.
Also, the basic formula is as follow :
    amount_to_buy  = base_stock + amount_sold + amount_sold/(2.5*ranking)                 if on the top 3
                   = base_stock + int((amount_sold)*trend_slope)                          if on the top 10, but not top 3
                   = base_stock - amount_left                                             otherwise           
trend_slope is predicted using linear regression on the trend with straight line.
base_stock is around 30, depends on the shop size.

Instruction: predict_restock(year,month,base_stock) where year and month comes from the date we want to restock.
The lastest timestamp is 2020-12-30. Beyond that won't show more graph, so assume the date you were at the moment.
*RETURN* -> list of [integer, tuple] where integer stands for amount of drugs needed to be bought and list of pivots for the graph (date, earning)

This is advance function calculate the shortage of stocks and maximize profit
"""
def predict_restock():

    return 1