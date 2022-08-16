import wmi
import win32evtlog
import win32
import datetime
import os
import winapps
from browser_history import get_history
import sqlite3 as sql

app_list = set()



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




def main():
    #events_log()
    #recent_files()
    #software_installed()
    start_menu()
    #open_process()
    #browser_history()
    #device_conected()



#time_test = datetime.datetime(2022, 8, 10, 8, 52, 51)
#print (time_test)
def open_process():
    print("\n   ----------------------------------------    \n")
    for process in c.Win32_Process ():
        print (process.ProcessId, process.Name)

def events_log():
    print("\n   ----------------------------------------    \n")

    hand = win32evtlog.OpenEventLog(None, 'EventLogRegister')
    flags= win32evtlog.EVENTLOG_BACKWARDS_READ|win32evtlog.EVENTLOG_SEQUENTIAL_READ
    records=win32evtlog.ReadEventLog(hand, flags, 0)

    for record in records:
        print(record.SourceName)
        print (record.TimeWritten)

def recent_files():
    print("\n   ----------------------------------------    \n")

    HOME = os.getenv("HOME")
    PATH_RECENT = HOME + "\AppData\Roaming\Microsoft\Windows\Recent"

    for root, dirs, files in os.walk(PATH_RECENT):
            for f in files:
                try:
                    r_time = os.path.getmtime(PATH_RECENT + "\\" + str(f))
                    f_time = datetime.date.fromtimestamp(r_time)
                    print(str(f) + "    " + str(f_time))
                except:
                    pass

def device_conected():
    print("\n   ----------------------------------------    \n")

    if not c.Win32_PhysicalMedia():
        print("No Physical Media devices")
    else:
        for item in c.Win32_PhysicalMedia():
            if item.Name:
                print(item.Name)

    for drive in c.Win32_DiskDrive():
        print(drive.Name)

    for disk in c.Win32_LogicalDisk():
        print(disk.Name + "     " + hd_type(disk.DriveType))

    if not c.Win32_USBController():
        print("No USB devices")
    else:
        for usb in c.Win32_USBController():
            print(usb)

def software_installed():
    global app_list
    print("\n   ----------------------------------------    \n")

    print(len(c.Win32_InstalledWin32Program ()))
#    for inst in c.Win32_InstalledWin32Program ():
#        print("\n   ++++++++++++++++++++++++++++++++++++++++    ")
#        print("Name:" + inst.Name)#
#        print("    ++++++++++++++++++++++++++++++++++++++++    \n")
    
    print("\n   ----------------------------------------    \n")
    installed_app()
    print("\n   ----------------------------------------    \n")
#    for inst_s in c.Win32_InstalledStoreProgram():
#        print(inst_s.Name)
    #print("\n   ----------------------------------------    \n")
    for product in c.Win32_Product():
        print(product.Name)
        app_list.add(product.Name)
        y = product.InstallDate[:4]
        m = product.InstallDate[4:6]
        d = product.InstallDate[7:]
        time_inst = datetime.date(int(y), int(m), int(d))
        print(time_inst)


def installed_app():
    global app_list
    for app in winapps.list_installed():
        name = str(app).split("name='")
        name = name[1].split("', ")
        #print(app.install_date)
        print (name[0])
        app_list.add(name[0])
        get_install_date(app)


def get_install_date(app):
    inst_date_r1 = str(app).split("install_date=")
    inst_date_r2 = (inst_date_r1[-1]).split(", i")
    if inst_date_r2[0] == "None":
        un_path_r = inst_date_r2[-1].split("uninstall_string='")
        un_path_r = un_path_r[-1].replace("\"", "")
        un_path_r = un_path_r.replace("')", "")
        if not (un_path_r.endswith(")")):
            c_time = os.path.getctime(un_path_r)
            dt_c = datetime.date.fromtimestamp(c_time)
            print(dt_c)
        else:
            print("None")
    else:
        num_date = inst_date_r2[0]
        splt_date = num_date.split(",")
        y_date = int(splt_date[0][14:])
        m_date = int(splt_date[-2])
        d_date = int(splt_date[-1][:-1])
        inst_date = datetime.date(int(y_date), int(m_date), int(d_date))
        print(inst_date) 
    print ("\n\n")


def start_menu():
    print("\n   ----------------------------------------    \n")
    PATH_APP = os.getenv("START_MENU_PATH")
    for folder in os.listdir(PATH_APP):
        if not str(folder).__contains__("."):
            folder_n = str(folder)
            for files in os.listdir(PATH_APP + "\\" + folder_n):
                if str(files).__contains__(folder_n):
                    print(folder_n)
        elif str(folder).__contains__(".lnk"):
            print(str(folder)[:-4])


def browser_history():
    outputs = get_history()

    his = outputs.histories
    for h in his:
        h_date = (h[0]).date()
        h_url = h[1]
        print(str(h_url) + "        " + str(h_date))
        print("\n")


if __name__ == "__main__":
    c = wmi.WMI()
    main()