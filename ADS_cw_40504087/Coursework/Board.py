class Board():
    def __init__(self, width, height):
        self.width: int = width
        self.height: int = height
    def getWidth(self) -> int:
        return self.width
    def getHeight(self) -> int:
        return self.height