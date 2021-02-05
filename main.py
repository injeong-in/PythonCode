import base64
import Vector
import os
import shutil

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

    def __init__(self, width, height):

            self.height = height
            self.width = width

            vector = Vector.VectorClass()  # 벡터 객체 생성(벡터값 생성)

            self.jsonData = '''
            {
                "version": "4.5.6",
                "flags": {},
                "shapes": 
                    ''' + vector.value + '''
                ,
        
        
                "imageHeight": ''' + str(self.height) + ''',
                "imageWidth": ''' + str(self.width) + ''',
        
              '''
            print('객체 생성되었습니다.')



    def setFinalName(self, format): #이미지 파일 이름
        return self.file_name + str(self.file_no) + format

    def setFinalFile(self): #결과물 파일 이름
        return self.file_name + str(self.file_no) + '.json'

    # def createFile(self, maximumNo): #json파일 결과물 생성함수
    #     while self.file_no < maximumNo + 1:
    #         with open('./imgs/' + self.setFinalName('.jpg'), 'rb') as img: #이미지 파일 확장자 필요시 변경 (.jpg -> .png)
    #             base64_str = base64.b64encode(img.read())
    #             base64_str = base64_str.decode('utf-8')
    #
    #
    #             f = open("Z:/AI_DATA/work/video/GH010038(354)_박정인_작업완료/Yacht(270)/" + self.setFinalFile(), 'w') #저장경로(NAS 저장)
    #             f.write(
    #                 self.jsonData + '"imageData": "' + base64_str + '",' + '''"imagePath": "''' + self.setFinalName(
    #                     '.jpg') + '''"
    #                     } ''') #final_name함수 포맷 매개변수 입력할것!
    #
    #             local_f = open("./JsonFolder/" + self.setFinalFile(), 'w')  # 로컬 저장
    #             local_f.write(
    #                 self.jsonData + '"imageData": "' + base64_str + '",' + '''"imagePath": "''' + self.setFinalName(
    #                     '.jpg') + '''"
    #                                     } ''')  # final_name함수 포맷 매개변수 입력할것!
    #
    #             self.file_no = self.file_no + 1;

    def createFile(self, path_str):
        list = os.listdir(path_str)

        for i in list:
            with open(path_str + i , 'rb') as img:
                base64_str = base64.b64encode(img.read())
                base64_str = base64_str.decode('utf-8')

                local_f = open("./JsonFolder/" + i.replace('.JPG','.json'), 'w')  # 로컬 저장
                local_f.write(
                    self.jsonData + '"imageData": "' + base64_str + '",' + '''"imagePath": "''' + i + '''" } ''' )

    def getSizeList(self, path_str): # 특정 파일사이즈를 만족하는 파일명만 리스트로 추출
        list = os.listdir(path_str)
        new_list = []

        for i in list:
            size = os.path.getsize(path_str + i)
            if size > 463000 and size < 463100: #파일 사이즈 조건
                new_list.append(i)


        return new_list;


    def preprocessorImg(self, path_str): #getSizeList에서 얻어진 .json파일과 이름일치하는 .JPG 파일을 복사
        jsonList = self.getSizeList(path_str)
        imgList = os.listdir('./imgs')
        new_list = []
        dst = './preImgs' #복사 원하는 폴더경로 지정
        for i in jsonList:
            for j in imgList:
                if i.replace('.json','.JPG') == j:

                    shutil.copy('./imgs/'+j, dst) #dst 폴더로 복사
                    print(j)
                    break;
                    # print(i)
                    # print('삭제된 파일: '+j)
                    # os.remove('./imgs/'+ j)



# list = os.listdir('./imgs')
# print(len(list))

# num = 0
# for i in list:
#     if i == 'a':
#         print(num)
#     num+=1

# obj = AutoLabel(1904,988) #파일명, 시작 파일번호, 클래스(label)명, 이미지폭, 이미지넓이
#
# obj.createFile('./imgs/')

# path_str = 'C:/Users/admin/Desktop/MMU-Simulation2/N_BR000_V60_B6_CPA03_CTN CMC(721)/Json/'
# jsonList = obj.getSizeList(path_str)
#
# obj.preprocessorImg(path_str)