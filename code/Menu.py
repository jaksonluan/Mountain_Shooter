import pygame.image
from .Const import WIN_HEIGTH, WIN_WIDTH 
from .Const import COLOR_ORANGE, COLOR_WHITE, COLOR_YELLOW
from .Const import MENU_OPTION

class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/MenuBg.png')
        self. rect = self.surf.get_rect(left=0, top=0)
        

    def run(self, ):
        option_menu = 2
        pygame.mixer_music.load('./assets/Menu.mp3')
        pygame.mixer_music.play(-1)

        while True:
            # MENU
            self.window.blit(source=self.surf, dest=self.rect) 
            self.menu_text(70, text="Mountain", text_color=COLOR_ORANGE, text_center_pos=((WIN_WIDTH / 2), 70))
            self.menu_text(70, text="Shooter", text_color=COLOR_ORANGE, text_center_pos=((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                if i == option_menu: 
                    self.menu_text(30, text=MENU_OPTION[i], text_color=COLOR_YELLOW, text_center_pos=((WIN_WIDTH / 2), 200 + 20 * i))
                else:
                    self.menu_text(30, text=MENU_OPTION[i], text_color=COLOR_WHITE, text_center_pos=((WIN_WIDTH / 2), 200 + 20 * i))

            
            pygame.display.flip()
        # Check for all events
            for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   pygame.quit() #Close window
                   quit() # End pygame

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

