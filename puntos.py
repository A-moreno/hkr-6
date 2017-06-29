
class puntos():

    def __init__(self,x,y):

        self.x=x 

        self.y=y 

    def move(self,x,y):

        self.X=x

        self.Y=y   

    def reset(self):

        self.x=0

        self.y=0   

    def DISTANCIA(self,punto2):

        u=(punto2.x-self.x)**2 + (punto2.y-self.y)**2

        d = u**0.5

        return d 
