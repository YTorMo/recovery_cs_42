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
    t_args = arg_getter()
    if not os.path.exists("\\\\VBOXSVR\\recovery_shared\\recovery.db"):
        createDB()
    table_name_list = Registry_branches_c_d(table_name_list)
    table_name_list = recent_files(table_name_list)
    table_name_list = temp_files(table_name_list)
    table_name_list = software_installed(table_name_list)
    table_name_list = open_process(table_name_list)
    table_name_list = browser_history(table_name_list)
    device_conected()
    table_name_list = events_log(table_name_list)
    for table_n in table_name_list:
        print("----------------------------------------")
        print(f"\t{table_n}")
        print("----------------------------------------")
        d_db = select_from_db(t_args, table_n)
        for data in d_db:
            print(data)

#----------------------------------MAIN----------------------------------------