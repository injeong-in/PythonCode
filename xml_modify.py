import shutil
import os
import fileinput
import sys
from xml_filter import xmlprocess

# path = 'F:/Container/00001~000030'
# # parentList = os.listdir(path)
# # print(parentList)
# #
# # for parent in parentList:
# #     path_str = path + '/{}/'.format(parent)
# #     list = os.listdir(path_str)
# #     print(parent,'개수:', len(list)-2)


# 파일 이름 전체 바꾸기
# path = './xml'
#
# file_names = os.listdir(path)
#
# for name in file_names:
#     src = os.path.join(path, name)
#     dst = name.replace('13_', '17_') #원하는 부분의 이름만 바꾸기
#     dst = os.path.join(path, dst)
#     os.rename(src, dst)


# xml라인 수정
index = 'files[-7] + files[-6] + files[-5]',



# obj = xmlprocess('F:/Container/')
# obj.filenameChange('./xml/','67_','68_')

xml_file = os.listdir('./xml/')


for files in xml_file:

    for line in fileinput.input('./xml/{}'.format(files), inplace = True):
        if '<folder>' in line :
            line = line.replace(line, '    <folder>ContainerRound000068</folder>\n')
        if '<filename>Container' in line :
            line = line.replace(line, '    <filename>ContainerRound000068_{}.jpg</filename>\n'.format(files[-7] + files[-6] + files[-5])) #인덱스 활용해서 부분수정
        if '<name>' in line :
            line = line.replace(line, '        <name>Ship</name>\n')
        if '<path>' in line :
            line = line.replace(line, '')
        sys.stdout.write(line)
