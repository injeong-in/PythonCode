import xml.etree.ElementTree as elemTree
import os

parentList = os.listdir('C:/Users/admin/Desktop/검수자 박정인 (3411)/')
print(parentList)

for parent in parentList:
    path_str = 'C:/Users/admin/Desktop/검수자 박정인 (3411)/{}/Xml/'.format(parent)
    list = os.listdir(path_str)
    delCount = 0

    for file in list:
        try:
            tree = elemTree.parse(path_str +'{}'.format(file))
            bouy = tree.find('./object')
            name = bouy.find('name')

            objectName = 'Buoy'

            if name.text == objectName:
                # print('정상입니다')
                pass

        except:
            os.remove(path_str+'{}'.format(file))
            delCount += 1
            print('{}의 {}이 삭제되었습니다: {}개'.format(parent,file,delCount))