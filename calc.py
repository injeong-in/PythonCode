import os

path = 'F:/Working/1.29/'
path2 = 'F:/Working/Class/'
parentList = os.listdir(path)
# print(parentList)

for parent in parentList:
    path_str = path + '/{}/'.format(parent) #path 수정할것
    list = os.listdir(path_str)
    print(parent,'개수:', len(list)-1)
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

# for parent in parentList:
#     path_str = path + '/{}/json/'.format(parent)
#     list = os.listdir(path_str)
#     print(parent, 'json개수:', len(list))