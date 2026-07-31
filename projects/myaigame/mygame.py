import pygame
from teachable_machine import TeachableMachine

import cv2

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("My AI Game")
model = TeachableMachine(
    model_path=r"C:\Users\gauta\OneDrive\Desktop\python AI\projects\myaigame\keras_model.h5",
    labels_file_path=r"C:\Users\gauta\OneDrive\Desktop\python AI\projects\myaigame\labels.txt"
)
camera = cv2.VideoCapture(0)
running = True
font = pygame.font.SysFont(None, 60)
displayText = "Hello World!"
player = pygame.Rect(200, 200, 35, 35)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    isSuccess, acutualImage = camera.read()

    if isSuccess:
        cv2.imshow("RIshu", acutualImage)
        cv2.imwrite("rishu.jpg", acutualImage)
        result = model.classify_image("rishu.jpg")
        displayText = result['class_name'].split(" ")[1]
        if displayText == "up":
            player.y= player.y -3
        if displayText == "left":
            player.x = player.x -3
        if displayText == "right":
            player.x= player.x +3
        if displayText == "down":
            player.y= player.y +3


    myText = font.render(displayText, True, (255,255,255))

    screen.fill((0,0,0))
    screen.blit(myText, (200, 100))
    pygame.draw.rect(screen, (255,0,0), player)
    pygame.display.update()