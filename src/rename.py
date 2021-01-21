import os
from xml_filter import xmlprocess
import shutil

# list = os.listdir('C:/Users/admin/Desktop/exam2/')
# print(list)




def rename(path_str):

    list = os.listdir(path_str)
    obj = xmlprocess('F:/Container/')
    for i in range(len(list)):
        if len(list[i]) == 26:
            obj.filenameChange(path_str,'_{}.jpg'.format(list[i][-5]),'_00{}.jpg'.format(list[i][-5]))
        if len(list[i]) == 27:
            obj.filenameChange(path_str,'_{}.jpg'.format(list[i][-6]+list[i][-5]),'_0{}.jpg'.format(list[i][-6]+list[i][-5]))

#
for i in range(2):
    rename('F:/Container/000061~000072/ContainerRound0000{}/'.format(i+71))


# rename('F:/Container/000031~000060/ContainerRound0000{}/'.format(60))