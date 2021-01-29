from xml_filter import xmlprocess
import os
import xml.etree.ElementTree as elemTree
if __name__ == '__main__':
    obj = xmlprocess('F:/Working/1.29/Ch01_CH 01_2814/Ship_1412/')
    xml ='F:/Working/1.29/Ch01_CH 01_2815/Ship_976/xml/'
    img='F:/Working/1.29/Ch01_CH 01_2815/Ship_976/'


    #xml존재하는 이미지 복사
    # obj.preprocessorImg(xml,img)




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

    obj.modifyXml('Fender','Ship')

    # obj.foldernameChange('F:/Working/1.29/2021-0123 IncheonPort')
    # 생성자 인자값(parent_path) 작성하고 실행
    # obj.process('Fender')