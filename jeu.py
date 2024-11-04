class Jeu:
    def __init__(self):
        self.position_balle = [400, 300]
        self.vitesse_balle = [4, 4]
        self.position_j1 = 250
        self.position_j2 = 250
        self.score1 = 0
        self.score2 = 0
        self.largeur_raquette = 10
        self.hauteur_raquette = 100
        self.largeur_ecran = 800
        self.hauteur_ecran = 600

    def update(self):
        # Mise à jour de la position de la balle
        self.position_balle[0] += self.vitesse_balle[0]
        self.position_balle[1] += self.vitesse_balle[1]

        # Collision avec le haut et le bas de l'écran
        if self.position_balle[1] <= 0 or self.position_balle[1] >= self.hauteur_ecran:
            self.vitesse_balle[1] = -self.vitesse_balle[1]

        # Collision avec les raquettes
        if self.position_balle[0] <= 50 + self.largeur_raquette:
            if self.position_j1 <= self.position_balle[1] <= self.position_j1 + self.hauteur_raquette:
                self.vitesse_balle[0] = -self.vitesse_balle[0]
            else:
                self.score2 += 1
                self.reset_balle()

        if self.position_balle[0] >= self.largeur_ecran - 50 - self.largeur_raquette:
            if self.position_j2 <= self.position_balle[1] <= self.position_j2 + self.hauteur_raquette:
                self.vitesse_balle[0] = -self.vitesse_balle[0]
            else:
                self.score1 += 1
                self.reset_balle()

    def reset_balle(self):
        self.position_balle = [self.largeur_ecran // 2, self.hauteur_ecran // 2]
        self.vitesse_balle = [4, 4]