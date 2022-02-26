
from sys import dllhandle


f1 = open("resourse\\level_raw.txt","r",encoding="utf-8")
f2 = open("resourse\\level.txt",'w',encoding='utf-8')
level_list = []
current_word=f1.read(4)
while current_word:
    level_list.append(current_word)
    current_word=f1.read(4)
# print(level_list)
day_list = []
for i in range(1,125,3):
    day_list.append(i)
for i in range(128,193,4):
    day_list.append(i)
for i in range(197,308,5):
    day_list.append(i)
for i in range(312,469,6):
    day_list.append(i)
for i in range(475,518,7):
    day_list.append(i)
for i in range(525,614,8):
    day_list.append(i)
day_list.append(667)
day_list.append(778)
# print(day_list)
# print(len(level_list))
# print(len(day_list))
for i in range(len(level_list)):
    f2.writelines(level_list[i]+" "+str(day_list[i]) + '\n')
f1.close()
f2.close()
