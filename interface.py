import pygame

class Interface:
    def __init__(self, ecran):
        self.ecran = ecran

    def render(self, jeu):
        # Remplir l'écran avec une couleur de fond (noir)
        self.ecran.fill((0, 0, 0))
        
        # Dessiner les raquettes
        pygame.draw.rect(self.ecran, (255, 255, 255), (50, jeu.position_j1, jeu.largeur_raquette, jeu.hauteur_raquette))
        pygame.draw.rect(self.ecran, (255, 255, 255), (jeu.largeur_ecran - 50 - jeu.largeur_raquette, jeu.position_j2, jeu.largeur_raquette, jeu.hauteur_raquette))
        
        # Dessiner la balle
        pygame.draw.circle(self.ecran, (255, 255, 255), jeu.position_balle, 10)
        
        # Afficher les scores
        font = pygame.font.Font(None, 74)
        score_text = self.font.render(f"{jeu.score1} -{jeu.score2}", True, (255, 255, 255))
        self.ecran.blit(score_text, (jeu.largeur_ecran // 2 - score_text.get_width() // 2, 50))