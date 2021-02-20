import os

path = 'C:/Working/02.17/'
path2 = 'F:/Working/02.02/2021-0123 Incheon/'
path3 ='F:/Working/02.01/2021-0123 Incheon/'

def calculator(path):
    parentList = os.listdir(path)
    sum = 0
    for parent in parentList:
        path_str = path + '/{}/'.format(parent)
        list = os.listdir(path_str)
        print(parent,'이미지 개수:', len(list)-1)
        try:
            path_str = path + '/{}/xml/'.format(parent)
            list = os.listdir(path_str)
            print(parent, 'xml개수:', len(list),'\n')
            sum += len(list)
        except:
            pass


    for parent in parentList:

        try:
            path_str = path + '/{}/xml/'.format(parent)
            list = os.listdir(path_str)
            print(parent +'({})'.format(len(list)))
        except:
            pass

    print("총합:{}장".format(sum))

def newCalc(path):
    for parent in os.listdir(path):
        for child in os.listdir(path+'/{}/'.format(parent)):
            path_str = path + '/{}/'.format(parent) +'{}/'.format(child)
            list = os.listdir(path_str)
            print(child,'개수:', len(list)-1)
            try:
                path_str = path_str +'/xml'
                list = os.listdir(path_str)
                print(child, 'xml개수:', len(list),'\n')
            except:
                pass

    for parent in os.listdir(path):
        for child in os.listdir(path + '/{}/'.format(parent)):
            try:
                path_str = path + '/{}/'.format(parent) +'{}/'.format(child)
                list = os.listdir(path_str+'/xml')
                print(child, 'xml개수:', len(list))
            except:
                pass

calculator(path)
# newCalc(path)
# for parent in parentList:
#     path_str = path + '/{}/json/'.format(parent)
#     list = os.listdir(path_str)
#     print(parent, 'json개수:', len(list))