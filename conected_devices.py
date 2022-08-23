from db_manage import *
import datetime
import wmi

c = wmi.WMI()

#----------------------------CONECTED DEVICES----------------------------------

def device_conected():

    tb_name_pm = "PhysicalMedia"
    try:
        createTable(tb_name_pm)
    except:
        pass
    if not c.Win32_PhysicalMedia():
        print("No Physical Media devices")
    else:
        for item in c.Win32_PhysicalMedia():
            if item.Name:
                regis = []
                regis.append(item.Name)
                regis.append(datetime.datetime.now())
                try:
                    insertRow(tb_name_pm, regis)
                except:
                    pass

    tb_name_dd = "DiskDrive"
    try:
        createTable(tb_name_dd)
    except:
        pass
    for drive in c.Win32_DiskDrive():
        regis = []
        regis.append(drive.Name)
        regis.append(datetime.datetime.now())
        try:
            insertRow(tb_name_dd, regis)
        except:
            pass
        else:
            updateRow(tb_name_dd, regis)

    tb_name_ld = "LogicalDisk"
    try:
        createTable_ld(tb_name_ld)
    except:
        pass
    for disk in c.Win32_LogicalDisk():
        regis = []
        regis.append(disk.Name)
        regis.append(hd_type(disk.DriveType))
        insertRow_ld(tb_name_ld, regis)
        try:
            insertRow_ld(tb_name_ld, regis)
        except:
            pass

    tb_name_usb = "USB"
    try:
        createTable(tb_name_usb)
    except:
        pass
    for usb in c.Win32_USBController():
        regis = []
        regis.append(usb.Name)
        regis.append(datetime.datetime.now())
        try:
            insertRow(tb_name_dd, regis)
        except:
            pass


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