class Boat:

    def __init__(self, image):
        self.side = "left"
        self.image = image
        self.rect = self.image.get_rect(topleft=(250, 360))

    def move(self):

        if self.side == "left":
            self.side = "right"
            self.rect.x = 600
        else:
            self.side = "left"
            self.rect.x = 250