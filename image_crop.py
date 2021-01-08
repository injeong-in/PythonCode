from PIL import Image
import warnings
import os


def image_crop(path, infilename, format, save_path):
    """
    image file 와 crop한이미지를 저장할 path 을 입력받아 crop_img를 저장한다.
    :param infilename:
        crop할 대상 image file 입력으로 넣는다.
    :param save_path:
        crop_image file의 저장 경로를 넣는다.
    :return:
    """

    img = Image.open(path + infilename + format)
    (img_h, img_w) = img.size
    print(img.size)

    # crop 할 사이즈 : grid_w, grid_h
    grid_w = 1080  # crop height w랑h 바꼈음
    grid_h = 1920  # crop width
    range_w = (int)(img_w / grid_w)
    range_h = (int)(img_h / grid_h)
    print(range_w, range_h)

    i = 0

    for w in range(range_w):
        for h in range(range_h):
            bbox = (h * grid_h, w * grid_w, (h + 1) * (grid_h), (w + 1) * (grid_w))
            print(h * grid_h, w * grid_w, (h + 1) * (grid_h), (w + 1) * (grid_w))
            # 가로 세로 시작, 가로 세로 끝
            crop_img = img.crop(bbox)

            # fname = "{}.jpg".format("{0:05d}".format(i))
            fname = "{}.jpg".format(infilename + '_{}'.format(i))
            savename = save_path + fname
            crop_img.save(savename)
            print('save file ' + savename + '....')
            i += 1


if __name__ == '__main__':
    warnings.simplefilter('ignore', Image.DecompressionBombWarning)
    # image_crop('F-101_1','.jpg', 'C:/이미지컷/')
    # list = os.listdir('E:/2.drone/15/examine')
    list = os.listdir('E:/2.drone/15/examine')
    print(list)

    a = 0

    for i in list:
        # if list[len(list)-1] == i+'.jpg':
        #     print('작업이 끝났습니다')
        if a < len(list):
            i = i.replace(".jpg","")
            image_crop('E:/2.drone/15/examine/', i, '.jpg', 'E:/2.drone/15/resize/')

        a += 1


