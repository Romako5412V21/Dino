import pygame
import pygame_menu
import os
import main3


pygame.init()

window = pygame.display.set_mode((600,400))
font1 = pygame_menu.font.FONT_DIGITAL
my_theme = pygame_menu.Theme(widget_font=font1, # шрифт меню
                             background_color=(0,0,0), # колір фону меню
                             widget_font_color=(255,0,0)) # колір тексту меню
url = "https://dino-chrome.com/"
def start():
    os.system(f"start {url}")

menu_rules = pygame_menu.Menu("Rules",600,400,
                        theme=my_theme)
menu_rules.add.label("Games rule:\n 1. Don't lose!\n")    
menu_rules.add.button("Back",pygame_menu.events.BACK)

menu_settings = pygame_menu.Menu("Settings",600,400,
                        theme=my_theme)
menu_settings.add.label("Settings\n")    
menu_settings.add.selector("Difficulty:\n",[('Easy',1),('Hard',2)])
#---------------------------------------------------
menu = pygame_menu.Menu("Main menu",600,400,
                        theme=pygame_menu.themes.THEME_BLUE)
menu.add.button("Start",start)

menu.add.button("Finish",pygame_menu.events.EXIT)






menu.mainloop(window)
