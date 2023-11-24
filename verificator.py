# listestr = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ()'[]}{_/\ &é~-è`ç^à@=+°²"

def floatVerif(ask):
    listestr = "1234567890-,."
    nb_points = 0

    while True:
        nb_prob = 0
        reponse = input(ask)

        for i in reponse:
            if i == "." or i == ",":
                nb_points += 1
                reponse.replace(",", ".")
            if i not in listestr:
                nb_prob += 1
                print("\nCette valeur est invalide, veuillez réhitérer.")
            elif i == "-" and reponse.index(i) != 0:
                nb_prob += 1
                print("\nCette valeur est invalide, veuillez réhitérer.")
            elif nb_points > 1:
                nb_prob += 1
                print("\nCette valeur est invalide, veuillez réhitérer.")
        if nb_prob == 0:
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
