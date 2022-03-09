import tkinter as tk
import time
import os
import locale

from matplotlib.pyplot import text
locale.setlocale(locale.LC_CTYPE, 'chinese')

#local parameter
WIDTH = 35
HEIGHT = 2
root = tk.Tk()
root.title('修仙辅助器')
root.geometry('500x500')
# 上次rush的时间
last_rush_datetime = -1
# 当前时间
now_datetime = -1
# 本次修炼时间
current_last_time = -1
# 到下一个等级剩余时间
next_level_remain_time = -1
# 当前等级
current_level = -1
# 下一个等级
next_level = ""
# 历史rush记录
history_datetime_list = []
# 所有等级列表
level_list = []

#创建界面元素
#上次坠机时间
last_rush_datetime_static_label = tk.Label(root, text='上次坠机时间',anchor="e", fg='blue', font=("黑体", 12),width=WIDTH,height=HEIGHT)
last_rush_datetime_dynamic_label = tk.Label(root, text='NULL',anchor="e", fg='blue', font=("黑体", 12),width=WIDTH,height=HEIGHT)
#道友当前时间
now_datetime_static_label = tk.Label(root, text='道友当前时间',anchor="e", fg='blue', font=("黑体", 12),width=WIDTH,height=HEIGHT)
now_datetime_dynamic_label = tk.Label(root, text='NULL',anchor="e", fg='blue', font=("黑体", 12),width=WIDTH,height=HEIGHT)
#道友当前等级
current_level_static_label = tk.Label(root, text='道友当前等级',anchor="e", fg='blue', font=("黑体", 12),width=WIDTH,height=HEIGHT)
current_level_dynamic_label = tk.Label(root, text='NULL',anchor="e", fg='blue', font=("黑体", 12),width=WIDTH,height=HEIGHT)
#道友下一割等级
next_level_static_label = tk.Label(root, text='道友下一割等级',anchor="e", fg='blue', font=("黑体", 12),width=WIDTH,height=HEIGHT)
next_level_dynamic_label = tk.Label(root, text='NULL',anchor="e", fg='blue', font=("黑体", 12),width=WIDTH,height=HEIGHT)
#美甲的窃魂卷持续时长
current_last_time_static_label = tk.Label(root, text='美甲的窃魂卷持续时长',anchor="e", fg='blue', font=("黑体", 12),width=WIDTH,height=HEIGHT)
current_last_time_dynamic_label = tk.Label(root, text='NULL',anchor="e", fg='blue', font=("黑体", 12),width=WIDTH,height=HEIGHT)
#突破倒计时
next_level_remain_time_static_label = tk.Label(root, text='突破倒计时',anchor="e", fg='blue', font=("黑体", 12),width=WIDTH,height=HEIGHT)
next_level_remain_time_dynamic_label = tk.Label(root, text='NULL',anchor="e", fg='blue', font=("黑体", 12),width=WIDTH,height=HEIGHT)

#为桌面元素布局
def grid_all():
    last_rush_datetime_static_label.grid(row=1,column=1)
    last_rush_datetime_dynamic_label.grid(row=1,column=2)
    #道友当前时间
    now_datetime_static_label.grid(row=2,column=1)
    now_datetime_dynamic_label.grid(row=2,column=2)
    #道友当前等级
    current_level_static_label.grid(row=3,column=1)
    current_level_dynamic_label.grid(row=3,column=2)
    #道友下一割等级
    next_level_static_label.grid(row=4,column=1)
    next_level_dynamic_label.grid(row=4,column=2)
    #美甲的窃魂卷持续时长
    current_last_time_static_label.grid(row=5,column=1)
    current_last_time_dynamic_label.grid(row=5,column=2)
    #突破倒计时
    next_level_remain_time_static_label.grid(row=6,column=1)
    next_level_remain_time_dynamic_label.grid(row=6,column=2)

#初始化
def init():
    #最开始要布局
    grid_all()
    global last_rush_datetime
    global now_datetime
    global level_list
    global current_level
    #初始化当前时间
    now_datetime = time.time()
    cwd = os.getcwd()
    f1 = open(cwd+"\\resourse\\current.txt","r",encoding="utf-8")
    f2 = open(cwd+"\\resourse\\level.txt","r",encoding="utf-8")
    #初始化上次rush时间
    last_rush_datetime = int(f1.readline().split('.')[0])
    #初始化level等级列表
    for line in f2.readlines():
        level_name , level_days = line.replace("\n",'').split(' ')
        level_list.append([level_name,int(level_days)])
    #初始化当前level
    for i in range(len(level_list)):
        # print(now_datetime-last_rush_datetime)
        if(now_datetime-last_rush_datetime  < (level_list[i+1][1])*86400):
            current_level = i
            break
    #初始化动态label的值
    last_rush_datetime_dynamic_label.configure(text=time.strftime("%Y年-%m月-%d号 %H小时%M分%S秒",last_rush_datetime))
    #tudo 上次的中断位置
    # current_level_dynamic_label.configure(text=)
    # last_rush_datetime_dynamic_label.configure(text=time.strftime("%Y年-%m月-%d号 %H小时%M分%S秒",last_rush_datetime))
    # last_rush_datetime_dynamic_label.configure(text=time.strftime("%Y年-%m月-%d号 %H小时%M分%S秒",last_rush_datetime))

#实时刷新
#Todo！
def update():
    global now_datetime
    global current_last_time
    global next_level_remain_time
    global current_level
    #更新datetime，time数据
    #更新实时数据
    now_datetime = time.time()
    current_last_time = now_datetime - last_rush_datetime
    next_level_remain_time = level_list[current_level+1][1]*86400 - current_last_time

    #实时判断是否升级
    #升级
    if next_level_remain_time <=0:
        current_level += 1
        #更新界面显示
        current_level_dynamic_label_str = f"Level {current_level} {level_list[current_level][0]} 嘻嘻"
        current_level_dynamic_label.configure(text=current_level_dynamic_label_str)
        next_level_remain_time_dynamic_label_str = f"Level {current_level+1} {level_list[current_level+1][0]} 嘻嘻嘻"
        next_level_remain_time_dynamic_label.configure(text=next_level_remain_time_dynamic_label_str)

    # 获取时间并转为字符串
    now_datetime_dynamic_label_str = time.strftime("%Y年-%m月-%d号 %H小时%M分%S秒",time.localtime(now_datetime))  
    current_last_time_dynamic_label_str = f"{int((current_last_time)/86400)}天"+time.strftime("%H小时%M分%S秒",time.gmtime(current_last_time))
    next_level_remain_time_dynamic_label_str = f"{int(next_level_remain_time/86400)}天"+time.strftime("%H小时%M分%S秒",time.gmtime(next_level_remain_time%86400))
    # 重新设置标签文本
    now_datetime_dynamic_label.configure(text=now_datetime_dynamic_label_str)
    current_last_time_dynamic_label.configure(text=current_last_time_dynamic_label_str)
    next_level_remain_time_dynamic_label.configure(text=next_level_remain_time_dynamic_label_str)
    # 每隔一秒调用函数gettime自身获取时间
    root.after(1000, update)

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


# var = tk.StringVar()    # 这时文字变量储存器
# l = tk.Label(root, 
#     textvariable=var,    # 标签的文字
#     bg='green',     # 标签背景颜色
#     font=('Arial', 12),     # 字体和字体大小
#     width=10, height=2  # 标签长宽(以字符长度计算)
#     )
# l.grid(row=0,column=0,pady=2)

# on_hit=False
 
# #按钮的函数
# def hit_me():
#     global on_hit#声明全局变量
#     if on_hit==False:
#         on_hit=True
#         var.set('You hit me!')
#     else:
#         on_hit=False
#         var.set('')
# #按钮
# b=tk.Button(root,text='点我',width=10,height=2,command=hit_me)#点击按钮执行一个名为“hit_me”的函数
# b.grid(row=0,column=2,pady=2)

init()

update()


root.mainloop()
