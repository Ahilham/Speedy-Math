import pygame
import os
import sys
from typing import Final
from buttons import Button
from equation_generator import EquationGenerator
import pygame_gui

#initialize the pygame
pygame.init()

width: Final = 800
height: Final = 600

screen = pygame.display.set_mode((width, height)) 
MANAGER = pygame_gui.UIManager((width, height))
CLOCK = pygame.time.Clock()




#Title and Icon
pygame.display.set_caption("Speedy Math")
curren_dir = os.path.dirname(__file__)
icon_file_name = 'Math_Play_icon.png'
background_file_name = 'blackboard.png'
play_file_name = 'Play_button.png'
play_pressed_file_name = 'Play_button_pressed.png'
logo_file_name = 'logo_menu.png'
background_path: Final = os.path.join(curren_dir, background_file_name) 
icon_path: Final = os.path.join(curren_dir, icon_file_name)
play_button_path: Final = os.path.join(curren_dir, play_file_name)
logo_path: Final = os.path.join(curren_dir, logo_file_name)

main_font: Final = pygame.font.SysFont("cambria", 50)
background = pygame.image.load(background_path)
background: Final = pygame.transform.scale(background, (width, height)) 
icon: Final = pygame.image.load(icon_path)
button_play_image = pygame.image.load(play_button_path)
button_play_image = pygame.transform.scale(button_play_image, (150, 100))
logo_image = pygame.image.load(logo_path)
logo_image: Final = pygame.transform.scale(logo_image, (400, 300))

text_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((355, 400), (100, 100)), manager=MANAGER, object_id="#main_text_entry")

timer_text = main_font.render("5:00", True, "white")
timer_text_rect = timer_text.get_rect(center=(385,100))

timer_minus = pygame.USEREVENT + 1


pygame.time.set_timer(timer_minus, 1000)

pygame.display.set_icon(icon)

#Points

highest_lvl_1 = 0


highest_lvl_2 = 0


highest_lvl_3 = 0


#main game
def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.SysFont(pygame.font.get_default_font(), size)



def level_1():
    global highest_lvl_1
    
    point1 = 0
    level = 1
    curr_seconds = 75
    
    ans, equation = EquationGenerator.equation_gen(level=level)

    

    
    def check_answer(answer: int, lvl: int):
        nonlocal ans, equation, point1
        

        if int(answer) == ans:
            ans, equation = EquationGenerator.equation_gen(level=lvl)
            point1 += 10
        else:
            pass
    

    while True:
        UI_refresh_rate = CLOCK.tick(60)/1000
        LEVEL_1_MOUSE_POS = pygame.mouse.get_pos()

        button_back = Button(image = button_play_image, pos = (200,150), text_input="BACK", font = get_font(55), base_color = "#ffffff", hovering_color = "#807a7a")
        


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_back.checkForInput(LEVEL_1_MOUSE_POS):
                    play()
                
            if event.type == timer_minus:
                curr_seconds -= 1
            if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "#main_text_entry":
                try:
                    check_answer(int(event.text), level)
                except ValueError:
                    pass
            MANAGER.process_events(event)
        screen.blit(background, (0, 0))



        #for the timer
        if curr_seconds >= 0:
            display_seconds = curr_seconds % 60
            display_minutes = int(curr_seconds/60) % 60
            display_time = f"{display_minutes:02}:{display_seconds:02}"

            question_text = main_font.render(f"{equation}", True, "white")
            question_text_rect = question_text.get_rect(center=(400,300))

            timer_text = main_font.render(display_time, True, "white")
            screen.blit(timer_text, timer_text_rect)

            MANAGER.update(UI_refresh_rate)
            MANAGER.draw_ui(screen)

            screen.blit(question_text, question_text_rect)

        else:
            if point1 > highest_lvl_1:
                highest_lvl_1 = point1

            point_text = main_font.render(f"Point: {point1}", True, "white")
            point_text_rect = point_text.get_rect(center=(400,300))

            point_text_high_score = main_font.render(f"Highest Score: {highest_lvl_1}", True, "white")
            point_text_high_score_rect = point_text.get_rect(center=(400,400))

            screen.blit(point_text, point_text_rect)
            screen.blit(point_text_high_score, point_text_high_score_rect)


    
        button_back.changeColor(LEVEL_1_MOUSE_POS)
        button_back.update(screen)
    
    
        pygame.display.update()

def level_2():
    global highest_lvl_2
       
    point2 = 0
    level = 2
    curr_seconds = 90
    
    ans, equation = EquationGenerator.equation_gen(level=level)

    

    
    def check_answer(answer: int, lvl: int):
        nonlocal ans, equation, point2
        

        if int(answer) == ans:
            ans, equation = EquationGenerator.equation_gen(level=lvl)
            point2 += 10
        else:
            pass
    

    while True:
        UI_refresh_rate = CLOCK.tick(60)/1000
        LEVEL_2_MOUSE_POS = pygame.mouse.get_pos()

        button_back = Button(image = button_play_image, pos = (200,150), text_input="BACK", font = get_font(55), base_color = "#ffffff", hovering_color = "#807a7a")
        


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_back.checkForInput(LEVEL_2_MOUSE_POS):
                    play()
                
            if event.type == timer_minus:
                curr_seconds -= 1
            if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "#main_text_entry":
                try:
                    check_answer(int(event.text), level)
                except ValueError:
                    pass
            MANAGER.process_events(event)
        screen.blit(background, (0, 0))



        #for the timer
        if curr_seconds >= 0:
            display_seconds = curr_seconds % 60
            display_minutes = int(curr_seconds/60) % 60
            display_time = f"{display_minutes:02}:{display_seconds:02}"

            question_text = main_font.render(f"{equation}", True, "white")
            question_text_rect = question_text.get_rect(center=(400,300))

            timer_text = main_font.render(display_time, True, "white")
            screen.blit(timer_text, timer_text_rect)

            MANAGER.update(UI_refresh_rate)
            MANAGER.draw_ui(screen)

            screen.blit(question_text, question_text_rect)

        else:
            if point2 > highest_lvl_2:
                highest_lvl_2 = point2

            point_text = main_font.render(f"Point: {point2}", True, "white")
            point_text_rect = point_text.get_rect(center=(400,300))

            point_text_high_score = main_font.render(f"Highest Score: {highest_lvl_2}", True, "white")
            point_text_high_score_rect = point_text.get_rect(center=(400,400))

            screen.blit(point_text, point_text_rect)
            screen.blit(point_text_high_score, point_text_high_score_rect)


    
        button_back.changeColor(LEVEL_2_MOUSE_POS)
        button_back.update(screen)
    
    
        pygame.display.update()

def level_3():
    global highest_lvl_3
       
    point3 = 0
    level = 3
    curr_seconds = 120
    
    ans, equation = EquationGenerator.equation_gen(level=level)

    

    
    def check_answer(answer: int, lvl: int):
        nonlocal ans, equation, point3
        

        if int(answer) == ans:
            ans, equation = EquationGenerator.equation_gen(level=lvl)
            point3 += 10
        else:
            pass
    

    while True:
        UI_refresh_rate = CLOCK.tick(60)/1000
        LEVEL_3_MOUSE_POS = pygame.mouse.get_pos()

        button_back = Button(image = button_play_image, pos = (200,150), text_input="BACK", font = get_font(55), base_color = "#ffffff", hovering_color = "#807a7a")
        


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_back.checkForInput(LEVEL_3_MOUSE_POS):
                    play()
                
            if event.type == timer_minus:
                curr_seconds -= 1
            if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "#main_text_entry":
                try:
                    check_answer(int(event.text), level)
                except ValueError:
                    pass
            MANAGER.process_events(event)
        screen.blit(background, (0, 0))



        #for the timer
        if curr_seconds >= 0:
            display_seconds = curr_seconds % 60
            display_minutes = int(curr_seconds/60) % 60
            display_time = f"{display_minutes:02}:{display_seconds:02}"

            question_text = main_font.render(f"{equation}", True, "white")
            question_text_rect = question_text.get_rect(center=(400,300))

            timer_text = main_font.render(display_time, True, "white")
            screen.blit(timer_text, timer_text_rect)

            MANAGER.update(UI_refresh_rate)
            MANAGER.draw_ui(screen)

            screen.blit(question_text, question_text_rect)

        else:
            if point3 > highest_lvl_2:
                highest_lvl_2 = point3

            point_text = main_font.render(f"Point: {point3}", True, "white")
            point_text_rect = point_text.get_rect(center=(400,300))

            point_text_high_score = main_font.render(f"Highest Score: {highest_lvl_3}", True, "white")
            point_text_high_score_rect = point_text.get_rect(center=(400,400))

            screen.blit(point_text, point_text_rect)
            screen.blit(point_text_high_score, point_text_high_score_rect)


    
        button_back.changeColor(LEVEL_3_MOUSE_POS)
        button_back.update(screen)
    
    
        pygame.display.update()
        

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        screen.blit(background, (0, 0))

        button_level_1 = Button(image = button_play_image, pos = (400, 150), text_input = "LEVEL 1", font = get_font(55), base_color = "#ffffff", hovering_color = "#807a7a")
        button_level_2 = Button(image = button_play_image, pos = (400, 300), text_input = "LEVEL 2", font = get_font(55), base_color = "#ffffff", hovering_color = "#807a7a")
        button_level_3 = Button(image = button_play_image, pos = (400, 450), text_input = "LEVEL 3", font = get_font(55), base_color = "#ffffff", hovering_color = "#807a7a")
        button_back = Button(image = button_play_image, pos = (200,150), text_input="BACK", font = get_font(55), base_color = "#ffffff", hovering_color = "#807a7a")

        
        button_level_1.changeColor(PLAY_MOUSE_POS)
        button_level_2.changeColor(PLAY_MOUSE_POS)
        button_level_3.changeColor(PLAY_MOUSE_POS)
        button_back.changeColor(PLAY_MOUSE_POS)

        button_level_1.update(screen)
        button_level_2.update(screen)
        button_level_3.update(screen)
        button_back.update(screen)
        

        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_back.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if button_level_1.checkForInput(PLAY_MOUSE_POS):
                    level_1()
                if button_level_2.checkForInput(PLAY_MOUSE_POS):
                    level_2()
                if button_level_3.checkForInput(PLAY_MOUSE_POS):
                    level_3()

        pygame.display.update()

def quit():
    pygame.quit()
    sys.exit()

def main_menu():
    while True:
        screen.blit(background, (0, 0))
        
        button_play = Button(image = button_play_image, pos = (400, 400), text_input = "PLAY", font = get_font(55), base_color = "#ffffff", hovering_color = "#807a7a")
        button_quit = Button(image = button_play_image, pos = (400, 500), text_input = "QUIT", font = get_font(55), base_color = "#ffffff", hovering_color = "#807a7a")

        MENU_MOUSE_POS = pygame.mouse.get_pos()
        MENU_RECT = logo_image.get_rect(center = (400, 200))

        screen.blit(logo_image, MENU_RECT)

        button_play.changeColor(MENU_MOUSE_POS)
        button_play.update(screen)

        button_quit.changeColor(MENU_MOUSE_POS)
        button_quit.update(screen)

        
	
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_play.checkForInput(MENU_MOUSE_POS):
                    play()
                if button_quit.checkForInput(MENU_MOUSE_POS):
                    quit()

        pygame.display.update()


if __name__ == "__main__":
    main_menu()