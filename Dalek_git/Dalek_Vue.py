class Vue():
    def __init__(self):
        pass

    def afficher_menu_initial(self):
        print("Bienvenue aux DALEKS")
        print("Choix: p-> Partie, s-> Score, o-> Option, q-> Quitter")
        reponse = input("Votre réponse ici : ")
        return reponse

    def afficher_menu_options(self):
        reponses = []
        print("Options de DALEKS")
        print("Nouvelle largeur: ")

        largeur = int(input("Votre réponse ici : "))
        reponses.append(largeur)
        print("Nouvelle hauteur: ")
        hauteur = int(input("Votre réponse ici : "))
        reponses.append(hauteur)
        return reponses

    def afficher_partie(self, partie):
        print("Partie courante")

        # Remplir la carte avec des -
        carte_visuelle = []
        for i in range(partie.hauteur):
            ligne=[]
            for j in range(partie.largeur):
                ligne.append("-")
            carte_visuelle.append(ligne)

        # Placer le docteur sur la carte
        carte_visuelle[partie.docteur.y][partie.docteur.x] = "W"

        # Placer les daleks
        for i in partie.daleks:
           carte_visuelle[i.y][i.x] = "D"

        # Placer les ferrailles
        for i in partie.ferrailles:
           carte_visuelle[i.y][i.x] = "F"

        # Afficher le résultat
        for i in carte_visuelle:
            print(i)

    # ajout pour offrir menu déplacement

    def afficher_actions_docteur(self):
        print("À vous de jouer")
        print("Utiliser le pavé numérique pour vous déplacer, z-> zapper, t->téléporter")
        action = input("Votre action ici : ")
        return action

    def afficher_score(self, partie):
        score = partie.voir_score()
        print(f'Votre score est :{score}')


#if __name__ == '__main__':
#    print("Je suis la vueeeee")