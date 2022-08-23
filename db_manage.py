import sqlite3 as sql

#-------------------------DATABASE CREATION--------------------------------

def createDB():
	conn = sql.connect("recovery.db")
	conn.commit()
	conn.close()

def createTable(tb_name):
	conn = sql.connect("recovery.db")
	cursor = conn.cursor()
	cursor.execute(
		"""CREATE TABLE """ + tb_name + """ (
			name TEXT,
			date_created TIMESTAMP
		)"""
	)
	conn.commit()
	conn.close()

def insertRow(tb_name,regis):
	conn = sql.connect("recovery.db")
	instruc = "INSERT INTO " + tb_name +" (name, date_created) VALUES (?, ?);"
	cursor = conn.cursor()
	cursor.execute(instruc, regis)
	conn.commit()
	conn.close()

def createTable_ld(tb_name):
	conn = sql.connect("recovery.db")
	cursor = conn.cursor()
	cursor.execute(
		"""CREATE TABLE """ + tb_name + """ (
			name TEXT,
			type TEXT
		)"""
	)
	conn.commit()
	conn.close()

def insertRow_ld(tb_name,regis):
	conn = sql.connect("recovery.db")
	instruc = "INSERT INTO " + tb_name +" (name, type) VALUES (?, ?);"
	cursor = conn.cursor()
	cursor.execute(instruc, regis)
	conn.commit()
	conn.close()

#-------------------------DATABASE CREATION--------------------------------

#------------------------DATABASE CONSULTING-------------------------------

def select_from_db(dates, tb_name):
    if(len(dates) == 1):
        date_1 = dates[0]
        date_2 = dates[0]
    else:
        date_1 = dates[0]
        date_2 = dates[1]
    conn = sql.connect("recovery.db")
    instruc = "SELECT * FROM " + tb_name + " WHERE date_created >= '%s' AND date_created <= '%s' ORDER BY date_created DESC;" % (str(date_1), str(date_2))
    cursor = conn.cursor()
    cursor.execute(instruc)
    d_list = cursor.fetchall()
    conn.commit()
    conn.close()
    return (d_list)

def select_from_db_ld(tb_name):
    conn = sql.connect("recovery.db")
    instruc = "SELECT * FROM " + tb_name + ";"
    cursor = conn.cursor()
    cursor.execute(instruc)
    d_list = cursor.fetchall()
    conn.commit()
    conn.close()
    return (d_list)

def select_exix(regis, tb_name):
    conn = sql.connect("recovery.db")
    instruc = "SELECT name FROM " + tb_name + " WHERE name = '%s';" % (str(regis[0]))
    cursor = conn.cursor()
    cursor.execute(instruc)
    d_list = cursor.fetchall()
    conn.commit()
    conn.close()
    return (d_list)

#------------------------DATABASE CONSULTING-------------------------------