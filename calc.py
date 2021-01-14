import os

path = 'C:/Users/admin/Desktop/segmentation'
parentList = os.listdir(path)
print(parentList)

for parent in parentList:
    path_str = path + '/{}/'.format(parent)
    list = os.listdir(path_str)
    print(parent,'개수:', len(list)-2)


for parent in parentList:
    path_str = path + '/{}/xml/'.format(parent)
    list = os.listdir(path_str)
    print(parent, 'xml개수:', len(list))

for parent in parentList:
    path_str = path + '/{}/json/'.format(parent)
    list = os.listdir(path_str)
    print(parent, 'json개수:', len(list))