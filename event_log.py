import win32evtlog
import datetime
from db_manage import *

#-------------------------------EVENTS LOG-------------------------------------

def events_log(table_name_list):
    tb_name = "events_log"
    table_name_list.add(tb_name)
    try:
        createTable(tb_name)
    except:
        pass

    hand = win32evtlog.OpenEventLog(None, 'EventLogRegister')
    flags= win32evtlog.EVENTLOG_BACKWARDS_READ|win32evtlog.EVENTLOG_SEQUENTIAL_READ
    records=win32evtlog.ReadEventLog(hand, flags, 0)

    for record in records:
        regis = []
        regis.append(str(record.SourceName))
        rec_time = record.TimeWritten
        rec_time = str(rec_time).split("-")
        y = rec_time[0]
        m = rec_time[1]
        rec_time = rec_time[2].split(" ")
        d = rec_time[0]
        rec_time = datetime.date(int(y), int(m), int(d))
        regis.append(rec_time)
        if (select_exix(regis, tb_name) == []):
            insertRow(tb_name, regis)
    return table_name_list

#-------------------------------EVENTS LOG-------------------------------------