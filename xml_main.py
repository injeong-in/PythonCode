from dataset import ChildAuto
import os

class AutoBox(ChildAuto):

    def __init__(self, xml_width, xml_height ):
        self.xml_width = xml_width
        self.xml_height = xml_height


        self.xml_text = '''
        <annotation>
            <folder>C0011</folder>
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
                <name>Ship</name>
                <pose>Unspecified</pose>
                <truncated>0</truncated>
                <difficult>0</difficult>
                <bndbox>
                    <xmin>595</xmin>
                    <ymin>310</ymin>
                    <xmax>1207</xmax>
                    <ymax>542</ymax>
                </bndbox>

            </object>
        
        '''.format(self.xml_width, self.xml_height)


    def createXML(self, path_str):
        list = os.listdir(path_str)

        for i in range(len(list) - 2):

                j = list[i]

                local_f = open("./xml/" + j.replace('.jpg','.xml'), 'w')  # 로컬 저장
                local_f.write(
                    self.xml_text + '<path>' '''</path>
                        <filename>{0}</filename>
                </annotation>'''.format(j) )




if __name__ == '__main__':

    obj = AutoBox('1920', '1080')
    obj.createXML('C:/Users/admin/Desktop/segmentation/C0012/')



    # list = os.listdir('C:/Users/admin/Desktop/segmentation/C0012/')
    #
    # for i in range(len(list) - 2):
    #     name = list[i]
    #     print(name)