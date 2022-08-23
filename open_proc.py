from db_manage import *
import datetime
import wmi

c = wmi.WMI()

#------------------------------OPEN PROCESS------------------------------------

def open_process(table_name_list_always):
    tb_name = "open_process"
    table_name_list_always.add(tb_name)
    try:
        createTable(tb_name)
    except:
        pass

    for process in c.Win32_Process ():
        regis = []
        regis.append(str(process.Name))
        regis.append(datetime.datetime.now().date())
        if (select_exix(regis, tb_name) == []):
            insertRow(tb_name, regis)
    return table_name_list_always

#------------------------------OPEN PROCESS------------------------------------