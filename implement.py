from xml_filter import xmlprocess
import os
import xml.etree.ElementTree as elemTree
if __name__ == '__main__':


    date = '02.18'
    class_name = 'Bulk_Carrier'

    obj = xmlprocess('C:/')
    # obj = xmlprocess('C:/Working/{}/'.format(date))
    xml = 'C:/Working/{0}/{1}/xml/'.format(date, class_name)
    img = 'C:/Working/{0}/{1}/'.format(date, class_name)


    # xml갯수 폴더이름 변경
    path = 'F:/Working/02.18/JeungIn(8512)/'


    obj.foldernameChange(path)

    # obj.process('Container_Ship')

    # obj.minimumProcess('',class_name)

    # obj.preprocessorImg(xml,img)
    # obj.preprocessorImg('./xml', img)


    # obj.deleteImg(class_name)

    # first_index = obj.searchIndex(class_name, '0210_JunHyuck_009_0384.xml')
    # last_index = obj.searchIndex(class_name, '0210_JunHyuck_009_1709.xml')

    # obj.deleteConfTag(class_name)
    # obj.deleteSecondTag(class_name)
    # obj.exceedDeleteTag(class_name, 10, 90)
    # obj.rangeBelowDeleteTag(class_name, first_index, last_index, 60, 30)
    # obj.belowDeleteTag(class_name, 139, 90)

    # obj.rangeDeleteTag(class_name, first_index, last_index, 0, 1920, 800, 1080)
    # obj.rangeDelteExtraTag(class_name, first_index, last_index, 0)
    # obj.deletePath(class_name)

    # obj.moveNoneXml(class_name)
    # obj.moveXml(class_name, 3)


    # tag_list = obj.modifyXml(class_name,'Fender',class_name)
    # obj.totalModifyXml(class_name, 'Bulk_Carrier')
    # obj.rangeReduceHeight(class_name, first_index, last_index, 100, 25)
    # obj.reduceHeight(class_name,40, 10)
    # obj.reduceHeight('AutoLabel',30, 6)





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
