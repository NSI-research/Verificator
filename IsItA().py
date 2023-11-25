def IsItA(Question, VariableType="integer", ListType="integer"):
    Value = str(input(str(Question)))
    Lettre = """azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN,;:!*$%/.?&éèûùàùìò\ä\
        ëüöïÄËÜÏÖÀÈÙÌÒ²@^`|}][{#ã€¤£µ§' 0123456789+°)"(#^=ç<>-_"""
    Chiffre = "0123456789"
    ScoreNegatif = 0
    ScorePoint = 0
    ScoreCrochet = 0
    ScoreSpace = 0
    Space = False
    Value2 = []
    Value3 = []
    Virgule = 0

    if VariableType == "integer":
        for i in range(len(Value)):
            if Value[i] not in Chiffre:
                if Value[i] == "-" and i == 0:
                    ScoreNegatif += 1
                elif Value[i] == "-" and i != 0:
                    return 'Error : Not an integer number'                   
                else:
                    return 'Error : Not an integer number'
        if ScoreNegatif > 1:
            return 'Error : Not an integer number'
        else:
            ScoreNegatif = 0
            return int(Value)
        
    elif VariableType == "float":
        for i in range(len(Value)):
            if Value[i] not in Chiffre:
                if Value[i] == "-" and i == 0:
                    ScoreNegatif += 1
                elif Value[i] == "-" and i != 0:
                    return 'Error : Not a float number'
                elif Value[i] == ".":
                    ScorePoint += 1
                elif Value[i] == ",":
                    ScorePoint += 1
                    Value = Value[0:i]+"."+Value[i+1:]
                else:
                    return 'Error : Not a float number'
        if ScoreNegatif > 1 or ScorePoint > 1 :
            return 'Error : Not a float number'
        else:
            return float(Value)
        
    elif VariableType == "string":
        for i in Value:
            if i not in Lettre:
                return "Error : One of the given value isn't known"
        return Value

    elif VariableType == "list":
        for i in range(len(Value)):
            if Value[i] == " " and i == 0:
                Space = True
                ScoreSpace += 1
            elif Value[i] == " " and Space == True:
                ScoreSpace += 1
            else:
                Space = False
            if Value[i] == "[" or Value[i] == "]":
                ScoreCrochet += 1
        if ScoreCrochet%2 != 0:
            return 'Not a list'
        Value = Value[ScoreSpace:]
        for i in range(len(Value)):
            if Value[i] != "[" and i == 0 or Value[i] != "]" and i == len(Value)-1:
                return 'Not a list'
        if Value[1] == " ":
            Value = Value[2:]
        else:
            Value = Value[1:]
        if Value[-2] == " ":
            Value = Value[:-2]
        else:
            Value = Value[:-1]
        for i in range(len(Value)):
            if  Value[i] == "," and Value[i+1] == " ":
                Value2 += [Value[Virgule:i]]
                Virgule = i+2
            elif Value[i] == ",":
                Value2 += [Value[Virgule:i]]
                Virgule = i+1
        Value2 += [Value[Virgule:]]

        if ListType == "integer":
            for i in Value2:
                for j in range(len(i)):
                    if i[j] not in Chiffre:
                        if i[j] == "-" and j == 0:
                            ScoreNegatif += 1
                        elif i[j] == "-" and j != 0:
                            return "Error : One of the element isn't an integer value"                   
                        else:
                            return "Error : One of the element isn't an integer value"
            if ScoreNegatif > 1:
                return "Error : One of the element isn't an integer value"
            else:
                ScoreNegatif = 0
            for i in Value2:
                Value3 += [int(i)]
            return Value3

        elif ListType == "float":
            for i in Value2:
                for j in range(len(i)):
                    if i[j] not in Chiffre:
                        if i[j] == "-" and j == 0:
                            ScoreNegatif += 1
                        elif i[j] == "-" and j != 0:
                            return "Error : One of the element isn't an integer value"
                        elif i[j] == ".":
                            ScorePoint += 1
                        else:
                            return "Error : One of the element isn't an integer value"
            if ScoreNegatif > 1 or ScorePoint > 1:
                return "Error : One of the element isn't an integer value"
            else:
                ScoreNegatif = 0
                ScorePoint = 0
            for i in Value2:
                Value3 += [int(i)]
            return Value3


        elif ListType == "string":
            for i in Value2:
                for j in range(len(i)):
                    if i[j] not in Lettre:
                        return "Error : One of the given value isn't known"
            for i in Value2:
                Value3 += [str(i)]
            return Value3

print(IsItA("Liste : ", "list", "float"))


###    elif VariableType == "dico":
##        
###    elif VariableType == "tuple":
##        
###    elif VariableType == "find":


