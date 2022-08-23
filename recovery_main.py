from db_manage import *
from arg_parse import *
from browser_h import *
from conected_devices import *
from event_log import *
from open_proc import *
from recent_and_temp_f import *
from registry_b import *
from sfw_installed import *


#----------------------------------MAIN----------------------------------------

def main():
    table_name_list = set()
    table_name_list_always = set()
    t_args = arg_getter()
    if not os.path.exists("\\\\VBOXSVR\\recovery_shared\\recovery.db"):
        createDB()
    table_name_list = Registry_branches_c_d(table_name_list)
    table_name_list = recent_files(table_name_list)
    table_name_list = temp_files(table_name_list)
    table_name_list = software_installed(table_name_list)
    table_name_list_always = open_process(table_name_list_always)
    table_name_list = browser_history(table_name_list)
    table_name_list_always = device_conected(table_name_list_always)
    table_name_list = events_log(table_name_list)
    data_printer(table_name_list, table_name_list_always, t_args)


#----------------------------------MAIN----------------------------------------

#------------------------------DATA PRINTER------------------------------------

def data_printer(table_name_list, table_name_list_always, t_args):
    for table_n in table_name_list:
        print("----------------------------------------")
        print(f"\t{table_n}")
        print("----------------------------------------")
        d_db = select_from_db(t_args, table_n)
        for data in d_db:
            print(data)
        print("----------------------------------------")
        print()
        print("----------------------------------------")
    for table_n_a in table_name_list_always:
        print("----------------------------------------")
        print(f"\t{table_n_a}")
        print("----------------------------------------")
        d_db = select_from_db_ld(table_n_a)
        for data in d_db:
            print(data)
        print("----------------------------------------")
        print()
        print("----------------------------------------")

#------------------------------DATA PRINTER------------------------------------