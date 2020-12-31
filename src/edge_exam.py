import cv2, sys
from  matplotlib import pyplot as plt
import numpy as np

class EdgeValue:

    def __init__(self,img):
        self.img = img;



    def imageChoice(filename, fileno, format):
            img = cv2.imread('../'+filename+'_'+fileno + format)
            image_gray = cv2.imread('../GH010038_354.jpg', cv2.IMREAD_GRAYSCALE)
            return img;

    def edgeSelector(self,img):
        edges = cv2.Canny(img, 100, 200)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
        closed = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

        contours, _ = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours_xy = np.array(contours)
        contours_xy.shape

        x_min, x_max = 0, 0

        return kernel,closed,contours

obj = EdgeValue(img = EdgeValue.imageChoice('GH010038','354','.jpg'))



edges = cv2.Canny(obj.img,100,200)
cv2.imshow('Canny', edges)
cv2.waitKey(0)


    # # 케니 엣지 적용
    # edges = cv2.Canny(img=imageChoice(),100,200)
    #
    # # 결과 출력
    # cv2.imshow('Original', img)
    # cv2.imshow('Canny', edges)
    # cv2.waitKey(0)
    #
    #
    # kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7,7))
    # closed = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)
    # cv2.imshow('closed', closed)
    # cv2.waitKey(0)
    #
    #
    #
    # contours, _ = cv2.findContours(closed.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # total = 0
    #
    # contours_image = cv2.drawContours(img, contours, -1, (0,255,0), 3)
    # cv2.imshow('contours_image', contours_image)
    # cv2.waitKey(0)
    #
    #
    # # x의 min과 max 찾기
    #
    # contours_xy = np.array(contours)
    # contours_xy.shape
    #
    #
    #
    # x_min, x_max = 0, 0
    # value = list()
    # for i in range(len(contours_xy)):
    #     for j in range(len(contours_xy[i])):
    #         value.append(contours_xy[i][j][0][0])  # 네번째 괄호가 0일때 x의 값
    #         x_min = min(value)
    #         x_max = max(value)
    #
    #
    # # y의 min과 max 찾기
    # y_min, y_max = 0, 0
    # value = list()
    # for i in range(len(contours_xy)):
    #     for j in range(len(contours_xy[i])):
    #         value.append(contours_xy[i][j][0][1])  # 네번째 괄호가 0일때 x의 값
    #         y_min = min(value)
    #         y_max = max(value)
    #
    #
    # x = x_min
    # y = y_min
    # w = x_max-x_min
    # h = y_max-y_min
    #
    # img_trim = img[y:y+h, x:x+w]
    # cv2.imwrite('org_trim.jpg', img_trim)
    # org_image = cv2.imread('org_trim.jpg')
    #
    #
    # cv2.imshow('org_image', org_image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    #
    #
    # print(contours)