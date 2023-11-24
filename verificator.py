# listestr = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ()'[]}{_/\ &é~-è`ç^à@=+°²"

def floatVerif(ask, pos=None, nul=None):
    listestr = "1234567890-,."

    while True:
        nb_points = 0
        nb_prob = 0
        reponse = input(ask)

        for i in reponse:
            if i not in listestr:
                nb_prob += 1
            elif i == "-" and reponse.index(i) != 0:
                nb_prob += 1
            elif i == "." or i == ",":
                nb_points += 1
                if i == ",":
                    liste_tempo = list(reponse)
                    liste_tempo[liste_tempo.index(i)] = "."
                    reponse = "".join(liste_tempo)

        if nb_prob != 0:
            print("\nRéponse invalide.")
        elif nb_points > 1:
            print("\nIl y a trop de points.")
        elif len(reponse) == 1 and "." in reponse:
            print("\nUn point seul ne veut rien dire.")
        elif pos is True and float(reponse) < 0:
            print("\nCe nombre n'est pas positif")
        elif pos is False and float(reponse) > 0:
            print("\nCe nombre n'est pas négatif")
        elif nul is False and float(reponse) == 0:
            print("\nCe nombre est nul.")

        else:
            return float(reponse)

def intVerif(ask, peer=None, pos=None, nul=None):
    listestr = "1234567890-"

    while True:
        nb_prob = 0
        reponse = input(ask)

        for i in reponse:
            if i not in listestr:
                nb_prob += 1
            elif i == "-" and reponse.index(i) != 0:
                nb_prob += 1
            
        if nb_prob != 0:
            print("\nRéponse invalide.")
        elif peer is True and int(reponse) % 2 != 0:
            print("\nCe nombre n'est pas pair.")
        elif peer is False and int(reponse) % 2 != 1:
            print("\nCe nombre n'est pas impair.")
        elif pos is True and int(reponse) < 0:
            print("\nCe nombre n'est pas positif")
        elif pos is False and int(reponse) > 0:
            print("\nCe nombre n'est pas négatif")
        elif nul is False and int(reponse) == 0:
            print("\nCe nombre est nul.")

        else:
            return int(reponse)
