import psycopg2
import numpy as np
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
    # for i in resultset:
    #     print(i)
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