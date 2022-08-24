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
    deleteTableRow(tb_name)

    hand = win32evtlog.OpenEventLog(None, 'EventLogRegister')
    flags= win32evtlog.EVENTLOG_BACKWARDS_READ|win32evtlog.EVENTLOG_SEQUENTIAL_READ
    records=win32evtlog.ReadEventLog(hand, flags, 0)

    for record in records:
        regis = []
        regis.append(str(record.SourceName))
        rec_time = record.TimeWritten.date()
        regis.append(rec_time)
        insertRow(tb_name, regis)
    return table_name_list

#-------------------------------EVENTS LOG-------------------------------------