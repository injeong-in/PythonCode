import cv2
from image_compare import find_almost_similar_image_locations
import os
from xml_main import AutoBox

class AutoLabelling(AutoBox):

    def __init__(self,xml_width, xml_height, xml_name):
        super().__init__(xml_width, xml_height, xml_name)

    def createXML(self, j, w_h_range):

        count = 0
        x_min, x_max, y_min, y_max, w, h = w_h_range
        local_f = open("./xml/" + j.replace('.jpg', '.xml'), 'w')  # 로컬 저장
        local_f.write(
            obj.xml_text + '''
                        <bndbox>
                            <xmin>{0}</xmin>
                            <ymin>{1}</ymin>
                            <xmax>{2}</xmax>
                            <ymax>{3}</ymax>
                        </bndbox>
                 </object>
                                <filename>{4}</filename>
                        </annotation>'''.format(x_min,y_min,x_max,y_max, j))

        count += 1
        print('{},{}개 생성'.format(j.replace('.jpg', '.xml'), count))

    def showimage(self,img_path, result):
        src = cv2.imread(img_path, cv2.IMREAD_COLOR)

        dst = src.copy()
        y0 = int(result['rectangle'][0][0])
        y1 = int(result['rectangle'][2][0])
        x0 = int(result['rectangle'][0][1])
        x1 = int(result['rectangle'][2][1])
        roi = src[x0:x1, y0:y1]

        cv2.imshow("dst", roi)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def test1(self):
        result, w_h_range = find_almost_similar_image_locations('search2.jpg', 'source.jpg')
        self.showimage('', result)


    def test2(self):
        result, w_h_range = find_almost_similar_image_locations('search2.jpg', 'source.jpg', 0.6)
        self.showimage('', result)


    def detectImg(self,source_path, searchNo, count):
        img = os.listdir(source_path) #원본 이미지
        search_path = './img'
        searchImg = os.listdir(search_path) #검증 데이터 이미지

        pass_count = 0 #이미지 검출 실패시 쌓을 카운트

        for i in range(searchNo, len(searchImg)):

            print(searchImg[i])

            for j in range(count, len(img)):

                try:
                    print(searchImg[i], img[j])
                    result, w_h_range = find_almost_similar_image_locations('./img/' + searchImg[i], source_path + img[j], 0.6)
                    self.createXML(img[j], w_h_range)
                    print(w_h_range)
                    count += 1
                    pass_count = 0 #0으로 초기화
                    # self.showimage(source_path + img[j], result)
                except:
                    print('turn over the loop')
                    pass_count += 1
                    count += 1
                    if pass_count > 10: #연속으로 10회 쌓일때만 break
                        pass_count = 0 #0으로 초기화
                        count -= 5
                        break;
                    pass



if __name__ == '__main__':
    class_name = 'Container_Ship'
    date = '02.17'
    obj = AutoLabelling('1920','1080','{0}'.format(class_name))
    source_path = 'C:/Working/{0}/{1}/'.format(date, class_name)

    obj.detectImg(source_path,1,373)