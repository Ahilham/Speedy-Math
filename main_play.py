import pygame
from typing import Final
from equation_generator import EquationGenerator
import pygame_gui

pygame.init()

CLOCK = pygame.time.Clock()


main_font: Final = pygame.font.SysFont("cambria", 50)

width: Final = 800
height: Final = 600
screen = pygame.display.set_mode((width, height))

MANAGER = pygame_gui.UIManager((width, height))

text_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((355, 400), (100, 100)), manager=MANAGER, object_id="#main_text_entry")


timer_text = main_font.render("5:00", True, "white")
timer_text_rect = timer_text.get_rect(center=(385,100))

timer_minus = pygame.USEREVENT + 1

curr_seconds = 75
pygame.time.set_timer(timer_minus, 1000)


ans, equation = EquationGenerator.equation_gen(level=1)

user_answer = None

response = None
point1 = 0

def check_answer(answer: int, lvl: int):
    global ans, equation, point1
    
    if int(answer) == ans:
        ans, equation = EquationGenerator.equation_gen(level=1)
        point1 += 10
    else:
        pass


testing = True
while testing:



    UI_refresh_rate = CLOCK.tick(60)/1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            testing = False
        if event.type == timer_minus:
            curr_seconds -= 1
        if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "#main_text_entry":
            try:
                check_answer(int(event.text), 1)
            except ValueError:
                error_text = main_font.render("Invalid input.", True, "white")
                error_text_rect = error_text.get_rect(center=(400,550))
                screen.blit(error_text, error_text_rect)

        MANAGER.process_events(event)
    screen.fill("#ba4949")



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
        point_text = main_font.render(f"Point: {point1}", True, "white")
        point_text_rect = point_text.get_rect(center=(400,300))

        screen.blit(point_text, point_text_rect)


    

    
    
    pygame.display.update()