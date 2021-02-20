import os
import xml.etree.ElementTree as elemTree

# target_path = '../xml/0207_SangEun_008_0778.xml'
# targetXML = open(target_path, 'rt', encoding='UTF8')
#
# tree = elemTree.parse(targetXML)
#
# root = tree.getroot()
#
# ##수정할 부분
# target_tag = root.findall("object")
#
# x_min = target_tag[0].find('bndbox').find('xmin').text
#
# if x_min is None:
#     print('This is None type')

list = os.listdir('C:/Working/02.17/Bulk_Carrier/')
string = ''

for i in range(0, len(list)):
    if list[i] == string:
        print(i)
