import os
from xml_filter import xmlprocess
import shutil

# list = os.listdir('C:/Users/admin/Desktop/exam2/')
# print(list)




def renameJpg(path_str, length):

    list = os.listdir(path_str)
    obj = xmlprocess('C:/')
    count = 0
    for i in range(len(list)):
        if len(list[i]) == length:
            obj.filenameChange(path_str, list[i], '_{}.jpg'.format(list[i][-5]),'_0000{}.jpg'.format(list[i][-5]))
            count += 1
            print(list[i], 'count:{}'.format(count))
        if len(list[i]) == length + 1:
            obj.filenameChange(path_str, list[i], '_{}.jpg'.format(list[i][-6]+list[i][-5]),'_000{}.jpg'.format(list[i][-6]+list[i][-5]))
            count += 1
            print(list[i], 'count:{}'.format(count))
        if len(list[i]) == length + 2:
            obj.filenameChange(path_str, list[i], '_{}.jpg'.format(list[i][-7]+list[i][-6]+list[i][-5]),'_00{}.jpg'.format(list[i][-7]+list[i][-6]+list[i][-5]))
            count += 1
            print(list[i], 'count:{}'.format(count))
        if len(list[i]) == length + 3:
            obj.filenameChange(path_str,list[i],'_{}.jpg'.format(list[i][-8]+list[i][-7]+list[i][-6]+list[i][-5]),'_0{}.jpg'.format(list[i][-8]+list[i][-7]+list[i][-6]+list[i][-5]))
            count += 1
            print(list[i], 'count:{}'.format(count))



def renameXml(path_str, length):
    list = os.listdir(path_str)
    obj = xmlprocess('C:/')
    count = 0
    for i in range(len(list)):
        if len(list[i]) == length:
            obj.filenameChange(path_str, list[i], '_{}.xml'.format(list[i][-5]),'_0000{}.xml'.format(list[i][-5]))
            count += 1
            print(list[i], 'count:{}'.format(count))
        if len(list[i]) == length + 1:
            obj.filenameChange(path_str, list[i], '_{}.xml'.format(list[i][-6]+list[i][-5]),'_000{}.xml'.format(list[i][-6]+list[i][-5]))
            count += 1
            print(list[i], 'count:{}'.format(count))
        if len(list[i]) == length + 2:
            obj.filenameChange(path_str, list[i], '_{}.xml'.format(list[i][-7]+list[i][-6]+list[i][-5]),'_00{}.xml'.format(list[i][-7]+list[i][-6]+list[i][-5]))
            count += 1
            print(list[i], 'count:{}'.format(count))
        if len(list[i]) == length + 3:
            obj.filenameChange(path_str,list[i],'_{}.xml'.format(list[i][-8]+list[i][-7]+list[i][-6]+list[i][-5]),'_0{}.xml'.format(list[i][-8]+list[i][-7]+list[i][-6]+list[i][-5]))
            count += 1
            print(list[i], 'count:{}'.format(count))

# var = 'Ch01_CH 01_0217_0.jpg'
# print(len(var))

path = 'C:/Working/02.08/Ch01_CH 01_0415/Ship/'
list = os.listdir(path)

print(len('Ch01_CH 01_0415_516.jpg'))



# renameJpg(path, 21)
renameXml(path+'xml/', 21)
# rename('F:/Container/000031~000060/ContainerRound0000{}/'.format(60))