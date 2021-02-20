from dataset import ChildAuto
import os

class AutoBox(ChildAuto):

    def __init__(self, xml_width, xml_height, xml_name):
        self.xml_width = xml_width
        self.xml_height = xml_height
        self.xml_name = xml_name

        self.xml_text = '''
        <annotation>
            
            <source>
                <database>Unknown</database>
            </source>
            <size>
                <width>{0}</width>
                <height>{1}</height>
                <depth>3</depth>
            </size>
            <segmented>0</segmented>
            <object>
                <name>{2}</name>
                <pose>Unspecified</pose>
                <truncated>0</truncated>
                <difficult>0</difficult>
                <bndbox>
                    <xmin></xmin>
                    <ymin></ymin>
                    <xmax></xmax>
                    <ymax></ymax>
                </bndbox>
            </object>


                
        
        '''.format(self.xml_width, self.xml_height, self.xml_name)


    def createXML(self, path_str):
        list = os.listdir(path_str)
        count = 0
        for i in range(len(list) - 1):

                j = list[i]

                local_f = open("./xml/" + j.replace('.jpg','.xml'), 'w')  # 로컬 저장
                local_f.write(
                    self.xml_text + '''
                        
                        <filename>{0}</filename>
                </annotation>'''.format(j) )

                count += 1
                print('{},{}개 생성'.format(j.replace('.jpg','.xml'), count))



if __name__ == '__main__':

    obj = AutoBox('1920', '1080', 'Bulk_Carrier')
    obj.createXML('C:/Working/02.17/Bulk_Carrier/')



    # list = os.listdir('C:/Users/admin/Desktop/segmentation/C0012/')
    #
    # for i in range(len(list) - 2):
    #     name = list[i]
    #     print(name)