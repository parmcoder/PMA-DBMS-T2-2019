import psycopg2
import numpy as np
import time
# CREATE TABLE receipt(
#                          rid integer,
#                          total integer,
#                          pid integer,
#                          r_date date,
#                          PRIMARY KEY (rid),
#                          FOREIGN KEY (pid) REFERENCES patient(pid));
# CREATE TABLE prescription(
#                          rid integer,
#                          stock_id integer,
#                          quantity integer,
#                          FOREIGN KEY (stock_id) REFERENCES medicine(stock_id),
#                          FOREIGN KEY (rid) REFERENCES receipt(rid));

def str_time_prop(start, end, format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))
def random_date(start, end, prop):
    return str_time_prop(start, end, '%Y-%m-%d', prop)

#Get price table
def get_price():
    conn = None
    pointer = None
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(database="defaultdb", user="doadmin", password="de53jzgsny7bamuk",
                                host="db4parm-do-user-7150737-0.db.ondigitalocean.com", port="25060")
        # create a cursor
        cur = conn.cursor()

        # execute a statement
        query = "SELECT stock_id,price from medicine order by stock_id desc"

        print('PostgreSQL executing query:'+ query)

        cur.execute(query)

        # display the PostgreSQL database server version
        pointer = cur.fetchall()

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
            return pointer

#Use for execute query, any query
def db_executer_with_commit(query_i):
    conn = None
    pointer = query_i
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
        conn.commit()

        # display the PostgreSQL database server version
        pointer2 = cur.fetchone()
        print(pointer2)
        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
            return pointer

def receipt_gen(n=100):
    receipts = []
    prescriptions = []
    price_table = get_price()
    receipt_query = "INSERT INTO receipt(rid, total, pid, r_date) VALUES "
    prescription_query = "INSERT INTO prescription(rid, stock_id, quantity) VALUES "
    #rid, pid, r_date, [stock_id,quantity]
    for i in range(1,n):
        date = random_date("2019-01-01", "2021-01-01", np.random.random())
        rid = i
        pid = np.random.randint(1,1000)
        total = 0
        for j in range(np.random.randint(1,4)):
            stock_id = np.random.randint(1,1000)
            quantity = np.random.randint(1,10)
            total = total + price_table[stock_id][1]*quantity
            prescriptions.append([rid,stock_id, quantity])
        receipts.append([rid, round(total), pid, date])

    #Turn into a string
    for i in receipts:
        addstr = "("+str(i[0])+","+str(i[1])+","+str(i[2])+",'"+str(i[3])+"'),"
        receipt_query = receipt_query + addstr
    for i in prescriptions:
        addstr = "("+str(i[0])+","+str(i[1])+","+str(i[2])+"),"
        prescription_query = prescription_query + addstr
    if len(receipts) > 0:
        receipt_query_complete = receipt_query[:len(receipt_query) - 1]
    else:
        receipt_query_complete = ""
    if len(prescriptions) > 0:
        prescription_query_complete = prescription_query[:len(prescription_query) - 1]
    else:
        prescription_query_complete = ""
    db_executer_with_commit(receipt_query_complete)
    db_executer_with_commit(prescription_query_complete)

db_executer_with_commit("delete from prescription")
db_executer_with_commit("delete from receipt")
receipt_gen() #How many data do you want to generate




