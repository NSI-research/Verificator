def isalist(ask=str, type=""):
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
            

while True:
    print(isalist("Test : ", "float"))