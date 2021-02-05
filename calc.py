import os

path = 'F:/Working/02.05/'
path2 = 'F:/Working/02.02/2021-0123 Incheon/'
path3 ='F:/Working/02.01/2021-0123 Incheon/'

def calculator(path):
    parentList = os.listdir(path)
    for parent in parentList:
        path_str = path + '/{}/'.format(parent)
        list = os.listdir(path_str)
        print(parent,'개수:', len(list)-2)
        try:
            path_str = path + '/{}/xml/'.format(parent)
            list = os.listdir(path_str)
            print(parent, 'xml개수:', len(list),'\n')
        except:
            pass


    for parent in parentList:

        try:
            path_str = path + '/{}/xml/'.format(parent)
            list = os.listdir(path_str)
            print(parent, 'xml개수:', len(list))
        except:
            pass

def newCalc(path):
    for parent in os.listdir(path):
        for child in os.listdir(path+'/{}/'.format(parent)):
            path_str = path + '/{}/'.format(parent) +'{}/'.format(child)
            list = os.listdir(path_str)
            print(child,'개수:', len(list)-2)
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

# calculator(path2)
newCalc(path)
# for parent in parentList:
#     path_str = path + '/{}/json/'.format(parent)
#     list = os.listdir(path_str)
#     print(parent, 'json개수:', len(list))