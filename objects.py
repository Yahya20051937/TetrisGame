import math
import random

import pygame


class Object:
    @staticmethod
    def build_I_block(x, y):
        head = Node(x=x, y=y, width=15, height=15, color='red', adjust=True)
        nodes = [head]
        for i in range(1, 4):
            parent = nodes[-1]
            child = Node(x=parent.rect.x, y=parent.rect.y + parent.height, width=parent.width, height=parent.height,
                         color='red', dx=0, dy=i * head.rect.height)
            nodes.append(child)
        square_block = Object('I', nodes)

        return square_block

    @staticmethod
    def build_Square_block(x, y):
        head = Node(x=x, y=y, width=15, height=15, color=(135, 206, 250), adjust=True)

        child1 = Node(x=head.rect.x, y=head.rect.y + head.rect.height, width=head.rect.width, height=head.rect.height,
                      color=(135, 206, 250), dx=0, dy=head.height)
        child2 = Node(x=head.rect.x + head.rect.width, y=head.rect.y, width=head.rect.width, height=head.rect.height,
                      color=(135, 206, 250), dx=head.width, dy=0)
        child3 = Node(x=head.rect.x + head.rect.width, y=head.rect.y + head.rect.height, width=head.rect.width,
                      height=head.rect.height, color=(135, 206, 250), dx=head.width, dy=head.height)

        nodes = [head, child1, child2, child3]
        I_block = Object('square', nodes)
        return I_block

    @staticmethod
    def build_T_block(x, y):
        head = Node(x=x, y=y, width=15, height=15, color=(255, 165, 0), adjust=True)

        child1 = Node(x=head.rect.x, y=head.rect.y + head.rect.height, width=head.rect.width, height=head.rect.height,
                      color=head.color, dx=0, dy=head.rect.height)
        child2 = Node(x=head.rect.x - head.rect.width, y=head.rect.y + head.rect.height, width=head.rect.width,
                      height=head.rect.height, color=head.color, dx=-head.rect.width, dy=head.rect.height)
        child3 = Node(x=head.rect.x + head.rect.width, y=head.rect.y + head.rect.height, width=head.rect.width,
                      height=head.rect.height, color=head.color, dx=head.rect.width, dy=head.rect.height)

        nodes = [head, child1, child2, child3]
        T_block = Object("T", nodes)
        return T_block

    @staticmethod
    def build_L_block(x, y):
        head = Node(x=x, y=y, width=15, height=15, color=(128, 0, 128), adjust=True)

        child1 = Node(x=head.rect.x, y=head.rect.y + head.rect.height, width=head.rect.width, height=head.rect.height,
                      color=head.color, dx=0, dy=head.height)
        child2 = Node(x=head.rect.x + head.rect.width, y=head.rect.y + head.rect.height, width=head.rect.width,
                      height=head.rect.height,
                      color=head.color, dx=head.width, dy=head.height)
        child3 = Node(x=head.rect.x + 2 * head.rect.width, y=head.rect.y + head.rect.height, width=head.rect.width,
                      height=head.rect.height, color=head.color, dx=2 * head.width, dy=head.height)

        nodes = [head, child1, child2, child3]
        L_block = Object("L", nodes)
        return L_block

    @staticmethod
    def build_J_block(x, y):
        head = Node(x=x, y=y, width=15, height=15, color=(0, 0, 255), adjust=True)

        child1 = Node(x=head.rect.x, y=head.rect.y + head.rect.height, width=head.rect.width, height=head.rect.height,
                      color=head.color, dx=0, dy=head.height)
        child2 = Node(x=head.rect.x - head.rect.width, y=head.rect.y + head.rect.height, width=head.rect.width,
                      height=head.rect.height,
                      color=head.color, dx=-head.width, dy=head.height)
        child3 = Node(x=head.rect.x - 2 * head.rect.width, y=head.rect.y + head.rect.height, width=head.rect.width,
                      height=head.rect.height, color=head.color, dx=-2 * head.width, dy=head.height)

        nodes = [head, child1, child2, child3]
        J_block = Object("J", nodes)
        return J_block

    @staticmethod
    def build_R_block(x, y):
        head = Node(x=x, y=y, width=15, height=15, color=(144, 238, 144), adjust=True)

        child1 = Node(x=head.rect.x + head.rect.width, y=head.rect.y, width=head.rect.width, height=head.rect.height,
                      color=head.color, dx=head.rect.width, dy=0)
        child2 = Node(x=head.rect.x + head.rect.width, y=head.rect.y + head.rect.height, width=head.rect.width,
                      height=head.rect.height, color=head.color, dx=head.rect.width, dy=head.rect.height)
        child3 = Node(x=head.rect.x + 2 * head.rect.width, y=head.rect.y + head.rect.height, width=head.rect.width,
                      height=head.rect.height, color=head.color, dx=2 * head.rect.width, dy=head.rect.height)

        nodes = [head, child1, child2, child3]
        R_block = Object("R", nodes)
        return R_block

    @staticmethod
    def build_S_block(x, y):
        head = Node(x=x, y=y, width=15, height=15, color=(128, 0, 128), adjust=True)

        child1 = Node(x=head.rect.x - head.rect.width, y=head.rect.y, width=head.rect.width, height=head.rect.height,
                      color=head.color, dx=-head.rect.width, dy=0)
        child2 = Node(x=head.rect.x - head.rect.width, y=head.rect.y + head.rect.height, width=head.rect.width,
                      height=head.rect.height, color=head.color, dx=-head.rect.width, dy=head.rect.height)
        child3 = Node(x=head.rect.x - 2 * head.rect.width, y=head.rect.y + head.rect.height, width=head.rect.width,
                      height=head.rect.height, color=head.color, dx=-2 * head.rect.width, dy=head.rect.height)

        nodes = [head, child1, child2, child3]
        S_block = Object("S", nodes)
        return S_block

    @staticmethod
    def buildRandomObject():
        objectsDict = {"square": Object.build_Square_block, "T": Object.build_T_block, "L": Object.build_L_block,
                       "S": Object.build_S_block, "R": Object.build_R_block, "I": Object.build_I_block,
                       "J": Object.build_J_block}
        # return objectsDict["I"](0, -300)
        return objectsDict[random.choice(["S", "T", "L", "R", "square", "J", "I"])](0, -300)

    def __init__(self, name, nodes):
        self.name = name
        self.id = random.randint(151, 4646494)
        self.nodes = nodes
        self.topNode = None
        self.bottomNode = None
        self.rightNode = None
        self.leftNode = None
        self.moving = False
        self.getTopBottomRightLeftNode()

    def draw(self, windows):
        for node in self.nodes:
            pygame.draw.rect(windows, node.color, node.rect)

    def getTopBottomRightLeftNode(self):
        topNode = self.nodes[0]
        bottomNode = self.nodes[0]
        rightNode = self.nodes[0]
        leftNode = self.nodes[0]
        for node in self.nodes:
            if node.rect.y < topNode.rect.y:
                topNode = node

            if node.rect.y > bottomNode.rect.y:
                bottomNode = node

            if node.rect.x > rightNode.rect.x:
                rightNode = node

            if node.rect.x < leftNode.rect.x:
                leftNode = node

        self.topNode = topNode
        self.bottomNode = bottomNode
        self.rightNode = rightNode
        self.leftNode = leftNode

    def rotate(self):
        head = self.nodes[0]
        for node in self.nodes[1:]:
            dx = - node.dy
            dy = node.dx
            node.dx = dx
            node.dy = dy
            node.rect.x = head.rect.x + dx
            node.rect.y = head.rect.y + dy

    def isOnSurface(self, WINDOWS, game):
        for node in self.nodes:
            if node.rect.y + node.rect.height > WINDOWS.get_height():
                errorValue = (node.rect.y + 15) - WINDOWS.get_height()
                print(errorValue)
                self.drop(-errorValue)

                return True
            for obj in game.objects:
                if obj.id != self.id:
                    for obj_node in obj.nodes:
                        if obj_node.rect.colliderect(node.rect):
                            errorValue = (node.rect.y + 15) - obj_node.rect.y
                            print(errorValue)
                            self.drop(-errorValue)

                            return True
        return False

    def isOutOfScreen(self, Windows, game):
        if self.topNode.rect.y <= 0 and self.isOnSurface(Windows, game):
            return True
        return False

    def drop(self, VEL):
        for node in self.nodes:
            node.rect.y += VEL

    def move(self, WINDOWS, VEL):
        if self.leftNode.rect.x - self.leftNode.rect.width >= 0 and self.rightNode.rect.x + 2 * self.rightNode.rect.width <= WINDOWS.get_width():
            for node in self.nodes:
                node.rect.x += VEL


class Node:
    def __init__(self, x, y, width, height, color, dx=0, dy=0, adjust=False):

        if adjust:
            self.rect = pygame.Rect(x + 150, y + 300, width, height)
        else:
            self.rect = pygame.Rect(x, y, width, height)
        self.width = width
        self.height = height
        self.color = color

        self.dx = dx
        self.dy = dy


class Line:
    def __init__(self, y, WINDOWS):
        self.y = y
        self.squares = []
        self.complete = False
        self.getSquares(WINDOWS)

    def getSquares(self, WINDOWS):
        i = 0
        while i < WINDOWS.get_width():
            square = Square(x=i, y=self.y, size=15)
            self.squares.append(square)
            i += 15

    def check_if_complete(self):
        self.complete = True
        for square in self.squares:
            if square.filled is False:
                self.complete = False
                break


class Square:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.filled = False

    def draw(self, WINDOWS):
        for i in range(16):
            pygame.draw.rect(WINDOWS, (0, 0, 0), pygame.Rect(self.x, self.y + i, 1, 1))

        for i in range(16):
            pygame.draw.rect(WINDOWS, (0, 0, 0), pygame.Rect(self.x + i, self.y + 15, 1, 1))

        for i in range(16):
            pygame.draw.rect(WINDOWS, (0, 0, 0), pygame.Rect(self.x + 15, self.y + i, 1, 1))

        for i in range(16):
            pygame.draw.rect(WINDOWS, (0, 0, 0), pygame.Rect(self.x + i, self.y, 1, 1))

    def check_if_filled(self, game):
        for obj in game.objects:
            if obj.moving is False:
                for node in obj.nodes:
                    if node.rect.y == self.y and node.rect.x == self.x:
                        self.filled = True
                        return


class Button:
    def __init__(self, x, y, width, height, text, color, func):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.command = func

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        font = pygame.font.Font(None, 24)
        text_surface = font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.command()
                return True
        return False


class Label:
    def __init__(self, x, y, width, height, text, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        font = pygame.font.Font(None, 24)
        text_surface = font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)
