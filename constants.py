import pygame as pg

# Window properties
pg.init()
width, height = 800, 800
screen = pg.display.set_mode((width, height))
clock = pg.time.Clock()
run = True

# Constants
pg.display.set_caption('Play Book')
icon = pg.image.load("C:\\Users\\jalen\\OneDrive\\Pictures\\Camera Roll\\playbook.png")
pg.display.set_icon(icon)
WHITE = (255,255,255)
GREY = (128,128,128)
BLACK = (0,0,0)

# Fonts
pg.font.init()
font = pg.font.SysFont("Comic Sans", 12)
pl_label = font.render("Add Players", True, WHITE)
sq_label = font.render("Add OL", True, WHITE)
ol_label = font.render("OL", True, WHITE)
route_label = font.render("Add Routes", True, WHITE)
delete_label = font.render("Delete", True, WHITE)
description_label = font.render("Description", True, WHITE)
name_label = font.render("Change Label", True, WHITE)
draw_label = font.render("Draw", True, WHITE)
clear_label = font.render("Clear", True, WHITE)
save_label = font.render("Save", True, WHITE)
open_label = font.render("Open", True, WHITE)
df_label = font.render("Remove File", True, WHITE)
print_label = font.render("Print", True, WHITE)

# Main Screen
def main_screen(width, height):
    screen.fill(WHITE)
    pg.draw.rect(screen, GREY, (0, height//1.33, width//1.33, height//2.33))
    pg.draw.rect(screen, BLACK, (width//1.33, 0, width//4, height), 10)