from constants import *
import tkinter as tk
from tkinter import simpledialog
import json
import os
import glob

pos = []
players = []
ols = []
drawing = []
routes = []
message = "Description"
rect_players = {}
rect_ols = {}
rect_draw = {}
rect_routes = {}

class Play():
    def __init__(self):
        self.mouse_x, self.mouse_y = pg.mouse.get_pos()

    def player(self, screen):
        pg.draw.ellipse(screen, BLACK, (self.mouse_x-10, self.mouse_y-10, 25, 25))

    def ol(self, screen):
        pg.draw.rect(screen, BLACK, (self.mouse_x-10, self.mouse_y, 25, 25))

    def route(self, screen):
        pg.draw.line(screen, BLACK, (self.mouse_x, self.mouse_y), (self.mouse_x, self.mouse_y), 3)

    def freehand(self, screen):
        pg.draw.circle(screen, BLACK, (self.mouse_x, self.mouse_y), 3)

    def add_player(self, screen, mouse_x, mouse_y, position):
        player = pg.draw.ellipse(screen, BLACK, (mouse_x-10, mouse_y-10, 25, 25))
        pos.append(position)
        players.append(player)

    def add_ol(self, screen, mouse_x, mouse_y):
        ol = pg.draw.rect(screen, BLACK, (mouse_x-10, mouse_y, 25, 25))
        ols.append(ol)

    def add_freehand(self):
        dot = pg.draw.circle(screen, BLACK, (self.mouse_x, self.mouse_y), 3)
        drawing.append(dot)

def delete_action():
    mouse = pg.mouse.get_pos()
    for p in players:
        if ((mouse[0] - p[0]) <= 25 and (mouse[0] - p[0]) >= 0):
            if ((mouse[1] - p[1]) <= 25 and (mouse[1] - p[1]) >= 0):
                index = players.index(p)
                players.remove(p)
                pos.pop(index)
    for o in ols:
        if ((mouse[0] - o[0]) <= 25 and (mouse[0] - o[0]) >= 0):
            if ((mouse[1] - o[1]) <= 25 and (mouse[1] - o[1]) >= 0):
                ols.remove(o)
    for r in routes:
        if ((mouse[0] - r[0]) <= 10 and (mouse[0] - r[0]) >= 0):
            if ((mouse[1] - r[1]) <= 10 and (mouse[1] - r[1]) >= 0):
                if routes.index(r)%2 == 0:
                    del routes[routes.index(r)+1]
                    routes.remove(r)
                elif routes.index(r)%2 == 1:
                    del routes[routes.index(r)-1]
                    routes.remove(r)

def delete_line():
    mouse_x, mouse_y = pg.mouse.get_pos()
    for route in drawing:
        if route[0]-5 <= mouse_x <= route[0]+5:
            if route[1]-5 <= mouse_y <= route[1]+5:
                drawing.remove(route)

def description():
    global root
    root = tk.Tk()

    # specify size of window.
    root.geometry("600x250")

    # Create label
    l = tk.Label(root, text="Play description")
    l.config(font=("Courier", 14))
    l.grid(row=0, column=0)

    # Create text widget and specify size.
    text = tk.Text(root, height=10, width=75)
    text.grid(row=1, column=0, columnspan=3, sticky=tk.NSEW)

    # Create button for next text.
    b1 = tk.Button(root, text="Enter", command=lambda: get_text(text))
    b1.grid(row=4, column=0)

    # Create an Exit button.
    b2 = tk.Button(root, text="Exit", command=root.destroy)
    b2.grid(row=4, column=1)

    root.mainloop()
    phase = None

    try:
        return phase, message
    except:
        return phase, "Description"

def split_text(t):
    text = []
    escape = "\n"
    t = t.split(escape)
    for i in t:
        text.append(i)
    return text

def get_text(text):
    global message
    message = text.get("1.0", tk.END)
    message = split_text(message)
    root.destroy()

def draw(message):
    if message == None:
        message = "Description"
    for m in range(0, len(message)):
        desc_label = font.render(f"{message[m]}", True, BLACK)
        screen.blit(desc_label, (0, height//1.33+15*m))
    for p in range(len(players)):
        pg.draw.ellipse(screen, BLACK, (players[p]))
        position_label = font.render(f"{pos[p]}", True, WHITE)
        screen.blit(position_label, (players[p][0]+3, players[p][1]+3))
    for o in ols:
        pg.draw.rect(screen, BLACK, (o))
        screen.blit(ol_label, (o[0]+3, o[1]+3))
    for route in range(1, len(routes), 2):
        if len(routes)%2==0:
            pg.draw.line(screen, BLACK, (routes[route-1][0], routes[route-1][1]), (routes[route][0], routes[route][1]), 3)
    for d in drawing:
        pg.draw.circle(screen, BLACK, (d[0], d[1]), 3)

def change_label():
    global message
    message = simpledialog.askstring("Message", "Enter your player label:")
    phase = "player"
    message = str(message)
    return phase, message

def clear():
    players.clear()
    routes.clear()
    drawing.clear()
    ols.clear()
    pos.clear()
    message = "Description"
    phase = None
    return phase, message

docs_folder = os.path.join(os.environ['USERPROFILE'], "Documents\\plays\\")

def save(phase):
    draw(message)
    phase = None
    if not os.path.exists(docs_folder):
        os.makedirs(docs_folder)
    try:
        save = simpledialog.askstring("Message", "Enter title to save:")
        draw(message)
        pg.image.save(screen, docs_folder+save+'.png')

        for rect in range(len(players)):
            rect_players[len(rect_players)] = (players[rect][0], players[rect][1], players[rect][2], players[rect][3])
        for rect in ols:
            rect_ols[len(rect_ols)] = (rect.x, rect.y, rect.width, rect.height)
        for rect in drawing:
            rect_draw[len(rect_draw)] = (rect.x, rect.y, rect.width, rect.height)
        for rect in range(1, len(routes), 2):
            rect_routes[len(rect_routes)] = (routes[rect-1], routes[rect])
        my_list = [rect_players, pos, rect_ols, rect_draw, rect_routes, message]
        with open(docs_folder+save+'.json', "w") as f:
            json.dump(my_list, f)
    except:
        pass
    return phase

def open_saved(message):
    clear()
    json_files = files()
    opened = simpledialog.askstring("Message", f"Enter file name:\n{json_files}")
    message = ""
    try:
        with open(docs_folder+str(opened)+'.json', "r") as f:
            pl, po, ol, dr, ro, ms = json.load(f)
            for values in pl.values():
                if values not in players:
                    players.append(values)
            for values in po:
                pos.append(values)
            for values in ol.values():
                ols.append(values)
            for key, values in dr.items():
                drawing.append(values)
            for values in ro.values():
                for v in values:
                    routes.append(v)
            message = ms
            return message
    except:
        pass

def delete_files(phase):
    clear()
    phase = None
    json_files = files()
    opened = simpledialog.askstring("Message", f"Enter file name:\n{json_files}")
    delete = (".json", ".png")
    for i in delete:
        try:
            os.remove(docs_folder+opened+i)
        except:
            pass
    return phase

def files():
    json_files = [f for f in glob.glob(docs_folder+"*.json")]
    formatted_files = []
    for i in json_files:
        i = i.split(".json")
        i = i[0].split("\\")
        formatted_files.append(i[-1])
    return formatted_files