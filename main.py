import time

import pygame

pygame.font.init()

FPS = 120
WIDTH, HEIGHT = 300, 600
WHITE = (255, 255, 255)
VEL = 12

WINDOWS = pygame.display.set_mode((WIDTH, HEIGHT))


class Game:
    def __init__(self):
        from objects import Object, Line
        self.run = True
        self.objects = []
        self.clock = pygame.time.Clock()
        self.current_object = Object.buildRandomObject()
        self.current_object.moving = True
        self.objects.append(self.current_object)
        self.boot = False
        self.score = 0

        self.lines = []
        self.getLines()

    def getLines(self):
        from objects import Line
        self.lines = []
        for i in range(15, WINDOWS.get_height() + 15):
            if i % 15 == 0:
                self.lines.append(Line(y=i, WINDOWS=WINDOWS))

    def handle_post_complete_line(self):
        # remove the most bottom line
        for obj in self.objects:
            for node in obj.nodes:
                node.rect.y += 15
        self.getLines()

    def handlePressedKeys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RSHIFT]:
            self.boot = True

        elif keys[pygame.K_DOWN]:
            self.current_object.drop(VEL)

    def play(self):
        from objects import Object
        while self.run:
            print(f"self.score = {self.score}")
            self.current_object.getTopBottomRightLeftNode()
            self.clock.tick(FPS)
            if not self.current_object.isOnSurface(WINDOWS, self):
                self.current_object.drop(VEL)
            else:
                self.current_object.moving = False
                self.current_object = Object.buildRandomObject()
                self.current_object.moving = True
                self.objects.append(self.current_object)

            for obj in self.objects:
                if obj.isOutOfScreen(WINDOWS, self):
                    self.objects = []

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.run = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.current_object.rotate()
                    elif event.key == pygame.K_RIGHT:
                        if self.boot:
                            self.current_object.move(WINDOWS, self.current_object.topNode.rect.width * 2)
                            self.boot = False
                        else:
                            self.current_object.move(WINDOWS, self.current_object.topNode.rect.width)

                    elif event.key == pygame.K_LEFT:
                        if self.boot:
                            self.current_object.move(WINDOWS, -self.current_object.topNode.rect.width * 2)
                            self.boot = False
                        else:
                            self.current_object.move(WINDOWS, -self.current_object.topNode.rect.width)

            self.handlePressedKeys()

            WINDOWS.fill(WHITE)
            for obj in self.objects:
                obj.draw(WINDOWS)

            for line in self.lines:
                for square in line.squares:
                    square.check_if_filled(game=self)
                    square.draw(WINDOWS)
                line.check_if_complete()

                if line.complete:
                    self.score += 1
                    self.handle_post_complete_line()

            pygame.display.update()


def main():
    from objects import Label, Button
    buttons = []
    label1 = Label(x=WINDOWS.get_width() / 2 - 100, y=10, width=200, height=50, text='Tetris', color=(255, 0, 0))
    button1 = Button(x=WINDOWS.get_width() / 2 - 25, y=30 + label1.rect.height, width=50, height=30, text='Play',
                     color=(0, 0, 255), func=Game().play)
    buttons.append(button1)
    background_image = pygame.image.load('tetris.jpg')
    pygame.transform.scale(background_image, (WINDOWS.get_width(), WINDOWS.get_height()))

    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        WINDOWS.fill(WHITE)
        label1.draw(WINDOWS)
        for button in buttons:
            button.draw(WINDOWS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            else:

                if button1.handle_event(event):
                    run = False

        WINDOWS.blit(background_image,
                     (WINDOWS.get_width() / 2 - background_image.get_width() / 2, WINDOWS.get_height() / 2 - 50))
        pygame.display.update()


main()
