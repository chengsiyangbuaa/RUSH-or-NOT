

import os

from matplotlib.pyplot import close
from numpy import record


cwd = os.getcwd()
history_path = cwd+"\\resourse\\history.txt"
#读出history.txt中的所有历史坠机记录
def read_history_total_records(path):
    f = open(path,'r',encoding="utf-8")
    record_list = []
    for line in f.readlines():
        record_list.append(line.split(' '))
    f.close()
    return record_list

#读出history.txt中的上次历史坠机记录
def read_history_last_record(path):
    return read_history_total_records(path)[-1]

#读出history.txt中的上次历史坠机时间
def read_history_last_datetime(path):
    return read_history_last_record(path)[2]

#增加history.txt内容，在尾部增加一条坠机记录
def append_history_a_new_record(path, start_time = 1645874396.3903117, end_time = 1705874396.3903117, level_name = '痴傻无知'):
    last_time = end_time - start_time
    id = len(read_history_total_records(path))
    new_line = str(id) + ' ' + str(start_time) + ' ' + str(end_time) + ' ' + str(last_time) + ' ' + level_name + '\n'
    f = open(path,'a',encoding="utf-8")
    f.write(new_line)
    f.close()

record_list = read_history_total_records(history_path)
# for line in record_list:
#     print(line)

last_record = read_history_last_record(history_path)
# print(last_record)

last_record_datetime = read_history_last_datetime(history_path)
# print(last_record_datetime)

append_history_a_new_record(history_path)