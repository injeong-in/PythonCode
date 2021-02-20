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


    def searchIndex(self, child_folder, xml_name):
        xml = self.parent_path + '{}/'.format(child_folder) + 'xml/'
        list = os.listdir(xml)
        indexNo = 0
        for i in range(0, len(list)):
            if list[i] == xml_name:
                indexNo = i
                print(i)
        return indexNo;

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


    # def filenameChange(self, path, new_name): #파일이름 일괄변경
    #     file_names = os.listdir(path)
    #     count_no = 0
    #     for name in file_names:
    #         src = os.path.join(path, name)
    #         dst = '{0}_0{1}.jpg'.format(new_name, count_no)
    #         dst = os.path.join(path, dst)
    #         os.rename(src, dst)
    #         count_no += 1


    def foldernameChange(self,path):
        folder_names = os.listdir(path)

        for name in folder_names:
                xml_count = os.listdir(path + name + '/xml/')
                src = os.path.join(path, name)
                dst = '{0}({1})'.format(name, len(xml_count))

                if name[-2] == '(' and name[-1] == ')':
                    dst = name.replace('()', '({})'.format(len(xml_count)))

                dst = os.path.join(path, dst)
                os.rename(src, dst)
                print('{}로 폴더명이 변경되었습니다'.format(dst))



    def filenameChange(self, path, name, old_name, new_name): #파일이름(부분변경) 일괄변경

            src = os.path.join(path, name)
            dst = name.replace(old_name, new_name)  # 원하는 부분의 이름만 바꾸기
            dst = os.path.join(path, dst)
            os.rename(src, dst)

    def process(self,class_name): #object name이 존재하고 name이 일치할경우 통과, 불일치하거나 name이 없을경우 삭제
        parentList = os.listdir(self.parent_path)

        for i in range(0, len(parentList)):
            path_str = self.parent_path + '{0}/{1}/xml/'.format(parentList[i],class_name) #child폴더 수정할것 /xml/
            list = os.listdir(path_str)
            delCount = 0 #삭제개수 카운트 초기화

            for file in list:
                try:
                    tree = elemTree.parse(path_str + '{}'.format(file))
                    root = tree.getroot()
                    object = root.findall('object')
                    name = object[0].find('name').text
                    objectName = class_name

                    if name==objectName or len(object) > 2:
                        # print('정상입니다')
                        pass

                    if len(object) > 3 or len(object) < 1:
                        os.remove(path_str + '{}'.format(file))
                        delCount += 1
                        print('{}의 {}이 삭제되었습니다: {}개'.format(parentList[i], file, delCount))

                except:
                    os.remove(path_str + '{}'.format(file))
                    delCount += 1
                    print('{}의 {}이 삭제되었습니다: {}개'.format(parentList[i], file, delCount))

    def minimumProcess(self,folder_name,class_name): #object name이 존재하고 name이 일치할경우 통과, 불일치하거나 name이 없을경우 삭제

            path_str = self.parent_path + '{0}/{1}/xml/'.format(folder_name, class_name) #child폴더 수정할것 /xml/
            list = os.listdir(path_str)
            delCount = 0 #삭제개수 카운트 초기화

            for file in list:

                try:
                    tree = elemTree.parse(path_str + '{}'.format(file))
                    root = tree.getroot()
                    object = root.findall('object')
                    name = object[0].find('name').text
                    objectName = class_name

                    if name==objectName or len(object) > 1:
                        # print('정상입니다')
                        pass
                    else:
                        os.remove(path_str + '{}'.format(file))
                        delCount += 1
                        print('{}의 {}이 삭제되었습니다: {}개'.format(folder_name, file, delCount))
                    # if len(object) > 3 or len(object) < 1:
                    #     os.remove(path_str + '{}'.format(file))
                    #     delCount += 1
                    #     print('{}의 {}이 삭제되었습니다: {}개'.format(folder_name, file, delCount))

                except:
                    os.remove(path_str + '{}'.format(file))
                    delCount += 1
                    print('{}의 {}이 삭제되었습니다: {}개'.format(folder_name, file, delCount))


    def preprocessorImg(self, xml_path, img_path): #path끝에 '/'붙일것, xml이름과 비교해서 copy
        xmlList = os.listdir(xml_path)
        imgList = os.listdir(img_path)
        countNo = 0

        dst = './preImgs'

        if len(os.listdir('./preImgs')) > 0:
            print('파일이 존재합니다')
            return


        for i in imgList:
            print('{}를 비교중입니다'.format(i))
            for j in xmlList:
                try:
                    if i.replace('.jpg', '.xml') == j or i.replace('.JPG', '.xml') == j:

                        countNo += 1

                        shutil.copy(img_path + i, dst)  # dst 폴더로 복사
                        print('{0} was copied. Count: {1}'.format(i, countNo))
                        break;
                        # print(i)
                        # print('삭제된 파일: '+j)
                        # os.remove('./imgs/'+ j)
                    if j == xmlList[len(xmlList)-1]:
                        print('{}는 같은값이 없습니다'.format(i))
                except:
                    print('Finish!')



    def modifyXml(self, child_folder, oldName, newName): #You can modify at <name> in Object tag, #param: old <name> -> new <name>
        xml = self.parent_path +'{}/'.format(child_folder)+ 'xml/'
        countNo = 0
        tag_list = []

        for xml_file in os.listdir(xml):

            target_path = xml + xml_file
            targetXML = open(target_path, 'rt', encoding='UTF8')

            tree = elemTree.parse(targetXML)

            root = tree.getroot()

            ##수정할 부분
            target_tag = root.findall("object")
            try:
                for i in range(0,5):
                    original = target_tag[i].find('name').text  # 원본 String
                    if original == newName:
                        pass
                    if oldName == original:
                        modified = original.replace(oldName, newName)
                        target_tag[i].find('name').text = modified  # 수정
                        tree.write(target_path)
                        print("{} was successed!, count:{}".format(xml_file, countNo), modified)
                        countNo += 1
                    else:
                        tag_list.append(original)

            except:
                pass

            return tag_list;

    def totalModifyXml(self, child_folder, newName): #You can modify at <name> in Object tag, #param: old <name> -> new <name>
        xml = self.parent_path +'{}/'.format(child_folder)+ 'xml/'
        countNo = 0

        for xml_file in os.listdir(xml):

            target_path = xml + xml_file
            targetXML = open(target_path, 'rt', encoding='UTF8')

            tree = elemTree.parse(targetXML)

            root = tree.getroot()

            ##수정할 부분
            target_tag = root.findall("object")
            try:
                for i in range(0,5):
                    original = target_tag[i].find('name').text  # 원본 String

                    target_tag[i].find('name').text = newName  # 수정
                    tree.write(target_path)
                    countNo += 1
                    print("{0}을 {1}로 변경, 개수: {2}".format(original, newName, countNo), xml_file)

            except:
                pass

    def exceedDeleteTag(self, child_folder, max_width, max_height):  # max_width, max_height 초과값이면 object 태그 삭제
        xml = self.parent_path + '{}/'.format(child_folder) + 'xml/'
        countNo = 0

        for xml_file in os.listdir(xml):

            target_path = xml + xml_file
            targetXML = open(target_path, 'rt', encoding='UTF8')
            try:
                tree = elemTree.parse(targetXML)

                root = tree.getroot()


                ##수정할 부분
                target_tag = root.findall("object")

                for j in range(0, len(target_tag)):
                        x_min = int(target_tag[j].find('bndbox').find('xmin').text)  # 원본 String
                        x_max = int(target_tag[j].find('bndbox').find('xmax').text)
                        y_min = int(target_tag[j].find('bndbox').find('ymin').text)
                        y_max = int(target_tag[j].find('bndbox').find('ymax').text)
                        width = x_max - x_min
                        height = y_max - y_min

                        if (width > max_width and height > max_height) or y_min < 100 or y_max > 1020 or x_min < 100 or x_max > 1910: # width가 과하게 크거나 height가 10보다 낮으면 삭제
                            root.remove(target_tag[j])
                            tree.write(target_path)
                            countNo += 1
                            print('{}의 {}번째 object 태그가 삭제되었습니다, 삭제개수: {}개'.format(xml_file, j, countNo))



            except:
                pass

    def rangeExceedDeleteTag(self, child_folder, first_index, last_index, max_width, max_height):  # max_width, max_height 초과값이면 object 태그 삭제
        xml = self.parent_path + '{}/'.format(child_folder) + 'xml/'
        countNo = 0
        list = os.listdir(xml)

        for i in range(first_index, last_index):

            target_path = xml + list[i]
            targetXML = open(target_path, 'rt', encoding='UTF8')

            try:
                tree = elemTree.parse(targetXML)

                root = tree.getroot()

                ##수정할 부분
                target_tag = root.findall("object")

                for j in range(0, len(target_tag)):
                        x_min = int(target_tag[j].find('bndbox').find('xmin').text)  # 원본 String
                        x_max = int(target_tag[j].find('bndbox').find('xmax').text)
                        y_min = int(target_tag[j].find('bndbox').find('ymin').text)
                        y_max = int(target_tag[j].find('bndbox').find('ymax').text)
                        width = x_max - x_min
                        height = y_max - y_min

                        if (width > max_width and height > max_height) or y_min < 100 or y_max > 1020 or x_min < 100 or x_max > 1910: # width가 과하게 크거나 height가 10보다 낮으면 삭제
                            root.remove(target_tag[j])
                            tree.write(target_path)
                            countNo += 1
                            print('{}의 {}번째 object 태그가 삭제되었습니다, 삭제개수: {}개'.format(list[i], j, countNo))



            except:
                pass


    def rangeDelteExtraTag(self, child_folder, first_index, last_index, tag_index):  # 입력한 인덱스넘버를 제외한 모든 object tag 삭제
        xml = self.parent_path + '{}/'.format(child_folder) + 'xml/'
        countNo = 0
        list = os.listdir(xml)

        for i in range(first_index, last_index):

            target_path = xml + list[i]
            targetXML = open(target_path, 'rt', encoding='UTF8')
            try:
                tree = elemTree.parse(targetXML)

                root = tree.getroot()


                ##수정할 부분
                target_tag = root.findall("object")
                for j in range(0, len(target_tag)):
                    if j == tag_index:
                        pass
                    else:
                        root.remove(target_tag[j])
                        tree.write(target_path)
                        countNo += 1
                        print('{}의 {}번째 object 태그가 삭제되었습니다, 삭제개수: {}개'.format(list[i], j+1, countNo))

            except:
                pass


    def rangeDeleteTag(self, child_folder,first_index,last_index, x_left, x_right, y_high, y_low):  # 원하는 x,y범위 안의 태그를 삭제
        xml = self.parent_path + '{}/'.format(child_folder) + 'xml/'
        countNo = 0
        list = os.listdir(xml)

        for i in range(first_index, last_index):

            target_path = xml + list[i]
            targetXML = open(target_path, 'rt', encoding='UTF8')
            try:
                tree = elemTree.parse(targetXML)

                root = tree.getroot()


                ##수정할 부분
                target_tag = root.findall("object")

                for j in range(0, len(target_tag)):
                        x_min = int(target_tag[j].find('bndbox').find('xmin').text)  # 원본 String
                        x_max = int(target_tag[j].find('bndbox').find('xmax').text)
                        y_min = int(target_tag[j].find('bndbox').find('ymin').text)
                        y_max = int(target_tag[j].find('bndbox').find('ymax').text)
                        width = x_max - x_min
                        height = y_max - y_min

                        if x_left < x_min < x_right and y_high < y_min < y_low:
                            root.remove(target_tag[j])
                            tree.write(target_path)
                            countNo += 1
                            print('{}의 {}번째 object 태그가 삭제되었습니다, 삭제개수: {}개'.format(list[i], j+1, countNo))



            except:
                pass

    def rangeDeleteTag2(self, child_folder,first_index,last_index, y_value):  # max_width, max_height 초과값이면 object 태그 삭제
        xml = self.parent_path + '{}/'.format(child_folder) + 'xml/'
        countNo = 0
        list = os.listdir(xml)

        for i in range(first_index, last_index):

            target_path = xml + list[i]
            targetXML = open(target_path, 'rt', encoding='UTF8')
            try:
                tree = elemTree.parse(targetXML)

                root = tree.getroot()


                ##수정할 부분
                target_tag = root.findall("object")

                for j in range(0, len(target_tag)):
                        x_min = int(target_tag[j].find('bndbox').find('xmin').text)  # 원본 String
                        x_max = int(target_tag[j].find('bndbox').find('xmax').text)
                        y_min = int(target_tag[j].find('bndbox').find('ymin').text)
                        y_max = int(target_tag[j].find('bndbox').find('ymax').text)
                        width = x_max - x_min
                        height = y_max - y_min

                        if y_min < y_value:
                            root.remove(target_tag[j])
                            tree.write(target_path)
                            countNo += 1
                            print('{}의 {}번째 object 태그가 삭제되었습니다, 삭제개수: {}개'.format(list[i], j, countNo))



            except:
                pass


    def deletePath(self, child_folder):  # max_width, max_height 초과값이면 object 태그 삭제
        xml = self.parent_path + '{}/'.format(child_folder) + 'xml/'
        countNo = 0

        for xml_file in os.listdir(xml):

            target_path = xml + xml_file
            targetXML = open(target_path, 'rt', encoding='UTF8')

            tree = elemTree.parse(targetXML)

            root = tree.getroot()


            ##삭제할 태그
            target_tag = root.findall("path")

            try:
                for i in range(0, len(target_tag)):
                    root.remove(target_tag[i])
                    tree.write(target_path)
                    countNo += 1
                    print('{}의 {}번째 path 태그가 삭제되었습니다, 삭제개수: {}개'.format(xml_file, i, countNo))

            except:
                pass

    def moveNoneXml(self, child_folder):  #
        xml = self.parent_path + '{}/'.format(child_folder) + 'xml/'
        countNo = 0

        for xml_file in os.listdir(xml):

            target_path = xml + xml_file
            targetXML = open(target_path, 'rt', encoding='UTF8')

            tree = elemTree.parse(targetXML)

            root = tree.getroot()

            ##수정할 부분
            target_tag = root.findall("object")
            try:
                for i in range(0, len(target_tag)):
                    x_min = target_tag[i].find('bndbox').find('xmin').text  # 원본 String

                    if x_min is None:
                        targetXML.close()
                        shutil.move(target_path, './xml')
                        countNo += 1
                        print(countNo)

            except:
                print('error')
                targetXML.close()
                shutil.move(target_path, './xml')
                countNo += 1
                print('error: '+ countNo)


    def moveXml(self, child_folder, tagCount):  #
        xml = self.parent_path + '{}/'.format(child_folder) + 'xml/'
        countNo = 0

        for xml_file in os.listdir(xml):

            target_path = xml + xml_file
            targetXML = open(target_path, 'rt', encoding='UTF8')

            tree = elemTree.parse(targetXML)

            root = tree.getroot()

            ##수정할 부분
            target_tag = root.findall("object")

            if len(target_tag) == tagCount:
                try:
                    targetXML.close()
                    shutil.move(target_path, './xml')
                    countNo += 1
                    print(countNo)

                except:
                    pass


    def rangeBelowDeleteTag(self, child_folder, first_index, last_index, max_width, max_height):  # max_width 초과값이면 object 태그 삭제
        xml = self.parent_path + '{}/'.format(child_folder) + 'xml/'
        countNo = 0
        list = os.listdir(xml)

        for i in range(first_index, last_index):

            target_path = xml + list[i]
            targetXML = open(target_path, 'rt', encoding='UTF8')
            try:
                tree = elemTree.parse(targetXML)

                root = tree.getroot()

                ##수정할 부분
                target_tag = root.findall("object")

                for j in range(0, len(target_tag)):
                        x_min = int(target_tag[j].find('bndbox').find('xmin').text)  # 원본 String
                        x_max = int(target_tag[j].find('bndbox').find('xmax').text)
                        y_min = int(target_tag[j].find('bndbox').find('ymin').text)
                        y_max = int(target_tag[j].find('bndbox').find('ymax').text)

                        width = x_max - x_min
                        height = y_max - y_min

                        if width < max_width:
                            pass

                        if (width < max_width and height < max_height): # width가 과하게 크거나 height가 10보다 낮으면 삭제
                            root.remove(target_tag[j])
                            tree.write(target_path)
                            countNo += 1
                            print('{}의 {}번째 object 태그가 삭제되었습니다, 삭제개수: {}개'.format(list[i], j, countNo))
            except:
                pass


    def belowDeleteTag(self, child_folder, max_width, max_height):  # max_width 초과값이면 object 태그 삭제
        xml = self.parent_path + '{}/'.format(child_folder) + 'xml/'
        countNo = 0

        for xml_file in os.listdir(xml):

            target_path = xml + xml_file
            targetXML = open(target_path, 'rt', encoding='UTF8')
            try:
                tree = elemTree.parse(targetXML)

                root = tree.getroot()

                ##수정할 부분
                target_tag = root.findall("object")

                for j in range(0, len(target_tag)):
                        x_min = int(target_tag[j].find('bndbox').find('xmin').text)  # 원본 String
                        x_max = int(target_tag[j].find('bndbox').find('xmax').text)
                        y_min = int(target_tag[j].find('bndbox').find('ymin').text)
                        y_max = int(target_tag[j].find('bndbox').find('ymax').text)

                        width = x_max - x_min
                        height = y_max - y_min

                        if width < max_width:
                            pass

                        if (width < max_width and height < max_height) or y_max == 1079 or 0 == x_min: # width가 과하게 크거나 height가 10보다 낮으면 삭제
                            root.remove(target_tag[j])
                            tree.write(target_path)
                            countNo += 1
                            print('{}의 {}번째 object 태그가 삭제되었습니다, 삭제개수: {}개'.format(xml_file, j, countNo))
            except:
                pass

    def rangeReduceHeight(self, child_folder, first_index, last_index, least_height, height):  # param: 아래폴더, 최소 height값(이상일 경우 높이값 줄이기), 줄이고싶은 수치
        xml = self.parent_path + '{}/'.format(child_folder) + 'xml/'
        countNo = 0
        list = os.listdir(xml)

        for i in range(first_index, last_index):

            target_path = xml + list[i]
            targetXML = open(target_path, 'rt', encoding='UTF8')
            try:
                tree = elemTree.parse(targetXML)

                root = tree.getroot()

                ##수정할 부분
                target_tag = root.findall("object")

                for j in range(0, len(target_tag)):
                        y_min = int(target_tag[j].find('bndbox').find('ymin').text)
                        y_max = int(target_tag[j].find('bndbox').find('ymax').text)
                        h_eight = y_max - y_min
                        if h_eight > least_height:
                            target_tag[j].find('bndbox').find('ymin').text = str(y_min + height)
                            tree.write(target_path)
                            countNo += 1
                            print('{}의 {}번째 object 태그가 변경되었습니다, 변경개수: {}개'.format(list[i], j+1, countNo))

                        # if i > 0:
                        #     root.remove(target_tag[i])
                        #     tree.write(target_path)
                        #     countNo += 1
                        #     print('{}의 {}번째 object 태그가 삭제되었습니다, 삭제개수: {}개'.format(xml_file, i+1, countNo))
            except:
                pass


    def reduceHeight(self, child_folder, least_height, height):  # param: 아래폴더, 최소 height값(이상일 경우 높이값 줄이기), 줄이고싶은 수치
        xml = self.parent_path + '{}/'.format(child_folder) + 'xml/'
        countNo = 0

        for xml_file in os.listdir(xml):

            target_path = xml + xml_file
            targetXML = open(target_path, 'rt', encoding='UTF8')

            try:
                tree = elemTree.parse(targetXML)

                root = tree.getroot()

                ##수정할 부분
                target_tag = root.findall("object")

                for i in range(0, len(target_tag)):
                        y_min = int(target_tag[i].find('bndbox').find('ymin').text)
                        y_max = int(target_tag[i].find('bndbox').find('ymax').text)
                        h_eight = y_max - y_min
                        if h_eight > least_height:
                            target_tag[i].find('bndbox').find('ymin').text = str(y_min + height)
                            tree.write(target_path)
                            countNo += 1
                            print('{}의 {}번째 object 태그가 변경되었습니다, 변경개수: {}개'.format(xml_file, i+1, countNo))

                        # if i > 0:
                        #     root.remove(target_tag[i])
                        #     tree.write(target_path)
                        #     countNo += 1
                        #     print('{}의 {}번째 object 태그가 삭제되었습니다, 삭제개수: {}개'.format(xml_file, i+1, countNo))
            except:
                pass

    def deleteSecondTag(self, child_folder):  # index 0번째 object태그 외에 모두 삭제
        xml = self.parent_path + '{}/'.format(child_folder) + 'xml/'
        countNo = 0

        for xml_file in os.listdir(xml):

            target_path = xml + xml_file
            targetXML = open(target_path, 'rt', encoding='UTF8')
            try:
                tree = elemTree.parse(targetXML)

                root = tree.getroot()

                ##수정할 부분
                target_tag = root.findall("object")


                for i in range(0, len(target_tag)):
                    if i > 2:
                        root.remove(target_tag[i])
                        tree.write(target_path)
                        countNo += 1
                        print('{}의 {}번째 object 태그가 삭제되었습니다, 삭제개수: {}개'.format(xml_file, i+1, countNo))
            except:
                pass

    def deleteConfTag(self, child_folder, conf_width=None):  # 두 박스의 xmin값의 차가 conf_width 이하 값이면 object 태그 삭제
        xml = self.parent_path + '{}/'.format(child_folder) + 'xml/'
        countNo = 0

        for xml_file in os.listdir(xml):

            target_path = xml + xml_file
            targetXML = open(target_path, 'rt', encoding='UTF8')

        try:
            tree = elemTree.parse(targetXML)

            root = tree.getroot()

            ##수정할 부분
            target_tag = root.findall("object")

            for i in range(0, len(target_tag)-1):
                for j in range(i+1, len(target_tag)):
                        x_min = int(target_tag[i].find('bndbox').find('xmin').text)  # 원본 String
                        x_min2 = int(target_tag[j].find('bndbox').find('xmin').text)  # 원본 String
                        x_max = int(target_tag[i].find('bndbox').find('xmax').text)
                        x_max2 = int(target_tag[j].find('bndbox').find('xmax').text)
                        y_min = int(target_tag[i].find('bndbox').find('ymin').text)
                        y_min2 = int(target_tag[j].find('bndbox').find('ymin').text)  # 원본 String
                        y_max = int(target_tag[i].find('bndbox').find('ymax').text)
                        y_max2 = int(target_tag[j].find('bndbox').find('ymax').text)

                        min_width = x_min - x_min2
                        max_width = x_max - x_max2

                        # if min_width > conf_width or max_width > conf_width:
                        #     pass
                        # else:
                        #     # if x_max-x_min < x_max2 - x_min2:
                        #     #     root.remove(target_tag[i])
                        #     #     tree.write(target_path)
                        #     #     countNo += 1
                        #     #     print('{}가 삭제되었습니다, 삭제개수: {}장'.format(xml_file, countNo))
                        #     #     break;
                        if (x_min2 < x_max < x_max2 or x_min < x_max2 < x_max) and (y_min < y_max2 < y_max or y_min2 < y_max < y_max2):
                                root.remove(target_tag[i])
                                tree.write(target_path)
                                countNo += 1
                                print('{}가 삭제되었습니다, 삭제개수: {}개'.format(xml_file, countNo))
                                break;
                        else:
                                # root.remove(target_tag[j])
                                # tree.write(target_path)
                                # countNo += 1
                                # print('{}가 삭제되었습니다, 삭제개수: {}개'.format(xml_file, countNo))
                                # break;
                                pass
        except:
            pass


    def deleteImg(self,childFolder,newImg=None,img=None):
        newImg = './preImgs'
        img = self.parent_path + '{}/'.format(childFolder)
        newImg = os.listdir(newImg)
        img = os.listdir(img)
        countNo = 0

        for i in newImg:
            for j in img:
                if i == j:
                    os.remove(self.parent_path +'{}/'.format(childFolder)+ j)
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