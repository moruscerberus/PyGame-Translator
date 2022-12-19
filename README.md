# PyGame-Translator
Just a simple test to load language files inside PyGame

## Code Example

```python
import translator
import pygame
import sys


class DropDown():

    def __init__(self, color_menu, color_option, x, y, w, h, font, main, options):
        self.color_menu = color_menu
        self.color_option = color_option
        self.rect = pygame.Rect(x, y, w, h)
        self.font = font
        self.main = main
        self.options = options
        self.draw_menu = False
        self.menu_active = False
        self.active_option = -1

    def draw(self, surf):
        pygame.draw.rect(surf, self.color_menu[self.menu_active], self.rect, 0)
        msg = self.font.render(self.main, 1, (0, 0, 0))
        surf.blit(msg, msg.get_rect(center = self.rect.center))

        if self.draw_menu:
            for i, text in enumerate(self.options):
                rect = self.rect.copy()
                rect.y += (i+1) * self.rect.height
                pygame.draw.rect(surf, self.color_option[1 if i == self.active_option else 0], rect, 0)
                msg = self.font.render(text, 1, (0, 0, 0))
                surf.blit(msg, msg.get_rect(center = rect.center))

    def update(self, event_list):
        mpos = pygame.mouse.get_pos()
        self.menu_active = self.rect.collidepoint(mpos)
        
        self.active_option = -1
        for i in range(len(self.options)):
            rect = self.rect.copy()
            rect.y += (i+1) * self.rect.height
            if rect.collidepoint(mpos):
                self.active_option = i
                break

        if not self.menu_active and self.active_option == -1:
            self.draw_menu = False

        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.menu_active:
                    self.draw_menu = not self.draw_menu
                elif self.draw_menu and self.active_option >= 0:
                    self.draw_menu = False
                    return self.active_option
        return -1

pygame.init()

(width, height) = (1280, 720)
background_colour = (255,255,255)

pygame.display.set_caption('Translator')
screen = pygame.display.set_mode((width, height))
index = 0
clock = pygame.time.Clock()

COLOR_INACTIVE = (100, 80, 255)
COLOR_ACTIVE = (100, 200, 255)
COLOR_LIST_INACTIVE = (255, 100, 100)
COLOR_LIST_ACTIVE = (255, 150, 150)

font = pygame.font.SysFont('simsun', 48)
font_small = pygame.font.SysFont('simsun', 24)

list1 = DropDown(
    [COLOR_INACTIVE, COLOR_ACTIVE],
    [COLOR_LIST_INACTIVE, COLOR_LIST_ACTIVE],
    50, 50, 200, 50, 
    font_small,
    "Select Language", ["English", "Swedish", "German", "Chinese", "Russian"])


while True:

    event_list = pygame.event.get()
    


    for event in event_list:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_SPACE:
        #         translator.set_language(translator.languages[index])
        #         if index < len(translator.languages) - 1:
        #             index += 1
        #         else:
        #             index = 0
 
        screen.fill(background_colour)
        translated_text = font.render((translator.get_language('example/title')), True, (255, 0, 0))
        screen.blit(translated_text, (450, 50))
        selected_option = list1.update(event_list)
        if selected_option >= 0:
            list1.main = list1.options[selected_option]
        list1.draw(screen)

        if selected_option == 0:
            translator.set_language(translator.languages[0])
        elif selected_option == 1:
            translator.set_language(translator.languages[1])
        elif selected_option == 2:
            translator.set_language(translator.languages[2])
        elif selected_option == 3:
            translator.set_language(translator.languages[3])
            
        elif selected_option == 4:
            translator.set_language(translator.languages[4])
            
    pygame.display.update()
    pygame.display.flip()
```
