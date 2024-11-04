import pygame

class Menu:
    def __init__(self, ecran):
        self.ecran = ecran
        self.font = pygame.font.Font(None, 74)
        self.options = ["Jouer", "Quitter"]
        self.selected_option = 0

    def render(self):
        self.ecran.fill((0, 0, 0))
        for i, option in enumerate(self.options):
            color = (255, 255, 255) if i == self.selected_option else (100, 100, 100)
            text = self.font.render(option, True, color)
            self.ecran.blit(text, (self.ecran.get_width() // 2 - text.get_width() // 2, 200 + i * 100))

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected_option = (self.selected_option - 1) % len(self.options)
            elif event.key == pygame.K_DOWN:
                self.selected_option = (self.selected_option + 1) % len(self.options)
            elif event.key == pygame.K_RETURN:
                return self.options[self.selected_option]
        return None