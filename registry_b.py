from db_manage import *
import datetime
import winreg

#----------------------------REGISTRY BRANCHES---------------------------------

def windows_ticks_to_unix_seconds(windows_ticks):
    return windows_ticks/10000000 - 11644473600

def Registry_branches_c_d(table_name_list):
    tb_name = "Registry_branches_c_d"
    table_name_list.add(tb_name)
    try:
        createTable(tb_name)
    except:
        pass
    deleteTableRow(tb_name)
    
    key_types = [winreg.HKEY_LOCAL_MACHINE, winreg.HKEY_CURRENT_USER]
    
    for key in key_types:
        # Data
        handler = winreg.OpenKey(key, "Software\\Microsoft\\Windows\\CurrentVersion\\Run")
        reg_key_ts = windows_ticks_to_unix_seconds(winreg.QueryInfoKey(handler)[2])
        
        # Date
        dt = datetime.date.fromtimestamp(reg_key_ts)
        
        # Info collection
        regis = ["Registry branches changes date (Software\\Microsoft\\Windows\\CurrentVersion\\Run)", dt]
        insertRow(tb_name, regis)
    
    return table_name_list

#----------------------------REGISTRY BRANCHES---------------------------------
