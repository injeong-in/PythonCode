import os



parentList = os.listdir('C:/Users/admin/Desktop/검수자 박정인 (3411)/')
print(parentList)

for parent in parentList:
    path_str = 'C:/Users/admin/Desktop/검수자 박정인 (3411)/{}/'.format(parent)
    list = os.listdir(path_str)
    print(parent,'갯수:', len(list))


for parent in parentList:
    path_str = 'C:/Users/admin/Desktop/검수자 박정인 (3411)/{}/Xml/'.format(parent)
    list = os.listdir(path_str)
    print(parent, 'xml갯수:', len(list))