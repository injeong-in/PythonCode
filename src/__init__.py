class jeongin:

    def __init__(self,hp,mp):
        self.hp = hp
        self.mp = mp


    def imageChoice(self, img):
        print(img)


obj = jeongin(5000,200000)

print("HP:",obj.hp,", MP:",obj.mp)

jeongin.imageChoice(jeongin, 'abc.jpg')
