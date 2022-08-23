from db_manage import *
from browser_history import get_history

#----------------------------BROWSER HISTORY-----------------------------------

def browser_history(table_name_list):

    tb_name = "browser_history"
    table_name_list.add(tb_name)
    try:
        createTable(tb_name)
    except:
        pass

    outputs = get_history()

    his = outputs.histories
    for h in his:
        regis = []
        h_date = (h[0]).date()
        h_url = h[1]
        regis.append(h_url)
        regis.append(h_date)
        if (select_exix(regis, tb_name) == []):
            insertRow(tb_name, regis)
    return table_name_list

#----------------------------BROWSER HISTORY-----------------------------------