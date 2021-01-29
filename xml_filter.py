import xml.etree.ElementTree as elemTree
import os
import shutil
from main import AutoLabel


#xml필터링 및 복사용 클래스
class xmlprocess(AutoLabel):

    def __init__(self, parent_path):
        self.parent_path = parent_path
        print('path가 등록되었습니다')

    def removeTag(self, path_str):
        list = os.listdir(path_str)
        for xml in list:
            tree = elemTree.parse(path_str + '{}'.format(xml))
            root = tree.getroot()

        print(len(root))


    def copyXml(self,xml_path,img_path,copy_folder):

        xmlList = os.listdir(xml_path)
        imgList = os.listdir(img_path)
        new_list = []
        dst = copy_folder  # 복사 원하는 폴더경로 지정
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
            dst = '{0}_0{1}.jpg'.format(new_name, count_no)
            dst = os.path.join(path, dst)
            os.rename(src, dst)
            count_no += 1


    def foldernameChange(self,path):
        folder_names = os.listdir(path)

        for name in folder_names:
                xml_count = os.listdir(path +'/{}/'.format(name)+ '/xml/')
                src = os.path.join(path, name)
                dst = '{0}_{1}'.format(name, len(xml_count))
                dst = os.path.join(path, dst)
                os.rename(src, dst)

    # def filenameChange(self, path, old_name, new_name): #파일이름(부분변경) 일괄변경
    #     super().filenameChange()
    #     file_names = os.listdir(path)
    #
    #     for name in file_names:
    #         src = os.path.join(path, name)
    #         dst = name.replace(old_name, new_name)  # 원하는 부분의 이름만 바꾸기
    #         dst = os.path.join(path, dst)
    #         os.rename(src, dst)

    def process(self,class_name): #object name이 존재하고 name이 일치할경우 통과, 불일치하거나 name이 없을경우 삭제
        parentList = os.listdir(self.parent_path)

        for parent in parentList:
            path_str = self.parent_path + '{}/xml/'.format(parent) #child폴더 수정할것 /xml/
            list = os.listdir(path_str)
            delCount = 0

            for file in list:
                try:
                    tree = elemTree.parse(path_str + '{}'.format(file))
                    root = tree.getroot()
                    object = root.findall('object')
                    name = object[0].find('name').text
                    objectName = class_name

                    if name==objectName or len(object) < 2:
                        # print('정상입니다')
                        pass

                    if len(object) >= 2 or len(object) < 1:
                        os.remove(path_str + '{}'.format(file))
                        delCount += 1
                        print('{}의 {}이 삭제되었습니다: {}개'.format(parent, file, delCount))

                except:
                    os.remove(path_str + '{}'.format(file))
                    delCount += 1
                    print('{}의 {}이 삭제되었습니다: {}개'.format(parent, file, delCount))

    def preprocessorImg(self, xml_path, img_path): #path끝에 '/'붙일것, xml이름과 비교해서 copy
        xmlList = os.listdir(xml_path)
        imgList = os.listdir(img_path)
        countNo = 0

        dst = './preImgs'
        for i in imgList:
            for j in xmlList:
                if i.replace('.jpg', '.xml') == j:

                    countNo += 1

                    shutil.copy(img_path + i, dst)  # dst 폴더로 복사
                    print('{0} was copied. Count: {1}'.format(i, countNo))
                    break;
                    # print(i)
                    # print('삭제된 파일: '+j)
                    # os.remove('./imgs/'+ j)


    def modifyXml(self, oldName, newName): #You can modify at <name> in Object tag, #param: old <name> -> new <name>
        xml = self.parent_path + 'xml/'
        countNo = 0

        for xml_file in os.listdir(xml):

            target_path = xml + xml_file
            targetXML = open(target_path, 'rt', encoding='UTF8')

            tree = elemTree.parse(targetXML)

            root = tree.getroot()

            ##수정할 부분
            target_tag = root.findall("object")
            try:
                original = target_tag[0].find('name').text  # 원본 String
                modified = original.replace(oldName, newName)
                target_tag[0].find('name').text = modified  # 수정

                tree.write(target_path)
                print("{} was successed!, count:{}".format(xml_file, countNo), modified)
                countNo += 1
            except:
                pass

    def deleteImg(self,newImg=None,img=None):
        newImg = './preImgs'
        img = obj.parent_path
        newImg = os.listdir(newImg)
        img = os.listdir(img)
        countNo = 0

        for i in newImg:
            for j in img:
                if i == j:
                    os.remove(obj.parent_path + j)
                    print('{0} was removed, count:{1}'.format(j, countNo))
                    countNo += 1
                    break;

if __name__ == '__main__':


    obj = xmlprocess('F:/Working/1.29/Ch01_CH 01_2815/Ship_976/')
    xml = obj.parent_path + 'xml/'
    newImg = './preImgs'
    img = obj.parent_path
    # obj.process()
         # obj.copyXml('F:/Container/000061~000072/ContainerRound000061/xml/', 'F:/Container/000061~000072/ContainerRound000062/', './xml')

    # obj.preprocessorImg(xml,newImg)


    # obj.modifyXml("Carrierge_Ship","Ship")

    newImg = os.listdir(newImg)
    img = os.listdir(img)
    countNo = 0

    for i in newImg:
        for j in img:
            if i == j:
                os.remove(obj.parent_path + j)
                print('{0} was removed, count:{1}'.format(j, countNo))
                countNo += 1
                break;








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