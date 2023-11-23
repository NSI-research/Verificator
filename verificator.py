# listestr = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ()'[]}{_/\ &é~-è`ç^à@=+°²"

def floatVerif(ask):
    listestr = "1234567890-,."
    nb_points = 0

    reponse = input(ask)

    for i in reponse:
        if i not in listestr:
            return False
        if i == "-" and reponse.index(i) != 0:
            return False
        if i == "." or i == ",":
            nb_points += 1
            reponse.replace(",", ".")
        if nb_points > 1:
            return False

    return float(reponse)

def intVerif(ask):
    listestr = "1234567890-"

    reponse = input(ask)

    for i in reponse:
        if i not in listestr:
            return False
        if i == "-" and reponse.index(i) != 0:
            return False
    return int(reponse)
