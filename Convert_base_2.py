def convert(n): #déinir un fonction qui converti un nombre en base 10 vers la  base 2
    s="" #faire du texte pour pas que les chiffres s'additionnent
    while n!= 0 : #boucle pour faire tous les nombres
        s = str( n%2)+s #ajouter le résultat puis s parceque binaire se compte à l'envers lorsqu'on convenrti
        n = n//2 #pour continuer avec la suite du calcul
    return s