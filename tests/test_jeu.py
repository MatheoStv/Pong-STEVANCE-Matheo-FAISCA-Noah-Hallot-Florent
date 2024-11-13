import unittest
from jeu import Jeu

class TestJeu(unittest.TestCase):
    def setUp(self):
        self.jeu = Jeu()

    def test_initialisation(self):
        """
        Objectif : Vérifier que les attributs du jeu sont correctement initialisés.
        Scénario : Initialiser un objet Jeu et vérifier les valeurs initiales des attributs.
        """
        self.assertEqual(self.jeu.position_balle, [400, 300])
        self.assertEqual(self.jeu.vitesse_balle, [4, 4])
        self.assertEqual(self.jeu.position_j1, 250)
        self.assertEqual(self.jeu.position_j2, 250)
        self.assertEqual(self.jeu.score1, 0)
        self.assertEqual(self.jeu.score2, 0)

    def test_mise_a_jour_position_balle(self):
        """
        Objectif : Vérifier que la position de la balle est mise à jour correctement.
        Scénario : Appeler la méthode update et vérifier la nouvelle position de la balle.
        """
        self.jeu.update()
        self.assertEqual(self.jeu.position_balle, [404, 304])

    def test_collision_haut_bas(self):
        """
        Objectif : Vérifier que la balle rebondit correctement lorsqu'elle touche le haut ou le bas de l'écran.
        Scénario : Placer la balle au bord supérieur et inférieur de l'écran et appeler la méthode update.
        """
        self.jeu.position_balle = [400, 0]
        self.jeu.update()
        self.assertEqual(self.jeu.vitesse_balle[1], 4)

        self.jeu.position_balle = [400, 600]
        self.jeu.update()
        self.assertEqual(self.jeu.vitesse_balle[1], -4)

    def test_collision_raquette_j1(self):
        """
        Objectif : Vérifier que la balle rebondit correctement lorsqu'elle touche la raquette du joueur 1.
        Scénario : Placer la balle en collision avec la raquette du joueur 1 et appeler la méthode update.
        """
        self.jeu.position_balle = [50 + self.jeu.largeur_raquette, self.jeu.position_j1 + 50]
        self.jeu.update()
        self.assertEqual(self.jeu.vitesse_balle[0], 4)

    def test_collision_raquette_j2(self):
        """
        Objectif : Vérifier que la balle rebondit correctement lorsqu'elle touche la raquette du joueur 2.
        Scénario : Placer la balle en collision avec la raquette du joueur 2 et appeler la méthode update.
        """
        self.jeu.position_balle = [self.jeu.largeur_ecran - 50 - self.jeu.largeur_raquette, self.jeu.position_j2 + 50]
        self.jeu.update()
        self.assertEqual(self.jeu.vitesse_balle[0], -4)

    def test_mise_a_jour_score_j1(self):
        """
        Objectif : Vérifier que le score du joueur 2 est mis à jour correctement lorsque la balle dépasse la raquette du joueur 1.
        Scénario : Placer la balle au-delà de la raquette du joueur 1 et appeler la méthode update.
        """
        self.jeu.position_balle = [50, self.jeu.position_j1 + self.jeu.hauteur_raquette + 10]
        self.jeu.update()
        self.assertEqual(self.jeu.score2, 1)
        self.assertEqual(self.jeu.position_balle, [400, 300])

    def test_mise_a_jour_score_j2(self):
        """
        Objectif : Vérifier que le score du joueur 1 est mis à jour correctement lorsque la balle dépasse la raquette du joueur 2.
        Scénario : Placer la balle au-delà de la raquette du joueur 2 et appeler la méthode update.
        """
        self.jeu.position_balle = [self.jeu.largeur_ecran - 50, self.jeu.position_j2 + self.jeu.hauteur_raquette + 10]
        self.jeu.update()
        self.assertEqual(self.jeu.score1, 1)
        self.assertEqual(self.jeu.position_balle, [400, 300])

    def test_reset_balle(self):
        """
        Objectif : Vérifier que la balle est correctement réinitialisée après qu'un point est marqué.
        Scénario : Appeler la méthode reset_balle et vérifier les valeurs de position_balle et vitesse_balle.
        """
        self.jeu.reset_balle()
        self.assertEqual(self.jeu.position_balle, [400, 300])
        self.assertEqual(self.jeu.vitesse_balle, [4, 4])

if __name__ == '__main__':
    unittest.main()