import psycopg2
import numpy as np
"""
Instruction: db_executer(query,mode,rows)
mode 0 is getting a single tuple of query.
mode 1 is getting whole list of tuples of query. That means you have to do result_set[tuple][attribute].
mode 2 is getting rows from whole list of result_set.

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
        if "insert" in (pointer.lower()):
            conn.commit()

        # display the PostgreSQL database server version
        if mode == 0:
            result_set = cur.fetchone()
        elif mode == 1:
            result_set = cur.fetchall()
        elif mode == 2:
            result_set = cur.fetchmany(rows)
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



