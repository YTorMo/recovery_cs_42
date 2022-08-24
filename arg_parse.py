import datetime

#--------------------------------ARG PARSE-------------------------------------

def arg_getter():
    v_format = False
    print("\nINFO:")
    print("Insert a range of dates. If you don't write anything, recovery displays info from the last 7 days. If you only write the fiirst date, second date will be the actual date. \nProgram only acceps date formats yyyy-mm-dd or dd-mm-yyyy.")
    print("\n\n")
    print("First date:")
    while (v_format == False):
        fd_1 = str(input())
        v_format = valid_format(fd_1, v_format)
    if (str(fd_1) == ""):
        t_fd_1 = datetime.datetime.now().date() - datetime.timedelta(days=7)
        t_fd_2 = datetime.datetime.now().date()
        args_t = [t_fd_1, t_fd_2]
        return args_t
    t_fd_1 = str_to_date(fd_1)
    print("Second date:")
    v_format = False
    while (v_format == False):
        fd_2 = str(input())
        v_format = valid_format(fd_2, v_format)
    if (str(fd_2) == ""):
        t_fd_2 = datetime.datetime.now().date()
    else:
        t_fd_2 = str_to_date(fd_2)
    if(t_fd_1 < t_fd_2):
        args_t = [t_fd_1, t_fd_2]
    else:
        args_t = [t_fd_2, t_fd_1]

    return args_t

def str_to_date(fd):
    s_fd = str(fd).split("-")
    if(len(s_fd[0]) == 4 and len(s_fd[1]) == 2 and len(s_fd[2]) == 2):
        t_fd = datetime.date(int(s_fd[0]), int(s_fd[1]), int(s_fd[2]))
    elif(len(s_fd[2]) == 4 and len(s_fd[1]) == 2 and len(s_fd[0]) == 2):
        t_fd = datetime.date(int(s_fd[2]), int(s_fd[1]), int(s_fd[0]))
    else:
        print("Invalid time format.\nProgram only acceps formats yyyy-mm-dd or dd-mm-yyyy.")
        #exit()
    return (t_fd)

def valid_format(fd, v_format):
    s_fd = str(fd).split("-")
    if(str(fd) == ""):
        return True
    if(len(s_fd) < 3):
        print("Invalid time format.\nProgram only acceps formats yyyy-mm-dd or dd-mm-yyyy.\nIntroduce a valid date:")
        return (v_format)
    if(len(s_fd[0]) == 4 and len(s_fd[1]) == 2 and len(s_fd[2]) == 2):
        try:
            int(s_fd[0])
            int(s_fd[1])
            int(s_fd[2])
        except:
            print("Invalid time format.\nProgram only acceps formats yyyy-mm-dd or dd-mm-yyyy.\nIntroduce a valid date:")
        else:
            v_format = True
    elif(len(s_fd[2]) == 4 and len(s_fd[1]) == 2 and len(s_fd[0]) == 2):
        try:
            int(s_fd[0])
            int(s_fd[1])
            int(s_fd[2])
        except:
            print("Invalid time format.\nProgram only acceps formats yyyy-mm-dd or dd-mm-yyyy.\nIntroduce a valid date:")
        else:
            v_format = True
    else:
        print("Invalid time format.\nProgram only acceps formats yyyy-mm-dd or dd-mm-yyyy.\nIntroduce a valid date:")
    return (v_format)


#--------------------------------ARG PARSE-------------------------------------