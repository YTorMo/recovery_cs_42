from db_manage import *
import os
import datetime

#------------------------------RECENT FILES------------------------------------

def recent_files(table_name_list):
    tb_name = "recent_files"
    table_name_list.add(tb_name)
    try:
        createTable(tb_name)
    except:
        pass

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
                    try:
                        insertRow(tb_name, regis)
                    except:
                        pass
                except:
                    pass
    return table_name_list

#------------------------------RECENT FILES------------------------------------

#-------------------------------TEMP FILES-------------------------------------

def temp_files(table_name_list):
    tb_name = "temp_files"
    table_name_list.add(tb_name)
    try:
        createTable(tb_name)
    except:
        pass

    HOME = os.getenv("HOME")
    PATH_RECENT = HOME + "\AppData\Local\Temp"

    for root, dirs, files in os.walk(PATH_RECENT):
            for f in files:
                try:
                    r_time = os.path.getmtime(PATH_RECENT + "\\" + str(f))
                    f_time = datetime.date.fromtimestamp(r_time)
                    regis = []
                    regis.append(f)
                    regis.append(f_time)
                    try:
                        insertRow(tb_name, regis)
                    except:
                        pass
                except:
                    pass
    return table_name_list

#-------------------------------TEMP FILES-------------------------------------