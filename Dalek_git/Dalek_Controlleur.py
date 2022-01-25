import Dalek_Modele
import Dalek_Vue

# Controleur gère le logiciel
# En python il n'y a pas de constructeur
# Une classe est une définition
class Controleur ():
    # Initialiser un objet, fonction invoquée automatiquement à la création d'un objet
    def __init__(self):
        self.modele = Dalek_Modele.Jeu() # Va générer un obj Jeu
        self.vue = Dalek_Vue.Vue()
        self.actions = {"p": self.demarrer_partie,
                        "o": self.choisir_option,
                        "s": self.voir_score,
                        "q": self.quitter_jeu}
        self.afficher_menu_initial()


    def afficher_menu_initial(self):
        reponse = ""
        while not reponse:
            reponse = self.vue.afficher_menu_initial()
            if reponse in self.actions.keys():
                self.actions[reponse]()
            else:
                print("RATÉ")

    def demarrer_partie(self):
        self.modele.demarrer_partie()
        self.vue.afficher_partie(self.modele.partie_courante)
        self.tour()

    def choisir_option(self):
        reponses = self.vue.afficher_menu_options()
        largeur = reponses[0]
        hauteur = reponses[1]
        self.modele.changer_options(largeur, hauteur)
        self.afficher_menu_initial()

    def voir_score(self):
        self.vue.afficher_score()
        print("SCORE")

    def quitter_jeu(self):
        print("Au Revoir!")


    def tour(self):
        while self.modele.partie_courante.docteur.en_vie:
            action = self.vue.afficher_actions_docteur()
            if action in self.modele.partie_courante.docteur.actions.keys():
               self.modele.partie_courante.docteur.actions[action]()
               self.modele.partie_courante.deplacer_daleks()
               self.modele.partie_courante.verifier_collisions()
            else:
                print("Invalide")
            self.vue.afficher_partie(self.modele.partie_courante)
        self.afficher_menu_initial()


# LE MAIN
# Double underscore signifie variable privée du langage
if __name__ == '__main__':
    c = Controleur()

    #print("FIN DE DALEKS")

    # With the parentheses => calling an object
    # No parentheses => calling the class