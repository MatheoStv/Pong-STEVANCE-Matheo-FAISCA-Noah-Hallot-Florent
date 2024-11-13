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
    
    horloge = pygame.time.Clock() # Horloge pour déterminer les i/s
    running = True # Boucle principale
    in_menu = True # Menu principal ou jeu
    
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

        # Gestion des touches pour les raquettes (J1 et J2)
        if not in_menu:
            touche = pygame.key.get_pressed()
            if touche[pygame.K_z]:
                jeu.position_j1 -= 5
            if touche[pygame.K_s]:
                jeu.position_j1 += 5
            if touche[pygame.K_UP]:
                jeu.position_j2 -= 5
            if touche[pygame.K_DOWN]:
                jeu.position_j2 += 5

            # Empêcher les raquettes de sortir de l'écran
            jeu.position_j1 = max(0, min(jeu.position_j1, jeu.hauteur_ecran - jeu.hauteur_raquette))
            jeu.position_j2 = max(0, min(jeu.position_j2, jeu.hauteur_ecran - jeu.hauteur_raquette))
            
            jeu.update()
            interface.render(jeu)
        else:
            menu.render()
        
        pygame.display.flip()
        horloge.tick(60) # 60 i/s
    
    pygame.quit()

if __name__ == '__main__':
    main()