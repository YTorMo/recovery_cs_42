from db_manage import *
import datetime
import wmi

c = wmi.WMI()

#----------------------------CONECTED DEVICES----------------------------------

def device_conected(table_name_list_always):

    tb_name_pm = "PhysicalMedia"
    table_name_list_always.add(tb_name_pm)
    try:
        createTable(tb_name_pm)
    except:
        pass
    deleteTableRow(tb_name_pm)
    if not c.Win32_PhysicalMedia():
        print("No Physical Media devices")
    else:
        for item in c.Win32_PhysicalMedia():
            if item.Name:
                regis = []
                regis.append(item.Name)
                regis.append(datetime.datetime.now().date())
                insertRow(tb_name_pm, regis)

    tb_name_dd = "DiskDrive"
    table_name_list_always.add(tb_name_dd)
    try:
        createTable(tb_name_dd)
    except:
        pass
    deleteTableRow(tb_name_dd)
    for drive in c.Win32_DiskDrive():
        regis = []
        regis.append(drive.Name)
        regis.append(datetime.datetime.now().date())
        insertRow(tb_name_dd, regis)

    tb_name_ld = "LogicalDisk"
    table_name_list_always.add(tb_name_ld)
    try:
        createTable_ld(tb_name_ld)
    except:
        pass
    deleteTableRow(tb_name_ld)
    for disk in c.Win32_LogicalDisk():
        regis = []
        regis.append(disk.Name)
        regis.append(hd_type(disk.DriveType))
        insertRow_ld(tb_name_ld, regis)

    tb_name_usb = "USB"
    table_name_list_always.add(tb_name_usb)
    try:
        createTable(tb_name_usb)
    except:
        pass
    deleteTableRow(tb_name_usb)
    for usb in c.Win32_USBController():
        regis = []
        regis.append(usb.Name)
        regis.append(datetime.datetime.now().date())
        insertRow(tb_name_usb, regis)
    
    return table_name_list_always


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