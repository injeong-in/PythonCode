import xml.etree.ElementTree as elemTree
import os

class xmlprocess:

    def __init__(self, parent_path):
        self.parent_path = parent_path
        print('path가 등록되었습니다')


    def process(self): #object name이 존재하고 name이 일치할경우 통과, 불일치하거나 name이 없을경우 삭제
        parentList = os.listdir(self.parent_path)
        for parent in parentList:
            path_str = self.parent_path + '{}/xml/'.format(parent) #child폴더 수정할것 /xml/
            list = os.listdir(path_str)
            delCount = 0

            for file in list:
                try:
                    tree = elemTree.parse(path_str + '{}'.format(file))
                    bouy = tree.find('./object')
                    name = bouy.find('name')

                    objectName = 'Buoy'

                    if name.text == objectName:
                        # print('정상입니다')
                        pass

                except:
                    os.remove(path_str + '{}'.format(file))
                    delCount += 1
                    print('{}의 {}이 삭제되었습니다: {}개'.format(parent, file, delCount))

if __name__ == '__main__':
     obj = xmlprocess('C:/Users/admin/Desktop/segmentation/')
     obj.process()


        # parentList = os.listdir('C:/Users/admin/Desktop/검수자 박정인 (3411)/')
        # print(parentList)
        #
        # for parent in parentList:
        #     path_str = 'C:/Users/admin/Desktop/검수자 박정인 (3411)/{}/Xml/'.format(parent)
        #     list = os.listdir(path_str)
        #     delCount = 0
        #
        #     for file in list:
        #         try:
        #             tree = elemTree.parse(path_str +'{}'.format(file))
        #             bouy = tree.find('./object')
        #             name = bouy.find('name')
        #
        #             objectName = 'Buoy'
        #
        #             if name.text == objectName:
        #                 # print('정상입니다')
        #                 pass
        #
        #         except:
        #             os.remove(path_str+'{}'.format(file))
        #             delCount += 1
        #             print('{}의 {}이 삭제되었습니다: {}개'.format(parent,file,delCount))