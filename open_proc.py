from db_manage import *
import datetime
import wmi

c = wmi.WMI()

#------------------------------OPEN PROCESS------------------------------------

def open_process():
    tb_name = "open_process"
    try:
        createTable(tb_name)
    except:
        pass
    deleteTableRow(tb_name)

    for process in c.Win32_Process ():
        regis = []
        regis.append(str(process.Name))
        regis.append(datetime.datetime.now().date())
        insertRow(tb_name, regis)
    return tb_name

#------------------------------OPEN PROCESS------------------------------------