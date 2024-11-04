import pygame
from jeu import Jeu
from interface import Interface
from menu import Menu

def main():
    pygame.init()
    ecran = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Pong')
    
    menu = Menu(ecran)
    jeu = Jeu()
    interface = Interface(ecran)
    
    clock = pygame.time.Clock()
    running = True
    in_menu = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if in_menu:
                action = menu.handle_event(event)
                if action == "Jouer":
                    in_menu = False
                elif action == "Quitter":
                    running = False

        if not in_menu:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_z]:
                jeu.position_j1 -= 5
            if keys[pygame.K_s]:
                jeu.position_j1 += 5
            if keys[pygame.K_UP]:
                jeu.position_j2 -= 5
            if keys[pygame.K_DOWN]:
                jeu.position_j2 += 5

            # Empêcher les raquettes de sortir de l'écran
            jeu.position_j1 = max(0, min(jeu.position_j1, jeu.hauteur_ecran - jeu.hauteur_raquette))
            jeu.position_j2 = max(0, min(jeu.position_j2, jeu.hauteur_ecran - jeu.hauteur_raquette))
            
            jeu.update()
            interface.render(jeu)
        else:
            menu.render()
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

if __name__ == '__main__':
    main()