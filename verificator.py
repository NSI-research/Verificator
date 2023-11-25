# listestr = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ()'[]}{_/\ &é~-è`ç^à@=+°²"

def is_list(ask=str, type=""):
    liste_int = "-123456789"
    liste_dec = "-123456789."

    while True:
        reponse_finale = []
        ValueTempo = 0
        reponse = input(ask)

        if "," in reponse:
            reponse = reponse.split(",")
        elif "," not in reponse:
            reponse = reponse.split(" ")
                    
        for i in reponse:
            if i != '':
                reponse_finale.append(i)
            if "[" in i or "]" in i:
                ValueTempo += 1

        for i in reponse_finale:
            if i[0:] == " ":
                reponse_finale[reponse_finale.index(i)] = i[1:]

        if ValueTempo == 0:
            
            if type == "int":
                for i in reponse_finale:
                    for j in i:
                        if j not in liste_int:
                            ValueTempo += 1
                        elif j == "-" and i.index(j) != 0:
                            ValueTempo += 1

                if ValueTempo == 0:
                    for i in range(len(reponse_finale)):
                        reponse_finale[i] = int(reponse_finale[i])

                    return reponse_finale
                else:
                    print("Il semble que une ou plusieurs valeurs ne sont pas correctes.")

            elif type == "float":
                for i in reponse_finale:
                    nb_points = 0
                    for j in i:
                        if j == ".":
                            nb_points += 1
                        elif j not in liste_dec:
                            ValueTempo += 1
                        elif j == "-" and i.index(j) != 0:
                            ValueTempo += 1
                    if nb_points > 1:
                        ValueTempo += 1
                    if i == ".":
                        ValueTempo += 1

                if ValueTempo == 0:
                    for i in range(len(reponse_finale)):
                        reponse_finale[i] = float(reponse_finale[i])

                    return reponse_finale
                else:
                    print("Il semble que une ou plusieurs valeurs ne sont pas correctes.")
            else:
                return reponse_finale
        else:
            print("Il semble que vous présentiez une liste de listes.")

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
