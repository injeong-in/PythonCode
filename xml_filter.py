import xml.etree.ElementTree as elemTree
import os
import shutil

class xmlprocess:

    def __init__(self, parent_path):
        self.parent_path = parent_path
        print('path가 등록되었습니다')

    def removeTag(self, path_str):
        list = os.listdir(path_str)
        for xml in list:
            tree = elemTree.parse(path_str + '{}'.format(xml))
            root = tree.getroot()

        print(len(root))


    def copyXml(self,xml_path,img_path):

        xmlList = os.listdir(xml_path)
        imgList = os.listdir(img_path)
        new_list = []
        dst = './xml'  # 복사 원하는 폴더경로 지정
        for i in xmlList:
            for j in imgList:
                if i[-6]+i[-5] == j[-6]+j[-5]:
                    shutil.copy(xml_path + i, dst)  # dst 폴더로 복사
                    print(j)
                    break;

    def filenameChange(self,path, new_name): #파일이름 일괄변경
        file_names = os.listdir(path)
        count_no = 0
        for name in file_names:
            src = os.path.join(path, name)
            dst = '{0}_{1}'.format(count_no, new_name)
            dst = os.path.join(path, dst)
            os.rename(src, dst)

    def filenameChange(self,path, old_name, new_name): #파일이름(부분변경) 일괄변경
        file_names = os.listdir(path)

        for name in file_names:
            src = os.path.join(path, name)
            dst = name.replace(old_name, new_name)  # 원하는 부분의 이름만 바꾸기
            dst = os.path.join(path, dst)
            os.rename(src, dst)

    def process(self): #object name이 존재하고 name이 일치할경우 통과, 불일치하거나 name이 없을경우 삭제
        parentList = os.listdir(self.parent_path)
        for parent in parentList:
            path_str = self.parent_path + '{}/xml/'.format(parent) #child폴더 수정할것 /xml/
            list = os.listdir(path_str)
            delCount = 0

            for file in list:
                try:
                    tree = elemTree.parse(path_str + '{}'.format(file))
                    object = tree.find('./object')
                    name = object.find('name')

                    objectName = 'Car_Carrier_Ship'

                    if name.text == objectName:
                        # print('정상입니다')
                        pass

                except:
                    os.remove(path_str + '{}'.format(file))
                    delCount += 1
                    print('{}의 {}이 삭제되었습니다: {}개'.format(parent, file, delCount))

if __name__ == '__main__':
     obj = xmlprocess('F:/Container/000031~000060/')
     obj.process()
     # obj.copyXml('F:/Container/00001~000030/ContainerRound000025/xml/','F:/Container/00001~000030/ContainerRound000027/')
     #
     # obj.filenameChange('./xml/','25_','27_')







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