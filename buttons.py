from constants import *
from draw import *

# Create buttons
def players_button(width):
    pg.draw.rect(screen, BLACK, (width//1.2, 50, width//10, 40))
    screen.blit(pl_label, (width//1.19, 60))

def square_button(width):
    pg.draw.rect(screen, BLACK, (width//1.2, 100, width//10, 40))
    screen.blit(sq_label, (width//1.19, 110))

def routes_button(width):
    pg.draw.rect(screen, BLACK, (width//1.2, 150, width//10, 40))
    screen.blit(route_label, (width//1.19, 160))

def delete_button(width):
    pg.draw.rect(screen, BLACK, (width//1.2, 200, width//10, 40))
    screen.blit(delete_label, (width//1.19, 210))

def description_button(width):
    pg.draw.rect(screen, BLACK, (width//1.2, 250, width//10, 40))
    screen.blit(description_label, (width//1.19, 260))

def name_button(width):
    pg.draw.rect(screen, BLACK, (width//1.2, 300, width//10, 40))
    screen.blit(name_label, (width//1.19, 310))

def draw_button(width):
    pg.draw.rect(screen, BLACK, (width//1.2, 350, width//10, 40))
    screen.blit(draw_label, (width//1.19, 360))

def clear_button(width):
    pg.draw.rect(screen, BLACK, (width//1.2, 500, width//10, 40))
    screen.blit(clear_label, (width//1.19, 510))

def save_button(width):
    pg.draw.rect(screen, BLACK, (width//1.2, 550, width//10, 40))
    screen.blit(save_label, (width//1.19, 560))

def open_button(width):
    pg.draw.rect(screen, BLACK, (width//1.2, 600, width//10, 40))
    screen.blit(open_label, (width//1.19, 610))

def df_button(width):
    pg.draw.rect(screen, BLACK, (width//1.2, 650, width//10, 40))
    screen.blit(df_label, (width//1.19, 660))