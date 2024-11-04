import unittest
from jeu import Jeu

class TestJeu(unittest.TestCase):
    def setUp(self):
        self.jeu = Jeu()

    def test_initialisation(self):
        self.assertEqual(self.jeu.position_balle, [400, 300])
        self.assertEqual(self.jeu.vitesse_balle, [4, 4])
        self.assertEqual(self.jeu.position_j1, 250)
        self.assertEqual(self.jeu.position_j2, 250)
        self.assertEqual(self.jeu.score1, 0)
        self.assertEqual(self.jeu.score2, 0)

    def test_mise_a_jour_position_balle(self):
        self.jeu.update()
        self.assertEqual(self.jeu.position_balle, [404, 304])

    def test_collision_haut_bas(self):
        self.jeu.position_balle = [400, 0]
        self.jeu.update()
        self.assertEqual(self.jeu.vitesse_balle[1], 4)

        self.jeu.position_balle = [400, 600]
        self.jeu.update()
        self.assertEqual(self.jeu.vitesse_balle[1], -4)

    def test_collision_raquette_j1(self):
        self.jeu.position_balle = [50 + self.jeu.largeur_raquette, self.jeu.position_j1 + 50]
        self.jeu.update()
        self.assertEqual(self.jeu.vitesse_balle[0], 4)

    def test_collision_raquette_j2(self):
        self.jeu.position_balle = [self.jeu.largeur_ecran - 50 - self.jeu.largeur_raquette, self.jeu.position_j2 + 50]
        self.jeu.update()
        self.assertEqual(self.jeu.vitesse_balle[0], -4)

    def test_mise_a_jour_score_j1(self):
        self.jeu.position_balle = [50, self.jeu.position_j1 + self.jeu.hauteur_raquette + 10]
        self.jeu.update()
        self.assertEqual(self.jeu.score2, 1)
        self.assertEqual(self.jeu.position_balle, [400, 300])

    def test_mise_a_jour_score_j2(self):
        self.jeu.position_balle = [self.jeu.largeur_ecran - 50, self.jeu.position_j2 + self.jeu.hauteur_raquette + 10]
        self.jeu.update()
        self.assertEqual(self.jeu.score1, 1)
        self.assertEqual(self.jeu.position_balle, [400, 300])

    def test_reset_balle(self):
        self.jeu.reset_balle()
        self.assertEqual(self.jeu.position_balle, [400, 300])
        self.assertEqual(self.jeu.vitesse_balle, [4, 4])

if __name__ == '__main__':
    unittest.main()