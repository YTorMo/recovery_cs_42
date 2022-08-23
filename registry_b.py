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
    registry_LM(tb_name)
    registry_CU(tb_name)
    return table_name_list

def registry_LM(tb_name):
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run")

    reg_win_ts = winreg.QueryInfoKey(key)[2]
    reg_key_ts = windows_ticks_to_unix_seconds(reg_win_ts)
    dt = datetime.date.fromtimestamp(reg_key_ts)
    regis = []
    regis.append("Local Machine registry branches changes date (CurrentVersionRun)")
    regis.append(dt)
    try:
        insertRow(tb_name, regis)
    except:
        pass

def registry_CU(tb_name):
    key_2 = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run")

    reg_win_ts_2 = winreg.QueryInfoKey(key_2)[2]
    reg_key_ts_2 = windows_ticks_to_unix_seconds(reg_win_ts_2)
    dt_2 = datetime.date.fromtimestamp(reg_key_ts_2)
    regis = []
    regis.append("Current User registry branches changes date (CurrentVersionRun)")
    regis.append(dt_2)
    try:
        insertRow(tb_name, regis)
    except:
        pass

#----------------------------REGISTRY BRANCHES---------------------------------