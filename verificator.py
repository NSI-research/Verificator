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

def intVerif(ask):
    listestr = "1234567890-"

    while True:
        nb_prob = 0
        reponse = input(ask)
        for i in reponse:
            if i not in listestr:
                nb_prob += 1
                print("\nCette valeur est invalide, veuillez réhitérer.")
            elif i == "-" and reponse.index(i) != 0:
                nb_prob += 1
                print("\nCette valeur est invalide, veuillez réhitérer.")
        if nb_prob == 0:
            return int(reponse)
                
        