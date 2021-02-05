from xml_filter import xmlprocess
import os
import xml.etree.ElementTree as elemTree
if __name__ == '__main__':
    obj = xmlprocess('C:/Working/02.05/Ch01_CH 01_0217/')
    xml = 'F:/Working/02.04/2021-0106 Yeosu^^^/Ship/xml/'
    img = 'F:/Working/02.04/2021-0106 Yeosu^^^/Ship/'


    # xml갯수 폴더이름 변경
    name = os.listdir('F:/Working/02.05/')

    for folder in name:
        obj.foldernameChange('F:/Working/02.05/{}'.format(folder)+'/')


    # obj.process('Ship')


    # obj.preprocessorImg(xml,img)

    # obj.deleteImg('Ship')

    # obj.deleteConfTag('Ship', 10)

    # obj.deleteTag('Ship', 350)
    
    # obj.modifyXml('Ship','Fender','Ship')

    # targetXML = open('F:/Working/1.29/Ch01_CH 01_2814/Ship_1412/xml/Ch01_CH 01_2814_1245.xml', 'rt', encoding='UTF8')
    #
    # tree = elemTree.parse(targetXML)
    #
    # root = tree.getroot()
    #
    # ##수정할 부분
    # target_tag = root.findall("object")
    #
    # original = target_tag[0].find('name').text  # 원본 String
    # print(original)


# target_path = 'C:/Working/02.05/Ch01_CH 01_0215/Ship/xml/Ch01_CH 01_0215_00665.xml'
#
# targetXML = open(target_path, 'rt', encoding='UTF8')
#
# tree = elemTree.parse(targetXML)
#
# root = tree.getroot()
#
# target_tag = root.findall("object")
#
# var = target_tag[1].find('bndbox').find('xmax').text
# print(var)
#
#
# for i in root.findall('object'):
#     print(i)
#     root.remove(i)
#     tree.write(target_path)



list = ['xmin','xmax']
count = 0
# for x in root.iter("bndbox"):
#     print(x.find(list[1]).text)
