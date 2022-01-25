import Dalek_Vue
import random


class Jeu():
    def __init__(self):
        self.largeur = 8
        self.hauteur = 6
        self.partie_courante = None
        self.high_score = []

    def demarrer_partie(self):
        self.partie_courante = Partie(self)

    def changer_options(self, largeur=8, hauteur=6):
        self.largeur = largeur
        self.hauteur = hauteur


class Partie():
    def __init__(self, parent):
        self.parent = parent
        self.score = 0
        self.niveau = 0
        self.nb_daleks_par_niveau = 5
        self.largeur = self.parent.largeur
        self.hauteur = self.parent.hauteur
        self.docteur = Docteur(self, int(self.largeur / 2), int(self.hauteur / 2))
        self.daleks = []
        self.ferrailles = []
        self.creer_niveau()

    def creer_niveau(self):
        self.niveau += 1
        nb_daleks = self.niveau * self.nb_daleks_par_niveau
        positions = [[self.docteur.x, self.docteur.y]]
        while nb_daleks:
            x = random.randrange(self.largeur)
            y = random.randrange(self.hauteur)
            if [x, y] not in positions:
                positions.append([x, y])
                nb_daleks -= 1
        positions.pop(0)
        for i in positions:
            self.daleks.append(Dalek(self, i[0], i[1]))

    def deplacer_daleks(self):
        for dalek in self.daleks:
            dalek.deplacer_dalek()

        for i in self.daleks:
            if i.x == self.docteur.x and i.y == self.docteur.y:
                self.docteur.en_vie = False
                print("Vous êtes mort")


    def verifier_collisions(self):
        daleks_morts = []
        for i in self.daleks:
            for j in self.daleks:
                if i != j and (i.x == j.x and i.y == j.y):
                    if i not in daleks_morts:
                        daleks_morts.append(i)
        for i in daleks_morts:
            self.daleks.remove(i)
            inexistant = 1
            for j in self.ferrailles:
                if i.x == j.x and i.y == j.y:
                    inexistant = 0
            if inexistant:
                self.ferrailles.append(Ferraille(self, i.x, i.y))

    def tour(self):
        while self.docteur.en_vie:
            action = self.vue.afficher_actions_docteur()
            if action in self.docteur.actions.keys():
                self.docteur.actions[action]()
                self.deplacer_daleks()
                self.verifier_collisions()
            else:
                print("Invalide")
            self.vue.afficher_partie()
        self.afficher_menu_initial()

class Dalek():
    def __init__(self, parent, x, y):
        self.parent = parent
        self.x = x
        self.y = y

    def deplacer_dalek(self):
        if self.x > self.parent.docteur.x:
            self.x -= 1
        elif self.x < self.parent.docteur.x:
            self.x += 1
        if self.y > self.parent.docteur.y:
            self.y -= 1
        elif self.y < self.parent.docteur.y:
            self.y += 1


class Ferraille():
    def __init__(self, parent, x, y):
        self.parent = parent
        self.x = x
        self.y = y

class Docteur():
    def __init__(self, parent, x=1, y=1):
        self.partie = parent
        self.x = x
        self.y = y
        self.en_vie = True
        self.nb_zapper = 1
        self.actions = {"5": self.immobile,
                        "8": self.monter,
                        "7": self.monter_gauche,
                        "9": self.monter_droite,
                        "2": self.descendre,
                        "1": self.descendre_gauche,
                        "3": self.descendre_droite,
                        "4": self.gauche,
                        "6": self.droite,
                        "t": self.teleporter,
                        "z": self.zapper
                        }

    def monter_gauche(self):
        if self.x >= 1:
            self.x -= 1
        if self.y >= 1:
            self.y -= 1

    def monter_droite(self):
        if self.x <= self.partie.largeur - 2:
            self.x += 1
        if self.y >= 1:
            self.y -= 1

    def descendre_gauche(self):
        if self.x >= 1:
            self.x -= 1
        if self.y <= self.partie.hauteur - 2:
            self.y += 1

    def descendre_droite(self):
        if self.x <= self.partie.largeur - 2:
            self.x += 1
        if self.y <= self.partie.hauteur - 2:
            self.y += 1

    def monter(self):
        if self.y >= 1:
            self.y -= 1

    def descendre(self):
        if self.y <= self.partie.hauteur - 2:
            self.y += 1

    def gauche(self):
        if self.x >= 1:
            self.x -= 1

    def droite(self):
        if self.x <= self.partie.largeur - 2:
            self.x += 1

    def immobile(self):
        self.x = self.x
        self.y = self.y

    def zapper(self):
        print("ici")
        # daleks_morts = []
        for dalek in self.partie.daleks:
            if abs(dalek.x - self.x) <= 1:
                self.partie.daleks.pop(self.partie.daleks.index(dalek))
            elif abs(dalek.y - self.y) <= 1:
                self.partie.daleks.pop(self.partie.daleks.index(dalek))
            elif abs(dalek.x - self.x & dalek.y - self.y) <= 1:
                self.partie.daleks.pop(self.partie.daleks.index(dalek))

            # daleks_morts.append(dalek)
            self.partie.score += 5

    def teleporter(self):
        x = random.randrange(self.partie.largeur)
        y = random.randrange(self.partie.hauteur)
        self.x = x
        self.y = y

