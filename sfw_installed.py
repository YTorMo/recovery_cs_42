import datetime
import os
import wmi
from db_manage import *
import winapps

app_list = set()
app_list_all = set()
app_list_diff = set()
c = wmi.WMI()

#---------------------------SOFTWARE INSTALLED---------------------------------

def software_installed(table_name_list):
    global app_list
    global app_list_all
    global app_list_diff

    tb_name = "software_installed"
    table_name_list.add(tb_name)
    try:
        createTable(tb_name)
    except:
        pass

    installed_app(tb_name)
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
        try:
            insertRow(tb_name, regis)
        except:
            pass


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
        try:
            insertRow(tb_name, regis)
        except:
            pass
    return table_name_list



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


def installed_app(tb_name):
    global app_list
    regis = []
    for app in winapps.list_installed():
        name = str(app).split("name='")
        name = name[1].split("', ")
        regis.append(name[0])
        app_list.add(name[0])
        get_install_date(app, tb_name, regis)
        regis = []


def get_install_date(app, tb_name, regis):
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
    try:
        insertRow(tb_name, regis)
    except:
        pass

#---------------------------SOFTWARE INSTALLED---------------------------------