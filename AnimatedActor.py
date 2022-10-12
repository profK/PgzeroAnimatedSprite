from pgzero.actor import Actor
from SpriteSheet import SpriteSheet
from pygame import image,Rect


class AnimatedActor(Actor) :
    def __init__(self,spriteSheet: str, numSprites: int) :
        self.spriteSheet: SpriteSheet = SpriteSheet(spriteSheet)
        spriteWidth: int = self.spriteSheet.width/numSprites;
        imageRect: Rect = Rect(0,0,spriteWidth,self.spriteSheet.height)
        self.frames: list = self.spriteSheet.load_strip(imageRect,numSprites)
        self.frameCount = numSprites
        super().__init__(spriteSheet) #needs dummy to load from
        self.setCurrentFrame(0)

    def setCurrentFrame(self,frameNum:int):
        self.currentFrame = frameNum
        self._surf = self.frames[frameNum]

