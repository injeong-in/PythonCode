import xml.etree.ElementTree as elemTree
import os
import shutil

# tree = elemTree.parse('./xml/ContainerRound000060_000.xml')
# root = tree.getroot()
# obj = root.findall("object")
# object = tree.find('./object')
# name = object.find('name')




# print(obj[0].find('name').text)
# print(obj[1].find('name').text)
# print(len(obj))

path = 'F:/OceanSandBoxMod3/Captures/2021-01-20/'
list = os.listdir(path)


newList = []

for i in list:
    print(i)
    newList.append(os.listdir(path + i))

print('----------------1월20일 폴더목록----------------')
for j in range(0,len(list)):
    print(newList[j])

path = 'F:/OceanSandBoxMod3/Captures/2021-01-21/'
list = os.listdir(path)

newList = []

for i in list:
    print(i)
    newList.append(os.listdir(path + i))

print('----------------1월21일 폴더목록----------------')
for j in range(0,len(list)):
    print(newList[j])

sum = 0
for h in range(2):
    two_ship = os.listdir(path+'two_ship/'+newList[4][h])

    if h==0:
        print('collision: ',two_ship, '갯수:{}개'.format(len(two_ship)))
    else:
        print('cross: ', two_ship, '갯수:{}개'.format(len(two_ship)))
    sum += len(two_ship)
print('two_ship 총합:{}개'.format(sum))

sum = 0
for k in range(9):
    spectrum = os.listdir(path+'Spectrum/'+newList[3][k])
    print('{0}: {1}, {2}개'.format(newList[3][k],spectrum, len(spectrum)))
    sum += len(spectrum)

print('Spectrum 총합:{}개'.format(sum))