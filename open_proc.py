from db_manage import *
import datetime
import wmi

c = wmi.WMI()

#------------------------------OPEN PROCESS------------------------------------

def open_process(table_name_list):
    tb_name = "open_process"
    table_name_list.add(tb_name)
    try:
        createTable(tb_name)
    except:
        pass

    for process in c.Win32_Process ():
        regis = []
        regis.append(str(process.Name))
        regis.append(datetime.datetime.now().date())
        try:
            insertRow(tb_name, regis)
        except:
            pass
        return table_name_list

#------------------------------OPEN PROCESS------------------------------------