from constants import *
from buttons import *
from draw import *
import time


def update(width, height, run):

    is_painting = False
    is_erase = False
    start = None
    end = None
    message = "Description"
    position = "QB"
    phase = None
    # Main loop
    while run:

        # Begin play
        play = Play()

        # Sreen set up
        main_screen(width, height)
        players_button(width)
        square_button(width)
        routes_button(width)
        delete_button(width)
        description_button(width)
        name_button(width)
        draw_button(width)
        clear_button(width)
        save_button(width)
        open_button(width)
        df_button(width)

        # Check for events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = pg.mouse.get_pos()
                if mouse_pos[0] >= width//1.2 and mouse_pos[1] >= 50:
                    if mouse_pos[0] <= width//1.2+width//10 and mouse_pos[1] <= 90:
                        phase = "player"
                    elif mouse_pos[0] <= width//1.2+width//10 and mouse_pos[1] <= 140:
                        phase = "OL"
                    elif mouse_pos[0] <= width//1.2+width//10 and mouse_pos[1] <= 190:
                        phase = "route"
                    elif mouse_pos[0] <= width//1.2+width//10 and mouse_pos[1] <= 240:
                        phase = "delete"
                    elif mouse_pos[0] <= width//1.2+width//10 and mouse_pos[1] <= 290:
                        phase = "description"
                    elif mouse_pos[0] <= width//1.2+width//10 and mouse_pos[1] <= 340:
                        phase = "change label"
                    elif mouse_pos[0] <= width//1.2+width//10 and mouse_pos[1] <= 390:
                        phase = "freehand"
                    elif mouse_pos[0] <= width//1.2+width//10 and mouse_pos[1] <= 540:
                        phase = "clear"
                    elif mouse_pos[0] <= width//1.2+width//10 and mouse_pos[1] <= 590:
                        message = save(phase)
                    elif mouse_pos[0] <= width//1.2+width//10 and mouse_pos[1] <= 640:
                        message = open_saved(message)
                        draw(message)
                    elif mouse_pos[0] <= width//1.2+width//10 and mouse_pos[1] <= 690:
                        phase = delete_files(phase)

        if phase == "player":
            play.player(screen)
            mouse_pos = pg.mouse.get_pos()
            if event.type == pg.MOUSEBUTTONDOWN and (mouse_pos[0]<=width//1.33 and mouse_pos[1] < height//1.33):
                time.sleep(.25)
                play.add_player(screen, mouse_pos[0], mouse_pos[1], position)
        elif phase == "OL":
            play.ol(screen)
            mouse_pos = pg.mouse.get_pos()
            if event.type == pg.MOUSEBUTTONDOWN and (mouse_pos[0]<=width//1.33 and mouse_pos[1] < height//1.33):
                time.sleep(.25)
                play.add_ol(screen, mouse_pos[0], mouse_pos[1])
        elif phase == "route":
            play.route(screen)
            if event.type == pg.MOUSEBUTTONDOWN and (mouse_pos[0]<=width//1.33 and mouse_pos[1] < height//1.33):
                if start is None:
                    start = pg.mouse.get_pos()
                    time.sleep(.25)
                elif end is None:
                    end = pg.mouse.get_pos()
                    routes.append(start)
                    routes.append(end)
                    time.sleep(.25)
                    start = None
                    end = None
        elif phase == "freehand":
            play.freehand(screen)
            if event.type == pg.MOUSEBUTTONDOWN and (mouse_pos[0]<=width//1.33 and mouse_pos[1] < height//1.33):
                is_painting = True
            if is_painting:
                if(mouse_pos[0]<=width//1.33 and mouse_pos[1] < height//1.33):
                    play.add_freehand()
            if event.type == pg.MOUSEBUTTONUP:
                is_painting = False
        elif phase == "delete":
            if event.type == pg.MOUSEBUTTONDOWN:
                is_erase = True
                delete_action()
            if is_erase:
                delete_line()
            if event.type == pg.MOUSEBUTTONUP:
                is_erase = False
        elif phase == "description":
            phase, message = description()
        elif phase == "change label":
            phase, position = change_label()
        elif phase == "clear":
            phase, message = clear()

        pos_label = font.render(f"{position}", True, BLACK)
        screen.blit(pos_label, (width//1.19+80, 310))

        # Draw all players, and routes
        draw(message)
        # Update window
        pg.display.flip()
        clock.tick(60)

    pg.quit()

# Update window
update(width, height, run)