import wmi
import win32evtlog
import win32
import datetime
import os
import winapps
from browser_history import get_history
import sqlite3 as sql
from datetime import date


app_list = set()
app_list_all = set()
app_list_diff = set()


#----------------------------------MAIN----------------------------------------

def main():
    createDB()
    events_log()
    recent_files()
    software_installed()
    open_process()
    browser_history()
    device_conected()

#----------------------------------MAIN----------------------------------------

#------------------------------OPEN PROCESS------------------------------------

def open_process():
    db_name = "open_process"
    createTable(db_name)

    for process in c.Win32_Process ():
        regis = []
        regis.append(str(process.Name))
        regis.append(datetime.datetime.now())
        insertRow(db_name, regis)

#------------------------------OPEN PROCESS------------------------------------

#-------------------------------EVENTS LOG-------------------------------------

def events_log():
    db_name = "events_log"
    createTable(db_name)

    hand = win32evtlog.OpenEventLog(None, 'EventLogRegister')
    flags= win32evtlog.EVENTLOG_BACKWARDS_READ|win32evtlog.EVENTLOG_SEQUENTIAL_READ
    records=win32evtlog.ReadEventLog(hand, flags, 0)

    for record in records:
        regis = []
        regis.append(str(record.SourceName))
        rec_time = record.TimeWritten
        rec_time = str(rec_time).split("-")
        y = rec_time[0]
        m = rec_time[1]
        rec_time = rec_time[2].split(" ")
        d = rec_time[0]
        rec_time = datetime.date(int(y), int(m), int(d))
        regis.append(rec_time)
        insertRow(db_name, regis)

#-------------------------------EVENTS LOG-------------------------------------

#------------------------------RECENT FILES------------------------------------

def recent_files():
    db_name = "recent_files"
    createTable(db_name)

    HOME = os.getenv("HOME")
    PATH_RECENT = HOME + "\AppData\Roaming\Microsoft\Windows\Recent"

    for root, dirs, files in os.walk(PATH_RECENT):
            for f in files:
                try:
                    r_time = os.path.getmtime(PATH_RECENT + "\\" + str(f))
                    f_time = datetime.date.fromtimestamp(r_time)
                    regis = []
                    regis.append(f)
                    regis.append(f_time)
                    insertRow(db_name, regis)
                except:
                    pass

#------------------------------RECENT FILES------------------------------------

#----------------------------CONECTED DEVICES----------------------------------

def device_conected():

    db_name_pm = "PhysicalMedia"
    createTable(db_name_pm)
    if not c.Win32_PhysicalMedia():
        print("No Physical Media devices")
    else:
        for item in c.Win32_PhysicalMedia():
            if item.Name:
                regis = []
                regis.append(item.Name)
                regis.append(datetime.datetime.now())
                insertRow(db_name_pm, regis)

    db_name_dd = "DiskDrive"
    createTable(db_name_dd)
    for drive in c.Win32_DiskDrive():
        regis = []
        regis.append(drive.Name)
        regis.append(datetime.datetime.now())
        insertRow(db_name_dd, regis)

    db_name_ld = "LogicalDisk"
    createTable_ld(db_name_ld)
    for disk in c.Win32_LogicalDisk():
        regis = []
        regis.append(disk.Name)
        regis.append(hd_type(disk.DriveType))
        insertRow_ld(db_name_ld, regis)

    db_name_usb = "USB"
    createTable(db_name_usb)
    for usb in c.Win32_USBController():
        regis = []
        regis.append(usb.Name)
        regis.append(datetime.datetime.now())
        insertRow(db_name_dd, regis)


def hd_type(h_type):
    if(h_type == 0):
        c_type = "Unknown"
    elif(h_type == 1):
        c_type = "No Root Directory"
    elif(h_type == 2):
        c_type = "Removable Disk"
    elif(h_type == 3):
        c_type = "Local Disk"
    elif(h_type == 4):
        c_type = "Network Drive"
    elif(h_type == 5):
        c_type = "Compact Disc"
    elif(h_type == 6):
        c_type = "RAM Disk"
    return c_type

#----------------------------CONECTED DEVICES----------------------------------

#---------------------------SOFTWARE INSTALLED---------------------------------

def software_installed():
    global app_list
    global app_list_all
    global app_list_diff

    db_name = "software_installed"
    createTable(db_name)

    installed_app(db_name)
#    for inst_s in c.Win32_InstalledStoreProgram():
#        print(inst_s.Name)
    for product in c.Win32_Product():
        regis = []
        app_list.add(product.Name)
        y = product.InstallDate[:4]
        m = product.InstallDate[4:6]
        d = product.InstallDate[7:]
        time_inst = datetime.date(int(y), int(m), int(d))
        regis.append(product.Name)
        regis.append(time_inst)
        insertRow(db_name, regis)


    for inst in c.Win32_InstalledWin32Program ():
        app_list_all.add(inst.Name)

    for all_elem in app_list_all:
        if not app_list.__contains__(all_elem):
            app_list.add(all_elem)
            all_elem = str(all_elem).split("Microsoft ")
            all_elem = str(all_elem[-1]).split(" (")
            app_list_diff.add(all_elem[0])
    for elem_diff in app_list_diff:
        regis = []
        path_date = find_path_date(elem_diff)
        regis.append(elem_diff)
        regis.append(path_date)
        insertRow(db_name, regis)



def find_path_date(pattern):
    time_low = None
    for root, dirs, files in os.walk("C:\\"):
        for name in files:
            if name.__contains__(pattern):
                c_time = os.path.getctime(os.path.join(root, name))
                fc_time = datetime.date.fromtimestamp(c_time)
                if time_low == None or time_low > fc_time:
                    time_low = fc_time
    return time_low


def installed_app(db_name):
    global app_list
    regis = []
    for app in winapps.list_installed():
        name = str(app).split("name='")
        name = name[1].split("', ")
        regis.append(name[0])
        app_list.add(name[0])
        get_install_date(app, db_name, regis)
        regis = []


def get_install_date(app, db_name, regis):
    inst_date_r1 = str(app).split("install_date=")
    inst_date_r2 = (inst_date_r1[-1]).split(", i")
    if inst_date_r2[0] == "None":
        un_path_r = inst_date_r2[-1].split("uninstall_string='")
        un_path_r = un_path_r[-1].replace("\"", "")
        un_path_r = un_path_r.replace("')", "")
        if not (un_path_r.endswith(")")):
            c_time = os.path.getctime(un_path_r)
            dt_c = datetime.date.fromtimestamp(c_time)
            regis.append(dt_c)
        else:
            regis.append(None)
    else:
        num_date = inst_date_r2[0]
        splt_date = num_date.split(",")
        y_date = int(splt_date[0][14:])
        m_date = int(splt_date[-2])
        d_date = int(splt_date[-1][:-1])
        inst_date = datetime.date(int(y_date), int(m_date), int(d_date))
        regis.append(inst_date)
    insertRow(db_name, regis)

#---------------------------SOFTWARE INSTALLED---------------------------------

#----------------------------BROWSER HISTORY-----------------------------------

def browser_history():

    db_name = "browser_history"
    createTable(db_name)

    outputs = get_history()

    his = outputs.histories
    for h in his:
        regis = []
        h_date = (h[0]).date()
        h_url = h[1]
        regis.append(h_url)
        regis.append(h_date)
        insertRow(db_name, regis)

#----------------------------BROWSER HISTORY-----------------------------------

#-------------------------DATABASE CREATION--------------------------------

def createDB():
	conn = sql.connect("recovery.db")
	conn.commit()
	conn.close()

def createTable(db_name):
	conn = sql.connect("recovery.db")
	cursor = conn.cursor()
	cursor.execute(
		"""CREATE TABLE """ + db_name + """ (
			name TEXT,
			date_created TIMESTAMP
		)"""
	)
	conn.commit()
	conn.close()

def insertRow(db_name,regis):
	conn = sql.connect("recovery.db")
	instruc = "INSERT INTO " + db_name +" (name, date_created) VALUES (?, ?);"
	cursor = conn.cursor()
	cursor.execute(instruc, regis)
	conn.commit()
	conn.close()

def createTable_ld(db_name):
	conn = sql.connect("recovery.db")
	cursor = conn.cursor()
	cursor.execute(
		"""CREATE TABLE """ + db_name + """ (
			name TEXT,
			type TEXT
		)"""
	)
	conn.commit()
	conn.close()

def insertRow_ld(db_name,regis):
	conn = sql.connect("recovery.db")
	instruc = "INSERT INTO " + db_name +" (name, type) VALUES (?, ?);"
	cursor = conn.cursor()
	cursor.execute(instruc, regis)
	conn.commit()
	conn.close()

#-------------------------DATABASE CREATION--------------------------------

#------------------------DATABASE CONSULTING-------------------------------
#------------------------DATABASE CONSULTING-------------------------------


if __name__ == "__main__":
    c = wmi.WMI()
    main()