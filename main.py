import base64
import Vector

class AutoLabel:

    def __init__(self, file_name, file_no, label_name, width, height):
        self.file_name = file_name
        self.file_no = file_no
        self.label_name = label_name
        self.height = height
        self.width = width

        vector = Vector.VectorClass() #벡터 객체 생성(벡터값 생성)

        self.jsonData = '''
{
    "version": "4.5.6",
    "flags": {},
    "shapes": 
        '''+ vector.value + '''
    ,


    "imageHeight": '''+ str(self.height) + ''',
    "imageWidth": '''+ str(self.width) + ''',

  '''
        print('객체 생성되었습니다.')

    def final_name(self, format): #이미지 파일 이름
        return self.file_name + str(self.file_no) + format

    def final_file(self): #결과물 파일 이름
        return self.file_name + str(self.file_no) + '.json'

    def createFile(self, maximumNo): #json파일 결과물 생성함수
        while self.file_no < maximumNo + 1:
            with open('./imgs/' + self.final_name('.jpg'), 'rb') as img: #이미지 파일 확장자 필요시 변경 (.jpg -> .png)
                base64_str = base64.b64encode(img.read())
                base64_str = base64_str.decode('utf-8')


                f = open("Z:/AI_DATA/work/video/GH010038(354)_박정인_작업완료/Yacht(270)/" + self.final_file(), 'w') #저장경로(NAS 저장)
                f.write(
                    self.jsonData + '"imageData": "' + base64_str + '",' + '''"imagePath": "''' + self.final_name(
                        '.jpg') + '''"
                        } ''') #final_name함수 포맷 매개변수 입력할것!

                local_f = open("./JsonFolder/" + self.final_file(), 'w')  # 로컬 저장
                local_f.write(
                    self.jsonData + '"imageData": "' + base64_str + '",' + '''"imagePath": "''' + self.final_name(
                        '.jpg') + '''"
                                        } ''')  # final_name함수 포맷 매개변수 입력할것!

                self.file_no = self.file_no + 1;






obj = AutoLabel('GH010038_',368,'Yacht',1920,1080) #파일명, 시작 파일번호, 클래스(label)명, 이미지폭, 이미지넓이

obj.createFile(492) #파일번호 최대값
