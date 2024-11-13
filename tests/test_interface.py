import pygame
import unittest
from interface import Interface
from jeu import Jeu

class TestInterface(unittest.TestCase):
    # Initialisation des tests
    def setUp(self):
        pygame.init()
        self.ecran = pygame.display.set_mode((800, 600))
        self.interface = Interface(self.ecran)
        self.jeu = Jeu()

    # Nettoyage après les tests
    def tearDown(self):
        pygame.quit()

    def test_initialisation_interface(self):
        """
        Objectif : Vérifier que l'interface est correctement initialisée.
        Scénario : Initialiser un objet Interface et vérifier les dimensions de l'écran.
        """
        self.assertIsNotNone(self.interface.ecran)
        self.assertEqual(self.interface.ecran.get_width(), 800)
        self.assertEqual(self.interface.ecran.get_height(), 600)

    def test_render_raquettes(self):
        """
        Objectif : Vérifier que les raquettes sont dessinées aux bonnes positions.
        Scénario : Définir les positions des raquettes, appeler la méthode render et vérifier les pixels aux positions attendues.
        """
        self.jeu.position_j1 = 100
        self.jeu.position_j2 = 200
        self.interface.render(self.jeu)
        # Vérifie que les raquettes sont dessinées aux bonnes positions
        self.assertEqual(self.ecran.get_at((50, self.jeu.position_j1)), (255, 255, 255, 255))
        self.assertEqual(self.ecran.get_at((self.jeu.largeur_ecran - 50 - self.jeu.largeur_raquette, self.jeu.position_j2)), (255, 255, 255, 255))

    def test_render_balle(self):
        """
        Objectif : Vérifier que la balle est dessinée à la bonne position.
        Scénario : Définir la position de la balle, appeler la méthode render et vérifier les pixels autour de la position attendue.
        """
        self.jeu.position_balle = [400, 300]
        self.interface.render(self.jeu)
        # Capture l'écran après le rendu
        pixels = pygame.surfarray.array3d(self.ecran)
        # Vérifie que la balle est dessinée à la bonne position
        self.assertTrue((pixels[395:405, 295:305] == [255, 255, 255]).all())

    def test_render_score(self):
        """
        Objectif : Vérifier que le score est affiché correctement.
        Scénario : Définir les scores des joueurs, appeler la méthode render et vérifier les pixels autour de la position attendue du score.
        """
        self.jeu.score1 = 3
        self.jeu.score2 = 5
        self.interface.render(self.jeu)
        # Capture l'écran après le rendu
        pixels = pygame.surfarray.array3d(self.ecran)
        # Vérifie que le score est affiché (approximativement)
        score_region = pixels[30:70, 300:500]  # Région autour de la position attendue du score
        self.assertTrue((score_region == [255, 255, 255]).any())

if __name__ == '__main__':
    unittest.main()