import json
import os
import shutil
from main import AutoLabel


class ChildAuto(AutoLabel):

    def __init__(self, width, height):
        super(self).__init__(width,height)


    def getList(self,path_str): #json객체 위치벡터 points 갯수가 3개이상 넘어가는 파일 골라내기
                                #param, 폴더경로
        list = os.listdir(path_str)
        new_list = []
        dst = './preJson' #전처리 후 카피시킬 폴더

        for i in list:
            with open(path_str + i, 'r') as f:

                json_data = json.load(f)
                # points = json_data['shapes'][0]['points']
                points = json_data['shapes']

                if (len(points) >= 3):
                    print('오류입니다: ' + i)
                    print('갯수:', len(points))
                    new_list.append(i)
                    shutil.copy(path_str + i, dst)

        return new_list



    def preprocessorImg(self, path_str, getList_param): # param path_str: img폴더 경로, override: none
            jsonList = self.getList(getList_param) #getList함수 매개변수 작성(원본 json파일 담긴 폴더)
            imgList = os.listdir(path_str)

            dst = './preImgs' #복사 원하는 폴더경로 지정
            for i in jsonList:
                for j in imgList:
                    if i.replace('.json','.JPG') == j:

                        shutil.copy(path_str + j, dst) #dst 폴더로 복사
                        print('복사완료: ' + j)
                        break;
                        # print(i)
                        # print('삭제된 파일: ' + j)
                        # os.remove('./imgs/'+ j)

    def removeFile(self, path_str):

        delFolder = os.listdir('./preJson')
        jsonFolder = os.listdir(path_str)

        for i in delFolder:
            for j in jsonFolder:
                if (i == j):
                    os.remove(path_str + j)
                    print('삭제완료: ' + j)
                    break

if __name__ == '__main__':

    obj = ChildAuto(1904,988)


